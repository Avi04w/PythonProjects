# This code allows you to take a ZIP file of images and process them. It searches through the images looking for the
# occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces
# which were located in the image which mentions "pizza".

from zipfile import ZipFile
import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import math

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('E:\\Avi Walia\\Documents\\FrontalFace/haarcascade_frontalface_default.xml')

# Getting the keyword
word = input()

# Getting the zip file
file_name = "E:\\images.zip"

file_names = []

with ZipFile(file_name, 'r') as zfile:
    zfile.extractall()
    for img in zfile.infolist():
        file_img = Image.open(img.filename)
        # Converting the image to text so we can search for keywords
        text = pytesseract.image_to_string(file_img)
        if word in text:
            file_names.append(img.filename)

    for file in file_names:
        img = cv.imread(file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Getting faces from image
        faces = face_cascade.detectMultiScale(gray, 1.5)
        pillow_image = Image.open(file)
        cropped_faces = []
        for x, y, w, h in faces:
            cropped_faces.append(pillow_image.crop((x, y, x + w, y + h)))

        max_height = 0
        max_width = 0

        for face in cropped_faces:
            max_size = (100, 100)
            face.thumbnail(max_size)

        print("Results found in file {}".format(file))

        if len(cropped_faces) == 0:
            print("But there were no faces in that file!")
        else:
            first_image = cropped_faces[0]
            rows = math.ceil(len(faces) / 5)
            contact_sheet = PIL.Image.new(first_image.mode, (500, 100 * rows))
            x = 0
            y = 0

            # Creating contact sheet
            for face in cropped_faces:
                contact_sheet.paste(face, (x, y))
                if x + 100 == contact_sheet.width:
                    x = 0
                    y += 100
                else:
                    x += 100
            # will display on Windows Live Photo Gallery
            contact_sheet.show()