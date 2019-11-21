"""FVE ScrollBot"""
from lib.FveHttpClient import FveHttpClient
from lib.FveXmlParser import FveXmlParser
from lib.FveFileWriter import FveFileWriter
from pathlib import Path


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
    actual_measurement = fve_xml_parser.parse_xml()
    print(actual_measurement)

    # Write Measurements to File
    project_folder_path = Path("measurements")
    actual_measurement_file = project_folder_path / "actual_measurement.txt"
    fve_file_writer = FveFileWriter(actual_measurement_file)
    fve_file_writer.write_actual_measurement(actual_measurement)


if __name__ == '__main__':
    main()
