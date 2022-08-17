import os
from pytube import YouTube
import requests

try:
    os.mkdir("images")
except FileExistsError:
    pass
try:
    os.mkdir("videos")
except FileExistsError:
    pass
    repeat2 = True
    while repeat2:
        import os
        import shutil
        import time
        choice1 = input("1. Download files\n2. Delete files\n")

        if choice1 == "2":
            choice2 = input("1. Delete videos\n2. Delete thumbnails\n")
            if choice2 == "1":
                for root, dirs, files in os.walk("videos"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    time.sleep(2)
                    print("Files successfully deleted")
                    shutdown_choice = input("Do you want to shutdown this program?\n")
                    shutdown_choice = shutdown_choice.lower()
                    if shutdown_choice == "yes":
                        quit()
                        repeat2 = False

            elif choice2 == "2":
                for root, dirs, files in os.walk("images"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    time.sleep(2)
                    print("Files successfully deleted")
                    shutdown_choice = input("Do you want to shutdown this program?\n")
                    shutdown_choice = shutdown_choice.lower()
                    if shutdown_choice == "yes":
                        quit()
                        repeat2 = False

        elif choice1 == "1":
            repeat2 = False
        elif choice1 != "1" or "2":
            print("invalid input")
    repeat1 = True
    while repeat1:
        url = input("paste in ur video url: ")
        video = YouTube(url)
        thumbnail_link = video.thumbnail_url
        video_title = video.title
        symbols = '<>:"//|?*'
        new_video_title = ""
        for character in video_title:
            if not character in symbols:
                new_video_title += character
            else:
                pass

        choice = input("Is this the video you want?\n" + new_video_title + "\n")
        choice = choice.lower()
        if choice == "yes":
            repeat1 = False
        elif choice == "no":
            repeat1 = True
        elif choice != "yes" or "no":
            print("Invalid input")


    download_choice = input("What do you want to download\n1.Thumbnail\n2.Video\n")

    if download_choice == "1":
        img_data = requests.get(thumbnail_link).content
        with open(os.path.join("images", new_video_title + ".jpg"), 'wb') as handler:
            handler.write(img_data)
            print("Done!\nYour downloaded thumbnail is in the images folder")
            quit()

    my_video = video.streams.get_highest_resolution()
    my_video.download(output_path=r"videos")
    print("Done!\nYour downloaded video is in the videos folder!")
    size = my_video.filesize
    size = str(size)
    sliced_size = size[:-3]
    sliced_size = int(sliced_size)
    sliced_size = sliced_size / 1000
    sliced_size = str(sliced_size)
    print("Your video is: " + sliced_size + " MB")
    shutdown_choice = input("Do you want to shutdown this program?\n")
    shutdown_choice = shutdown_choice.lower()
    if shutdown_choice == "yes":
        quit()
        repeat2 = False
    elif shutdown_choice != "no" or "yes":
        print("invalid input")


