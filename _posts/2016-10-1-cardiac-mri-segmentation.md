---
Title: Cardiac MRI Segmentation
Tagline: Develop a system capable of automatic segmentation of the right ventricle in images from cardiac magnetic resonance imaging (MRI) datasets.
Date: October 2016
Category: Applied Research
Mailing list: https://groups.google.com/forum/#!forum/aion-cardiac-mri-segmentation
Contact: Michael Avendi - Mra446@gmail.com
type: legacy
---

## Problem description

Develop a system capable of automatic segmentation of the right ventricle in images from cardiac magnetic resonance imaging (MRI) datasets. Until now, this has been mostly handled by classical image processing methods. Modern deep learning techniques have the potential to provide a more reliable, fully-automated solution.

A [recent Kaggle challenge](https://www.kaggle.com/c/second-annual-data-science-bowl) focused on measuring the volume of the left ventricle from MRI images. Deep learning techniques proved very effective, and some of the top entries from this challenge can provide inspiration for right-ventricle segmentation. Note that right-ventricle segmentation is likely to be a harder problem due to the more complex geometry of the right ventricle. Several challenges exist in the automatic segmentation of the right ventricle: presence of trabeculations in the cavity with signal intensities similar to that of the myocardium; the complex crescent shape of the RV, which varies from the base to the apex; difficulty in segmenting the apical image slices; considerable variability in shape and intensity of the chamber among subjects, notably in pathological cases, etc.


## Why this problem matters

This is required in order to estimate ventricular volume in patients with heart disease.

Cardiac MRI is routinely being used for the evaluation of the function and structure of
the cardiovascular system. The obtained magnetic resonance images of patients are inspected both visually and
quantitatively by clinicians to extract important information about heart function. Segmentation of the heart chambers,
such as the right ventricle, in cardiac magnetic resonance images is an essential step for the computation of clinical indices such
as ventricular volume and ejection fraction (note: you could also try to directly predict ventricular volume, although it would be more difficult).

Manual delineation by experts is currently the standard clinical practice for right ventricle segmentation. However, manual segmentation is tedious, time consuming and prone to intra and inter-observer variability. Therefore, it is necessary to reproducibly automate this task to accelerate and facilitate the process of diagnosis and follow-up.


## How to measure success

The [Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) can be used to compare the pixel-wise agreement between a predicted segmentation and its corresponding ground truth.


## Datasets

- [Dataset from Project RVSC](http://www.litislab.fr/?sub_project=how-to-download-the-data)


## References

- [Right Ventricle Segmentation From Cardiac MRI: A Collation Study](http://www.litislab.fr/wp-content/uploads/2014/07/RSCVMedIApaper_finalversion.pdf)
- [A survey of shaped-based registration and segmentation techniques for cardiac images](http://fulltext.study/preview/pdf/525781.pdf)
- [Right ventricular segmentation in cardiac MRI with moving mesh correspondences](http://ir.lib.uwo.ca/cgi/viewcontent.cgi?article=1053&context=biophysicspub)
- [Segmentation of RV in 4D cardiac mr volumes using region-merging graph cuts](http://www2.die.upm.es/im/papers/CinC2012.pdf)
