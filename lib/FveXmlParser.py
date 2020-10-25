"""FVE XML Parser"""
import xml.etree.ElementTree as ElementTree
from collections import defaultdict
from lib.FveScrollBotError import FveXmlError


class FveXmlParser:
    # constants

    # constructor
    # def __init__(self, xml):
    #     self.xml = xml

    # parse XML elements into dictionary
    def parse_root_child_elements_into_dictionary(self, xml):
        """
            Parse Actual Measurements
            Stores all the XML elements into a dictionary.
        :return: dictionary of all elements of the ROOT node
        """
        child_elements = defaultdict(str)

        try:
            root_element = ElementTree.fromstring(xml)
        except FveXmlError as error:
            raise FveXmlError(print(error))

        for child_element in root_element:
            child_elements[child_element.tag] = child_element.text

        return child_elements
