import requests
from bs4 import BeautifulSoup
import OSINToolkit_Main

R = '\033[1;31;40m'
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'

def Links():
    print(Y + "\n""URL Lookup in Webpages")
    print("--------------------------")
    print(Y + "URL example : http://example.com")
    url = input(C + "Enter URL >> ")
    if url.lower() == 'exit':
        exit()
    elif url.lower() == 'menu':
        OSINToolkit_Main.printmenu()
    print('')
    print(G + "[+] Fetching links.....")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            lin = link.get('href')
            if lin is not None and lin.startswith('http'):
                print(C + "[+] ", lin)
        print(G + "Fetched Successfully...")
    except requests.exceptions.MissingSchema as ms:
        print(R + "Error Occurred: " + str(ms))
    except Exception as e:
        print(R + "Error Occurred: " + str(e))
    except KeyboardInterrupt:
        print(R + "\nKeyboard interruption detected. Exiting...")
        exit()
    finally:
        Links()

if __name__ == "__main__":
    Links()
