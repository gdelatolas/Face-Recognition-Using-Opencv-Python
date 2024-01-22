This project presents a face recognition system developed using the OpenCV library in Python. The system consists of three main scripts - datacollect.py, trainingdemo.py, and testmodel.py.

The datacollect.py script captures video from the default camera and employs a Haar Cascade Classifier to detect faces. Users are prompted to input their ID, and the script continuously captures grayscale face images, saving them in the './datasets' directory. The process is concluded after collecting 300 images or upon user interruption by pressing 'q'.

The trainingdemo.py script utilizes the LBPH Face Recognizer to train on the collected face data. Grayscale face images are loaded, converted to NumPy arrays, and associated with user IDs extracted from filenames. The trained model is saved to a file named "Trainer.yml."

The testmodel.py script captures video and uses the Haar Cascade Classifier for face detection. It loads the pre-trained LBPH Face Recognizer from the "Trainer.yml" file, predicts user IDs for detected faces, and displays rectangles around recognized faces along with corresponding names or labels them as "Unknown" based on a predefined confidence threshold.

The system provides an efficient and user-friendly approach to face recognition, making it applicable for various applications such as access control, security systems, and personalized user interfaces. The modular structure of the scripts allows for easy integration into different projects, and the reliance on open-source libraries like OpenCV ensures accessibility and adaptability.


The results:

<img width="403" alt="image" src="https://github.com/gdelatolas/Face-Recognition-Using-Opencv-Python/assets/62467773/7f21c4a2-3dc9-4062-84d2-89edc6f25f50">
