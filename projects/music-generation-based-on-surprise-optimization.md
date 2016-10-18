Title: Music generation based on surprise optimization
Tagline: Use neuroscience and deep learning to generate music that pushes the right buttons in our brains.
Date: October 2016
Category: Fundamental Research
Mailing list: https://groups.google.com/d/forum/aion-music-generation-based-on-surprise-optimization
Contact: Francois Chollet - fchollet@google.com


## Problem description

It has been suggested that part of our appreciation for music comes from dopamine responses triggered by building-up then breaking sensory expectations, i.e. that music manufactures continuous surprise during listening, an effect that appears sustainable even after repeated exposure to a given musical pattern.

At the same time, techniques for music generation have recently made great progress, with WaveNet [1] in particular appearing to be a promising avenue.

We propose to combine such music generation techniques with a "critic" component that would analyze the degree of sustained surprise (i.e. enjoyment) that a musical track generates during listening. This critic may be a model attempting to predict the short-term evolution of the musical track; the error signal of such a model would provide visibility into listening surprise. This component would guide the music generation process so as to produce tracks that not only sound "like music" but also sound enjoyable.


## Datasets

- [Million song dataset](http://labrosa.ee.columbia.edu/millionsong/)


## References

- 1: [WaveNet: A Generative Model for Raw Audio](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)
- [Magenta project](https://magenta.tensorflow.org/welcome-to-magenta)