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
    #displays warning to user
    print("---Before continuing make sure the image you wish to add is placed in the same folder as the Program---")
    #asks user for the image name so python can locate image    
    image_name = input("Enter the name of the image (include ,png/.jpg)")
    #asks user or the expression displayed in the image
    expression=input("Enter displayed expression")
    #checks to see if user has entered correct or acceptable values
    if(len(expression)<1):
        print("Incorrect Entry, Please enter an expression...")
        add_sample()
    # load the input image and convert it from RGB (OpenCV ordering)
	# to dlib ordering (RGB)
    #try and except function to check if the image_name exists in the folder and can be encoded
    try:
        image = cv2.imread(image_name)
    except:
        Print("Image could not be found to encode, Please enter correct image name or check location")
        add_sample()
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # detect the (x, y)-coordinates of the bounding boxes
	# corresponding to each face in the input image
    boxes =face_recognition.face_locations(rgb, model="cnn")
	# compute the facial embedding for the face
    encoding = face_recognition.face_encodings(rgb, boxes)
    # dump the facial encodings + expressions to disk
    data = {"encodings": encoding, "expression": expression}
    #uses ab to append to existing files, not overwrite them
    f = open("encoded_images.pickle", "ab")
    #write this data to the file
    f.write(pickle.dumps(data))
    f.close()   
    #once completed loops back to main menu
    Main_Menu()
#defines live_capture function
def live_capture():
    #try catch to check a file exists that can be opened containing encoded images
    try:
        encoded_faces = pickle.loads(open("encoded_images.pickle","rb").read())
    except:
        #tells the user a file can not be found
        print("ERROR no encoded images found")
        Main_Menu()
    #calls the function to collect images needed to be processed, function returns an image ready for comparison
    live_image = collect_photo()
    #begins comparison
    rgb = cv2.cvtColor(live_image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,model="cnn")
    encodings = face_recognition.face_encodings(rgb, boxes)
    #stores boolean true or false if a reconized face was found
    matches =face_recongition.compare_faces(encoded_faces["encoding"], encodings)
    #defines future variables
    expression="Unkown_expression"
    expression_list=[]
    #adds a count to determine which face is reconised more
    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        count={}
        for i in matchedIDxs:
            expression=data["expression"][i]
            counts[expression] =counts.get(expression,0)+1
        expression=max(counts, key=counts.get)
    expression_list.append(name)
    # draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
    # show the output image
    cv2.imshow("Image", image)
    a=input("...")
    #either waits for user responce or can be changed to repeate every so many seconds creating a live update and constant reconizing
    Main_Menu()


#defines encoding function
def collect_photo():
    ##cv2 cv2.imread(args["image"])]
    #where the code for the intergration for the webcam would be placed, future expandability
    #asks the user for the name of the image to compare
    while(True):
            user_photo_name=input("Enter the name of the image you wish to compare:")
        try:
            user_photo_name=cv2.imread(user_photo_name)
            return user_photo_name
        except:
            print("ERROR, image entered was not found or entered incorrectly")
        



Main_Menu()


    
    
