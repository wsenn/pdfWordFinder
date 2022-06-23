#!/usr/bin/env python
# Import necessary modules
# User chose a directory, if not, use the current directory
# User chose a word
# Extract all pdfs from the directory
# Read all pdfs and extract text
# Search for the word in the text
# If the word is found, print the pdf file name
# Open the pdf file when the word is found at the exact position
# If the word is not found, print "Word not found"
# import necessary modules

import os
import PyPDF2 as pyPdf
import re
import sys
import subprocess

# User chose a directory, if not, use the current directory
if len(sys.argv) == 1:
    directory = os.getcwd()
else:
    directory = sys.argv[1]
# User chose a word
word = sys.argv[2]
# Extract all pdfs from the directory
pdf_files = [pdf for pdf in os.listdir(directory) if pdf.endswith('.pdf')]
# Read all pdfs and extract text
for pdf in pdf_files:
    # Open the pdf file
    pdf_file = open(pdf, 'rb')
    # Read the pdf file
    read_pdf = pyPdf.PdfFileReader(pdf_file)
    # Extract text
    for page in range(read_pdf.numPages):
        # Try to extract text if the page is not encrypted
        try:
            text = read_pdf.getPage(page).extractText()
        # If the page is encrypted, skip it
        except:
            continue
        # Search for the word in the text if it can't decode the text, ignore it
        if text is not None:
            # Search for the word in the text if it can't decode the text, ignore it
            try:
                if re.search(word, text, re.IGNORECASE):
                    # If the word is found, print the pdf file name
                    print(pdf)
                    # Open the pdf file when the word is found at the exact position
                    subprocess.call(['open', pdf])
                    # If the word is not found, print "Word not found"
                    break
            except:
                continue
        if re.search(word, text, re.IGNORECASE):
            # If the word is found, print the pdf file name
            print('Found in ' + pdf)
            # Open the pdf file in the default application when the word is found at the exact position
            subprocess.call(['open', pdf])
            break
        # If the word is not found, print "Word not found"
    if not re.search(word, text, re.IGNORECASE):
        print('Word not found in ' + pdf)
# Stop the program
sys.exit()

