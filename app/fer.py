import cv2
import numpy as np
from typing import Dict
from tensorflow import keras
from tensorflow.keras.applications import xception


class FacialExpressionRecognizer():
    """
    Class for facial expression recognition
    """
    def __init__(self, model_path: str):
        """
        Constructor

        Args:
            model_path (str): path to facial expression recognizer model
        """
        # load pre trained facial expression recognizer model
        self.model: keras.Model = keras.models.load_model(model_path)


    def pre_process_image(self, img: np.ndarray) -> np.ndarray:
        """
        Method to preprocess image for model

        Args:
            img (np.ndarray): image

        Returns:
            np.ndarray: preprocessed image
        """
        # resize image
        preprocessed_img: np.ndarray = cv2.resize(img, (96,96))
        # transfrom image to grayscale
        preprocessed_img: np.ndarray = cv2.cvtColor(preprocessed_img,
                                                    cv2.COLOR_BGR2GRAY)
        # create 3 dimension grayscale image
        preprocessed_img: np.ndarray = cv2.cvtColor(preprocessed_img,
                                                    cv2.COLOR_GRAY2RGB)
        # preprocess image
        preprocessed_img: np.ndarray = xception.preprocess_input(
            preprocessed_img)
        return preprocessed_img
    

    def get_facial_expression_value(self, img: np.ndarray) -> int:
        """
        method to get image facial expression value

        Args:
            img (np.ndarray): image

        Returns:
            int: number between 0-6
        """
        return np.argmax(self.model.predict(np.asarray([img])),
                         axis=-1)[0]


    def get_facial_expression_label(self, img: np.ndarray) -> str:
        """
        method to get image facial expression label

        Args:
            img (np.ndarray): image

        Returns:
            str: facial expression label
        """
        # map of emotion value to string 
        emotion_map: Dict[int,str] = {0:"Angry", 1:"Disgust", 2:"Fear",
                                      3:"Happy", 4:"Sad", 5:"Surprise",
                                      6:"Neutral"}
        return emotion_map[self.get_facial_expression_value(img)]
