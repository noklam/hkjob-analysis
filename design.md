An app that send new job notification
=====================================

I can probably use scrapy for replacement, but I want to practise individual component, and it allows me to use Airflow to schedule jobs for different component. It is also a good change to practice my OO programming and as a little fun exercise.

# Features

- [ ] Crawler runs every week
- [ ] Features, subscribe to particular company
- [ ] Weekly, send notification if new jobs - [ ] appears through Slack
- [ ] parser to parse meta-data, such as job level, salary, company, title, location, education level etc.
- [ ] A database to store all this data in a structural way
- [ ] A datalake to dump all those HTML files
- [ ] Airflow will run these batch jobs daily, fail on retry
- [ ] Validate if the site is crawled already, if so skip it.
- [ ] Use Logger to replace print for generating systematic log


Optionally:
------------
- [ ] Validate if two jobs are same for posting repeatly (ML models, or simple Bag of Words)
- [ ] Website UI
- [ ] Dashboard to analyze some data
- [ ] Is Data Scientist Trending?
- [ ] Does Mid-level Job increasing?
- [ ] What kind of skills is trending?
- [ ] Make use of CI, unit-testing
- [ ] Altair/Flask interactive Dashboard with Vue

Tools
* sphinx/mkdoc for doc generation, API site
* pandas - data analysis
* Plotly/altair
* Django/Flask
* Database (sqlite/mysql/PSQL)
* Beautiful Soup - for parser
* Request - for crawling
* pytest
* Airflow - for scheduling
* SlackAPI
* CI/CD - Travis
* Hosting on Github pages
* logger

Why weekly?
Jobsdb usually persist for 1/2 week at least, crawling weekly reduce pressure on server and is reasonable


