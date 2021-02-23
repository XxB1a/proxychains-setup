y = ['y', 'yes']
n = ['n', 'no']

def cls():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

def installation():
    print('Hmmm.. Dependencies were NOT found!!!')
    yon = input('May I install them (Y/N) ')
    yon = yon.lower()

    if yon in y:
        print('ty qt uwu')

        try:
            os.system('pip install time -y && pip install colorama -y && pip3 install time -y && pip3 install colorama -y')
            print('Installed!!')
            time.sleep(3)

            cls()
            main()

        except:
            print('Something went wrong ~~')

    else:
        print(':(')

def main():
    cls()

    print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
    print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

    proxy = str(input('Proxy IP: '))

    cls()
    print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
    print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

    port = str(input('Port: '))

    cls()
    print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
    print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

    type = str(input('DO NOT MAKE A TYPO HERE SILLY\n(socks4, socks5, http) Proxy type: '))
    type = type.lower()

    cls()
    print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
    print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
    print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

    uap = str(input('Does the proxy use usernames and passwords: '))
    uap = uap.lower()

    if uap in y:
        cls()
        print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
        print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

        username = str(input('Username: '))

        cls()
        print(f'{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗{Fore.RED}    ██{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}╗   {Fore.RED}██{Fore.MAGENTA}╗')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}    ██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED} █{Fore.MAGENTA}╗ {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}███{Fore.MAGENTA}╗{Fore.RED}██{Fore.MAGENTA}║{Fore.RED}██{Fore.MAGENTA}║   {Fore.RED}██{Fore.MAGENTA}║')
        print(f'{Fore.MAGENTA}╚{Fore.RED}██████{Fore.MAGENTA}╔╝╚{Fore.RED}███╔{Fore.RED}███{Fore.MAGENTA}╔╝╚{Fore.RED}██████{Fore.MAGENTA}╔╝')
        print(f'{Fore.MAGENTA}  ╚═════╝  ╚══╝╚══╝  ╚═════╝ ')

        password = str(input('Password: '))

        cls()

        Fore.RESET
        new_conf = f"""strict_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
{type} {proxy} {port} {username} {password}"""

        with open('/etc/proxychains.conf', 'w+') as f:
            f.write(new_conf)

    else:
        Fore.RESET
        new_conf = f"""strict_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
{type} {proxy} {port}"""

        with open('/etc/proxychains.conf', 'w+') as f:
            f.write(new_conf)

    print('done qt')

if __name__ == '__main__':
    try:
        import os
        import time
        from colorama import *

        os.system('sudo apt install proxychains -y && sudo yum install proxychains -y')
        cls()

        main()

    except ImportError:
        installation()
