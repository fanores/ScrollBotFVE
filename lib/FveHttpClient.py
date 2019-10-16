"""FVE HTTP Client"""
import requests
from requests.exceptions import HTTPError


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
            Get Actual Results -> 'http://185.152.113.8:8003/meas.xml'
            List of Elements:
            -> <PPS> : sum of phase L1 + L2 + L3
            -> <FE1> : total produced power
            -> <DaR> : date
            -> <TiR> : time
        :return: request response
        """
        request_url = self.url + self.ACTUAL_MEASUREMENT_URL_SUFFIX

        try:
            response = requests.get(request_url)
            response.raise_for_status()
        except HTTPError as http_error:
            response_body = ''
        except Exception as error:
            response_body = ''
        else:
            response_body = response.text

        return response_body
