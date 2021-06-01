#Importations des librairies
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
from PIL.Image import * 

#Lecture de l'image 
Chemin = "Images_Resistance/resistance_1.png"

<<<<<<< HEAD:Detection_couleur.py
Image_Couleur=open(Chemin)
Image_Forme= cv2.imread(Chemin) 
cv2.imshow('myimage',Image_Forme)
cv2.waitKey(2000)
cv2.destroyImage('myImage')
=======
Image_Couleur = open(Chemin)
Image_Forme = cv2.imread(Chemin) 
>>>>>>> b0f7f635aacba8ac67c9843a904524537b6d1532:Detection_couleur/Detection_couleur.py
