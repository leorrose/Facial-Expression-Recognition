# set base image (host OS)
FROM python:3.8.7

# set the working directory in the container
WORKDIR /code

# copy files to the working directory
COPY app app
COPY requirements.txt .
COPY .streamlit .streamlit

# install dependencies
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libgl1-mesa-glx -y

# command to run on container start
CMD [ "streamlit", "run", "./app/fer_app.py"]