import importkit

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = "\033[1;33;40m"

def Main():
    try:
        inp = input(cyan + "Enter Tool Number >> ")
        if inp == "1":
            importkit.iplocate()
        elif inp == "2":
            importkit.urlinfo()
        elif inp == "3":
            importkit.Links()
        elif inp == "4":
            importkit.Name()
        elif inp == "5":
            importkit.fuzz()
        elif inp == "6":
            importkit.dns()
        elif inp == "exit":
            exit()
        else:
            print(red + "Enter a valid option")
            Main()
    except KeyboardInterrupt:
        print(red + "\nKeyboard interruption detected. Exiting...")
        exit()

def printmenu():
    print(
        """
     ██████╗ ███████╗██╗███╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
    ██║   ██║███████╗██║██╔██╗ ██║   ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
    ██║   ██║╚════██║██║██║╚██╗██║   ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
    ╚██████╔╝███████║██║██║ ╚████║   ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ By Indrasena Reddy Devireddy  
                                                                                       Github profile: https://github.com/IndrasenaReddyDevireddy 
        """
    )
    print(
        green
        + """Available Tools:
                    1.Trace IP address
                    2.URL redirection checker
                    3.URL lookup in webpages
                    4.Information Gathering using Name 
                    5.Subdomain enumeration
                    6.DNS Enumeration
                    Usage : Enter exit to stop or menu for Main menu
                    """ + green
    )

    Main()


if __name__ == "__main__":
    printmenu()
