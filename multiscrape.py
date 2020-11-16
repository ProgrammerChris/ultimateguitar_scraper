#Read and save artistname from file to variable
#Read and save songname from file to variable
#Read and save url from file to variable
#Call get_site_content and make_pdf from scrape.py
#Repeat until end of file

from scrape import get_site_content, make_pdf
import os

def get_all_urls():

    file_length = 0
    artistName = ''
    songName = ''
    url = ''

    with open('chordurls.txt') as infp:
        for line in infp:
            if line.strip():
                file_length += 1

    f = open('chordurls.txt', 'r')

    index = 0
    done = 0
    print('0 out of ', int(file_length/3), 'done')
    while(done != int(file_length/3)):
        line = f.readline()
        if line.rstrip() == '':
            break
        if index == 0:
            artistName = line.rstrip()
            index = index + 1
        elif index == 1:
            songName = line.rstrip()
            index = index + 1
        elif index == 2:
            url = line.rstrip()
            make_pdf(artistName, songName, get_site_content(url))
            index = 0
            done = done + 1
            os.system('cls')
            print(done, ' out of ', int(file_length/3), 'done')

    f.close()

if __name__ == "__main__":
    get_all_urls()
