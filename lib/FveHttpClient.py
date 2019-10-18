"""FVE HTTP Client"""
from lib.HttpClient import HttpClient
from lib.FveScrollBotError import FveHttpError


class FveHttpClient:
    # constants
    ACTUAL_MEASUREMENT_URL_SUFFIX = 'meas.xml'
    DAY_MEASUREMENT_URL_SUFFIX = 'stat_day.xml?day={index}'
    WEEK_MEASUREMENT_URL_SUFFIX = 'stat_week.xml'
    MONTH_MEASUREMENT_URL_SUFFIX = 'stat_month.xml'

    # constructor
    def __init__(self, url):
        self.url = url

    # get actual measurements response body
    def get_actual_measurements(self):
        """
            Get Actual Results -> 'http://192.168.2.51:8003/meas.xml'
            List of Elements:
            -> <PPS> : sum of phase L1 + L2 + L3
            -> <FE1> : total produced power
            -> <DaR> : date
            -> <TiR> : time
        :return: request response from FVE
        """
        request_url = self.url + self.ACTUAL_MEASUREMENT_URL_SUFFIX

        try:
            fve_response = HttpClient.get_request(request_url)
        except FveHttpError as error:
            raise FveHttpError(print(error))

        return fve_response
