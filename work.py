import os
import shutil
print("Welcome to self-organizer!")
sourcepath= str(input("Enter the path which you want to organize:"))
sourcefiles = os.listdir(sourcepath)

destiImagespath = str(input("Enter in which directory you want Images to move. By default, it is \"Images\":"))
if not destiImagespath:
    destiImagespath = "Images"
destiMusicpath = str(input("Enter in which directory you want Music to move. By default, it is \"Music\":"))
if not destiMusicpath:
    destiMusicpath = "Music"
destiDocpath = str(input("Enter in which directory you want Documents to move. By default, it is \"Documents\":"))
if not destiDocpath:
    destiDocpath = "Documents"
destiOtherpath = str(input("Enter in which directory you want Other files to move. By default, it is \"Others\":"))
if not destiOtherpath:
    destiOtherpath = "Others"
#destination path can be modified accordingly 


for file in sourcefiles:
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.jpeg'):
        if not destiImagespath in os.listdir(sourcepath):
            os.mkdir(os.path.join(sourcepath, destiImagespath))
        shutil.move(os.path.join(sourcepath,file), os.path.join(sourcepath, destiImagespath, file))
    elif file.endswith('.mp4') or  file.endswith('.mpg') or  file.endswith(".mpeg") or file.endswith(".swf") or file.endswith(".vob") or  file.endswith(".wmv") or  file.endswith(".3g2") or  file.endswith(".3gp") or  file.endswith(".asf") or  file.endswith(".asx") or  file.endswith(".avi") or file.endswith(".flv") or file.endswith(".m2ts") or file.endswith(".mkv") or  file.endswith(".mov"):
        if not destiMusicpath in os.listdir(sourcepath):
            os.mkdir(os.path.join(sourcepath, destiMusicpath))
        shutil.move(os.path.join(sourcepath,file), os.path.join(sourcepath, destiMusicpath, file))
    elif file.endswith('.doc') or file.endswith('.html') or file.endswith('.odt') or file.endswith('.pdf') or file.endswith('.xls') or file.endswith('.ods') or file.endswith('.ppt') or file.endswith('.txt'):
        if not destiDocpath in os.listdir(sourcepath):
            os.mkdir(os.path.join(sourcepath, destiDocpath))
        shutil.move(os.path.join(sourcepath,file), os.path.join(sourcepath, destiDocpath, file))
    else:
        if not destiOtherpath in os.listdir(sourcepath):
            os.mkdir(os.path.join(sourcepath, destiOtherpath))
        shutil.move(os.path.join(sourcepath,file), os.path.join(sourcepath, destiOtherpath, file))