---
Title: Subpixel CNN in Upsampling Applications
Tagline: Improve segmentation models and generative models by using a subpixel CNN as the upsampling operation.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/d/forum/aion-subpixel-cnn-in-upsampling-applications
Contact: Eder Santana - edersantana@ufl.edu
Type: legacy
---

## Problem description

The upsampling of feature maps in convolutional neural networks is useful in many types of models, such as generative models [1], image segmentation models [2], and more. Currently these models use transposed convolution (also called "deconvolution") as their upsampling operation. Subpixel CNNs [3] are a promising new way to do upsampling of feature maps which may be preferrable to transposed convolution. Currently it seems this has only been used in one CVPR 2016 paper about super-resolution [3]. We propose to investigate the use of subpixel CNNs for a wide range of models that use upsampling, in particular segmentation models and generative models.


## Why this problem matters

Generative models grew to be one of the main topics in Deep Learning. For example, experts in the field considered Generative Adversarial Networks to be one of the most important research directions in deep learning [4]. Image segmentation on the other hand is one of the fundamental techniques in the new industry of self-driving cars. Image segmentation could be used to classify drivable paths, detection of obstacles, pedestrians, other cars, etc. Beyond self-driving cars, image segmentation is useful for any classification problem where one needs more information than the existence or not of an object in a scene.


## How to measure success

Sucess measures are problem-specific. For the segmentation problem we should compare networks with similar number of operations and check if the subpixel improves the number of correctly segmented pixels. In the generative model case the measure to track is the log-likelihood of generated samples (in small datasets like MNIST). Beyond the quality of generated samples, we should also test the stability of the generatie models and how useful parts of it can be used for other tasks such as feature extraction for classification [1].


## Datasets

### Generative models:

- [MS COCO](http://mscoco.org/)
- [Imagenet](http://image-net.org)
- [OpenImage](https://github.com/openimages/dataset)

### Image segmentation:

- [Kitti](http://www.cvlibs.net/datasets/kitti/)
- [CamVid](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/)

### Datasets generated from video games:

- [Virtual Kitti](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds)
- [Playing for Data](http://download.visinf.tu-darmstadt.de/data/from_games/)


## References

- 1: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
- 2: [ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation](https://arxiv.org/abs/1606.02147)
- 3: [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158)
- 4: [Yann LeCun on upcoming breakthroughs in deep learning](https://www.quora.com/What-are-some-recent-and-potentially-upcoming-breakthroughs-in-deep-learning)
