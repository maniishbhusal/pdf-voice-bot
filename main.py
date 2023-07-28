from pypdf import PdfReader
from gtts import gTTS
import os

reader = PdfReader("PDFs/Linux_for_beginners.pdf")
text = ""

# Extract text from each page
for page in range(8,9):
    text += reader.pages[page].extract_text().strip().replace("\n", " ")

print(text)

# Initialize gTTS and convert text to speech
tts = gTTS(text)
tts.save("Voices/Linux_for_beginners.mp3")

# Optionally, you can also play the speech using the OS default player
os.system("Linux_for_beginners.mp3")
