---
Title: Chromosome Segmentation
Tagline: Develop a specialized visual segmentation model to help cytogeneticists conduct research.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/d/forum/aion-visual-segmentation-of-chromosomal-preparations
Contact: Jean-Patrick Pommier - Univerité Pierre et Marie Curie
Type: legacy
---

## Problem description

In cytogenetics, experiments typically starts from chromosomal preparations fixed on glass slides. Occasionally a chromosome can fall on another one, yielding overlapping chromosomes in the image. Before computers and images processing with photography, chromosomes were cut from a paper picture and then classified (at least two paper pictures were required when chromosomes are overlapping). More recently, automatic segmentation methods were developped to overcome this problem. Most of the time these methods rely on a geometric analysis of the chromosome contour and require some human intervention when partial overlap occurs. Modern deep learning techniques have the potential to provide a more reliable, fully-automated solution.


## Why this problem matters

A fast and fully-automated segmentation solution can allow to scale certain experiments to very large number of chromosomes, which was not possible before. E.g. quantitative analysis of hybridization fluorescent signal on metaphasic chromosomes in the case of telomere length analysis.


## Datasets

- [overlapping-chromosomes](https://www.kaggle.com/jeanpat/overlapping-chromosomes/downloads/overlapping-chromosomes.zip) - note that following this link triggers a download.


## References

- [A Geometric Approach To Fully Automatic Chromosome Segmentation](https://arxiv.org/abs/1112.4164)
- [Automated Discrimination of Dicentric and Monocentric Chromosomes by Machine Learning-based Image Processing](http://biorxiv.org/content/biorxiv/early/2016/01/19/037309.full.pdf)
- [An Efficient Segmentation Method for Overlapping Chromosome Images](http://research.ijcaonline.org/volume95/number1/pxc3894861.pdf)
- [A Review of Cytogenetics and its Automation](http://www.scialert.net/qredirect.php?doi=jms.2007.1.18&linkid=pdf)
