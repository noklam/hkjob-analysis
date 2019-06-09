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


# %%
class Crawler:
    class_no_jobs = "_1f-toO_" # Subject to change
    HOME_PAGE = "https://hk.jobsdb.com/hk/jobs/information-technology/1"
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
       


# %%
crawler = Crawler()

# %%
crawler.get_numbers_of_job(soup)
crawler.get_numbers_of_page()

# %%

# %%
a = Crawler()

# %%
Crawler.__instance


# %% [markdown]
# # Unit Test

# %%
def test_get_page_response_200(request: requests.models.Response):
    assert request.status_code == 200

test_get_page_response_200(req)

# %%
