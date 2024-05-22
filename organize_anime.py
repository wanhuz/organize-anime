#!/usr/bin/python
import os
import anitopy
import logging
from modules.mover import Mover
from modules.util import Util

logging.basicConfig(
    filename="organise_anime.log", 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s')

SRC_PATH = "/home/user/src"
DEST_PATH = "/home/user/dest"
exts = ['.mkv']

mover = Mover(SRC_PATH, DEST_PATH)

for file in os.listdir(SRC_PATH):
    if (Util.is_match_extension(file, exts)):
        logging.info(file + " detected")

        anime_data = anitopy.parse(file)
        mover.move_file(file, anime_data)
    elif(os.path.isdir(SRC_PATH + "/" + file)):
        logging.info(file + " detected")

        mover.move_directory(file)