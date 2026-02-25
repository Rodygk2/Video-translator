import subprocess

def embed_subtitles(video, subtitles, output):
    command = [
        "ffmpeg",
        "-i", video,
        "-i", subtitles,
        "-c", "copy",
        "-c:s", "mov_text",
        output
    ]

    subprocess.run(command, check=True)