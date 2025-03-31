Dependencies 
Set up : Clone the github respositary https://github.com/tensorflow/models.git and download the requirements from the nightly_requirements.txt  
colab : python 3.7 , tensorflow default version of colab , protobuf 3.19  
visual studio code : python 3.7.13, tensorflow 2.11, protobuf 3.19  

Protobuf Compilation
The Tensorflow Object Detection API uses Protobufs to configure model and training parameters. Before the framework can be used, the Protobuf libraries must be compiled. This should be done by running the following command from the tensorflow/models/research/ directory: protoc object_detection/protos/*.proto --python_out=.
