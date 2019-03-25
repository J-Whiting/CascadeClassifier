import cv2 as cv
import math
from options import Options
import os

if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether `negative_images` folder exists
    if not os.path.exists(options.negative_folder):
        print("Creating " + options.negative_folder + " folder")
        os.makedirs(options.negative_folder)
        print("...Done")
        print()

    # The minimum number of negative frames to generate
    min_frame_count = 2000

    # Opening the video file
    cap = cv.VideoCapture(options.video_file)

    # Number of frames in the video file
    frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)

    # Saving the frame every frame_counter loops
    frame_counter = math.floor(frame_count / min_frame_count)

    print("Generating negative frames from " + options.video_file)

    progress_counter = 0
    print("...Progress: 0%")

    while cap.isOpened():

        # 0-based index of the frame to be decoded/captured next
        frame_index = int(cap.get(cv.CAP_PROP_POS_FRAMES))

        # Capture frame
        ret, frame = cap.read()

        if ret:

            # Saving the frame every frame_counter loops
            if frame_index % frame_counter == 0:

                # Saving the frames
                cv.imwrite(os.path.join(options.negative_folder, str(frame_index) + ".png"), frame)

                # Write out the percentage progress
                if int(100 * frame_index / frame_count) > progress_counter:
                    progress_counter += 1
                    print("...Progress: " + str(progress_counter) + "%")

        else:
            print("...Progress: 100%")
            break
    print("...Done")
    print()

    # Closing the video file
    cap.release()
