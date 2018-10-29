
from selenium.webdriver import Chrome as originChrome
from selenium.webdriver import ChromeOptions
import itertools as _itertools


class Chrome(originChrome):
    def _xpath(self, xfunc, xpath):
        try:
            elements = xfunc(xpath)
        except Exception as e:
            elements = anti_frame_xpath(self, xpath)
            if not(elements):
                raise
        return elements or anti_frame_xpath(self, xpath)

    def xpath(self, xpath):
        return self._xpath(self.find_element_by_xpath, xpath)

    def xpaths(self, xpath):
        return self._xpath(self.find_elements_by_xpath, xpath)

    def click(self, xpath):
        return self.xpath(xpath).click()

    def send_keys(self, xpath, *keys):
        return self.xpath(xpath).send_keys(*keys)

    def exist(self, xpath):
        return bool(len(self.xpaths(xpath)))

    def text(self, xpath):
        return self.xpath(xpath).text

    def texts(self, xpath):
        return [e.text for e in self.xpaths(xpath)]

    def get_attribute(self, xpath, attribute):
        self.xpath(xpath).get_attribute(attribute)


def anti_frame_xpath(chrome, xpath):
    for frame_index in _itertools.count():
        try:
            chrome.switch_to.parent_frame()
        except Exception as e:
            pass
        frames = chrome.find_elements_by_tag_name("frame")
        if frame_index >= len(frames):
            return []
        chrome.switch_to_frame(frames[frame_index])
        elements = chrome.find_elements_by_xpath(xpath)
        if len(elements):
            return elements


def gen_chtomeoptions():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    return options
