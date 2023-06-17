import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import time
import yaml

colorama.init(autoreset=True)

def loading_animation():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)  # Add a small delay to control the animation speed
        print(f"\rLoading {animation[i % len(animation)]}", end="", flush=True)

# Get the path of the current script
script_path = os.path.realpath(__file__)

# Check if the script has been modified in a Git repository
try:
    # Run 'git diff' command to check if the script has modifications
    subprocess.check_output(['git', 'diff', '--exit-code', script_path])

    # No modifications found
    print(f"{Fore.BLACK + Back.WHITE}The script has not been modified.")

    # Load the YAML file
    with open('config.yaml') as file:
        config_data = yaml.safe_load(file)

    # Retrieve the API key from the config data
    APIKEY = config_data['openAI_API_KEY']

    # Check if the user has agreed to the licenses
    if not config_data['agree_to_license/eula']:
        print(f"{Fore.RED}You must agree to the license agreements before running the script.")
        exit()

    # Perform the loading animation
    print(f"Hello and welcome to my script. Here are your options: (Please wait while the script loads)")
    loading_animation()

except subprocess.CalledProcessError:
    # Modifications found
    print(f"{Fore.RED}Either you modified the script or there is an update.\nPlease ensure the integrity of the script. To update, please run\nready.sh")

def search():
    os.system('clear')
    print(f'{Fore.RED + Style.BRIGHT}[{Fore.YELLOW}#{Fore.RED}] Options:')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}1{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search Amazon')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}2{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}DuckDuckGo')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}3{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search Youtube')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}4{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search NewEgg')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}5{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search Google')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}6{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search open VSCODE Web Builder')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}0{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Back')
    searchPick = int(input(f'{Style.BRIGHT + Fore.RED}Better Day 5 {Fore.YELLOW} > {Fore.RED} Choose: '))
    if searchPick == 1:
        searchAmazon = str(input('What would you like to search for. Spaces must be +: '))
        os.system('firefox https://www.amazon.ca/s?k='+searchAmazon+'')
        os.system('python3 main.py')
    elif searchPick == 2:
        searchDuck = str(input('What would you like to search for. Spaces must be +: '))
        os.system('firefox https://duckduckgo.com/?q='+searchDuck+' ')
        os.system('python3 main.py')
    elif searchPick == 3:
        searchYT = str(input('What would you like to search for. Spaces must be +: '))
        os.system('firefox https://www.youtube.com/results?search_query='+searchYT+'')
        os.system('python3 main.py')
    elif searchPick == 4:
        searchEgg = str(input('What would you like to search for. Spaces must be +: '))
        os.system('firefox https://www.newegg.ca/p/pl?d='+searchEgg+'')
        os.system('python3 main.py')
    elif searchPick == 5:
        searchG = str(input('What would you like to search for. Spaces must be +: '))
        os.system('firefox https://www.google.com/search?q='+searchG+'')
        os.system('python3 main.py')
    elif searchPick == 6:
        os.system('firefox vscode.dev')
        os.system('python3 main.py') 
    elif searchPick == 0:
        os.system('clear')
        exit()
    else:
        print('INVALID INPUT')
        search()
    
    
def system():
    os.system('clear')
    print(f'{Fore.RED + Style.BRIGHT}[{Fore.YELLOW}#{Fore.RED}] Options:')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}1{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Run Train')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}2{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}HTOP')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}3{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Clone something off of github')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}4{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Make File')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}0{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Back')
    systemPick = int(input(f'{Style.BRIGHT + Fore.RED}Better Day 5 {Fore.YELLOW} > {Fore.RED} Choose: '))
    if systemPick == 1:
        os.system('sl')
    elif systemPick == 2:
        os.system('htop')
    elif systemPick == 3:
        gitClone = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What would you like to clone? ')))
        os.system('git clone '+gitClone+'')
        os.system('python3 main.py')
    elif systemPick == 4:
        makeFile = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What file would you like to make? ')))
        os.system('touch '+makeFile+'')
        os.system('python3 main.py')    
    elif systemPick == 0:
        firstSrc()
    else:
        print('INVALID INPUT')   
    
#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
def firstSrc():
    os.system('clear')
    print(f'{Fore.RED + Style.BRIGHT}[{Fore.YELLOW}#{Fore.RED}] Options:')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}1{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Search')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}2{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}System')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}3{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}chatGPT')
    print(f'{Style.BRIGHT + Fore.RED}   ({Fore.WHITE}0{Fore.RED}) {Fore.YELLOW}~> {Fore.WHITE}Exit')
    firstPick = int(input(f'{Style.BRIGHT + Fore.RED}Better Day 5 {Fore.YELLOW} > {Fore.RED} Choose: '))

    if firstPick == 1:
        search()
    elif firstPick == 2:
        system()
    elif firstPick == 0:
        os.system('clear')
        exit()
    else:
        print('Invalid Input')
        firstSrc()

firstSrc()