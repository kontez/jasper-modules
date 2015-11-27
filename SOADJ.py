# -*- coding: utf-8-*-

#SYSTEM ORDER ANTI DISORDER for JASPER 0.1
#stupid name 'cuz i like system of a down, ok?
#Kn0t - kontez

import re
import os
import time

WORDS = ["ORDER"]

dir = "/home/pi/Files"  # directory

def documents():
    fil_ext = ['txt','pdf','odt','ods','odp','odb','doc','docx','csv','sgml','rtf','xls']
    dir = "Documents"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def images():
    fil_ext = ['jpg','png','gif', 'bmp','jpeg','pict','tiff']
    dir = "Images"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def archives():
    fil_ext = ['iso','rar','zip','tar','tar.gz','tar.bz2','tgz','tar.lzma','bz2','gz','jar','7z','arc','arj','ace','lha','mdf']
    dir = "Archives"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def scripts():
    fil_ext = ['py','pl','bs','sh','rb','pas','c','o','cpp','asm','bas','cs','h','java',]
    dir = "Scripts"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def logs():
    fil_ext = ['log','bak']
    dir = "Logs"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def webpages():
    fil_ext = ['php','asp','js','html','htm','shtml','shtm','stm','aspx','css','xml']
    dir = "Webpages"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def songs():
    fil_ext = ['mp1','mp2','mp3','m4a','wma','wav','flac','ogg']
    dir = "Music"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def video():
    fil_ext = ['avi','dvx','mpeg','wmv','mp4','mkv']
    dir = "Video"
    for i in fil_ext:
        os.system("mv *."+i+" "+dir)

def other():
    dir = "Other"
    os.system("mv *.* "+dir)

def downloads():
    os.chdir("Downloads")
    os.system("mv * ..")
    os.chdir(dir)
    



def handle(text, mic, profile):
    """
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("Cleaning started...")
    time.sleep(3) # actually not for the lulz - had issues without it idk

    os.chdir(dir)
    downloads()
    documents()
    images()
    archives()
    scripts()
    logs()
    webpages()
    songs()
    video()
    other()

    mic.say("All cleaned up.")

    
def isValid(text):
    """
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\border\b', text, re.IGNORECASE))
