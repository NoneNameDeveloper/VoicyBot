import subprocess


class Converter:

    def __init__(self):
        pass

    def ogg2wav(self, path_to_ogg: str, path_to_wav: str) -> str:
        """
        converting .ogg from telegram to .wav 
        using ffmpeg and subprocess to call ii

        Args:
            path_to_ogg (str): path to your .ogg/.oga file
            path_to_wav (str): path to your .wav file
        
        Returns:
            str: path_to_wav
        """

        # converting using ffmpeg
        subprocess.call(["ffmpeg", "-loglevel", "warning", "-i", path_to_ogg, path_to_wav])

        return path_to_wav

