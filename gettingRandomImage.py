import urllib.request
import os
import re
def save_as(file_name):
    ''' File exists '''
    if(os.path.exists(file_name)):
        print("File already exists...")
        print("Renaming file...")
        ''' Repeat until the file name is unique so it does not overwrite '''
        while(os.path.exists(file_name)):
            ''' File name does not have a number '''
            if not (re.search(r'\d+', file_name)):
                ''' Assign a number '''
                new_file_name = file_name.split(".")[0] + "0.png"
                file_name = new_file_name
                new_file_name = re.search(r'\d+', file_name).group()
            else:
                    ''' File name already has a number '''
                    new_file_name = re.search(r'\d+', file_name).group()
                    ''' Increment file name number.
                    For instance, xxx9 -> xxx10 '''
                    file_name = file_name.replace(new_file_name,str(int(new_file_name) + 1))
                    ''' Check if it is a unique name '''
                    if not(os.path.exists(file_name)):
                        print("New file has been saved as ", file_name)
                        return file_name
    else:
        ''' Valid file name'''
        print("New image file created as ", file_name)
        return file_name
        ''' Request images from a url '''
urllib.request.urlretrieve("https://picsum.photos/256/256/?random", save_as("pub.png") )
urllib.request.urlretrieve("https://picsum.photos/256/256/?random", save_as("pk.png"))