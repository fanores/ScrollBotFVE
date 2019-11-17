"""FVE XML Parser"""
import xml.etree.ElementTree as ElementTree
from collections import defaultdict
from lib.FveScrollBotError import FveXmlError


class FveXmlParser:
    # constants

    # constructor
    def __init__(self, xml):
        self.xml = xml

    # parse actual measurements from response
    def parse_xml(self):
        """
            Parse Actual Measurements
            Stores all the XML elements into a dictionary.
        :return: dictionary of all elements of the ROOT node
        """
        actual_measurements = defaultdict(str)

        try:
            root_element = ElementTree.fromstring(self.xml)
        except FveXmlError as error:
            raise FveXmlError(print(error))

        for child_element in root_element:
            actual_measurements[child_element.tag] = child_element.text

        return actual_measurements
