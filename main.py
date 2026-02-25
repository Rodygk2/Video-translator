from src.extract_audio import extract_audio
from src.speech_to_text import transcribe
from src.translate_text import translate
from src.subtitle_generator import generate_subtitles

VIDEO_PATH = "videos/video.mp4"
AUDIO_PATH = "audio/audio.wav"

TRANSCRIPT = "outputs/transcripts/text.txt"
TRANSLATION = "outputs/translations/translated.txt"
SUBTITLE_FILE = "outputs/subtitles/subtitles.srt"


def main():

    print("Extraction audio...")
    extract_audio(VIDEO_PATH, AUDIO_PATH)

    print("Transcription...")
    result = transcribe(AUDIO_PATH)

    text = result["text"]
    lang = result["language"]
    segments = result["segments"]

    print("Langue détectée :", lang)

    print("Sauvegarde transcription...")
    with open(TRANSCRIPT, "w", encoding="utf-8") as f:
        f.write(text)

    print("Traduction...")
    translated = translate(text, lang)

    with open(TRANSLATION, "w", encoding="utf-8") as f:
        f.write(translated)

    print("Génération sous-titres...")
    generate_subtitles(segments, SUBTITLE_FILE)

    print("Terminé !")


if __name__ == "__main__":
    main()