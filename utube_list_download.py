# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:00:28 2023

@author: abhia
"""
'''
##################################################
This script can be used to download a series of videos from a given list of link.
In this script we extract the list links form a column of an excel file.

Parameters: 
        1. filenmae        : Path of the video_list.xlx file from where the links will be extracted.
        2. columnname      : Name of the column which consists the video links in the video_list.xlx file 

Output:
        1. log_filename    : Name of the log file name whose suffix is dynamic based on the time of the execution of the code.
                             It consists the log of the downloaded videos and the downloads which failed with the error details.
        2. log_filenamecsv : list of the video with couldn't be downloaded.
        3. Downloded files and log files are saved in the same directory as that of this python script.
##################################################
'''

from pytube import YouTube

def Download(link):
    '''
    Downloads the youtube video with the given link and a custom filename
    '''
    youtubeObj = YouTube(link)
    youtubeObj = youtubeObj.streams.get_highest_resolution()
    try:
        youtubeObj.download(filename=str(apparant_index) +"-" + link_titles.values[i][0]+".mp4")
        #youtubeObj.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")



import pandas as pd
import time
import os 
import csv

filename= "D:/UNITN work/Video downloads/video_list.xls"
columnname= "Youtube_link"
utube_links = pd.read_excel(filename)[["Youtube_link"]]
link_titles = pd.read_excel(filename)[["Title"]]

log_filename = "Save_download_log"+ str(time.time()) + ".txt"
log_filenamecsv = "Not_downloaded_log"+ str(time.time()) + ".csv"

failed_indexes= []

start_index=0
for j in range(len(utube_links)):
    i=j+start_index
    apparant_index= i+1
    if os.path.isfile(str(apparant_index) +"-" + link_titles.values[i][0]+'.mp4'):
        txt= "\n"+ str(apparant_index)+ ": Download already found: "+ link_titles.values[i][0]
        print(txt)
        txtfile = open(log_filename,"a+") 
        try:
            txtfile.write(txt)
        except:
            pass
        

    else:
        try:
            #i=j
            print(apparant_index, ": Trying to download: ", link_titles.values[i][0])
            Download(utube_links.values[i][0])
            
            txt= "\n"+ str(apparant_index)+ ": Download successfull: "+ link_titles.values[i][0]
            txtfile = open(log_filename,"a+") 
            try:
                txtfile.write(txt)
            except:
                pass
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            txt= "\n"+str(apparant_index)+ ": Download failed: "+ link_titles.values[i][0]
            txtfile = open(log_filename,"a+") 
            try:
                txtfile.write(txt)
            except:
                pass
            try:
                print(apparant_index, ": Trying to download again: ", link_titles.values[i][0])
                Download(utube_links.values[i][0])
                
                txt= "\n"+str(apparant_index)+ ": Download successfull: "+ link_titles.values[i][0]
                txtfile = open(log_filename,"a+") 
                try:
                    txtfile.write(txt)
                except:
                    pass
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                txt= "\n"+ str(apparant_index)+ ": Download failed again: "+ link_titles.values[i][0] +"\n"+ f"Unexpected {err=}, {type(err)=}"
                txtfile = open(log_filename,"a+") 
                txtfile.write(txt)
                failed_indexes.append(apparant_index)
                
                with open(log_filenamecsv, "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(failed_indexes)
         

txtfile = open(log_filename,"a+") 
txtfile.write("\nFailed indexes are: " + str(failed_indexes))

with open(log_filenamecsv, "w") as f:
    writer = csv.writer(f)
    writer.writerow(failed_indexes)

