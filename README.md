# NeuroPredict: Comprehensive Alzheimer’s Disease Prediction and Medical Assisting Kit

**Affiliation:**  
Electronics and Communication, The National Institute of Engineering, Mysuru

**Conference:**  
2023 International Conference on Recent Advances in Science Engineering Technology (ICRASET)

## Overview

NeuroPredict is a system designed to address Alzheimer’s disease (AD) through early prediction and diagnosis using a Convolutional Neural Network (CNN) model on MRI images. With an 80% accuracy rate, NeuroPredict aims to provide a robust solution for the early detection and management of AD. The project also introduces MemorEyes, a low-cost hardware kit to assist individuals in the early stages of AD, offering personalized support and proactive prevention.

## Table of Contents

- [Introduction](#introduction)
- [Methodology](#methodology)
  - [Data Collection](#data-collection)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Building](#model-building)
  - [Model Training](#model-training)
  - [Exploratory Data Analysis](#exploratory-data-analysis)
- [MemorEyes Hardware Kit](#memoreyes-hardware-kit)
- [Website](#website)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Alzheimer’s disease is a global health concern that significantly impacts individuals, families, and healthcare systems. Early prediction and diagnosis are crucial for timely interventions and better patient outcomes. NeuroPredict leverages a CNN model to predict AD based on MRI images and includes a user-friendly web application for clinicians and researchers.

## Methodology

### Data Collection

The dataset includes MRI images from various reliable sources, such as the Alzheimer’s Disease Neuroimaging Initiative (ADNI) and Kaggle. The data is divided into training and testing sets to ensure robust model evaluation.

### Data Preprocessing

To ensure the quality and suitability of neuroimaging data for CNN-based AD classification, the following preprocessing steps are employed:
- **Image Registration:** Aligns images to a common coordinate system.
- **Skull Stripping:** Isolates the brain from surrounding tissues.
- **Intensity Normalization:** Standardizes intensity values across images.
- **Voxel Resampling:** Achieves a consistent voxel size across all images.

### Model Building

The CNN model architecture includes:
- **Convolutional Layers:** Extract local features from input images.
- **Pooling Layers:** Reduce spatial dimensions while retaining important features.
- **Fully Connected Layers:** Perform the final classification based on extracted features.
- **Dropout Regularization:** Prevents overfitting.

### Model Training

The training process involves optimizing model parameters using labeled training data. The dataset is divided into training, validation, and testing sets. Hyperparameter tuning is performed to achieve optimal results.

### Exploratory Data Analysis

Exploratory Data Analysis (EDA) is conducted to uncover patterns and relationships within the AD patient dataset, providing valuable insights for research and interventions.

## MemorEyes Hardware Kit

MemorEyes is a low-cost hardware kit designed to assist AD patients. It includes:
- **Smart Spectacles:** Display pictures of loved ones with details.
- **Smart Wristband:** Provides live location tracking and reminders for exercise and medication.
- **Caretaker Alerts:** Promotes proactive prevention and personalized support.

## Website

The NeuroPredict system includes a user-friendly web application for clinicians and researchers to upload MRI images, run predictions using the CNN model, and access detailed reports and visualizations.

## Results

The NeuroPredict system achieves an 80% accuracy rate in predicting AD using MRI images, offering a reliable solution for early diagnosis. The combination of CNN models, EDA insights, and innovative hardware and web applications addresses the critical need for early prediction and personalized care in AD.


For more information, please visit our [conference paper](https://ieeexplore.ieee.org/document/10419914).
