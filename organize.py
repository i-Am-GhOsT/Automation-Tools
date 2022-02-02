# Media Organizer

import os 
import shutil
from time import sleep

def make_folder(tempList,folder):
    for eachEle in tempList:
        if not os.path.isdir(os.path.join(folder,eachEle)):
            os.mkdir(os.path.join(folder,eachEle))
        else:
            print("[ "+eachEle+" ]!! Exits Already in "+folder+" Skipping !!")
    

def start_organize(PWD):
    while True:
        files = os.listdir(PWD)
        for file in files:
            if os.path.isfile(file) and file != "organizer.py":
                ext = (file.split(".")[-1]).lower()

                if ext in image_formats:
                    shutil.move(file,"Images/"+file)
                elif ext in audio_formats:
                    shutil.move(file,"Audios/"+file)
                elif ext in gif_formats:
                    shutil.move(file,"Gifs/"+file)                
                elif ext in video_formats:
                    shutil.move(file,"Videos/"+file)
                elif ext in file_formats:
                    shutil.move(file,"Files/"+file)
                elif ext in binary_formats:
                    shutil.move(file,"Softwares/"+file)
                else:
                    shutil.move(file,"Others/"+file)
        del files


# What Kind Of Format Needed To Be Foldered
formats = ["Images","Gifs","Audios","Videos","Softwares","Files","Others"]

## Different Types of Format for each object
image_formats = ["jpg","png","jgpeg","webp","tiff"]
gif_formats = ["gif","svg"]
audio_formats = ["mp3","wav"]
video_formats = ["mp4","avi","webm"]
file_formats = [".pdf",".txt",".docx",".md","ai","ait","txt","rtf","xlsx","csv"]
binary_formats = [".exe",".msi"]

# Present Working Directory
folder = os.getcwd()

#Making The Folder
make_folder(formats,folder)

# Running The Infinite Loop
start_organize(folder)
