# Social-Network-Facial-Expression-Recognition

A social network facial expression recognition using deep learning based on FER2013 data set.

The target of this project is to create an application to classify the emotion from social network images.

This project was created with <b> Python(3.8.7), tensorflow, keras, streamlit, pandas, numpy and more libraries</b>.

## Project Research

In order to understand the steps and what we did you are welcome to look at [the research jupyter notebook](https://github.com/leorrose/Social-Network-Facial-Expression-Recognition/blob/main/Facial_Expression_Recognition.ipynb).

## Benchmarking on FER2013:
|Model                                                  |Data with disgust class|Data without disgust class|
|:------------------------------------------------------|:----------------------|:-------------------------|
|Transfer Learning using Xception                       |0.4078                 |0.4149                    |
|Transfer Learning + Fine Tuning using Xception         |0.6485                 |0.6517                    |
|Transfer Learning using ResNet152V2                    |0.3798                 |0.3898                    |
|Transfer Learning + Fine Tuning using ResNet152V2      |0.5551                 |0.2714                    |
|Transfer Learning using MobileNetV2                    |0.4013                 |0.3941                    |
|Transfer Learning + Fine Tuning using MobileNetV2      |0.4771                 |0.4675                    |
|Transfer Learning using EfficientNetB0                 |0.4084                 |0.4122                    |
|Transfer Learning + Fine Tuning using EfficientNetB0   |0.5856                 |0.5961                    |
|Transfer Learning using InceptionResNetV2              |0.4153                 |0.4235                    |
|Transfer Learning + Fine Tuning using InceptionResNetV2|0.4138                 |0.4154                    |
|Self Made CNN                                          |0.5857                 |0.5888                    |


## Project Setup and Run:
1. To Add
2. To Add
3. To Add
4. To Add

## Demo
[![Add Demo]("")


## Examples:
|Image|Emotion|
|:-------------------------:|:-------------------------:|
|To Add Image|To Add Label|
|To Add Image|To Add Label|
|To Add Image|To Add Label|
|To Add Image|To Add Label|
|To Add Image|To Add Label|
|To Add Image|To Add Label|



Please let me know if you find bugs or something that needs to be fixed.

Hope you enjoy.

## Citations

```
@MISC{Goodfeli-et-al-2013,
       author = {Goodfellow, Ian and Erhan, Dumitru and Carrier,
			Pierre-Luc and Courville, Aaron and Mirza, Mehdi and Hamner, 
			Ben and Cukierski, Will and Tang, Yichuan and Thaler,
			David and Lee, Dong-Hyun and Zhou, Yingbo and Ramaiah, 
			Chetan and Feng, Fangxiang and Li, Ruifan and Wang,
			Xiaojie and Athanasakis, Dimitris and Shawe-Taylor,
			John and Milakov, Maxim and Park, John and Ionescu,
			Radu and Popescu, Marius and Grozea, Cristian and Bergstra,
			James and Xie, Jingjing and Romaszko, Lukasz and Xu,
			Bing and Chuang, Zhang and Bengio, Yoshua},
     keywords = {competition, dataset, representation learning},
        title = {Challenges in Representation Learning: A report on three machine learning contests},
         year = {2013},
  institution = {Unicer},
          url = {http://arxiv.org/abs/1307.0414},
     abstract = {The ICML 2013 Workshop on Challenges in Representation
Learning focused on three challenges: the black box learning challenge,
the facial expression recognition challenge, and the multimodal learn-
ing challenge. We describe the datasets created for these challenges and
summarize the results of the competitions. We provide suggestions for or-
ganizers of future challenges and some comments on what kind of knowl-
edge can be gained from machine learning competitions.

http://deeplearning.net/icml2013-workshop-competition}
}

@inproceedings{BarsoumICMI2016,
    title={Training Deep Networks for Facial Expression Recognition with Crowd-Sourced Label Distribution},
    author={Barsoum, Emad and Zhang, Cha and Canton Ferrer, Cristian and Zhang, Zhengyou},
    booktitle={ACM International Conference on Multimodal Interaction (ICMI)},
    year={2016}
}
```
