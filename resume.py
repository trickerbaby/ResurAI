from PIL import Image
import pytesseract
from openai import OpenAI


# Path to the Tesseract executable (assuming it's in the system PATH)
# If Tesseract is not in the PATH, provide the full path to the executable
# Provide the full path to the Tesseract executable, including the executable file itself
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

client = OpenAI(
  api_key="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"
)


quary = ""
def perform_ocr(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Perform OCR on the image
        global quary
        text = pytesseract.image_to_string(img)
        quary = text
        # Print the extracted text
       
        

    except Exception as e:
        print(f"Error: {e}")

# Replace 'path/to/your/image.png' with the path to your image file
image_path = 'resume.png'
perform_ocr(image_path)
print("I want you to filter out the programming languages from which technical questions can be asked the text given is this  '"+quary+"'")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an interviewer."},
    {"role": "user", "content": "I want you to filter out the programming languages ,softwares and programming projects that i have worked on from which technical questions can be asked from this given text '"+quary+"', Now Ask me 10 technical questions from what you find out "}
  ]
)

print(completion.choices[0].message)
