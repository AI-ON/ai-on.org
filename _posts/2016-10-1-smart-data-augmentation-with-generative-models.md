---
Title: Smart data augmentation with generative models
Tagline: Use GANs and other generative models to develop better data augmentation techniques for computer vision models.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/forum/#!forum/aion-smart-data-augmentation-with-generative-models
Contact: Ellick Chan - ellick.chan@northwestern.edu
Type: legacy
---

## Problem description

Current methods of data augmentation usually involve simple transformations like translations, rotations and scaling. These produce highly correlated outputs and are thus a weak form of data augmentation. An alternative would be to learn the latent manifold on which the input data lies, and sample realistic pictures (and their labels) from this manifold. This could be achieved by using an auxiliary network trained to perform data augmentation in a plausible way (similar to the process of generative adversarial networks [1]), or by using non-learned transformations such as "liquid resizing" and "content-aware fill", with the resulting images being filtered by a "critic" network trying to determine if the result is still plausible or not.

This has the potential to provide better regularization for computer vision model, as well as making it possible to train models using less labeled data, since the generative networks or critic networks may be trained in a completely unsupervised manner.


## Why this problem matters

Data augmentation is universally used in computer vision models. Improving it by a significant factor (at a reasonable computational cost) would result in broad adoption and significant gains across the entire field.


## How to measure success

Success on this problem would translate to two important results:

- Achieving baseline performance on an image classification (or detection, or segmentation) dataset using significantly less data.
- Achieving higher performance with the same data, via better regularization.

Your goal should thus be to demonstrate any of these two results on a benchmark dataset such as ImageNet or MS COCO.


## Datasets

- [ImageNet](http://image-net.org) - large-scale classification.
- [OpenImages](https://github.com/openimages/dataset) - large-scale classification.
- [MS COCO](http://mscoco.org/) - smaller scale classification, detection, segmentation.
- [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) - small scale classification.


## References

- 1: [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)