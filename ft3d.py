from math import atan2;import cv2 ;from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from threading import Thread 

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

app = Ursina(); Sky(texture='sky')

def update():
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(faces):
        x = faces[0][0]+faces[0][2]/2
        y = faces[0][1]+faces[0][3]/2
        rot_x=atan2(y-320,320)*180/3
        rot_y=atan2(x-240,240)*-180/3 +20
        cube.rotation = (rot_x, rot_y, 0)
        cube.position = (-rot_y/100, -rot_x/100, 0)

def close():    video_capture.release();cv2.destroyAllWindows()

def input(key): 
    if key == 'escape': close();quit()

cube = Entity(model='cube', texture='brick', 
scale=1, collider='box', position=(0, 0, 0))
cube.shader = bls; camera.position =(0,0,-5)
app.run()


