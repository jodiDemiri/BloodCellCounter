import argparse
import io
from PIL import Image
import datetime
import torch
import cv2
import numpy as np
from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for, Response
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
from subprocess import Popen
import re
import requests
import shutil
import time
import yolov5.detect as dt
import pandas as pd

app = Flask(__name__) 

uploads_dir = './uploads'


def get_yolov5():
    model = torch.hub.load('/Users/jodigarcia/Downloads/web_app/yolov5', 'custom', path='/Users/jodigarcia/Downloads/web_app/yolov5/yolov5s.pt', source= 'local')
    return model



model = get_yolov5()



@app.route("/")
def hello_world():
    return render_template('index.html')


    
@app.route("/", methods=["GET", "POST"])
def predict_img():
    if request.method == "POST":
        # filepath = '/Users/jodigarcia/Downloads/web_app/runs/detect/uploads'
        file = request.files['image']
        file.save(os.path.join(uploads_dir, file.filename))
        # input_image = Image.open(io.BytesIO(file))
        # print(input_image.getdata())
        data = dt.run(source= os.path.join(uploads_dir, file.filename))
        img_path = os.path.join(data, file.filename)
        cell_count_base_filename = os.path.splitext(file.filename)[0]
        cell_count_path =  str(data) + '/labels/' + cell_count_base_filename + '.csv'

        # column_names=['Names','R','L','BL','BR']
        # df = pd.read_csv(cell_count_path, names= column_names)

        labels_list = []
        with open(cell_count_path) as f:
            for row in f:
                labels_list.append(row.split()[0])

        
        platelets_count = labels_list.count('0')
        RBC_count = labels_list.count('1')
        WBC_count = labels_list.count('2')


    
    return render_template('result.html', res = img_path, pCount = platelets_count, rCount = RBC_count, wCount = WBC_count)



if __name__ == "__main__":
    

    app.run(debug=True)  # debug=True causes Restarting with stat













# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
       
#         return render_template('result.html', )
    
#     # Mostrar página de carga de imagen
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True)

