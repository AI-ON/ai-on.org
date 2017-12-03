---
Title: Multitask and Transfer Learning
Tagline: Benchmark and build RL architectures that can do multitask and transfer learning.
Date: December 2016
Category: Fundamental Research
Contact: deontologician@gmail.com
Type: legacy
---

## Project Status

Currently in the early stages of writing the benchmark for measuring performance.

- [Github repository](https://github.com/deontologician/atari_multitask)


## Community Links

- TBA


## Problem Description

First, create a benchmark for multi task learning and transfer learning.
The benchmark should measure improvement in learning that is directly attributable
to knowledge transfer between games. The benchmark should also be able to measure
performance by a single agent on multiple games. The benchmark should use cross-validation
to mitigate the effects of a small sample size of games.

Second, design and implement deep reinforcement learning architectures that do well
on the benchmark. For methodological reasons, we think it's important to design the ideal benchmark
before getting too attached to a particular architecture. It's important that
we're sure the benchmark is measuring the crux of the transfer and multi-task problem
rather than measuring something our architecture is good at.


## Why this problem matters

Generalizing across tasks is a crucial component of human intelligence. Current
deep RL architectures get less effective the more tasks they are put to, whereas
for humans, diversity of experience is a strength that improves performance on
new tasks. Overcoming catastrophic forgetting and achieving one-shot learning
are abilities that should fall out naturally if this task is solved
convincingly.

At a more meta-level, this problem is both out of reach of current reinforcement
learning architectures, but it seems reasonably within reach within a year or
two. Much like ImageNet spurred innovation by creating a common target for
researchers to aim for, this project could similarly provide a common idea of
success for multitask and transfer learning. Many papers researching multi-task
and transfer learning using Atari are doing it in ad-hoc ways that cherry-pick
games that get good results.

## How to measure success

Success is in degrees, since an architecture (in principle) could surpass human
ability in multi-task Atari, getting both higher scores on all games, and
picking up new games faster than a human does. Ideally, a good waterline would
be human level performance on the benchmark, but creating a robust dataset on
human performance is beyond the scope of this project.

The fundamental benchmark then will be two measures:

1. **Transfer Learning**: How much a given architecture improves on an unseen
game when it is untrained versus when it has been trained on other games firest.
Measured as a ratio of total score pre-trained vs. untrained. Ratio is averaged using
cross-validation given that there is a small number of available games and the
fact that high scores are not comparable across games.
2. **Multitask Learning**: How well a given architecture does across all games
with a single architecture and set of weights. Rather than an aggregate, this
result will be a vector of top scores achieved for each game.

In addition to the scores, the benchmark will also make some strict demands on
the architecture itself due to the testing/training regime:

- Training will happen on random games sequentially. After each loss a new
  random game from the training set will be selected to play next.
- **No out of band signal** will be given to indicate which game is being played, so
  architectures that need to allocate a set of extra weights for each game will
  have to be more clever.
- All games in ALE will be used, **even ones which standard DQNs perform poorly on**
  like Montezuma’s Revenge.

## Data Sets

Currently no datasets, but it’s possible the dataset being created at
[atarigrandchallenge.com](http://atarigrandchallenge.com/) will potentially be a useful comparison once
it’s available. Measuring human performance needs to be done with a large sample
size, both to control for pre-training (some people have played Atari games
before, or other video games before) and to control for individual human skill
levels (this could be seen as pre-training on non-Atari games, generalization
from real life, or natural ability etc).

Akin to a dataset will be the benchmark framework itself. Since this is a
reinforcement learning problem, the testing environment provides the data,
rather than a static dataset.

## Relevant/Related Work

Since the original Mnih paper, the Atari 2600 environment has been a popular
target for testing out RL architectures

- [Overcoming Catastrophic forgetting in neural networks [Dec 2016]](https://arxiv.org/abs/1612.00796)
    - Uses a technique they call “elastic weight consolidation” to dynamically adjust learning speed for each weight, avoiding catastrophic forgetting.
    - Chooses a subset of games to play
    - Avoids games like Montezuma’s Revenge that performed poorly in the original Atari paper.

- [Progressive Neural networks [June 2016]](https://arxiv.org/abs/1606.04671v3)
    - Addresses both multitask and transfer learning on a small number of games through freezing weights for a previous game when learning a new game.
    - Number of weights grows with the number of tasks, a very hands-on approach

- [Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning [Nov 2015]](https://arxiv.org/abs/1511.06342v4)
    - Trains a common network, along with an expert network for each game.
    - Uses the transfer learning benchmark of random initialization vs. pre-trained on other games.
    - Trained mostly on games that DQNs perform well on, though Seaquest was included.

- [Modular Multitask Reinforcement Learning with Policy Sketches [Nov 2016]](https://arxiv.org/abs/1611.01796v1)
    - Uses as extra input a list of high level actions which need to be accomplished to complete a task. The network must learn to use this signal to create heirarchical representations.
    - Uses two custom test environments for which their approach is more amenable.

- [Human-level control through deep reinforcement [2015]](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html)
    - Original DeepMind Atari paper
        - [Related workshop paper from 2013](https://arxiv.org/abs/1312.5602v1)
    - No multi-task or transfer learning attempted, but has some reasonable baselines for human performance on the games (which are then re-used in many subsequent papers)

- [Reinforcement Learning with Unsupervised Auxiliary Tasks](https://arxiv.org/abs/1611.05397v1)
