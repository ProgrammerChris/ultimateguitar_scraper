# Scrape UltimateGuitar for lyrics and chords


## System requirements
This is for Windows machines with Chrome installed!

## If it does not work, check that you have the correct chromedriver.exe file, this must match the version of your installed chrome.

## Usage:
    
    1. clone repo
    
    2. python3 -m pip install -r requirements.txt
    
    3. python3 scrape.py "artist name" "song title" "full url to chords" (-p for PDF, -w for word doc or -b for both formats)

    
This will then save the PDF to "pdfs" in the same folder as this project, and .docx in the "docs" folder.

## Made with python 3.6.7 using
- beautifulsoup4
- reportlab
- python-docx
- selenium
- urllib3

### GUI version is in the making and coming for windows soon!