import gdown
import os
import shutil
def download():
    url = 'https://drive.google.com/drive/u/0/folders/1vR4DmsbhnV0i4x8ShIVt070_ebVIdlYv'
    gdown.download_folder(url)
    for root, dirs, files in os.walk('D:\\Face_Detection_For_Attendance'):
        os.chdir(root)
        if root != 'D:\\6=':
            for file in files:
                if file.endswith('.jpg') or file.endswith('.jpeg'):
                    if file != "bg.jpg":
                        print(root)
                        print(file)
                        source = 'D:\\Face_Detection_For_Attendance' + "\\" + file
                        destination = root + "\\" + "ImagesAttendance"
                        print(destination)
                        shutil.copy(source, destination)
                        os.remove(source)
download()