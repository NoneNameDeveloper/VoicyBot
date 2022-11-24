import wave
import contextlib
import speech_recognition as sr


class Recognizer:

    def __init__(self):
        pass

    
    def _get_duration(self, path_to_wav: str) -> float:
        """
        getting .wav audio file duration

        Args:
            path_to_wav (str): path to wav audio file
        
        Returns:
            float: audio file duration
        """

        # opening filestream
        with contextlib.closing(wave.open(path_to_wav, "r")) as f:
            
            # getting frames
            frames = f.getnframes()

            # getting frames rate
            frames_rate = f.getframerate()

        return float(frames / frames_rate)


    def wav2text(self, path_to_wav: str, language: str = "ru") -> dict:
        """
        converting wav to text using google speech recognition 

        Args:
            path_to_wav (str): path to wav audio file
            language (str) : language for transcripting. Default RU.

        Returns:
            dict: {"transcription": text, "duration": 10 (s)}
        """

        # initializing speech recognition
        recognizer = sr.Recognizer()

        # creating AudioFile instance for manipulating
        audio_file = sr.AudioFile(path_to_wav)

        # recording source into AudioData instance
        with audio_file as source:
            data = recognizer.record(source)
        
        # getting duration with wave 
        duration = self._get_duration(path_to_wav=path_to_wav)

        try:
            # getting text transcription
            transcript = recognizer.recognize_google(data, language=language, pfilter=0) # , grammar='counting.gram') # key=None, language=language)

        except:
            transcript = "Не удалось распознать ;("

        return {"transcription": transcript, "duration": duration}

