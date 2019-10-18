"""FVE ScrollBot"""
from lib.FveHttpClient import FveHttpClient


def main():
    url = 'http://192.168.2.51:8003/'
    print('Request starts at: {}'.format(url))

    fve_http_client = FveHttpClient(url)
    fve_response = fve_http_client.get_actual_measurements()
    print(fve_response.text)


if __name__ == '__main__':
    main()
