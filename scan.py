import requests

def menu():
    print(r'''
                                             __
   _____  _____  ____ _   ____          ____/ /
  / ___/ / ___/ / __ `/  / __ \ ______ / __  /
 (__  ) / /__  / /_/ /  / / / //_____// /_/ /
/____/  \___/  \__,_/  /_/ /_/        \__,_/
            
            [*] Version >> 0.2
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
                print('Find Subdomain.')
            elif option == 3:
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
            response = requests.get(url)
            headers_response = response.headers
            print('____________SECURITY HEADERS____________\n')
            for headers in headers_response:
                if headers in headers_list:
                    print(f'{headers}')
            print('________________________________________\n')
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

if __name__ == '__main__':
    main()
