import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        self.parser.add_argument("--video_file", type=str, default="", help="filename of video file")
        self.parser.add_argument("--positive_folder", type=str, default="positive_images",
                                 help="path to positive images folder")
        self.parser.add_argument("--negative_folder", type=str, default="negative_images",
                                 help="path to negative images folder")
        self.parser.add_argument("--sample_folder", type=str, default="sample_images",
                                 help="path to sample images folder")
        self.parser.add_argument("--output_folder", type=str, default="output",
                                 help="path to the training output")
        self.parser.add_argument("--image_size", type=int, default=32, help="height and width of the sampled image")
        self.parser.add_argument("--sample_count", type=int, default=128,
                                 help="the number of samples to generate per positive image")

        # Validation
        self.parser.add_argument("--cascade_file", type=str, default=r"classifier\haarcascade_frontalface_default.xml",
                                 help="filename of cascade file. Leave blank if cascade file does not exist")
        self.parser.add_argument("--scene_start", type=int, default=0, help="frame number of the scene start")
        self.parser.add_argument("--scene_end", type=int, default=1000, help="frame number of the scene end")

        self.options = self.parser.parse_args()

        # Print the option values to the console
        args = vars(self.options)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')
        print()
