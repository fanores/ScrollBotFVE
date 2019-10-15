import requests

def main():
    print('Request - start at: 185.152.113.8:8003')
    response = requests.get('http://185.152.113.8:8003/meas.xml')

    if response.status_code == 200:
        print('200: Success')
    elif response.status_code == 404:
        print('400: Error')

if __name__ == '__main__': main()
