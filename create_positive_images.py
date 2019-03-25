import cv2 as cv
from options import Options
import os
import sys


def save_frame():
    # Crop image
    crop = frame[current_y:current_y + current_h, current_x:current_x + current_w]

    # Shrink image to 128 pixels
    zoom = cv.resize(crop, (128, 128))

    # Saving the frames
    cv.imwrite(os.path.join(options.positive_folder, str(int(cap.get(cv.CAP_PROP_POS_FRAMES)))) + ".png", zoom)


if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether `cascade_file` exists
    if (options.cascade_file == "") | (not os.path.exists(options.cascade_file)):
        print("Cascade file required to create positive images")
        sys.exit()

    # Check whether `positive_images` folder exists
    if not os.path.exists(options.positive_folder):
        print("Creating " + options.positive_folder + " folder")
        os.makedirs(options.positive_folder)
        print("...Done")
        print()

    # Variables
    current = False
    current_x = 0
    current_y = 0
    current_w = 0
    current_h = 0

    # Load the cascade file
    cascade = cv.CascadeClassifier(options.cascade_file)

    # Opening the video file
    cap = cv.VideoCapture(options.video_file)

    while cap.isOpened():

        # Capture frame
        ret, frame = cap.read()

        if ret:
            # Convert to grayscale
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)

            # Detect faces in the image
            rects = cascade.detectMultiScale(frame_gray)

            # Saving the current frame, and storing the image dimensions
            for (x, y, w, h) in rects:
                current = True
                current_x = x
                current_y = y
                current_w = w
                current_h = h

                save_frame()

            # If the program found an image in the previous frame, save the next image
            # as that is probably also the image as well
            if (len(rects) == 0) & current:
                current = False

                save_frame()
        else:
            break

    # Closing the video file
    cap.release()
