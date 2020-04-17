import sys

from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
#defines the menu function to list the options
def Main_Menu():
    #text to inform the user of options
    print(" Welcome")
    print("Please select one of the following options:")
    print("A) ADD NEW SAMPLE")
    print("B) START CAPTURE")
    print("C) EXIT")
    #stores the user's input in variable
    user_option=input()
    #call the function depending on the user's choice
    if(user_option=="A"or user_option=="a"):
        add_sample()
    elif(user_option=="B"or user_option=="b"):
        live_capture()
    elif(user_option=="C"or user_option=="c"):
        print("Program Quitting")
    else:
        #if user makes a selection not known by the program, user is prompted to try again
        print("Unknown Selection, Try Again")
        Main_Menu()
#defines add_sample function



###ask user to locate images they wish to add to the program
    ###once found encode the image and add to the text file
    ###loop back to menu once completed, add option to add another file - repeate the menu
    ###user needs to locate the file  


#may be worth adding the option to encode a new folder?? if time is left
def add_sample():
    #
    ###used to find the file where the images are stored in, so instead of using args get the user to input the address of the picture,
    ###like where it is stored ect
    print("---Before continuing make sure the image you wish to add is placed in the same folder as the Program---")
    ###here
    #imagePaths = list(paths.list_images(args["dataset"]))

    
    
    imagePath = input("Enter the name of the image (include ,png/.jpg)")
    ##if the image is placed in the same folder as the python code, the user can just type the code in, if not then the user will neeed the address


    # extract the person name from the image path 
    # ##need to extract expression not name
    #might have to remove this part and get user to specifiy the expression dispalyed
    #---name = imagePath.split(os.path.sep)[-2]
    name=input("Enter displayed expression")
    # load the input image and convert it from RGB (OpenCV ordering)
	# to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # detect the (x, y)-coordinates of the bounding boxes
	# corresponding to each face in the input image
    #####################need to understand what args does
    ###nvm i uderstand now, replace args["detection_method"] with just "cnn" this is constant and removes the user input that is needed
    #boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
    boxes =face_recognition.face_locations(rgb, model="cnn")

	# compute the facial embedding for the face
    encoding = face_recognition.face_encodings(rgb, boxes)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    #doesnt need the loops because only one image is added
    data = {"encodings": encoding, "names": name}
    ###similar to the model above can be used here, can be hard coded in
    ####when opening need to append not write over the exisitg file, for example "ab", stille creates a new file if doesnt exist but append to the file 

    f = open("encoded_images.pickle", "ab")
    #f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()   
    
    Main_Menu()
#defines live_capture function
def live_capture():
    ###add a check to see if the text file is present and has values
    print("live_capture")
    encode_image()
    print("returned")
    Main_Menu()

#defines encoding function
def encode_image():
    #function should encode the images in the folder and add them to the text file
    print("encodes images")
    return


Main_Menu()


    
    
