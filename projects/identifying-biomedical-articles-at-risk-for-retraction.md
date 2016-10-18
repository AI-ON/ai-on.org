Title: Identifying biomedical articles at risk for retraction
Tagline: Develop a model to analyze the content of new biomedical articles to determine the likelihood of fraud or scientific error.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/forum/#!forum/aion-identifying-biomedical-articles-at-risk-for-retraction
Contact: Andrew Goldstein - ag3304@cumc.columbia.edu


## Problem description

Develop a model capable of reliably flagging biomedical articles (appearing on bioRxiv or in biomedical scientific publications) that may be at risk of retraction. Such articles would then be carefully reviewed by peers in the community.


## Why this problem matters

Although the retraction of a scientific article in the biomedical literature is still a rare event, is is getting increasingly frequent [1, 2]. Retractions reflect error, misconduct, and fraud, which can significantly affect the scientific community and [undermine the trust that the public puts in science](https://www.washingtonpost.com/news/morning-mix/wp/2015/03/27/fabricated-peer-reviews-prompt-scientific-journal-to-retract-43-papers-systematic-scheme-may-affect-other-journals/). Detecting articles at risk of retraction could help focus the attention of efforts like [Retraction Watch](http://retractionwatch.com/) and other post-publication peer review groups. In turn, if the detection of problematic articles becomes more effective, the incentive for fraud is greatly diminished and the penalty for errors is increased, which should improve the overall quality and reliability of the biomedical literature.


## Datasets

Start by using MEDLINE meta-data [3], with the core clinical journals filter. The meta-data tag "Retracted Publication" can serve as ground-truth label.


## References

- 1: [A Comprehensive Analysis of Articles Retracted Between 2004 and 2013 from Biomedical Literature – A Call for Reforms](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4142449/)
- 2: [Why Has the Number of Scientific Retractions Increased?](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0068397)
- 3: [Why and how do journals retract articles? An analysis of Medline retractions 1988-2008](https://www.ncbi.nlm.nih.gov/pubmed/21486985)
