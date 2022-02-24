import pytesseract
import re
import  cv2
import numpy as np

# Include tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"


def detect_text(frame):
    image_to_text = pytesseract.image_to_string(image=frame)
    #print(image_to_text)
    image_to_text.strip() # remove extra spaces and unneccessary newlines
    sliced = image_to_text.split('\n') # convert list string to list by newline character
    aadhaar = [i for i in sliced if len(i)==14] # append the string with length == 14 i.e. length of aadhaar number "1234 4568 9876" == 14
    # print(aadhaar)
    try :
        x = re.findall("^\d.*\d$", str(aadhaar[0]))  # varify if it is aadhaar or not i.e. string starts with digit and end with digit too
        return x[0]
    except:
        pass


def extract_aadhaar (data):
    # print(data)
    x = re.findall("^\d.*\d$", data) # varify if it is aadhaar or not i.e. string starts with digit and end with digit too
    try:
        # print(f' AADHAAR : {x[0]}' ) # printing aadhaar number
        return x[0]
    except:
        pass



cap = cv2.VideoCapture(1)

def live_vid():
    while True:
        _, frame = cap.read()
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        image_sharp = cv2.filter2D(src=frame, ddepth=-5, kernel=kernel) # sharpening of image to remove blurriness
        cv2.imshow('AV CV- Winter Wonder Sharpened', image_sharp)
        cv2.imshow("live", frame)
        aadhar = detect_text(image_sharp)
        if aadhar:
             print(aadhar)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
live_vid()