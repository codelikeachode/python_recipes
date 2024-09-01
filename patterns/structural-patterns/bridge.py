from abc import ABC, abstractmethod


# Abstraction
class IText(ABC):
    def __init__(self, text_imp):
        self.textImp = text_imp

    # Operations
    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def add_line(self, value):
        pass


# Refined Abstraction
class TextMaker(IText):
    def get_text(self):
        return self.textImp.get_string()

    def add_line(self, value):
        self.textImp.append_line(value)


# Implementor
class TextBuilder:
    def __init__(self):
        self.rows = []

    def get_string(self):
        return "\n".join(self.rows)

    def append_line(self, value):
        self.rows.append(value)


# Concrete Implementor
class HtmlBuilder(TextBuilder):
    def append_line(self, value):
        self.rows.append("<span>" + value + "</span><br/>")


def fill_text_builder(text_imp):
    text_maker = TextMaker(text_imp)
    text_maker.add_line("line 1")
    text_maker.add_line("line 2")
    return text_maker


# Client
textMaker = fill_text_builder(TextBuilder())
text = textMaker.get_text()
# test: line 1
#       line 2

htmlMaker = fill_text_builder(HtmlBuilder())
html = htmlMaker.get_text()
# html: <span>line 1</span><br/>
#       <span>line 2</span><br/>

print(text)
print(html)

"""
Decouple an abstraction from its implementation so that the two can vary independently.
"""
