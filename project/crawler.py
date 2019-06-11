import requests
from bs4 import BeautifulSoup
import re
from functional import seq
from tqdm import tqdm


# from tqdm import tqdm_notebook as tqdm

def has_href(x):
    return hasattr(x, "href")


def extract_href(x):
    return x.get("href")


class Crawler:
    _class_no_jobs = "_1f-toO_"  # Subject to change
    _class_jobs_pane = "_35U47DP"
    _jobs_per_page = 30

    def __init__(self,
                 base_url: str = "https://hk.jobsdb.com/hk/jobs/information-technology/"):
        self.base_url = base_url
        self.home_url = self.base_url + "1"
        self.soup_homepage = BeautifulSoup(requests.get(self.home_url).content, "lxml")

    def get_numbers_of_job(self):
        # '1-30 of 7634 jobs'
        string = self.soup_homepage.find("span", {"class": self._class_no_jobs}).parent.get_text()
        pattern = re.compile(r'.+ of (\d+) jobs')
        search_group = pattern.search(string)
        self.no_jobs = int(search_group.group(1))  # Extract the first group, group(0) is full match
        if self.no_jobs:
            print(f"There are {self.no_jobs} jobs")
        else:
            print('Maybe site is changed? cannot locate the numbers of jobs')

    def get_numbers_of_page(self):
        if self.no_jobs is None:
            self.get_numbers_of_job(self.soup)
        self.no_pages = self.no_jobs // self._jobs_per_page + 1
        print(f"There are {self.no_pages} pages")
        return self.no_jobs

    def execute(self) -> list:
        print('Start Crawling')

        jobs_list = []
        for current_page in tqdm(range(1, self.no_pages + 1)):
            page_to_crawl = self.base_url + str(current_page)
            req = requests.get(page_to_crawl)
            soup = BeautifulSoup(req.content, "lxml")
            jobs_list = jobs_list + self.parse_href(soup)

        print("Finish")
        print(f"We Crawl {len(jobs_list)} jobs")
        return jobs_list

    #             break

    @classmethod
    def is_job_href(self, href: str):
        # https://hk.jobsdb.com/hk/en/job/associate-avp-vp-debt-capital-market-100003007140188
        return href.startswith("https://hk.jobsdb.com/hk/en/job/")

    @classmethod
    def parse_href(self, soup: BeautifulSoup):
        #         print("parse job")
        tag_jobs_list = soup.select("#contentContainer")[0].select("div > span > a")
        # Adopting some functional programming style here
        href_list = (seq(tag_jobs_list)
                     .filter(has_href)
                     .map(extract_href)
                     )
        return list(href_list)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.get_numbers_of_job()  # Dirty Hack
    crawler.get_numbers_of_page()
    crawler.jobs_list = crawler.execute()
