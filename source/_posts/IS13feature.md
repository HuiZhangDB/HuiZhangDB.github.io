---
title: 2013 ComParE Feature Set
date: 2017-05-02 12:46:53
tags:
  - MER
  - feature
categories:
---
This blog will introduce a well-evolved feature set for automatic recognition of audio emotion, ie. 2013 ComParE Feature Set[1]. The ComParE feature set contains `6373` features. It consists of some `generic acoustic emotion descriptors` and their `statistical functionals`.

<!--More-->

## 65 Acoustic low-level descriptors(LLDs)
The low-level descriptors cover a broad set of descriptors from the fields of `speech processing`, `Music Information Retrieval`, and `general sound analysis`. The set includes `energy`, `spectral`, and `voicing related low-level descriptors (LLDs)` including logarithmic harmonic-to-noise ratio (HNR), spectral harmonicity, and psychoacoustic spectral sharpness. Details are shown below.[2]

### 4 ENERGY RELATED LLD
* Sum of auditory spectrum (loudness)* Sum of RASTA-style filtered auditory spectrum 
* RMS energy 
* zero-crossing rate

### 55 SPECTRAL LLD
* RASTA-style auditory spectrum, bands 1–26 (0–8 kHz) 
* MFCC 1–14* Spectral energy 250–650 Hz, 1 k–4 kHz* Spectral roll off point 0.25, 0.50, 0.75, 0.90* Spectral flux, centroid, entropy, slope 
* Psychoacoustic sharpness, harmonicity 
* Spectral variance, skewness, kurtosis

### 6 VOICING RELATED LLD
* F 0 (SHS and viterbi smoothing)* Prob. of voice* Log. HNR, Jitter (local, delta), Shimmer (local)

## Statistical functionals
Statistical functionals include mean, moments, quartiles, 1- and 99-percentiles, as well as contour related measurements such as (relative) rise and fall times, amplitudes and standard deviations of local maxima (‘peaks’), and linear and quadratic regression coefficients.

### FUNCTIONALS APPLIED TO LLD/deta_LLD
* Quartiles 1–3, 3 inter-quartile ranges* 1% Percentile (~=min), 99% percentile (~=max) 
* Percentile range 1–99%
* Position of min/max, range (max   min) 
* Arithmetic mean, root quadratic mean
* Contour centroid, flatness
* Standard deviation, skewness, kurtosis
* Rel. duration LLD is above 25/50/75/90% range 
* Rel. duration LLD is rising
* Rel. duration LLD has positive curvature
* Gain of linear prediction (LP), LP coefficients 1–5 
* Mean, max, min, SD of segment length

### FUNCTIONALS APPLIED TO LLD ONLY
* Mean value of peaks
* Mean value of peaks – arithmetic mean 
* Mean/SD of inter peak distances
* Amplitude mean of peaks, of minima
* Amplitude range of peaks
* Mean/SD of rising/falling slopes
* Linear regression slope, offset, quadratic error 
* Quadratic regression a, b, offset, quadratic error 
* Percentage of non-zero frames

## Reference
[1] Schuller B, Steidl S, Batliner A, et al. The INTERSPEECH 2013 computational paralinguistics challenge: social signals, conflict, emotion, autism[J]. 2013.  
[2] Weninger F, Eyben F, Schuller B W, et al. On the acoustics of emotion in audio: what speech, music, and sound have in common[J]. 2013.