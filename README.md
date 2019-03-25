# Cascade Classifier Training

[Cascade Classifier Training](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html)

[Creating your own Haar Cascade OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)

[Training Haar Cascades](https://memememememememe.me/post/training-haar-cascades/)

[TRAIN YOUR OWN OPENCV HAAR CLASSIFIER](https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)

[Tutorial: OpenCV haartraining (Rapid Object Detection With A Cascade of Boosted Classifiers Based on Haar-like Features)](http://note.sonots.com/SciSoftware/haartraining.html)

[Viola–Jones object detection framework](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework)



- Update `options.py` to point to the correct files.

## Negatives

- Run `create_negative_images.py` to generate negative images in the `negative_images` folder.

- Manually check the generated frames and remove any with the target in the image.

- Run `create_negative_description.py` to create `negatives.txt`.

## Positives

- Create images in the `positive_images` folder.  If you already have a classifier then you can run `create_positive_images.py` to populate the `positive_images` folder with matches from the video.

- Run `create_sample_images.py`:

  - It will ask for an image size which is the width and height of the sampled image (Smaller is better).
  - It will then create sample images in the sample_images folder by applying transformations to positive images and putting them onto negative images.
  - For each positive image a description text file `samples*.txt` is also created, detailing the filename, x-position, y-position, height and width of the image in the sample.
  - It will then concatenate all these description text files into `samples.txt`.
  - It will then create a `positives.vec` file, which collects all of the sample data into a single file.
  - The final step shows examples of positive images generated from the `positives.vec` file.

## Train

- Run `train.py` to train the classifier.  Once it is complete the file `cascade.xml` is the result.

## Validation

- Run `validation.py` to validate the accuracy of the classifier.  It shows frames from a scene in the video and applies the classifier, and you click `y` if the marked area is correct, and `n` if not.  When the scene finishes it displays the result.
