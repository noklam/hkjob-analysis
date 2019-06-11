import pytest
# import crawler
from ..project.crawler import Crawler


hrefs = ["https://hk.jobsdb.com/hk/en/job/associate-avp-vp-debt-capital-market-100003007140188",]

@pytest.mark.parametrize("href", hrefs)
def test_is_job_href(href):
    crawler = Crawler()
    assert crawler.is_job_href(href)

