# from .pdf_analyzer.module_pdf_analyzer import PDFAnalyzer
from .pdf_analyzer.module_pdf_analyzer import PDFAnalyzer
# Не работает --->
# from Homework.Homwork_23_10_2_PDF_Analyzer_tool.doc_analyzer.pdf_analyzer.module_pdf_analyzer import PDFAnalyzer

class MainApp():
    def __init__(self, path):
        self.path = path

#
    def run(self):
        pdf = PDFAnalyzer(self.path)
        pdf.link_analyzer.collect_links(pdf.get_links)
        pdf.link_analyzer.review_links(pdf.url_cls[2:9])
        pdf.link_analyzer.make_report(pdf.url_cls)

if __name__ == "__main__":
    print("Run Package")
    pdf = MainApp("/Users/evgenijmarinosenko/Desktop/imperfect-forward-secrecy.pdf").run()


    # pdf = PDFAnalyzer("/Users/evgen/Downloads/imperfect-forward-secrecy.pdf")
    # print(pdf.link_analyzer.collect_links(pdf.get_links))
    # pdf.link_analyzer.check_link(pdf.url_cls)
    # print(pdf.link_analyzer.review_link(pdf.url_cls[9]))
    # print(pdf.link_analyzer.review_links(pdf.url_cls[2:4]))
    # print(pdf.link_analyzer.make_report(pdf.url_cls))
