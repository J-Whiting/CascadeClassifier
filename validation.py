import cv2 as cv
from options import Options

if __name__ == "__main__":
    # Options
    options = Options().options

    # Load the cascade file
    cascade_file = cv.CascadeClassifier(options.cascade_file)

    # Opening the video file
    cap = cv.VideoCapture(options.video_file)

    # Set the start of the scene
    cap.set(cv.CAP_PROP_POS_FRAMES, options.scene_start - 1)

    correct = 0
    incorrect = 0

    while cap.isOpened():

        # Capture frame
        ret, frame = cap.read()

        if ret:
            # Stopping if the scene ends
            if cap.get(cv.CAP_PROP_POS_FRAMES) > options.scene_end:
                break

            # Convert to grayscale
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)

            # Detect faces in the image
            rects = cascade_file.detectMultiScale(frame_gray)

            # Draw rectangles over the matches
            for (x, y, w, h) in rects:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Showing the frames
            cv.imshow("", frame)

            # Waiting for user input
            key = cv.waitKey(6000) & 0xFF

            # If q is pressed, stop the program
            if key == ord('q'):
                break
            # If y is pressed, it is a correct result
            elif key == ord('y'):
                correct += 1
            # If n is pressed, it is an incorrect result
            elif key == ord('n'):
                incorrect += 1

        else:
            break

    # Closing the video file
    cap.release()
    cv.destroyAllWindows()

    # Output the results
    print("Correct: " + str(correct))
    print("Incorrect: " + str(incorrect))
    print("..." + str(int(100 * correct / (correct + incorrect))) + "%")
    print()
