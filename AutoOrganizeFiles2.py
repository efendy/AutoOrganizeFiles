#!/usr/bin/python

import os, sys, time
from pathlib import Path

SCRIPT_NAME = os.path.basename(__file__)
INTERVAL = 5
KIND = {
    "Image": ["png", "jpg", "jpeg", "gif", ""],
    "Video": ["mp4"],
    "Audio": ["acc", "mp3"],
    "Subtitle": ["srt", "vtt", "webvtt", "dfxp"],
    "Stream": ["m3u8", "mpd", "ism", "f4m"],
    "Installer": ["dmg", "exe", "msi"],
    "Document": ["xlsx", "xls"],
    "Text": ["csv", "txt"],
    "XML": ["xml"]
}

def process(directorypath):
    path = Path(directorypath)
    for file in path.iterdir():
        filenamesplit = file.name.split(".")
        if len(filenamesplit) > 1:
            fileext = filenamesplit[-1].lower()
            subdir = directorypath + "/" + fileext
            if not os.path.isdir(subdir):
                os.mkdir(subdir)
            src_file = directorypath + "/" + file.name
            dst_file = subdir + "/" + file.name
            os.rename(src_file, dst_file)

def run(directorypath):
    if not os.path.isdir(directorypath):
        print("Error: {} does not exist.".format(directorypath))
        help()
        sys.exit(2)
    while(True):
        process(directorypath)
        time.sleep(INTERVAL)

def help():
    print("")
    print("Usage: {} <directory_path>".format(SCRIPT_NAME))
    print(" i.e: python3 {} ~/Downloads/".format(SCRIPT_NAME))
    print("- end -")

def main(argv):
    if len(argv) == 1:
        directorypath = argv[0]
        run(directorypath)
        sys.exit()
    help()

if __name__ == "__main__":
   main(sys.argv[1:])
   