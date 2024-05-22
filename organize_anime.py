#!/usr/bin/python
import os
import anitopy
import logging
from modules.mover import Mover
from modules.util import Util
from yaml import safe_load as yaml_safe_load

logging.basicConfig(
    filename="organise_anime.log", 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    with open('config.yaml', 'r') as file:
        config = yaml_safe_load(file)
except IOError:
    exit('Config.yaml file could not be found. Create yaml file using config_example.yaml')

SRC_PATH = config['options']['src_path']
DEST_PATH = config['options']['dest_path']
exts = config['options']['extension_to_organize']

mover = Mover(SRC_PATH, DEST_PATH)

for file in os.listdir(SRC_PATH):
    if (Util.is_match_extension(file, exts)):
        logging.info(file + " detected")

        anime_data = anitopy.parse(file)
        mover.move_file(file, anime_data)
    elif(os.path.isdir(SRC_PATH + "/" + file)):
        logging.info(file + " detected")

        mover.move_directory(file)