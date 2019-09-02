import os
import shutil

print("how may I help you !")
sourcepath= str(input("Enter the path from which you want to move:"))
sourcefiles = os.listdir(sourcepath)

destinationpath= sourcepath= str(input("Enter the path from which you want to move:"))
extension = str(input("Enter extension:"))

for file in sourcefiles:
    if file.endswith(extension):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    # elif file.endswith('.mp4') or file.endswith('.mpg') or file.endswith('.mpeg') or file.endswith('.swf') or file.endswith('.vob') or file.endswith('.wmv') or file.endswith('.3g2') or file.endswith('.3gp') or file.endswith('.asf') or file.endswith('.asx') or file.endswith('.avi') or file.endswith('.flv') or file.endswith('.m2ts') or file.endswith('.mkv') or file.endswith('.mov'):
       # shutil.move(os.path.join(sourcepath,file), os.path.join(destiMusicpath,file))
   # elif file.endswith('.doc') or file.endswith('.html') or file.endswith('.odt') or file.endswith('.pdf') or file.endswith('.xls') or file.endswith('.ods') or file.endswith('.ppt') or file.endswith('.txt'):
       # shutil.move(os.path.join(sourcepath,file), os.path.join(destiDocpath,file))
    #else:
        # shutil.move(os.path.join(sourcepath,file), os.path.join(destiOtherpath,file))



