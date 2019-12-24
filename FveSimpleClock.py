"""FVE Simple Clock with Day Measurement Storage"""
# ScrollPhatHD requirements
import time
import scrollphathd
from scrollphathd.fonts import font5x5
# FVE data processing requirements
from lib.FveHttpClient import FveHttpClient
from lib.FveXmlParser import FveXmlParser
from lib.FveFileWriter import FveFileWriter
from pathlib import Path

def main():
    # Brightness of Scroll Phat HD
    BRIGHTNESS = 0.3

    # FVE Pimoroni Scroll Bot is upside down, fix this!
    scrollphathd.rotate(degrees=180)

    while True:
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
