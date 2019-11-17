"""FVE ScrollBot"""
from lib.FveHttpClient import FveHttpClient
from lib.FveXmlParser import FveXmlParser


def main():
    # Initialize FVE ScrollBot
    url = 'http://192.168.2.51:8003/'
    print('Request starts at: {}'.format(url))

    # Get Actual Measurements
    fve_http_client = FveHttpClient(url)
    fve_response = fve_http_client.get_actual_measurements()
    print(fve_response.text)

    # Parse Measurements
    fve_xml_parser = FveXmlParser(fve_response.text)
    actual_measurements = fve_xml_parser.parse_xml()
    print(actual_measurements)


if __name__ == '__main__':
    main()
