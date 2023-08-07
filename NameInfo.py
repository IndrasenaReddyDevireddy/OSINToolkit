import requests
import webbrowser
from bs4 import BeautifulSoup
import OSINToolkit_Main
import re

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = "\033[1;33;40m"


def validate_name(name):
    return re.match("^[ a-zA-Z]+$", name)


def Name():
    print(Y + "\n""Information Gathering using Name ")
    print("-------------------------------------")
    name = input(cyan + "Enter the Full Name  >> ")
    if name.lower() == 'exit':
        exit()
    elif name.lower() == 'menu':
        OSINToolkit_Main.printmenu()
    elif not validate_name(name):
        print(red + "Invalid input. Enter only names.")
        Name()
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }
    try:
        url = "https://www.google.com/search?q=" + name
        response = requests.get(url, headers=headers)
        socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github", "scholar", "hackerearth", "hackerrank",
                       "hackerone", "tiktok", "youtube", "books", "researchgate", "publons", "orcid", "maps"]
        linklist = []
        soup = BeautifulSoup(response.content, 'html.parser')
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if 'href' in str(anchors[0]):
                linklist.append(anchors[0]['href'])
        c = 0
        foundedlinks = []
        for i in socialmedia:
            sm = str(i)
            for j in linklist:
                if sm in str(j):
                    c += 1
                    foundedlinks.append(j)
                    print(cyan + "[+]" + j)

        for i in foundedlinks:
            webbrowser.open(i)

        print(red + "[-] Checking for any pdf documents associated with this name .....")
        url = "https://www.google.com/search?q=%22" + name + "%22+filetype%3Apdf&oq=%22" + name + "%22+filetype%3Apdf"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        f = 0
        for g in soup.find_all('div', class_='g'):
            links = g.find_all('a')
            if 'href' in str(links[0]):
                print(green + "[+]" + links[0]['href'])
                Name()

        if c == 0:
            print(red + "No Info about this person")
            Name()

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print(red + "\nKeyboard interruption detected. Exiting...")
        exit()


if __name__ == "__main__":
    Name()
