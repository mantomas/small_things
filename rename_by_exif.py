#!/usr/bin/env python3
"""
script to rename images in selected folder according to EXIF datetime_origin

depend on: 'exif' - pip3 install exif
usage: python3 rename_by_exif.py
"""

import os
import sys
import tkinter as tk
from datetime import datetime
from exif import Image
from tkinter import filedialog


def set_directory() -> str:
    """tkinter dialogue to select directory for processing

    return directory path as a string
    """
    path_find = tk.Tk()
    path_find.withdraw()
    path = tk.filedialog.askdirectory()
    if path:
        return path

    print("No directory selected!")
    sys.exit()


def exif_date_time(file_path: str) -> str:
    """retrieve EXIF informations from file

    return string in format: YYYY-mm-dd_HHMMSS
    return "missing exif" if not image or EXIF is missing
    """
    with open(file_path, "rb") as image_file:
        my_image = Image(image_file)
        try:
            exD = datetime.strptime(
                my_image.datetime_original,
                "%Y:%m:%d %H:%M:%S"
                )
            exif_date_time = datetime.strftime(exD, "%Y-%m-%d_%H%M%S")
            return exif_date_time
        except AttributeError:
            return "missing exif"


def exif_rename(folder_path: str, jpg: str, datetime: str) -> None:
    """rename one JPG file"""
    src = os.path.join(folder_path, jpg)  # old filename path
    dst = os.path.join(folder_path, datetime + ".jpg")
    os.rename(src, dst)


if __name__ == "__main__":
    is_jpg = (".jpg", ".jpeg")  # alowed file extensions
    processed = 0
    passed = 0
    duplicity = 0
    files_list_clear = []  # only JPG's
    folder_path = set_directory()  # call for folder selection dialogue
    files_list = os.listdir(folder_path)  # list files in directory
    if len(files_list) == 0:
        print("Empty directory")
    else:
        # clear list - only JPG files
        for file in files_list:
            try:
                extension = file[file.rindex("."):]
                if extension.lower() in is_jpg:
                    files_list_clear.append(file)
            except ValueError:
                continue
        # rename files if EXIF datetime find
        for jpg in files_list_clear:
            date_time = exif_date_time(os.path.join(folder_path, jpg))
            # skip no exif files
            if date_time == "missing exif":
                passed += 1
                pass
            # skip exif duplicity images (edited versions etc...)
            elif os.path.isfile(os.path.join(folder_path, date_time + ".jpg")):
                duplicity += 1
                pass
            # if all clear, rename file
            else:
                exif_rename(folder_path, jpg, date_time)
                processed += 1

        # final report
        if processed > 0:
            print("Images renamed: " + str(processed))
            print("Files skiped: " + str(passed))
            if duplicity > 0:
                print(
                    "There was "
                    + str(duplicity)
                    + " skiped images \nEXIF match, missing or file exist."
                )
        else:
            print(
                "No files out of "
                + str(len(files_list))
                + " processed. \nEXIF match, missing or file exist."
            )
