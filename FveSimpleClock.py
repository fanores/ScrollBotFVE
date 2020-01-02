"""FVE Simple Clock with Day Measurement Storage"""
# ScrollPhatHD requirements
import time
from datetime import date
import scrollphathd
from scrollphathd.fonts import font5x5
# FVE data processing requirements
from lib.FveHttpClient import FveHttpClient
from lib.FveXmlParser import FveXmlParser
from lib.FveFileWriter import FveFileWriter
from pathlib import Path

def main():
	# CONSTANTS: ScrollPhat HD
	BRIGHTNESS = 0.1 # Brightness of Scroll Phat HD

	# CONSTANTS: FVE
	URL = 'http://192.168.2.51:8003/'

	# FVE Pimoroni Scroll Bot is upside down, fix this!
	scrollphathd.rotate(degrees=180)

	# Initialize FVE prerequisites
	fve_http_client = FveHttpClient(URL)
	measurements_folder_path = Path("measurements")
	day_measurement_file = measurements_folder_path / "day_measurement.txt"
	date_for_measurement = ''

	while True:
		# ##############################################################
		# FVE day measurement
		# ##############################################################
		if date_for_measurement != date.today() and time.strftime("%H") >= "00" and time.strftime("%M") >= "10":
			fve_response = fve_http_client.get_day_measurements('1')
			fve_xml_parser = FveXmlParser(fve_response.text)
			day_measurement = fve_xml_parser.parse_xml()
			fve_file_writer = FveFileWriter(day_measurement_file)
			fve_file_writer.write_day_measurement(day_measurement)
			date_for_measurement = date.today()

		# ##############################################################
		# ScrollPhat HD time display
		# ##############################################################
		scrollphathd.clear()

		# Display the time (HH:MM) in a 5x5 pixel font
		scrollphathd.write_string(
			time.strftime("%H:%M"),
			x=0,  # Align to the left of the buffer
			y=0,  # Align to the top of the buffer
			font=font5x5,  # Use the font5x5 font we imported above
			brightness=BRIGHTNESS  # Use our global brightness value
		)

		# int(time.time()) % 2 will tick between 0 and 1 every second.
		# We can use this fact to clear the ":" and cause it to blink on/off
		# every other second, like a digital clock.
		# To do this we clear a rectangle 8 pixels along, 0 down,
		# that's 1 pixel wide and 5 pixels tall.
		if int(time.time()) % 2 == 0:
			scrollphathd.clear_rect(8, 0, 1, 5)

		# Display our time and sleep a bit. Using 1 second in time.sleep
		# is not recommended, since you might get quite far out of phase
		# with the passing of real wall-time seconds and it'll look weird!
		#
		# 1/10th of a second is accurate enough for a simple clock though :D
		scrollphathd.show()
		time.sleep(0.1)

if __name__ == '__main__':
	print(
		"""
			FVE Simple Clock:
			Displays hours and minutes in text,
			plus stores FVE day measurements.
			Press Ctrl+C to exit!
		""")
	main()
