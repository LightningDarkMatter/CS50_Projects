# create python program to convert pdf to voice

# import the required module
import PyPDF2
import pyttsx3

# open the pdf file
pdfFileObj = open('sample.pdf', 'rb')

# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# get the number of pages
pages = pdfReader.numPages

# create a pdf writer object for the output file
pdfWriter = PyPDF2.PdfFileWriter()

# create an engine object
engine = pyttsx3.init()

# set the rate
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

# set volume
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)       # setting up volume level  between 0 and 1

# set voice
voices = engine.getProperty('voices')       # getting details of current voice

# convert pdf in mp3
for page in range(pages):
    # create a page object
    pageObj = pdfReader.getPage(page)

    # extracting text from page
    text = pageObj.extractText()

    # reading the text
    engine.say(text)

    # saving the pdf
    pdfWriter.addPage(pageObj)

# save the pdf file
with open('sample.pdf', 'wb') as f:
    pdfWriter.write(f)

# run the speech
engine.runAndWait()

# close the pdf file object
pdfFileObj.close()

# close the engine
engine.stop()
