# import the OpenCV library for computer vision
import cv2
import sys
import math

# Load the dictionary that was used to generate the markers.
# There's different aruco marker dictionaries, this code uses 6x6
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_250)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()

# initialize the webcam as "camera" object


# loop that runs the program forever
# at least until the "q" key is pressed
if _name_ == "_main_":

    # creates an "img" var that takes in a camera frame
    img = cv2.imread("test_image1.png")

    if img is None:
        sys.exit("could not read this imgae")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect aruco tags within the frame
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    # draw box around aruco marker within camera frame
    #img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

    # if a tag is found...
    if markerIds is not None:
        # for every tag in the array of detected tags...
        for i in range(len(markerIds)):

            print(markerIds[0])
            cv2.putText(img, "qw", (25, 450), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
            # get the center point of the tag
            center = markerCorners[i][0]
            M = cv2.moments(center)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draws a red dot on the marker center
            cv2.circle(img, (cX, cY), 1, (0, 0, 255), 8)
            # writes the coordinates of the center of the tag
            #cv2.putText(img, str(cX) + "," + str(cY), (cX + 40, cY - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            # (0, 255, 0), 2)
            (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            print(topRight)

            # draw the bounding box of the ArUCo detection
            cv2.circle(img, (topRight) ,1,(0, 255, 0), 2)
            cv2.circle(img, (topLeft) ,1,(0, 255, 0), 2)
            cv2.circle(img, (bottomRight),1, (0, 255, 0), 2)
            cv2.circle(img, (bottomLeft),1, (0, 255, 0), 2)

            #angle_calculate(topRight,topLeft, trigger = 0)
            angle_list_1 = list(range(359,0,-1))
            angle_list_1 = angle_list_1[90:] + angle_list_1[:90]
            angle_list_2 = list(range(359,0,-1))
            angle_list_2 = angle_list_2[-90:] + angle_list_2[:-90]
            x=topLeft[0]-topRight[0]
            y=topLeft[1]-topRight[1]
            angle=int(math.degrees(math.atan2(y,x)))
            cv2.putText(img, str(angle) + "," + str(markerIds), (cX + 40, cY - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            



    # Display the resulting frame 
    cv2.imshow('frame', img)

    # handler to press the "q" key to exit the program
    cv2.imshow("dis window", img)
    j = cv2.waitKey(0)