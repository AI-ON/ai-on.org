---
Title: Machine learning in non-stationary environments
Tagline: Explore techniques for developing models that can perform well on data that significantly differs from the training data.
Date: October 2016
Category: Fundamental Research
Mailing list: https://groups.google.com/d/forum/aion-machine-learning-in-non-stationary-environments
Contact: Okba Bekhelifi - okba.bekhelifi@univ-usto.dz
Type: legacy
---

## Problem description

Develop novel approaches to building machine learning systems capable of reliable inference on test data that follows a different distribution from the training data. Apply these approaches to brain-computer interfaces and robotics control.

Current approaches include covariate shift adaptation [1] and stationary subspace analysis [2].


## Why this problem matters

The universal assumption underlying machine learning is that the phenomenon being modeled is stationary and that the training data at hand is representative of it, i.e. that the data on which the model will be tested follows the same distribution as the training data. This doesn't hold true for several important practical applications, in particular brain-computer interfaces (where there are large discrepancies in brain signal patterns across different individuals) and robotics control (where robot control policy may be trained in simulated environments or controlled environments different from the deployment environment). This leads to a repetitive requirement of additional data collection and calibration before any serious use of such systems.

Solving this issue would help brain-computer interfaces to become mainstream. Additionally, it would allow for training robotics systems on simulation data while retaining real-world capabilities, which would prove immensely valuable for the entire field of robotics.


## Datasets

- [BNCI Horizon 2020 - brain computer interface data](http://bnci-horizon-2020.eu/database/data-sets)
- [Kaggle INRIA BCI challenge](https://www.kaggle.com/c/inria-bci-challenge)


## References

- 1: [Covariate Shift Adaptation by Importance Weighted Cross Validation](http://www.jmlr.org/papers/volume8/sugiyama07a/sugiyama07a.pdf)
- 2: [Finding stationary subspaces in multivariate time series](http://www.ncbi.nlm.nih.gov/pubmed/20366040)
- [Interpretable Deep Neural Networks for Single-Trial EEG Classification](http://arxiv.org/abs/1604.08201)
- [Geometry-aware stationary subspace analysis](https://arxiv.org/abs/1605.07785)
