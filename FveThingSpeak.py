"""FVE ThingSpeak - Upload"""
from lib.FveRestApi import FveRestApi
from lib.FveXmlParser import FveXmlParser
from lib.ThingSpeakRestApi import ThingSpeakRestApi
from datetime import datetime


def main():
    # Initialize FVE
    fve_url = 'http://192.168.2.51:8003/'
    thing_speak_url = 'https://api.thingspeak.com/'
    ts_api_key = '123'

    # TODO: Schedule a job
    actual_measurement_job(fve_url, thing_speak_url, ts_api_key)


def actual_measurement_job(fve_url, ts_url, ts_api_key):
    # --- START
    print('Measurement starts at: {}'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    # --- FVE -> get actual measurement
    fve = FveRestApi(fve_url)
    fve_response = fve.get_actual_measurements()

    # --- PARSER -> parse measurement into a dictionary
    xml_parser = FveXmlParser()
    measurement = xml_parser.parse_root_child_elements_into_dictionary(fve_response.text)

    # --- THING-SPEAK -> upload measurement
    thing_speak = ThingSpeakRestApi(ts_url, ts_api_key)
    thing_speak.write_one_measurement_value(measurement.get('PPS', ""))

    # --- END
    print('Measurement is finished!')


if __name__ == '__main__':
    main()
