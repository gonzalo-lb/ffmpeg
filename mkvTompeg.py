import os
import ffmpeg

start_dir = os.getcwd()

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

for path, folder, files in os.walk(start_dir):
    for file in files:
        if file.endswith('.mkv'):
            print("Found file: %s" % file)
            convert_to_mp4(os.path.join(start_dir, file))
        else:
            pass