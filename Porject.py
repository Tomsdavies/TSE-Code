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

def add_sample():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--dataset", required=True,
    help="path to input directory of faces + images")
    ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
    ap.add_argument("-d", "--detection-method", type=str, default="cnn",
    help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())
    knownEncodings = []
    knownNames = []
    ###ask user to locate images they wish to add to the program
    ###once found encode the image and add to the text file
    ###loop back to menu once completed, add option to add another file - repeate the menu
    ###user needs to locate the file  
    imagePaths = input("Enter the name of the image")
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
    boxes = face_recognition.face_locations(rgb, model=args["detection_method"])

	# compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)
    # loop over the encodings
    for encoding in encodings:
		# add each encoding + name to our set of known names and
        ##where name is need to expression
		# encodings
        knownEncodings.append(encoding)
        knownNames.append(name) 
    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open(args["encodings"], "wb")
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


    
    
