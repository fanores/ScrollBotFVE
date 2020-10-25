"""FVE File Writer"""
from lib.FveScrollBotError import FveFileError


class FveFileWriter:
    # constants
    SEMICOLON = ";"
    ACTUAL_MEASUREMENT_IDS = ['DaR', 'TiR', 'FE1', 'PPS', 'FP', 'Te', 'EL1', 'ETS', 'ETL']
    DAY_MEASUREMENT_IDS = ['SDD1', 'SDD2', 'SDD3', 'SDD4', 'SDD5', 'SDD6', 'SDD7', 'SDS4', 'SDH4', 'SDL4', 'SDP4']
    ELEMENT_NOT_AVAILABLE = "N/A"

    # constructor
    def __init__(self, file):
        self.file = file

    # write actual measurements into file
    def write_actual_measurement(self, actual_measurement):
        """
            Write Actual Measurement
            1. <DaR> - Date
            2. <TiR> - Time
            3. <FE1> - Produced Till Today
            4. <PPS> - Produced Now
            5. <FP> - Power on Regulator
            6. <Te> - Temperature on Regulator
            7. <EL1> - Fault - Voltage
            8. <ETS> - Fault - Temperature Sensor
            9. <ETL> - Fault - Temperature Limit
        :return: dictionary of all elements of the ROOT node
        """

        measurement_ids = self.ACTUAL_MEASUREMENT_IDS
        try:
            file = open(str(self.file), 'a+')
        except FileNotFoundError as error:
            raise FveFileError(print(error))

        line = ''
        for element in measurement_ids:
            line = line + actual_measurement.get(element, "") + self.SEMICOLON

        file.write(line + "\n")
        file.close()

    # write day measurements into file
    def write_day_measurement(self, day_measurement):
        """
            Write Day Measurement
            1. <SDD{index}> - Date
            2. <SDS4> - Surplus
            3. <SDH4> - Consumed High Tariff
            4. <SDL4> - Consumed Low Tariff
            5. <SDP4> - Produced
        :return: dictionary of all elements of the ROOT node
        """
        day_measurement_ids = self.DAY_MEASUREMENT_IDS
        try:
            file = open(str(self.file), 'a+')
        except FileNotFoundError as error:
            raise FveFileError(print(error))

        line = ''
        for element in day_measurement_ids:
            element_value = day_measurement.get(element, self.ELEMENT_NOT_AVAILABLE)

            # store element if it is available
            if element_value != self.ELEMENT_NOT_AVAILABLE:
                line = line + day_measurement.get(element, "") + self.SEMICOLON

        file.write(line + "\n")
        file.close()
