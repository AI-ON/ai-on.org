---
Title: Photorealistic post-processing of rendered 3D scenes
Tagline: Develop a model (similar to a super-resolution model) capable of enhacing the realism of 3D-rendered scenes.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/forum/#!forum/aion-photorealistic-3d-scene-postprocessing
Contact: Dave Sullivan - dave.brian.sullivan@gmail.com
Type: legacy
---

## Problem description

It is now possible to produce near-photorealistic 3D graphics relatively cheaply; however reaching complete photo-realism requires one order of magnitude more resources. At the same time, deep learning-based super-resolution techniques have proven capable of rendering low-resolution images into photo-realistic higher-resolution images. As such, it may be possible to use related techniques to post-process 3D renders (especially renders featuring people) to become photo-realistic; especially since the remaining issues with 3D renders tend to be at the level of local textures and micro light effects, which a super resolution-type model may be able to handle. Generative adversarial networks may also prove effective (with an adversarial network attempting to disciminate between photos and post-processed 3D renders).


## Why this problem matters

Such a model would stand a chance to eventually end up changing the way a lot of entertainment is produced. If the resulting network can be made to run in real-time, it could serve as a video-game shader, for instance.


## References

- [Image Restoration Using Very Deep Convolutional Encoder-Decoder Networks with Symmetric Skip Connections](https://arxiv.org/abs/1603.09056)
- [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158)
- [Learning from Simulated and Unsupervised Images through Adversarial Training](https://arxiv.org/abs/1612.07828)
