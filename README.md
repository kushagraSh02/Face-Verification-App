# Face-Verification-App
A Face Verification App using Siamese Neural Network Architecture.

A Siamese Neural Network is a class of neural network architectures that contain two or more identical subnetworks. Parameter updating is mirrored across both sub-networks. It is used to find the similarity of the inputs by comparing its feature vectors. Thus, we can train it to see if the two images are the same.

We use Face dataset to get images of random people to create negative samples and then collect some positive samples through our device webcam. Then we take some anchor images and create positive and negative labels for images to create our labeled dataset.

The embedding layer of model consists of 4 Convolutional, 3 Pooling and 1 Dense Layer. We have also created a custom Distance Layer for our Siamese model. We use Binary Cross-entropy as our loss function and Adam as our optimizer.

For the app, I have used Kivy library to create a basic app layout. We use openCV to get image from webcam and and use our pretrained model and a verification function to verify the person.

Lbraries Needed:
1. Tensorflow
2. Tensorflow-gpu
3. openCV
4. matplotlib

Face Dataset URL: http://vis-www.cs.umass.edu/lfw/

Note: we can also use Data augmentation to create more Accurate model for verification.

To run: First run the FaceDetection.ipynb file and create/save the siamesemodel.h5 file then paste the file in app folder to run the app correctly.
