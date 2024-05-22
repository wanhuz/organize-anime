#!/usr/bin/python
import os
import anitopy
import re
import logging

logging.basicConfig(
    filename="organise_anime", 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s')

def moveFile(file, file_data):
   full_series_path, file_path, new_file_path = generate_new_path(file_data)

   logging.info("Moving " + file)
   logging.info("Folder destination: " + full_series_path)
   logging.info("File source: " + file_path)
   logging.info("File destination: " + new_file_path)

   if not os.path.exists(full_series_path): 
       os.makedirs(full_series_path) # path to series
   os.rename(file_path, new_file_path)

def generate_new_path(file_data):
   series_name = file_data["anime_title"]
   if ("anime_season" in file_data):
       full_series_path = ANIME_PATH + "/" + series_name + " " + "S" + file_data["anime_season"]
   else:
       full_series_path = ANIME_PATH + "/" + series_name
   file_path = DOWNLOAD_PATH + "/" + file
   new_file_path = full_series_path + "/" + file

   return full_series_path, file_path, new_file_path

def moveFolder(folder):
   folder_path = DOWNLOAD_PATH + "/" + folder
   new_folder_path = ANIME_PATH + "/" + folder
   
   os.rename(folder_path, new_folder_path)

   logging.info("Moving " + folder)
   logging.info("Folder source: " + folder_path)
   logging.info("Folder destination: " + new_folder_path)

ANIME_PATH = "/home/user/myAnimeFolder"
DOWNLOAD_PATH = "/home/user/temp"

for file in os.listdir(DOWNLOAD_PATH):
    if (re.search(r'\.mkv$', file)):
        logging.info(file + " detected")
        file_data = anitopy.parse(file)
        moveFile(file, file_data)
    elif(os.path.isdir(DOWNLOAD_PATH + "/" + file)):
        logging.info(file + " detected")
        moveFolder(file)