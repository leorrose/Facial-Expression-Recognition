import os
import cv2
import numpy as np
import streamlit as st
from typing import List
from PIL import Image
from fer import FacialExpressionRecognizer

# get script directory
script_dir: str = os.path.dirname(os.path.realpath(__file__))
# get facial expression recognizer model path
fer_model_path: str = f"{script_dir}/models/model.h5"
# get face detection model path
cascade_model_path: str = f"{script_dir}/models/haarcascade_frontalface_default.xml"
# facial expression recognizer
fer: FacialExpressionRecognizer = FacialExpressionRecognizer(fer_model_path)
# face detection
classifier: cv2.CascadeClassifier = cv2.CascadeClassifier(cascade_model_path)

@st.cache(suppress_st_warning=True)
def classify_image(img: np.ndarray) -> np.ndarray:
    """[summary]

    Args:
        img (np.ndarray): [description]

    Returns:
        np.ndarray: [description]
    """
    # perform face detection
    bboxes: np.ndarray = classifier.detectMultiScale(img)

    # predict labels for each detected face
    labels: List[str] = []
    for box in bboxes:
        # extract
        x: int = 0
        y: int = 0
        w: int = 0
        h: int = 0
        x, y, w, h = box
        # crop image
        face: np.ndarray = img[y:y + h, x:x + w]
        # pre process image
        face: np.ndarray = fer.pre_process_image(face)
        # add facial expression label to labels
        labels.append(fer.get_facial_expression_label(face))

    # print bounding box and label 
    for index, box in enumerate(bboxes):
        # extract
        x: int = 0
        y: int = 0
        w: int = 0
        h: int = 0
        x, y, w, h = box
        # draw a rectangle over the img
        cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 1)
        # add prediction
        cv2.putText(img, labels[index], (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    # show the image
    return img


if __name__ == "__main__":
    # app title
    st.markdown("# Facial Expression Recognition")
    st.text("\n")
    st.text("\n")
    
    # app upload image for model
    st.markdown("### Upload Image")
    st.write(("Please upload an image for facial "
             "expression recognition."))
    uploaded_file: st.uploaded_file_manager.UploadedFile = st.file_uploader(
        "", type=['png', 'jpg', 'jpeg'])
    
    # app button to start facial expression recognition
    if st.button("Classify Facial Expression"):
        if uploaded_file is None:
            st.error("Please upload a image to classify")
        else:
            with st.spinner('Classifying ...'):
                st.image(classify_image(np.asarray(Image.open(uploaded_file))))
