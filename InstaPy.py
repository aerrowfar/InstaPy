"""
A simple script to download the latest 20 images from your Instagram profile using your own
access token.

"""

import os
from os import path
import json
import urllib
import constant



#Enter your name in constants.py located in directory or default will be used.
def main():

    url = constant.API_URL + get_token()
    webUrl = urllib.urlopen(url)
    #Checks to see if data was fetched succesfully.
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        create_folder()
        jsonresults(data)
    else:
        print("JSON data was not succesfully fetched, check token value.")
        exit(1)


# Gets your API access token from the token.txt file in directory.
def get_token():
    try:
        f = open("token.txt","r")
        #Checks for read access.
        if f.mode == 'r':
            token=f.read()
            return token
        else:
            print("Token file not readable.")
            exit(1)
        f.close()
    #if token is not found.
    except IOError:
        print ("Token file not found.")
        exit(1)


# Parses the JSON data from Instagram API for the highest resolution image URLs.
def jsonresults(data):
    json_data = json.loads(data)
    i = 0
    #Looping necessary since API return is an array turned list of dictionaries.
    for img in json_data['data']:
        #Grabbing the last part of the URL to capture the unique name assigned by server.
        word = img['images']['standard_resolution']['url'].split('/', 8)
        #Replacing any "/" from the old server naming convention with "-" so our
        #script does not trip up on "/" being folder paths.
        name = word[8].replace("/","-")
        imageDownload(name,img['images']['standard_resolution']['url'])


#Checks to see if a folder named after exists in directory, if not makes one.
def create_folder():
    #If folder exists, dont recreate it and wipe the existing content.
    if path.exists(constant.USER):
        pass
    else:
        os.mkdir(constant.USER)


#Downloads and renames images in order using the JSON URLs into the folder named after you.
def imageDownload(file_name, address):
    #ext = ".jpg"
    image = urllib.urlopen(address)
    # If a unique image has already been downloaded, dont replace it.
    if path.exists(constant.USER+'/'+file_name):
        print("An image was skipped.")
    else:
        output = open(constant.USER+'/'+file_name, "wb")
        output.write(image.read())
        output.close()


main()
