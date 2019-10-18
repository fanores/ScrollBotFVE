"""HTTP Client"""
import requests
from requests.exceptions import HTTPError


class HttpClient:
    @staticmethod
    def get_request(url):
        """
            Get Request: returns the response of the request call
        :return: request response
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_error:
            raise Exception('Request error: {}'.format(print(http_error)))
        except Exception as error:
            raise Exception('Request error: {}'.format(print(error)))
        else:
            response_body = response.text

        return response_body
