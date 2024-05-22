import os, logging
from modules.util import Util

logging = logging.getLogger()

class Mover:
    def __init__(self, src_path : str, dest_path : str):
        self.src_path = src_path
        self.dest_path = dest_path

    def move_directory(self, folder_name):
        src_dir_path = self.src_path + "/" + folder_name
        target_dest_folder_path = self.dest_path + "/" + folder_name
        
        os.rename(src_dir_path, target_dest_folder_path)

        logging.info("Moving " + folder_name)
        logging.info("Folder source: " + src_dir_path)
        logging.info("Folder destination: " + target_dest_folder_path)

    def move_file(self, filename, anime_data):
        src_file_path = self.src_path + "/" + filename
        target_dest_path_file = Util.generate_anime_file_dest_path(self.dest_path, filename, anime_data)
        target_dest_path_dir = Util.extract_base_folder(target_dest_path_file)

        logging.info("Moving " + filename)
        logging.info("File source: " + src_file_path)
        logging.info("File destination: " + target_dest_path_file)

        self.init_directory(target_dest_path_dir)
        os.rename(src_file_path, target_dest_path_file)
    
    def init_directory(self, dir_path):
        if not os.path.exists(dir_path): 
            os.makedirs(dir_path)