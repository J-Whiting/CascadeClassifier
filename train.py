import math
from options import Options
import os
import subprocess

if __name__ == "__main__":
    # Options
    options = Options().options

    # Check whether `output` folder exists
    if not os.path.exists(options.output_folder):
        print("Creating " + options.output_folder + " folder")
        os.makedirs(options.output_folder)
        print("...Done")
        print()

    # The number of sample images
    sample_count = 0
    for filename in os.listdir(options.sample_folder):
        if filename.endswith(".jpg"):
            sample_count += 1
    print("Sample Count:" + str(sample_count))

    # The number of negative images
    negative_count = 0
    for filename in os.listdir(options.negative_folder):
        if filename.endswith(".png"):
            negative_count += 1
    print("Negative Count:" + str(negative_count))

    # There is a known bug with opencv_traincascade where it overflow the image counts,
    # so we reduce the count by 15% to make sure it doesn't overflow
    data_reduction = 0.15
    sample_count = math.floor(sample_count * (1 - data_reduction))
    negative_count = math.floor(negative_count * (1 - data_reduction))

    print("Training the cascade")
    subprocess.call([r"C:\opencv\build\x64\vc15\bin\opencv_traincascade",
                     "-data", "output",
                     "-vec", "positives.vec",
                     "-bg", "negatives.txt",
                     "-numPos", str(sample_count),
                     "-numNeg", str(negative_count),
                     "-numStages", "20",
                     "-w", str(options.image_size),
                     "-h", str(options.image_size)])
    print("...Done")
    print()
