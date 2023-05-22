# BloodCellCounter
A web app developed using Flask that counts blood cells and displays the blood cell types through the use of computer vision techniques. 

On the backend, a pre-trained YOLOv5 model is utilized to detect and count the blood cells in each image. The images are passed to the detect.py file, then the results are saved locally and returned to the user. Locally, the resulting image showing the bounding boxes and class of each encountered cell is displayed, and a .txt file of the coordinates of each bounding box is also saved. On the frontend, the image returned from the YOLOv5 model is displayed with the bounding boxes and class of each encountered cell. In addition, the sum of each encountered cell type is displayed.
