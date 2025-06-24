## Duality AI Hackathon Submission: Space_Station_Object_Detection

Welcome, Judge! This README will guide you through our submission, including where to find the report, model, results, and application.



## Submission Overview

| Section                   | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `Hackathon_Report.pdf`    | Complete write-up: methodology, results, challenges, and visuals            |
| `Code/`                   | YOLOv8 training and inference code, config files, final model weights       |
| `Model_Results/`          | Confusion matrix, precision-recall curves, and detection results visuals    |
| `Application/`            | use-case app proposal and mockup for the same detection system              |



## Quick Project Summary

**Project Title**: Space_Station_Object_Detection  
**Team Name**: Team Recursion  
**Dataset Used**: Falcon synthetic dataset (provided by Duality AI)  
**Goal**: Detect and classify objects in a simulated space station environment (ToolBox, Fire Extinguisher, Oxygen Tank) using YOLOv8.  
**Final mAP@0.5**: **0.862**



## How to Reproduce Our Results

1. Clone this repository

2. Make sure you have Anaconda installed, and open an Anaconda Prompt window

3. Navigate to Code/ENV_SETUP

4. Run the setup_env.bat file in the Anaconda Prompt window  (This will set up an environment called “EDU”, containing all the dependencies required to run the training and prediction scripts)

5. Train the model:
    i. conda activate EDU
    ii. python train.py  (This will begin training your model and save logs + checkpoints to the runs/ directory. )
    
6. Run inference:
    i. python predict.py   ( This tests its performance on real-world test images and gives mAP@0.5 , Predictions , Confusion_Matrix,Precision and Recall)
    
7. Outputs will be saved in `runs/` or directly viewed in `Model_Results/`



## Evaluation Notes

- Model trained exclusively on Falcon-provided training and validation set
- No test images were used during training (test set strictly reserved for evaluation)
- YOLOv8 hyperparameters customized in `yolo_params.yaml`
- Data augmentation and optimization strategies detailed in `Hackathon_Report.pdf`



## Use-Case App

Our app proposal, **Space_Station_Object_Detection**, is located in the `Application/` folder. It includes:
- A short proposal PDF (Application link and the repo link is present in this pdf)
 

This app demonstrates how object detection in the space station environment can be deployed and maintained using Falcon-generated data.



## Thank You

Thank you for your time and for organizing this innovative and exciting challenge!

— Team Recursion
