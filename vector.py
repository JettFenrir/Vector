import socket
import os
import requests
import platform
import colorama
from colorama import Fore

def back():
    print()
    back = input('\033[92mDo you want to continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print("""\033[93m 
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
 Recon Tool with Automated XSS and Open Redirection finder made by Abhijeet, Sameer, Shantanu and Aakanksha""")
        exit
    else:
        print('\033[92m?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def vector():
    clear()
    print("""\033[93m                                                              
 ___      ___ _______   ________ _________  ________  ________     
|\  \    /  /|\  ___ \ |\   ____\\___   ___\\   __  \|\   __  \    
\ \  \  /  / | \   __/|\ \  \___\|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \  \/  / / \ \  \_|/_\ \  \       \ \  \ \ \  \\\  \ \   _  _\  
  \ \    / /   \ \  \_|\ \ \  \____   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \__/ /     \ \_______\ \_______\  \ \__\ \ \_______\ \__\\ _\ 
    \|__|/       \|_______|\|_______|   \|__|  \|_______|\|__|\|__|
 Recon Tool with Automated XSS and Open Redirection finder made by Abhijeet, Sameer, Shantanu and Aakanksha""")
    print()

def banner():
    print("""\033[96m
 1) DNS Lookup                 11) XSS Hunter		               
 2) GeoIP Lookup               12) Subdomain listing
 3) Subnet Lookup              13) Redirection             
 4) Page Links                 14) About Vector 
 5) Reserve IP Lookup          15) EXIT
 6) HTTP Header                16) All of the above.
 7) Host Finder                
 8) IP-Locator                
 9) Find Shared DNS Servers   
 10) Get Robots.txt""")
    print()

def iseeverything():
    try:
        what = input('\033[92mAre you want to collect information of website or IP address? [website/IP]: ')
     			
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
            
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of this domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('Enter Valid Website name')
            iseeverything()

        choose = input('What information would you like to collect? (1-16): ')

        if choose == '1':
            print("""\033[93m 
█▀▄ █▄░█ █▀   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
█▄▀ █░▀█ ▄█   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
	    
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            back()


        elif choose == '2':
            print("""\033[93m
█▀▀ █▀▀ █▀█   █ █▀█
█▄█ ██▄ █▄█   █ █▀▀\n\n\n""")
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m',info.text)
            back()

        elif choose == '3':
            print("""\033[93m
█▀ █░█ █▄▄ █▄░█ █▀▀ ▀█▀   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
▄█ █▄█ █▄█ █░▀█ ██▄ ░█░   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print('\033[91m',info.text)
            back()

       

        elif choose == '4':
            print("""\033[93m
█▀█ ▄▀█ █▀▀ █▀▀   █░░ █ █▄░█ █▄▀ █▀
█▀▀ █▀█ █▄█ ██▄   █▄▄ █ █░▀█ █░█ ▄█\n\n\n""")
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print('\033[91m',info.text)
            back()

        elif choose == '5':
            print("""\033[93m
█▀█ █▀▀ █░█ █▀▀ █▀█ █▀ █▀▀   █ █▀█   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
█▀▄ ██▄ ▀▄▀ ██▄ █▀▄ ▄█ ██▄   █ █▀▀   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q='+victim
            info = requests.get(reserve)
            print('\033[91m',info.text)
            back()
            

        elif choose == '6':
            print("""\033[93m
█░█ █▀█ █▀ ▀█▀   █░█ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█
█▀█ █▄█ ▄█ ░█░   █▀█ ██▄ █▀█ █▄▀ ██▄ █▀▄\n\n\n""")
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print('\033[91m',info.text)
            back()

        elif choose == '7':
            print("""\033[93m
█░█ █▀█ █▀ ▀█▀   █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
█▀█ █▄█ ▄█ ░█░   █▀░ █ █░▀█ █▄▀ ██▄ █▀▄\n\n\n""")
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m',info.text)
            back()

        elif choose == '8':
            print("""\033[93m
█ █▀█   █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
█ █▀▀   █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n\n\n""")
            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print('\033[91m',info.text)
            back()

        elif choose == '9':
            print("""\033[93m
█▀ █░█ ▄▀█ █▀█ █▀▀ █▀▄   █▀▄ █▄░█ █▀   █▀ █▀▀ █▀█ █░█ █▀▀ █▀█
▄█ █▀█ █▀█ █▀▄ ██▄ █▄▀   █▄▀ █░▀█ ▄█   ▄█ ██▄ █▀▄ ▀▄▀ ██▄ █▀▄\n\n\n""")
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m',info.text)
            back()

        elif choose == '10':
            print("""\033[93m
█▀█ █▀█ █▄▄ █▀█ ▀█▀ ░ ▀█▀ ▀▄▀ ▀█▀
█▀▄ █▄█ █▄█ █▄█ ░█░ ▄ ░█░ █░█ ░█░\n\n\n""")
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print('\033[91m',info.text)
            back()

       

        elif choose == '11':
            clear()
            os.system('python3 xsshunter.py -u http://'+victim)
            back()

       

        elif choose == '12':
            clear()
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀ █░█ █▄▄ █▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█   █░░ █ █▀ ▀█▀ █▀▀ █▄░█ █ █▄░█ █▀▀
▄█ █▄█ █▄█ █▄▀ █▄█ █░▀░█ █▀█ █ █░▀█   █▄▄ █ ▄█ ░█░ ██▄ █░▀█ █ █░▀█ █▄█\n\n\n""")
            os.system('cd modules/waybackurls && waybackurls '+victim)
            back()


        elif choose == '13':
            clear()
            
            os.system('python3 openredirector.py -t http://'+victim)
            back()
            
        elif choose == '16':
            clear()
            
            #print(Fore.GREEN+"\n\nDNS Lookup\n\n")
            print(Fore.GREEN+"""\033[93m 
█▀▄ █▄░█ █▀   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
█▄▀ █░▀█ ▄█   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
            
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀▀ █▀▀ █▀█   █ █▀█
█▄█ ██▄ █▄█   █ █▀▀\n\n\n""")
            
            
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀ █░█ █▄▄ █▄░█ █▀▀ ▀█▀   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
▄█ █▄█ █▄█ █░▀█ ██▄ ░█░   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
            
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀█ ▄▀█ █▀▀ █▀▀   █░░ █ █▄░█ █▄▀ █▀
█▀▀ █▀█ █▄█ ██▄   █▄▄ █ █░▀█ █░█ ▄█\n\n\n""")
            
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀█ █▀▀ █░█ █▀▀ █▀█ █▀ █▀▀   █ █▀█   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
█▀▄ ██▄ ▀▄▀ ██▄ █▀▄ ▄█ ██▄   █ █▀▀   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀\n\n\n""")
            
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q='+victim
            info = requests.get(reserve)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█░█ █▀█ █▀ ▀█▀   █░█ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█
█▀█ █▄█ ▄█ ░█░   █▀█ ██▄ █▀█ █▄▀ ██▄ █▀▄\n\n\n""")
            
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█░█ █▀█ █▀ ▀█▀   █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
█▀█ █▄█ ▄█ ░█░   █▀░ █ █░▀█ █▄▀ ██▄ █▀▄\n\n\n""")
            
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█ █▀█   █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
█ █▀▀   █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n\n\n""")
            
            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀ █░█ ▄▀█ █▀█ █▀▀ █▀▄   █▀▄ █▄░█ █▀   █▀ █▀▀ █▀█ █░█ █▀▀ █▀█
▄█ █▀█ █▀█ █▀▄ ██▄ █▄▀   █▄▀ █░▀█ ▄█   ▄█ ██▄ █▀▄ ▀▄▀ ██▄ █▀▄\n\n\n""")
            
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m',info.text)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀█ █▀█ █▄▄ █▀█ ▀█▀ ░ ▀█▀ ▀▄▀ ▀█▀
█▀▄ █▄█ █▄█ █▄█ ░█░ ▄ ░█░ █░█ ░█░\n\n\n""")
            
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print('\033[91m',info.text)
            
            
            
            os.system('python3 xsshunter.py -u http://'+victim)
            
            print(Fore.GREEN+"""\n\n\n\033[93m
█▀ █░█ █▄▄ █▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█   █░░ █ █▀ ▀█▀ █▀▀ █▄░█ █ █▄░█ █▀▀
▄█ █▄█ █▄█ █▄▀ █▄█ █░▀░█ █▀█ █ █░▀█   █▄▄ █ ▄█ ░█░ ██▄ █░▀█ █ █░▀█ █▄█\n\n\n""")
            
            
            os.system('cd modules/waybackurls && waybackurls '+victim)
            
            
            
            os.system('python3 openredirector.py -t http://'+victim)
            
            
            print('\n\n\n')
            print("""\033[93m 
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
 Recon Tool with Automated XSS and Open Redirection finder made by Abhijeet, Sameer, Shantanu and Aakanksha""")
            
            exit()

        elif choose == '14':
          
            back()

        elif choose == '15':
            
            print("""\033[93m 
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ██╗░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ╚██╗░██╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ░╚████╔╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░░╚██╔╝░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
Recon Tool with Automated XSS and Open Redirection finder made by Abhijeet, Sameer, Shantanu and Aakanksha""")
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service not known!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()

vector()
iseeverything()
