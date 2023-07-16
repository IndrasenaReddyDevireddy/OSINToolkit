import OSINToolkit_Main
import requests
from datetime import datetime

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def urlinfo():
    print(Y + "\n""URL Redirection checker")
    print("--------------------------")
    print(Y + "URL example = http://example.com")
    url = input(cyan + "Enter URL >> ")

    if url.lower() == 'exit':
        exit()
    elif url.lower() == 'menu':
        OSINToolkit_Main.printmenu()

    print("-" * 50)
    print(cyan + "          Trace Results        ")
    print("-" * 50)
    try:
        r = requests.get(url)
        print()
        current_datetime = datetime.now()
        print("[+] Traced Date and Time:", current_datetime)
        print(green + "[-] 301 Redirected")
        print(cyan + "[-]" + r.url)
        urlinfo()
    except TypeError as te:
        print(red + "Error Occurred: " + str(te))
        urlinfo()
    except Exception as e:
        print(red + "Error Occurred: " + str(e))
        urlinfo()
    except KeyboardInterrupt:
        print(red + "\nKeyboard interruption detected. Exiting...")
        exit()

if __name__ == "__main__":
    urlinfo()
