
def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"


def generate_subtitles(segments, output_file):

    with open(output_file, "w", encoding="utf-8") as f:

        for i, segment in enumerate(segments, start=1):

            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")