import requests
import time

def menu():
    print(r'''
                                             __
   _____  _____  ____ _   ____          ____/ /
  / ___/ / ___/ / __ `/  / __ \ ______ / __  /
 (__  ) / /__  / /_/ /  / / / //_____// /_/ /
/____/  \___/  \__,_/  /_/ /_/        \__,_/
            
            [*] Version >> 0.3
            [*] Date >> 24-05-2024
            [*] Github >> LASDovah
            [*] Tool to know the status of headers and find existing subdomains.
    
    ________MENU_________

    [1] Security Header.
    [2] Find Subdomain.      
    [3] Exit.
    _____________________
    ''')

def main():
    try:
        while True:
            menu()
            option = int(input('Enter an option> '))
            if option == 1:
                security_headers()
            elif option == 2:
                subdomains()
                break
            elif option == 4:
                print('Exit.')
                break
            else:
                print("[-] Data entered not recognized.")
    except ValueError:
        print("[-] Please enter a valid number.")
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\n[-] Interrupted by user.")


def security_headers():
    headers_list = ['X-Frame-Options',
                    'X-Content-Type-Options',
                    'X-Content-Security-Policy',
                    'X-XSS-Protection',
                    'Content-Security-Policy',
                    'Strict-Transport-Security']
    opt = True
    while opt:
        try:
            url = input('[*] URL: ')
            print('')
            response = requests.get(url)
            headers_response = response.headers
            result = '____________SECURITY HEADERS____________\n'
            result += f'URL: {url}\n\n'
            for headers in headers_response:
                if headers in headers_list:
                    result += f'{headers}\n'
            result += '________________________________________\n'
            print(result)
            with open('header.txt', 'a') as file:
                file.write(result)
            print("[+] Headers exported to 'header.txt'.")                
            while True:
                another_url = input('[*] Do you want to enter another URL? [Y/n]: ').lower()
                if another_url == 'y':
                    break
                elif another_url == 'n':
                    opt = False
                    break
                else:
                    print('[-] Command entered incorrectly.')
        except requests.exceptions.MissingSchema:
            print("[-] INVALID URL. Be sure to include the scheme (http:// or https://).")
        except requests.exceptions.Timeout:
            print("[-] Expired request.")        
        except requests.exceptions.ConnectionError:
            print("[-] Connection error: Could not connect with the provided URL.")
        except requests.exceptions.RequestException as e:
            print(f'[-] RequestException: {e}')

def subdomains():
    print('\n[*] Enter a option.')
    print('[*] The level defines the aggressiveness of the search.\n')
    level_scan=int(input('[*] Scan type > (Select level [1/2/3]): '))
    domain = input('[*] Enter Domain: ')#Enter domain....
    print(f'\n[+] You selected the level >> {level_scan}...')
    print('[+] Searching...\n')
    time.sleep(5)
    try:
        if level_scan == 1 and not (domain.startswith('https://') or domain.startswith('http://')):
            with open('subdomains.txt','r') as file:
                for line in file:
                    subdomain = line.strip()
                    full_url = f"http://{subdomain}.{domain}"
                    try:
                        response = requests.get(full_url)
                        if response.status_code in [200, 202, 304, 400, 403, 404, 500, 502]:
                            result = f'{subdomain}.{domain} | [{response.status_code}]'
                            result2 = f'{subdomain}.{domain}'
                            print(result)
                            with open(f'subdomains_code_{domain}.txt', 'a') as output_file:
                                output_file.write(result+'\n')
                            with open(f'subdomain_{domain}.txt', 'a') as output_file:
                                output_file.write(result2+'\n')
                    except requests.RequestException as e:
                        pass
                print('[+] FINISH.')
                print(f"\n[+] Subdomains and status code, exported to 'subdomains_code_{domain}.txt'.")
                print(f"[+] Subdomains exported to 'subdomains_{domain}.txt'.")
        
        elif level_scan == 2 and not (domain.startswith('https://') or domain.startswith('http://')):
            with open('subdomains-v2.txt','r') as file:
                for line in file:
                    subdomain = line.strip()
                    full_url = f"http://{subdomain}.{domain}"
                    try:
                        response = requests.get(full_url)
                        if response.status_code in [200, 202, 304, 400, 403, 404, 500, 502]:
                            result = f'{subdomain}.{domain} | [{response.status_code}]'
                            result2 = f'{subdomain}.{domain}'
                            print(result)
                            with open(f'subdomains_code_{domain}.txt', 'a') as output_file:
                                output_file.write(result+'\n')
                            with open(f'subdomain_{domain}.txt', 'a') as output_file:
                                output_file.write(result2+'\n')    
                    except requests.RequestException as e:
                        pass
                print('[+] FINISH.')
                print(f"\n[+] Subdomains and status code, exported to 'subdomains_code_{domain}.txt'.")
                print(f"[+] Subdomains exported to 'subdomains_{domain}.txt'.")
        elif level_scan == 3 and not (domain.startswith('https://') or domain.startswith('http://')):
            with open('subdomains-v3.txt','r') as file:
                for line in file:
                    subdomain = line.strip()
                    full_url = f"http://{subdomain}.{domain}"
                    try:
                        response = requests.get(full_url)
                        if response.status_code in [200, 202, 304, 400, 403, 404, 500, 502]:
                            result = f'{subdomain}.{domain} | [{response.status_code}]'
                            result2 = f'{subdomain}.{domain}'
                            print(result)
                            with open(f'subdomains_code_{domain}.txt', 'a') as output_file:
                                output_file.write(result+'\n')
                            with open(f'subdomain_{domain}.txt', 'a') as output_file:
                                output_file.write(result2+'\n')    
                    except requests.RequestException as e:
                        pass
                print('[+] FINISH.')
                print(f"\n[+] Subdomains and status code, exported to 'subdomains_code_{domain}.txt'.")
                print(f"[+] Subdomains exported to 'subdomains_{domain}.txt'.")                
        else:
            print("[-] Sorry. Could not find subdomains.")
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt as k:
        print(k)
if __name__ == '__main__':
    main()
