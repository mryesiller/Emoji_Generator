from PIL import Image

import numpy as np

import os

from random import randint

dirname = os.path.dirname(__file__)

dimensions = 480, 480        #resize 24x24 to 480x480

for x in range(0,30):        #Number of generated pictures     
    
    
    f = randint(0, 1000)     #Common-Rare-Epic-Legendary
    if f > 400:            
        bw = (255, 255, 255) #Borders-inside
        bg = (255, 255, 255) #Background       
        bc = (0, 0, 0)       #Borders-outside
        eb = (0,0,0)         #Face   
    elif 400 >= f > 47:
        bw = (255, 255, 255)
        bg = (255, 255, 204)
        bc = (31, 57, 186)
        eb = (0,0,0)
    elif 47 >= f > 7:
        bw = (255, 255, 255)
        bg = (255, 255, 102)
        bc = (186, 31, 160)
        eb = (0,0,0)
    else: 
        bw = (255, 255, 255)       
        bg = (255, 51, 255)
        bc = (226, 144, 21)
        eb = (0,0,0)   
                  
    emoji = [
        [bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc],
        [bc, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bc],
        [bc, bw, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, bg, bg, eb, eb, eb, eb, eb, eb, eb, eb, bg, bg, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bw, bc],
        [bc, bw, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bw, bc],
        [bc, bw, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bw, bc],
        [bc, bw, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bg, bg, bg, eb, bg, bg, bg, bg, bg, bw, bc],
        [bc, bw, bg, bg, bg, bg, bg, bg, eb, eb, eb, eb, eb, eb, eb, eb, bg, bg, bg, bg, bg, bg, bw, bc],
        [bc, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bw, bc],
        [bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc]
    ] 


    #mouth settings
    mouth=randint(0, 1000)
    if mouth > 600:
        #straight mouth          
        emoji[16][9]=(0,0,0)
        emoji[16][10]=(0,0,0)
        emoji[16][11]=(0,0,0)
        emoji[16][12]=(0,0,0)
        emoji[16][13]=(0,0,0)
        emoji[16][14]=(0,0,0)
    elif 600 >= mouth > 247:
        #upset
        emoji[15][10]=(0,0,0)
        emoji[15][11]=(0,0,0)
        emoji[15][12]=(0,0,0)
        emoji[15][13]=(0,0,0)
        emoji[16][9]=(0,0,0)
        emoji[17][8]=(0,0,0)
        emoji[16][14]=(0,0,0)
        emoji[17][15]=(0,0,0)  
    elif 247 >= mouth > 107:
        #smile
        emoji[17][10]=(0,0,0)
        emoji[17][11]=(0,0,0)
        emoji[17][12]=(0,0,0)
        emoji[17][13]=(0,0,0)
        emoji[16][9]=(0,0,0)
        emoji[15][8]=(0,0,0)
        emoji[16][14]=(0,0,0)
        emoji[15][15]=(0,0,0)
    elif 107 >= mouth > 17:
        #circle mouth        
        emoji[18][10]=(0,0,0)
        emoji[18][11]=(0,0,0)
        emoji[18][12]=(0,0,0)
        emoji[18][13]=(0,0,0)
        emoji[17][9]=(0,0,0)
        emoji[16][9]=(0,0,0)
        emoji[17][14]=(0,0,0)
        emoji[16][14]=(0,0,0)
        emoji[15][9]=(0,0,0)
        emoji[14][10]=(0,0,0)
        emoji[14][11]=(0,0,0)
        emoji[14][12]=(0,0,0)
        emoji[14][13]=(0,0,0)
        emoji[15][14]=(0,0,0)    
    else: 
        #grin 
        emoji[18][10]=(0,0,0)
        emoji[18][11]=(0,0,0)
        emoji[18][12]=(0,0,0)
        emoji[18][13]=(0,0,0)
        emoji[17][9]=(0,0,0)
        emoji[16][8]=(0,0,0)
        emoji[17][14]=(0,0,0)
        emoji[16][15]=(0,0,0)
        emoji[15][7]=(0,0,0)
        emoji[15][16]=(0,0,0)
        emoji[14][7]=(0,0,0)
        emoji[14][16]=(0,0,0)
        emoji[14][8]=(0,0,0)
        emoji[14][9]=(0,0,0)
        emoji[14][10]=(0,0,0)
        emoji[14][11]=(0,0,0)
        emoji[14][12]=(0,0,0)
        emoji[14][13]=(0,0,0)
        emoji[14][14]=(0,0,0)
        emoji[14][15]=(0,0,0)
        emoji[15][10]=(0,0,0)
        emoji[15][13]=(0,0,0)


    #eye settings
    eye=randint(0, 1000)
    if eye > 600:            
        #straight eyes
        emoji[9][7]=(0,0,0)
        emoji[9][8]=(0,0,0)
        emoji[9][9]=(0,0,0)
        emoji[9][10]=(0,0,0)
        emoji[9][16]=(0,0,0)
        emoji[9][15]=(0,0,0)
        emoji[9][14]=(0,0,0)
        emoji[9][13]=(0,0,0)
    elif 600 >= eye > 247:
        #down eyes    
        emoji[10][7]=(0,0,0)
        emoji[11][7]=(0,0,0)    
        emoji[11][8]=(0,0,0)
        emoji[11][9]=(0,0,0)
        emoji[11][10]=(0,0,0)       
        emoji[10][10]=(0,0,0) 
        #-------------------    
        emoji[10][13]=(0,0,0)
        emoji[11][13]=(0,0,0)    
        emoji[11][14]=(0,0,0)
        emoji[11][15]=(0,0,0)
        emoji[11][16]=(0,0,0)       
        emoji[10][16]=(0,0,0)
    elif 247 >= eye > 107:       
        #single eyebrow eyes
        emoji[11][7]=(0,0,0)
        emoji[10][7]=(0,0,0)
        emoji[9][8]=(0,0,0)
        emoji[9][9]=(0,0,0)
        emoji[9][10]=(0,0,0)
        emoji[10][11]=(0,0,0)
        emoji[11][11]=(0,0,0)
        emoji[11][16]=(0,0,0)
        emoji[10][16]=(0,0,0)
        emoji[9][15]=(0,0,0)
        emoji[9][14]=(0,0,0)
        emoji[9][13]=(0,0,0)
        emoji[10][12]=(0,0,0)
        emoji[11][12]=(0,0,0)
    else:
       #circle eyes
        emoji[8][8]=(0,0,0)
        emoji[8][9]=(0,0,0)
        emoji[8][10]=(0,0,0)
        emoji[8][7]=(0,0,0)
        emoji[9][7]=(0,0,0)
        emoji[10][7]=(0,0,0)
        emoji[11][7]=(0,0,0)    
        emoji[11][8]=(0,0,0)
        emoji[11][9]=(0,0,0)
        emoji[11][10]=(0,0,0)       
        emoji[10][10]=(0,0,0)
        emoji[9][10]=(0,0,0)
        #-------------------
        emoji[8][13]=(0,0,0)
        emoji[8][14]=(0,0,0)
        emoji[8][15]=(0,0,0)
        emoji[8][16]=(0,0,0)
        emoji[9][13]=(0,0,0)
        emoji[10][13]=(0,0,0)
        emoji[11][13]=(0,0,0)    
        emoji[11][14]=(0,0,0)
        emoji[11][15]=(0,0,0)
        emoji[11][16]=(0,0,0)       
        emoji[10][16]=(0,0,0)
        emoji[9][16]=(0,0,0)     
    
    

    pixels=emoji

    array = np.array(pixels, dtype=np.uint8)

    
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/emoji_images/' + (str(x)) + '.png'
    new_image.save(imgname) 
  