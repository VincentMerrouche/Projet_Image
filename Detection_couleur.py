#Importations des librairies
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
from PIL.Image import * 

#Lecture de l'image 
Chemin="Images_Resistance/resistance_1.png"

Image_Couleur=open(Chemin)
Image_Forme= cv2.imread(Chemin) 
cv2.imshow('myimage',Image_Forme)
cv2.waitKey(2000)
cv2.destroyImage('myImage')