---
Title: Layer-wise supervised incremental training of residual networks
Tagline: Explore techniques for training supervised residual networks in a layer-by-layer fashion, rather than end-to-end.
Date: October 2016
Category: Fundamental Research
Mailing list: https://groups.google.com/d/forum/aion-incremental-training-of-residual-networks
Contact: Giorgio Patrini - giorgio.patrini@anu.edu.au
Type: legacy
---

## Problem description

Due to their structure, it may be that residual modules [1] could be trained incrementally, starting from a previous, shallower net learned with full supervision. At each step, the network would learn an additional residual module, which would be an additional non-linear feature representation of the input that is fed into the previous module — the classifier. A very useful reading to help intuition of this effect is [2], which gives an ensemble-like interpretation of residual networks. The re-use of the previously trained layers should save computational time. Moreover, it is possible to show that at each step we are learning in a strictly larger model space, of which network learned in the previous step is the optimal model when we zero-out the weights of the new residual units just added.

Some approaches for incremental learning have been recently investigated [3, 4]. They share some intuition with this one. Although they try to solve the more general problem of transfer learning and they are not tailored to residual networks specifically.


## Why this problem matters

Efficient layer-wise training of deep networks could allow to significantly speed up training of large models. It is one of the long-standing "dreams" of deep learning, but has proven elusive so far. If such a method were to be devised and performed competitively with end-to-end trained models while providing computational benefits, it would quickly be adopted across the entire field.


## Datasets

- [ImageNet](http://image-net.org) - large-scale classification.
- [OpenImages](https://github.com/openimages/dataset) - large-scale classification.
- [MS COCO](http://mscoco.org/) - smaller scale classification, detection, segmentation.
- [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) - small scale classification.


## References

- 1: [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- 2: [Residual Networks are Exponential Ensembles of Relatively Shallow Networks](https://arxiv.org/abs/1605.06431)
- 3: [Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641)
- 4: [Progressive Neural Networks](https://arxiv.org/abs/1606.04671)
