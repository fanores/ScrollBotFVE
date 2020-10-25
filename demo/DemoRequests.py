import requests


def main():
	print('Request - start at: 192.168.2.51:8003')

	def get_actual_results(url):
		# Get Actual Results -> 'http://192.168.2.51:8003/meas.xml'
		# List of Elements:
		# -> <PPS> : sum of phase L1 + L2 + L3
		# -> <FE1> : total produced power
		# -> <DaR> : date
		# -> <TiR> : time

		response = requests.get(url)

		if response.status_code == 200:
			print('200: Success')
			response_body = response.text
		elif response.status_code == 404:
			print('400: Error')
			response_body = ''
		else:
			response_body = ''

		return response_body

	print('ACTUAL RESULTS:')
	print(get_actual_results('http://192.168.2.51:8003/meas.xml'))


if __name__ == '__main__':
	main()
