# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import requests
from bs4 import BeautifulSoup
import re
from functional import seq
from tqdm import tqdm_notebook as tqdm


# %%
class Crawler:
    class_no_jobs = "_1f-toO_" # Subject to change
    class_jobs_pane = "_35U47DP"
    HOME_PAGE = "https://hk.jobsdb.com/hk/jobs/information-technology/1"
    BASE_LINK = "https://hk.jobsdb.com/hk/jobs/information-technology/"
    req = requests.get(HOME_PAGE)
    soup = BeautifulSoup(req.content)
    jobs_per_page = 30
        
    def get_numbers_of_job(self, soup:BeautifulSoup):
            string = soup.find("span", {"class": self.class_no_jobs}).parent.get_text() # '1-30 of 7634 jobs'
            pattern = re.compile(r'.+ of (\d+) jobs') 
            search_group = pattern.search(string)
            self.no_jobs = int(search_group.group(1)) # Extract the first group, group(0) is full match
            if self.no_jobs:                
                print(f"There are {self.no_jobs} jobs")
            else:
                print('Maybe site is changed? cannot locate the numbers of jobs')
                
    def get_numbers_of_page(self):
        if self.no_jobs is None:
            self.get_numbers_of_job(self.soup)
        self.no_pages = self.no_jobs // self.jobs_per_page + 1  
        print(f"There are {self.no_pages} pages")
        return self.no_jobs
    
    def is_job_href(self, href:str):
        # https://hk.jobsdb.com/hk/en/job/associate-avp-vp-debt-capital-market-100003007140188
        return href.startwith("https://hk.jobsdb.com/hk/en/jobs/")
    
    def parse_href(self, soup:BeautifulSoup):
#         print("parse job")
        tag_jobs_list = soup.select("#contentContainer")[0].select("div > span > a")
        # Adopting some functional programming style here
        href_list = (seq(tag_jobs_list)
                     .filter(has_href)
                     .map(extract_href)
                    )
        return list(href_list)
            
    def execute(self):
        print('Start Crawling')
        
        jobs_list = []
        current_page = 1
        page_to_crawl = self.BASE_LINK + str(current_page)
                
        req = requests.get(page_to_crawl)
        soup = BeautifulSoup(req.content)              
        
        for current_page in tqdm(range(1, self.no_pages + 1)):
            jobs_list = jobs_list + self.parse_href(soup)
 
        print("Finish")         
        print(f"We Crawl {len(jobs_list)} jobs")
        return jobs_list
#             break

        
            
       


# %%
p = soup.select("#contentContainer")[0].select("div > span > a")
# filter non href > list extract get href

# %%
def has_href(x):
    return hasattr(x, "href")

def extract_href(x):
    return x.get("href")


# %%
crawler = Crawler()

# %%
crawler.get_numbers_of_job(soup)
crawler.get_numbers_of_page()

# %%
crawler.jobs_per_p

# %%
crawler.jobs_list = crawler.execute()


# %% [markdown]
# # Unit Test

# %%
def test_get_page_response_200(request: requests.models.Response):
    assert request.status_code == 200

test_get_page_response_200(req)


# %%
def test_is_job_href():
    crawler = Crawler()
    href = "https://hk.jobsdb.com/hk/en/job/associate-avp-vp-debt-capital-market-100003007140188"
    assert  crawler.is_job_href(href)
    
  
    

# %%
