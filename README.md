# DistractedDriverDetection
### Computer Vision Project #1

## Overview

We've all been there: a light turns green and the car in front of you doesn't budge. Or, a previously unremarkable vehicle suddenly slows and starts swerving from side-to-side. When you pass the offending driver, what do you expect to see? You certainly aren't surprised when you spot a driver who is texting, seemingly enraptured by social media, or in a lively hand-held conversation on their phone. According to the CDC motor vehicle safety division, one in five car accidents is caused by a distracted driver. Sadly, this translates to 425,000 people injured and 3,000 people killed by distracted driving every year.

Given a dataset of 2D dashboard camera images, classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?

## Approach
### Data

The dataset used is provided [here](https://www.kaggle.com/c/state-farm-distracted-driver-detection/data).

### Data-preprocessing

The images are loaded in RGB format and resized to 224x224 pixels.

### IPYNB

Model were trained on Kaggle kernel.

### Class description

* c0: safe driving
* c1: texting - right
* c2: talking on the phone - right
* c3: texting - left
* c4: talking on the phone - left
* c5: operating the radio
* c6: drinking
* c7: reaching behind
* c8: hair and makeup
* c9: talking to passenger

### Model

Standard computer vision models were trained on the dataset.

1. VGG-16 
2. Wide Residual Newtowrk (WRN)

WRN performed better and hence is chosen for further usage.

## Upgrades for future

1. Add openCV integration for live classification of the driver's actions.
2. Develop an alerting system incase of distractions.
3. Data collection from different angles.
