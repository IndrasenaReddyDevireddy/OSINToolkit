import requests
import webbrowser
import OSINToolkit_Main

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'


def iplocate():
    print(Y +"\n""Trace IP Address")
    print("------------------")
    try:
        ipinfo={}
        ip=input(cyan+"Enter Ip address >> ")
        url="http://ip-api.com/json/"+ip
        r=requests.get(url)
        ipinfo=r.json()
        if ipinfo['status'] == 'success':
            lat=ipinfo['lat']
            lon=ipinfo['lon']
            print(green+"Ip location Found !!")
            print('Country     : ',ipinfo['country'])
            print('Region Name : ',ipinfo['regionName'])
            print('City        : ',ipinfo['city'])
            print('Time zone   : ',ipinfo['timezone'])
            print('ISP         : ',ipinfo['isp'])
            iplocate()
        elif (ip == 'exit'):
            exit()
        elif(ip == 'menu'):
            OSINToolkit_Main.printmenu()

        elif (ip != int):
           print(red + "Invalid Ip")
           iplocate()
        else:
            print(red+"Ip location Not Found !!")
            iplocate()
    except KeyboardInterrupt:
        print(red + "\nKeyboard interruption detected. Exiting...")
        exit()

        
if __name__=="__main__":
    iplocate()
