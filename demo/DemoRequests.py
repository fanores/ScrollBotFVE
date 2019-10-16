import requests

def main():
    print('Request - start at: 185.152.113.8:8003')

    def getActualResults(url):
        # Get Actual Results -> 'http://185.152.113.8:8003/meas.xml'
        # List of Elements:
        # -> <PPS> : sum of phase L1 + L2 + L3
        # -> <FE1> : total produced power
        # -> <DaR> : date
        # -> <TiR> : time

        response = requests.get(url)

        if response.status_code == 200:
            print('200: Success')
            responseBody = response.text
        elif response.status_code == 404:
            print('400: Error')
            responseBody = ''

        return  responseBody

    print('ACTUAL RESULTS:')
    print(getActualResults('http://185.152.113.8:8003/meas.xml'))


if __name__ == '__main__': main()
