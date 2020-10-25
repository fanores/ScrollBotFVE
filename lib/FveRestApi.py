"""FVE REST API"""
from lib.HttpClient import HttpClient
from lib.FveScrollBotError import FveHttpError


class FveRestApi:
    # constants
    ACTUAL_MEASUREMENT_URL_SUFFIX = 'meas.xml'
    DAY_MEASUREMENT_URL_SUFFIX = 'stat_day.xml?day={index}'
    WEEK_MEASUREMENT_URL_SUFFIX = 'stat_week.xml'
    MONTH_MEASUREMENT_URL_SUFFIX = 'stat_month.xml'

    # constructor
    def __init__(self, url):
        self.url = url

    # send get request to HTTP client
    def __send_get_request(self, request_url):
        try:
            fve_response = HttpClient.get_request(request_url)
        except FveHttpError as error:
            raise FveHttpError(print(error))

        return fve_response

    # get actual measurements response body
    def get_actual_measurements(self):
        """
            Get Actual Results -> 'http://127.0.1.1:8080/meas.xml'
            List of Elements:
            -> <PPS> : sum of phase L1 + L2 + L3
            -> <FE1> : total produced power
            -> <DaR> : date
            -> <TiR> : time
        :return: request response from FVE
        """
        request_url = self.url + self.ACTUAL_MEASUREMENT_URL_SUFFIX

        return self.__send_get_request(request_url)

    # get daily measurements response body
    def get_day_measurements(self, day):
        """
            Get Day Results -> 'http://127.0.0.1:8080/stat_day.xml?day={index}'
            {index} - 1: yesterday
                      2: day before yesterday
                      ...
            List of Elements:
            -> <SDD{index}> : measured day
            -> <SDS4>       : surplus (not consumed) by all phases L1 + L2 + L3
            -> <SDH4>       : consumed by all phases L1 + L2 + L3 (high tariff)
            -> <SDL4>       : consumed by all phases L1 + L2 + L3 (low tariff)
            -> <SDP4>       : produced by all phases L1 + L2 + L3
        :return: request response from FVE
        """
        request_url = self.url + self.DAY_MEASUREMENT_URL_SUFFIX
        request_url = request_url.replace('{index}', day)

        return self.__send_get_request(request_url)
