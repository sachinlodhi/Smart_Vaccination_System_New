from PIL import Image
import pytesseract
import re
import  cv2

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
        extract_aadhaar(str(aadhaar[0])) # If anystring exist with the length of 14 send it to verify if it is aadhaar number
    except:
        pass

def extract_aadhaar (data):
    # print(data)
    x = re.findall("^\d.*\d$", data) # varify if it is aadhaar or not i.e. string starts with digit and end with digit too
    try:
        print(f' AADHAAR : {x[0]}' ) # printing aadhaar number
    except:
        pass


cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    cv2.imshow("live", frame)
    detect_text(frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
