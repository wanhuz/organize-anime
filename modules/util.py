
import os, re

class Util:

    def generate_anime_file_dest_path(dest_path, filename, anime_data):
        series_name = anime_data["anime_title"]

        if ("anime_season" in anime_data):
            target_series_path = dest_path + "/" + series_name + " " + "S" + anime_data["anime_season"]
        else:
            target_series_path = dest_path + "/" + series_name
        
        file_dest_path = target_series_path + "/" + filename

        return file_dest_path
    
    def extract_base_folder(path_to_file):
        path, filename = os.path.split(path_to_file)
        return path
        
    def is_match_extension(filename : str, exts : list):
        for ext in exts:
            ext = ext.replace('.', '')

            regex_to_search = '\.' + ext + r'$'
            if (re.search(regex_to_search, filename)):
                return True
        return False
        