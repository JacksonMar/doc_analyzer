from ..link_analyzer.module_link_analyzer import LinkAnalyzer

import pdfx

# Находим и открываем ПДФ

class PDFAnalyzer:

    url_cls = []

    def __init__(self, path):
        self.path = path
        self.text = self.read()
        self.url = self.get_links
        self.link_analyzer = LinkAnalyzer()

    def read(self):
        pdf = pdfx.PDFx(self.path)
        return pdf

    @property  # обеспечивает интерфейс для атрибутов экземпляра класса.
    def get_links(self):
        link_list = []
        some_dict = self.read().get_references_as_dict()
        for v in some_dict.values():
            link_list.append(v)

        collect_links = []
        for i in link_list:
            if isinstance(i, list):
                for b in i:
                    collect_links.append(b)
            else:
                collect_links.append(i)
        self.url_cls = collect_links.copy()
        return collect_links
