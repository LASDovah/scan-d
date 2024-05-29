import requests
import time

def main():
    try:
        option = int(input('Enter an option> '))
        while True:
            if option == 1:
                security_headers()
                break
            elif option == 2:
                print('Find Subdomain.')
            elif option == 3:
                print('Exit.')
                break
            else:
                print("[-] Data entered not recognized.")
    except Exception as e:
        print(e)
    except KeyboardInterrupt as k:
        print(k)

def security_headers():
    try:
        headers_list = ['X-Frame-Options','X-Content-Type-Options','X-Content-Security-Policy','X-XSS-Protection','Content-Security-Policy']
        url = input('URL>> ')
        response = requests.get(url)
        headers_response = response.headers
        for headers in headers_response:
            if headers_list[0] in headers:
                print(f'{headers_list[0]}: True.')
            if headers_list[1] in headers:
                print(f'{headers_list[1]}: True.')
            if headers_list[2] in headers:
                print(f'{headers_list[2]}: True.')
            if headers_list[3] in headers:
                print(f'{headers_list[3]}: True.')
            if headers_list[4] in headers:
                print(f'{headers_list[4]}: True.')
            print("[*] Finish scan.")
        
    except requests.exceptions.RequestException as e:
        print('[-] Some security headers are missing.')

if __name__ == '__main__':

    print(r'''
                                             __
   _____  _____  ____ _   ____          ____/ /
  / ___/ / ___/ / __ `/  / __ \ ______ / __  /
 (__  ) / /__  / /_/ /  / / / //_____// /_/ /
/____/  \___/  \__,_/  /_/ /_/        \__,_/
            
            [*] Version >> 0.1
            [*] Date >> 24-05-2024
            [*] Github >> LASDovah
            [*] Tool to know the status of headers and find existing subdomains.

    ________MENU_________

    [1] Security Header.
    [2] Find Subdomain.'
    [3] Exit.
    _____________________
''')
main()