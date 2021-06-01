close all;
clear variables;

%lecture de l'image 

image=imread('resistance_6.png'); %lecture de l'image

figure (1)
imshow(image)                %affichage de l'image
title('Résistance étudiée')


image2=rgb2gray(image); %image en gris
seuil = 190;
image2(image2<=seuil)=0;
image2(image2>seuil)=255;


figure (2)
imshow(image2);     %image avec bandes en noir:0 et le reste en blanc:255



%addition des deux images 
image_couleur = image - image2;

figure (3)
imshow(image_couleur); 