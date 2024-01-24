# Brain MRI Segmentation

## Overview
"Brain MRI Segmentation" is a project focusing on segmenting brain tissues in MRI scans into distinct regions such as white matter, gray matter, and cerebrospinal fluid. This segmentation plays a crucial role in diagnosing and studying various neurological conditions.

## Key Features
- **Segmentation of Brain Tissues:** Classifies MRI images into white matter, gray matter, and cerebrospinal fluid.
- **Deep Learning Model:** Utilizes a 2D patch-based U-Net architecture for effective segmentation.
- **Data Augmentation:** Employs techniques like flipping, rotation, and Gaussian blur for robust model training.
- **Performance Metrics:** Uses Dice Coefficient, Hausdorff Distance, and Relative Absolute Volume Difference for evaluation.

## Methodology
- **Algorithm Implementation:** Development of a deep learning model based on the U-Net architecture.
- **Data Handling:** Patch-based approach for handling MRI images.
- **Model Training:** Includes customization of hyperparameters, loss function, and data augmentation techniques.

## Images
Images demonstrating the segmentation results and model architecture can be found in the repository's `results` folder.
- With Aumentation 
![with agumentation](https://github.com/taiaburbd/brain_mri_segmentation/blob/main/results/with_agumentation.png)
- Without Aumentation
![without agumentation](https://github.com/taiaburbd/brain_mri_segmentation/blob/main/results/without_agumentation.png)

