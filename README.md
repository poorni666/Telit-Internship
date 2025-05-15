# S.P.A.C.E

**S.P.A.C.E** is a computer vision project focused on object detection for smart parking applications. It performs parking lot detection and vehicle classification using a lightweight CNN model optimized for Edge AI deployment. The solution runs on the **ALIF E7 processor**, making it suitable for real-time inference in resource-constrained environments.

---

## 🛠 Prerequisites

All the files are organized in the **master** branch, refer to the navigation directory to know how to navigate the respo:

- Python 3.7  
- TensorFlow 2.11  
- ALIF E7 Processor for Edge AI Deployment

---

## 📁 Dataset

Dataset is in the drive : 



### 📋 Steps

- **Step 1** : Clone the repository 
- **Step 2**: Set up the environment using Docker or .venv with prerequisites  
- **Step 3**: Navigate to `models/research/object_detection`  
- **Step 4**: Refer to the `SSD.ipynb` notebook for training instructions in the path  
  `/research/object_detection/colab_notebooks`  
- **Step 5**: Set up and install the TensorFlow Object Detection API within the training  
  notebook `SSD.ipynb`  
- **Step 6**: Configure the SSD Mobilenet V2 FPNLite pipeline  
- **Step 7**: Follow the complete inference guide for testing procedures.  
- **Step 8** : Model Conversion of Tflite  
