# Driver Drowsiness Detection System
Drowsiness detection system detect if person is feeling sleepy or not based on his/her behavior of yawning while driving a vehicle and can further extend to trigger if alarm is required.

## Feature of Driver Drowsiness Detection Model
Model use concept of Transfer Learning with Pre-trained InceptionV3 model architecture.

A person’s state of being i.e. whether he is feeling sleepy or not can be detected by the live feed derived from the system’s camera which can be dashboard camera for vehicles.
This project can also be used to gather information about a person’s usual behavior when driving, i.e., Sleepy, Awake.
Model is trained for daylight, darkness and face at multiple view angles of camera.

Driver Drowsiness Detection Model have proven to be very useful in pattern recognition, classification which has trained for efficiency 94.68% and 
can be implemented in vehicles to reduce road mishaps.

## Preview
https://user-images.githubusercontent.com/96331104/155891753-7c80c040-454d-4b1e-b562-674f4fbc59eb.mp4

# Installations
Follow steps to use this project:

1. Clone repository
```
git clone https://github.com/YashBorikar/Driver-Drowsiness.git
```
2. Change directory to clone repository

```
cd Driver-Drowsiness
```
3. Create a Python virtual environment and activate it
```
$ virtualenv venv
```
```
$ source venv/bin/activate      # For Linux
$ venv\Scripts\activate         # For Windows
```
4. Install required libraries
```
pip install -r requirements.txt
```
# Getting Started
Run DrowsinessDetection.py
```
python DrowsinessDetection.py
```

# Results

<a href="https://colab.research.google.com/drive/12mKaPj5764tvnd5dBqjUZGDqT5cDN4Ma?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

 Training Accuracy: 94.68%, Training Loss: 13.83%, Testing Accuracy: 90.37%, Testing Loss: 24.10%

<p>
  <img src="Git Assets/Accuracy.png" width="400" alt="Accuracy">
</p>

Model has 95% accuracy for Driver Drowsiness Detection after training


# Connect me
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/yashborikar/)
