"""FVE ScrollBot"""
from lib.FveHttpClient import FveHttpClient
from lib.FveXmlParser import FveXmlParser
from lib.FveFileWriter import FveFileWriter
from pathlib import Path


def main():
    # Initialize FVE ScrollBot
    url = 'http://192.168.2.51:8003/'
    print('Request starts at: {}'.format(url))

    # --------------------------------------------------------------------------------
    # Get & Process Actual Measurements
    # --------------------------------------------------------------------------------
    print('ACTUAL MEASUREMENT DETAILS:')
    fve_http_client = FveHttpClient(url)
    fve_response = fve_http_client.get_actual_measurements()
    print(fve_response.text)

    # Parse Measurements
    fve_xml_parser = FveXmlParser(fve_response.text)
    actual_measurement = fve_xml_parser.parse_xml()
    print(actual_measurement)

    # Write Actual Measurements to File
    project_folder_path = Path("measurements")
    actual_measurement_file = project_folder_path / "actual_measurement.txt"
    fve_file_writer = FveFileWriter(actual_measurement_file)
    fve_file_writer.write_actual_measurement(actual_measurement)

    # --------------------------------------------------------------------------------
    # Get & Process Daily Measurements
    # --------------------------------------------------------------------------------
    print('YESTERDAY MEASUREMENT DETAILS:')
    fve_http_client = FveHttpClient(url)
    fve_response = fve_http_client.get_day_measurements('1')
    print(fve_response.text)

    # Parse Measurements
    fve_xml_parser = FveXmlParser(fve_response.text)
    day_measurement = fve_xml_parser.parse_xml()
    print(day_measurement)

    # Write Day Measurements to File
    project_folder_path = Path("measurements")
    day_measurement_file = project_folder_path / "day_measurement.txt"
    fve_file_writer = FveFileWriter(day_measurement_file)
    fve_file_writer.write_day_measurement(day_measurement)

if __name__ == '__main__':
    main()
