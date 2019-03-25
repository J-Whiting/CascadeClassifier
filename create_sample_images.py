from options import Options
import os
import re
import subprocess

if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether negative folder exists
    if not os.path.exists(options.sample_folder):
        print("Creating " + options.sample_folder + " folder")
        os.makedirs(options.sample_folder)
        print("...Done")
        print()

    # Default rngseed value.  This gets incremented after every use
    rngseed = 12345

    print("Looping over all the positive images")
    for image_filename in os.listdir(options.positive_folder):
        # CreateTrainingSamplesFromInfo
        # Create positive samples for all positive images
        subprocess.call([r"C:\opencv\build\x64\vc15\bin\opencv_createsamples",
                         "-img", os.path.join(options.positive_folder, image_filename),
                         "-bg", "negatives.txt",
                         # The positive images are png files, so replacing their filename with txt
                         "-info", os.path.join(options.sample_folder, "samples" + re.sub("png", "txt", image_filename)),
                         "-num", str(options.sample_count),
                         "-bgcolor", "255",
                         "-bgthresh", "8",
                         "-maxxangle", "0",
                         "-maxyangle", "0",
                         "-maxzangle", "0.3",
                         "-w", str(options.image_size),
                         "-h", str(options.image_size),
                         "-rngseed", str(rngseed)])

        # Increment the rngseed to make all generated images are different
        rngseed += 1
    print("...Done")
    print()

    print("Concatenate all `samples*.txt` files into `samples.txt`")
    subprocess.call(["COPY", "/B",
                     os.path.join(options.sample_folder, "*.txt"),
                     os.path.join(options.sample_folder, "samples.txt")],
                    shell=True)
    print("...Done")
    print()

    # The number of sample images
    sample_count = 0
    for filename in os.listdir(options.sample_folder):
        if filename.endswith(".jpg"):
            sample_count += 1

    # CreateTestSamples
    print("Convert `samples.txt` into `positives.vec`")
    subprocess.call([r"C:\opencv\build\x64\vc15\bin\opencv_createsamples",
                     # The positive images are png files, so replacing their filename with txt
                     "-info", os.path.join(options.sample_folder, "samples.txt"),
                     "-vec", "positives.vec",
                     "-bg", "negatives.txt",
                     "-num", str(sample_count),
                     "-w", str(options.image_size),
                     "-h", str(options.image_size)])
    print("...Done")
    print()

    # ShowVecSamples
    print("Show images within a vec file")
    subprocess.call([r"C:\opencv\build\x64\vc15\bin\opencv_createsamples",
                     "-vec", "positives.vec",
                     "-w", str(options.image_size),
                     "-h", str(options.image_size)])
    print("...Done")
    print()
