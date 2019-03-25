from options import Options
import os

if __name__ == "__main__":
    # Options
    options = Options().options

    print("Creating negative description file `negatives.txt`")
    with open("negatives.txt", "w+") as file:

        # Looping over the images in the negative folder
        for image_filename in os.listdir(options.negative_folder):
            # Write the filepath of the images, plus a new line symbol
            file.write(os.path.join(options.negative_folder, image_filename) + "\n")

    file.close()
    print("...Done")
    print()
