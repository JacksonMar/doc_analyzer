import requests
import datetime


class LinkAnalyzer:

    INVALID_URL = []

    def __int__(self, text):
        self.text = text

    def collect_links(self, link_list):
        collect_links = []
        for i in link_list:
            if isinstance(i, list):
                for b in i:
                    collect_links.append(b)
            else:
                collect_links.append(i)
        return collect_links

    def check_link(self, link_list):
        for i in self.collect_links(link_list):
            try:
                respond = requests.get(i)
                print(f"{respond.status_code} --->  {i}")
            except:
                print(f"Invalid URL ---> {i}")
                self.INVALID_URL.append(i)

    def review_link(self, url):
        try:
            respond = requests.get(url)
            print(f"{respond.status_code} --->  {url}")
        except:
            print(f"Invalid URL ---> {url}")
            self.INVALID_URL.append(url)

    def review_links(self, link_list):
        for i in link_list:
            try:
                respond = requests.get(i)
                print(f"{respond.status_code} --->  {i}")
            except:
                print(f"Invalid URL ---> {i}")
                self.INVALID_URL.append(i)

    def clean(self, link_list):
        link_list.clear()
        return link_list

    def make_report(self, link_list):
        data_time = datetime.datetime.now()
        with open("report_date_time_number_of_links.txt", "w") as f:
            f.write(str(data_time) + "\n" + str(link_list) + "\n"
                    + "Invalid URL --->" + str(self.INVALID_URL))