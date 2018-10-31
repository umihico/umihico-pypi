from lxml.etree import ElementBase as _ElementBase
from lxml.html import fromstring as _fromstring


def elements_to_strings_list(lxml_elements):
    lxml_elements = lxml_elements if isinstance(
        lxml_elements, list) else [lxml_elements, ]
    return [str(element.text_content() if isinstance(
        element, _ElementBase) else element) for element in lxml_elements]


def vaild_xpath(xpath):
    emptylxml = _fromstring(
        '<html><head><title></title></head><body></body></html>')
    try:
        emptylxml.xpath(xpath)
        return True
    except Exception as e:
        return False
