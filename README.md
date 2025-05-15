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

Dataset is in the drive : https://drive.google.com/drive/folders/1mxb0ElnUcqMA5p3Koa6BcZG-fmnAKJfV?usp=drive_link



### 📋 Steps

- **Step 1** : Clone the repository  ``` https://github.com/tensorflow/models.git ```
- **Step 2**: Set up the environment using Docker or .venv with prerequisites  
- **Step 3**: Navigate to `models/research/object_detection`  
- **Step 4**: Refer to the `SSD.ipynb` notebook you can find it under `Downloads/Training notebook/SSD.ipynb` of master branch, follow the training instructions in that notebook  , Feel free to move this notebook to the directory in step 3 when you are done cloning.
- **Step 5**: Set up and install the TensorFlow Object Detection API within the training  
  notebook `SSD.ipynb`  
- **Step 6**: Configure the SSD Mobilenet V2 FPNLite pipeline  
- **Step 7**: Follow the complete inference guide for testing procedures in the notebook     ```
  cd Inference/SSD_Testing_Inference.ipynb   ```
- **Step 8** : Model Conversion of Tflite  

## Step 6: Configure the SSD Mobilenet V2 FPNLite Pipeline

This pipeline config can be found in the following directory in this master branch:

<pre> cd colab_notebooks/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8 </pre>

- Open the `pipeline.config` file and modify the following parameters to change paths directing to your custom dataset and fine-tuned checkpoints:
  - **fine_tune_checkpoint**: Set the path to the downloaded pre-trained model checkpoint.  
    Example:
    ```text
    fine_tune_checkpoint: "/path/to/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/model.ckpt"
    ```
  - **label_map_path**: Set the path to your label map file (e.g., `label_map.pbtxt`).
    ```text
    label_map_path: "/path/to/label_map.pbtxt"
    ```
  - **Training TFRecord Path**:
    ```protobuf
    train_input_reader {
      tf_record_input_reader {
        input_path: "/path/to/train_tfrecord"
      }
    }
    ```
  - **Validation TFRecord Path**:
    ```protobuf
    eval_input_reader {
      tf_record_input_reader {
        input_path: "/path/to/val_tfrecord"
      }
    }
    ```

