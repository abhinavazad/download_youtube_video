# download_youtube_video
This script can be used to download a series of videos from a given list of links. In this script we extract the list links form a column of an excel file.


## Parameters: 
###        1. filenmae       
Path of the video_list.xlx file from where the links will be extracted.
###        2. columnname      
Name of the column which consists the video links in the video_list.xlx file 

## Output:
###        1. log_filename    
Name of the log file name whose suffix is dynamic based on the time of the execution of the code.
It consists the log of the downloaded videos and the downloads which failed with the error details.
###        2. log_filenamecsv 
THe list of the video with couldn't be downloaded will reflect in the first row as column elements

Downloded files and log files are saved in the same directory as that of this python script.
