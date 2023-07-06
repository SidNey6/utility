import os

folders = ["Images", "Videos", "Documents", "IT", "Other"]

# check if a list of folders exist, and if not, create them
def check_folders_exist(folders):
    # get the path to my desktop
    desktop_path = os.path.expanduser("~/Desktop")
    # get all the files on my desktop
    files_on_desktop = os.listdir(desktop_path)
    # check if the folders exist
    for folder in folders:
        if folder not in files_on_desktop:
            # create the folder
            os.mkdir(desktop_path + "/" + folder)

# create a function that moves all the files on my desktop to the correct folder
def move_files_to_correct_folder():
    # get the path to my desktop
    desktop_path = os.path.expanduser("~/Desktop")
    # get all the files on my desktop
    files_on_desktop = os.listdir(desktop_path)
    # move the files to the correct folder
    for file in files_on_desktop:
        if file not in folders:
            # move the file to the correct folder
            # check if the file is an image
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".gif"):
                os.rename(desktop_path + "/" + file, desktop_path + "/" + "Images" + "/" + file)
            # check if the file is a video
            elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi"):
                os.rename(desktop_path + "/" + file, desktop_path + "/" + "Videos" + "/" + file)
            # check if the file is a document
            elif file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt") or file.endswith(".xlsx") or file.endswith(".csv"):
                os.rename(desktop_path + "/" + file, desktop_path + "/" + "Documents" + "/" + file)
            # check if the file is an IT file
            elif file.endswith(".py") or file.endswith(".js") or file.endswith(".html") or file.endswith(".css"):
                os.rename(desktop_path + "/" + file, desktop_path + "/" + "IT" + "/" + file)
            # check if the file is a folder, if yes, do nothing
            elif os.path.isdir(desktop_path + "/" + file):
                pass
            # move the file to the other folder
            else:
                os.rename(desktop_path + "/" + file, desktop_path + "/" + "Other" + "/" + file)
