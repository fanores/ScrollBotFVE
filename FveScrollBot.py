"""FVE ScrollBot"""
from lib.FveHttpClient import FveHttpClient


def main():
    url = 'http://192.168.2.51:8003/'
    print('Request starts at: {}'.format(url))

    http_client = FveHttpClient(url)
    print(http_client.get_actual_measurements())


if __name__ == '__main__':
    main()
