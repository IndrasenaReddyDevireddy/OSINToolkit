import OSINToolkit_Main

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'

def dns():
    print(Y + "\n""DNS Enumeration")
    print("------------------")
    print("Domain example = example.com")
    import dns.resolver
    record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

    try:
        domain = input(cyan + "Enter domain name >>")
        if domain.lower() == 'exit':
            exit()
        elif domain.lower() == 'menu':
            OSINToolkit_Main.printmenu()
    except KeyboardInterrupt:
        print(red + '\nKeyboard interruption detected. Exiting...')
        quit()

    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google DNS servers

    for record_type in record_types:
        try:
            answers = resolver.query(domain, record_type)
            print(f'\n{record_type} Records')
            print('-' * 30)
            for answer in answers:
                print(answer.to_text())

        except dns.resolver.NoAnswer:
            pass

        except dns.resolver.NXDOMAIN:
            print(f'{domain} does not exist.')
            quit()

        except dns.resolver.NoNameservers:
            print('All nameservers failed to answer the query.')
            quit()

        except dns.resolver.Timeout:
            print('DNS resolution timed out.')
            quit()

        except KeyboardInterrupt:
            print('Quitting.')
            quit()

        except Exception as e:
            print(f'An error occurred: {str(e)}')
            quit()

if __name__=="__main__":
    dns()