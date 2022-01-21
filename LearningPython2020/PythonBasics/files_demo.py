# --------------------------------
# Working with Files
# - Reading and Writing Files 
# - OS Path   
# --------------------------------

import os
from os import path 
import datetime 
from datetime import date, time, timedelta
import time 
import shutil 
from shutil import make_archive
from zipfile import ZipFile

# Writing Data to a Text File
# ---------------------------------
def write_demo():
    # open a file or creating if it doesn't exist
    my_file = open("demofile.txt", "w+")

    # write lines to the demo text file
    for n in range(5):
        my_file.write(f"This is line {n+1} \n")

    # close the file when done 
    my_file.close()

# Appending Data to a Text File 
def append_demo():
    # open file we want to append to 
    my_file = open("demofile.txt", "a")
    
    # write lines to append to the demo text file 
    for n in range(5):
        my_file.write(f"The is an appended line {n+1}\n")

    # close the file when done 
    my_file.close()

# Reading Data from a Text File 
def read_demo():
    # try to open file for read access 
    try: 
        my_file = open("demofile.txt", "r")
        # read lines in file
        lines = my_file.readlines()
        for line in lines: 
            print(line)
        my_file.close()
    except: 
        print("Cannot find demo file")

# OS Path Utilities 
# --------------------------------
# example working with os.path module 
def os_demo():
    # show the name of the os 
    print(os.name)

    # make a demo file
    f = open("demofile.txt", "w")
    f.close() 
    # check if the file exists, is a file
    print("Does the item exist?", str(path.exists("demofile.txt")))
    print("Is the item a file?", str(path.isfile("demofile.txt")))

    # file modification time 
    t = time.ctime(path.getmtime("demofile.txt"))
    print(f"Modification Time: {t}")

    # remove the file 
    os.remove("demofile.txt")
    print("Does the item exist?", str(path.exists("demofile.txt")))
    
# Shell Utilities, shutil 
# ---------------------------------
def shutil_demo():
    # make demo file to work with 
    f = open("demo.txt", "w")
    f.close() 

    # make duplicate of existing file 
    if path.exists("demo.txt"):
        
        # get the path of the file in current directory 
        src = path.realpath("demo.txt")

        # destination for copy w/ backup name 
        dst = src + ".bak"

        # copy file with shutil 
        shutil.copy(src, dst)
        # copy permissions, modification times, other info
        shutil.copystat(src, dst)

        # rename original demo file 
        os.rename("demo.txt", "first_demo.txt")

        # put EVERYTHING into a ZIP archive 
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        # control over ZIP files 
        # we only want the demo.txt and backup in zip archive
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("first_demo.txt")
            newzip.write("demo.txt.bak")


    # remove all the files we just made 
    os.remove("testzip.zip")
    os.remove("first_demo.txt")
    os.remove("demo.txt.bak")
        

