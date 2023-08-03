#!/usr/bin/python
import os
import anitopy
import re
import logging
from datetime import datetime

def moveFile(file, file_data):
   series_name = file_data["anime_title"]
   if ("anime_season" in file_data):
       full_series_path = ANIME_PATH + "/" + series_name + " " + "S" + file_data["anime_season"]
   else:
       full_series_path = ANIME_PATH + "/" + series_name
   file_path = DOWNLOAD_PATH + "/" + file
   new_file_path = full_series_path + "/" + file

   logging.debug( getCurrentTime() + "Moving " + file)
   logging.debug( getCurrentTime() + "Folder destination: " + full_series_path)
   logging.debug( getCurrentTime() + "File source: " + file_path)
   logging.debug( getCurrentTime() + "File destination: " + new_file_path)

   if not os.path.exists(full_series_path):
       os.makedirs(full_series_path)
   os.rename(file_path, new_file_path)

def moveFolder(folder):
   folder_path = DOWNLOAD_PATH + "/" + folder
   new_folder_path = ANIME_PATH + "/" + folder
   os.rename(folder_path, new_folder_path)
   logging.debug( getCurrentTime() + "Moving " + folder)
   logging.debug( getCurrentTime() + "Folder source: " + folder_path)
   logging.debug( getCurrentTime() + "Folder destination: " + new_folder_path)

def getCurrentTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    finalString = dt_string + ":"
    return finalString

logging.basicConfig(filename="organise_anime.log", level=logging.DEBUG)
ANIME_PATH = "/home/user/myAnimeFolder"
DOWNLOAD_PATH = "/home/user/temp"

for file in os.listdir(DOWNLOAD_PATH):
    if (re.search(r'\.mkv$', file)):
        logging.debug( getCurrentTime() + file + " detected")
        file_data = anitopy.parse(file)
        moveFile(file, file_data)
    elif(os.path.isdir(DOWNLOAD_PATH + "/" + file)):
        logging.debug( getCurrentTime() + file + " detected")
        moveFolder(file)