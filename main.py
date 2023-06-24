import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import time
import yaml
import time
colorama.init(autoreset=True)
import openai
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

def chatGPT():
    try:
        # Load API key and language model from config.yaml file
        with open('config.yaml') as file:
            config = yaml.safe_load(file)
            language_model = config['language_model']

        # Set up OpenAI API credentials
        openai.api_key = APIKEY



        # Define the initial user prompt
        prompt = str(input(f'{Style.BRIGHT + Fore.RED}chatGPT 5{Fore.YELLOW} > {Fore.RED} Prompt: '))

        # Initialize the conversation
        conversation = f"User: {prompt}\nAI:"

        while True:
            # Show loading animation
            loading_symbols = "|/-\\"
            for _ in range(10):
                for symbol in loading_symbols:
                    print(f"\rAI is thinking... {symbol}", end='')
                    time.sleep(0.1)

            # Prompt ChatGPT for the next response
            response = openai.Completion.create(
                engine=language_model,
                prompt=conversation,
                max_tokens=1000,
                temperature=0.7,
            )

            # Extract the generated response
            ai_response = response.choices[0].text.strip()

            # Clear the loading animation line
            print(" " * 30, end='\r')

            # Format the AI's response in a box
            os.system('clear')
            response_box = f"""
        ********************************
        {ai_response.center(30)}
        ********************************
        """

            # Print the AI's response with enhanced typewriter-style effect
            print(response_box)

            # Update the conversation
            conversation += f"\nUser: {prompt}\nAI: {ai_response}\n"
            prompt = str(input(f'\n{Style.BRIGHT + Fore.RED}chatGPT 5{Fore.YELLOW} > {Fore.RED} Prompt: '))

    
    except openai.error.InvalidRequestError as e:
        print("\nAn InvalidRequestError occurred:", str(e) + '\n\n\nThis could mean that the model you are using can\'t handel the amount of tokens (Text) That you have given it.\nJust change the model you are using.')

    except openai.error.AuthenticationError:
        print('You either have a invalid (openAI) API key of none at ALL. ADD one.')

    except yaml.YAMLError:
        print('There was a error with the config.yaml file. Make sure it is in the same directory as the main.py file.')
    except yaml.parser.ParserError:
        print('You have a syntax error in the config file.')


    except KeyboardInterrupt:
        print(f'\n\nGoing back to start src')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        exit()
        

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
    elif firstPick == 3:
        os.system('clear')
        chatGPT()
    elif firstPick == 0:
        os.system('clear')
        exit()
    else:
        print('Invalid Input')
        firstSrc()

firstSrc()