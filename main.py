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
    with open('agreement.yaml') as file:
        license_data = yaml.safe_load(file)

    # Check if the user has agreed to the licenses
    if not license_data['agree_to_license/eula']:
        print(f"{Fore.RED}You must agree to the license agreements before running the script.")
        exit()

    # Perform the loading animation
    print(f"Hello and welcome to my script. Here are your options: (Please wait while the script loads)")
    loading_animation()

except subprocess.CalledProcessError:
    # Modifications found
    print(f"{Fore.RED}Either you modifed the script or there is an update.\nPlease ensure the integrity of the script. To update please run\nready.sh")
    

def firstSrc():
    print(f'{Fore.RED + Style.BRIGHT}({Fore.YELLOW}#{Fore.RED})')
    print(f'{Fore.YELLOW}   1. {Fore.GREEN}Search')
    print(f'{Fore.YELLOW}   1. {Fore.GREEN}System')
    firstPick = int(input(f'{Style.BRIGHT + Fore.RED}Better Day 5 {Fore.YELLOW} > {Fore.RED} Choose'))
