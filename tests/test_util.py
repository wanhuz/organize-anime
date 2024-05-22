from modules.util import Util
import unittest
import anitopy

class UtilTest(unittest.TestCase):
    
    def test_generate_anime_file_dest_path_episode(self):
        
        dest_path = "/home/user/download"
        anime_filename = '[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].mkv'
        anime_data = anitopy.parse(anime_filename)

        valid_anime_file_dest_path = "/home/user/download/Sousou no Frieren/[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].mkv"

        anime_file_dest_path = Util.generate_anime_file_dest_path(dest_path, anime_filename, anime_data)
        
        self.assertEqual(anime_file_dest_path, valid_anime_file_dest_path)

    def test_generate_anime_file_dest_path_episode_seasons(self):
        
        dest_path = "/home/user/download"
        anime_filename = '[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].mkv'
        anime_data = anitopy.parse(anime_filename)

        valid_anime_file_dest_path = "/home/user/download/Hibike! Euphonium S3/[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].mkv"

        anime_file_dest_path = Util.generate_anime_file_dest_path(dest_path, anime_filename, anime_data)
        
        self.assertEqual(anime_file_dest_path, valid_anime_file_dest_path)

    def test_extract_base_folder(self):
        anime_file_dest_path = "/home/user/download/Hibike! Euphonium S3/[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].mkv"
        valid_base_folder_path = "/home/user/download/Hibike! Euphonium S3"

        base_folder_path = Util.extract_base_folder(anime_file_dest_path)

        self.assertEqual(base_folder_path, valid_base_folder_path)

    def test_is_match_extension_one_file_type(self):
        anime_filename = '[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].mkv'
        exts = ['.mkv']

        self.assertTrue(Util.is_match_extension(anime_filename, exts))

    def test_is_match_extension_more_file_type(self):
        anime_filename = '[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].avi'
        exts = ['.mkv', '.avi']

        self.assertTrue(Util.is_match_extension(anime_filename, exts))

    def test_is_match_extension_not_match(self):
        anime_filename = '[SubsPlease] Hibike! Euphonium S3 - 03 (720p) [A8FA240A].avi'
        exts = ['.mkv']

        self.assertFalse(Util.is_match_extension(anime_filename, exts))