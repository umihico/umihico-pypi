
def elements_to_strings_list(lxml_elements):
    lxml_elements = lxml_elements if isinstance(
        lxml_elements, list) else [lxml_elements, ]
    return [str(element.text_content() if isinstance(
        element, _ElementBase) else element) for element in lxml_elements]
