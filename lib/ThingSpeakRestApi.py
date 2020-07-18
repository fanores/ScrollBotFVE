"""Thing Speak REST API"""
from lib.HttpClient import HttpClient
from lib.FveScrollBotError import FveHttpError


class ThingSpeakRestApi:
    # constants
    URL_UPDATE_SUFFIX = 'update.json'
    URL_QUESTION_MARK = '?'
    URL_WRITE_API = 'api_key='
    URL_AMPERSAND = '&'
    URL_FIELD1 = 'field1='
    URL_FIELD2 = 'field2='

    # constructor
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    # send get request to HTTP client
    def __send_get_request(self, request_url):
        try:
            fve_response = HttpClient.get_request(request_url)
        except FveHttpError as error:
            raise FveHttpError(print(error))

        return fve_response

    # write one data value to ThingSpeak
    def write_one_measurement_value(self, field1=None):
        """
            Write Measurements -> 'https://api.thingspeak.com/update.json?api_key=<write_api_key>&field1=<field1_value>'
            List of Parameters:
            -> <write_api_key> : API key from ThingSpeak profile
            -> <field1_value> : measurement value
        :return: request response from FVE
        """
        if field1 is None:
            field1 = 0

        request_url = (self.url + self.URL_UPDATE_SUFFIX + self.URL_QUESTION_MARK + self.URL_WRITE_API +
                       self.api_key + self.URL_AMPERSAND + self.URL_FIELD1 + field1)

        return self.__send_get_request(request_url)
