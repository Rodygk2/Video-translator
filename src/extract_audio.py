"""
extract_audio.py

Ce module extrait l'audio d'une vidéo grâce à FFmpeg.
"""

import subprocess


def extract_audio(video_path, output_audio_path):
    """
    Extrait l'audio d'une vidéo.

    Parameters
    ----------
    video_path : str
        chemin vers la vidéo
    output_audio_path : str
        chemin du fichier audio généré
    """

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",                 # pas de vidéo
        "-acodec", "pcm_s16le",
        "-ar", "16000",        # format optimal pour Whisper
        "-ac", "1",            # mono
        output_audio_path
    ]

    subprocess.run(command, check=True)