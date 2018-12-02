# InstaPy

A simple script to download the most recent 20 pictures of the user using Instagram API and the user's access token.

Unfortunately, Instagram API is extremely limited in capability and you can no longer interact with other users.

Getting your own profile info and most recent content is about the limit of Instagram API functionality as of December 1st, 2018. 

Requires: Instagram Account

# Instruction for Use:

1) Clone the repository onto your personal computer.
2) Obtain your Instagram Access Token. Instruction can be found here: https://www.instagram.com/developer/authentication/
3) Open token.txt and replace the placeholder text with your access token, save file. 
4) Open constant.py in your text editor. Change USER value to a your name or a name that you would like to save under. Save file.
5) Run InstaPy.py using terminal in OSX or cmd (Command Prompt) in Windows. 

The script will create a folder in the script directory and download the maximum available resolution of your most recent twenty photos. 

# Notes:

You can run InstaPy.py everytime you upload a new post to Instagram, it identifies each image using a unique server side name and won't replace or delete them with subsequent runs of the script, including when more recent images are available. 
