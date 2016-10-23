# -*- coding: utf-8 -*-
'''Code for generating the AION static website.
'''

from __future__ import unicode_literals
import markdown
import os
import jinja2

PROJECTS_MD_DIR = './projects'
HTML_DIR = './website'
TEMPLATES_DIR = './templates'

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))


def parse_project_file(fpath):
    f = open(fpath)
    metadata = {}
    headers = {'title', 'date', 'category', 'contact', 'tagline', 'mailing_list','repository'}
    for line in f:
        line = line.decode('utf-8')
        if not line.strip().split():
            break
        if ':' in line:
            split_index = line.find(':')
            header = line[:split_index].strip().lower()
            header = header.replace(' ', '_')
            header_content = line[split_index + 1:].strip()
            if header in headers:
                metadata[header] = header_content
    content_lines = []
    for line in f:
        content_lines.append(line.decode('utf-8'))
    content = ''.join(content_lines)
    f.close()
    return content, metadata


def render_project_pages():
    fnames = [n for n in os.listdir(PROJECTS_MD_DIR) if n.endswith('.md')]
    template = jinja_env.get_template('project.html')
    folder = os.path.join(HTML_DIR, 'projects')
    if not os.path.exists(folder):
        os.makedirs(folder)

    research_projects = []
    applied_projects = []

    for fname in fnames:
        fpath = os.path.join(PROJECTS_MD_DIR, fname)
        # parse project file into metadata and content
        md_content, metadata = parse_project_file(fpath)
        # render content as HTML
        html_content = mdown_to_html(md_content)
        # render project HTML page using Jinja
        page = template.render(content=html_content, **metadata)
        # save project page to website/projects
        page_fname = fname.replace('.md', '.html')
        page_fpath = os.path.join(folder, page_fname)
        metadata['fname'] = page_fname
        f = open(page_fpath, 'w')
        f.write(page.encode('utf-8'))
        f.close()

        if 'category' in metadata:
            category = metadata['category'].lower()
            if category == 'applied research':
                applied_projects.append(metadata)
            if category == 'fundamental research':
                research_projects.append(metadata)

    return research_projects, applied_projects


def mdown_to_html(mdown):
    return markdown.markdown(mdown, extensions=[
        'fenced_code',
        'codehilite(css_class=highlight)',
        'toc',
        'tables',
        'sane_lists',
    ])


def render_page(template, title, tab, fpath, **kwargs):
    fpath = os.path.join(HTML_DIR, fpath)
    folder = os.path.dirname(fpath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    head = head_template.render(title=title)
    header = header_template.render(tab=tab)
    template = jinja_env.get_template(template)
    page = template.render(head=head, header=header, **kwargs)
    f = open(fpath, 'w')
    f.write(page.encode('utf-8'))
    f.close()


if __name__ == '__main__':
    head_template = jinja_env.get_template('head.html')
    header_template = jinja_env.get_template('header.html')

    # renders core website
    render_page(template='home.html', title=None, tab='home', fpath='index.html')
    render_page(template='process.html', title='Process', tab='process', fpath='process/index.html')
    render_page(template='about.html', title='About', tab='about', fpath='about/index.html')
    render_page(template='error.html', title=None, tab=None, fpath='error.html')

    # render projects page
    research_projects, applied_projects = render_project_pages()
    projects_list_template = jinja_env.get_template('projects_list.html')
    applied = projects_list_template.render(projects=applied_projects)
    fundamental = projects_list_template.render(projects=research_projects)
    render_page(template='projects.html', title='Projects', tab='projects', fpath='projects/index.html',
                applied=applied, fundamental=fundamental)
