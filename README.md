# Overview
This is a small project for Competency-Test as a Data Engineer Position.

#Goal
Development of WebCrawler using Scrapy Library

#Language
Python

#Development Environment
- OS : Mac
- Python ver3.4
- MongoDB ver3.2.3
- AWS (optional)


# Intructions

- Please use hosted MongoDB at [Compose](https://compose.io/) for storing the results of the scraped documents
- Candidate should put their test results on a public code repository hosted on Github
- Once test is completed please share the Github repository URL to hiring team so they can review your work
- You are building a backend application and no UI is required, input can be provided using a configuration file or command line

# Challenge - News Content Collect and Store

Create a solution that crawls for articles from a news website, cleanses the response, stores in a mongo database then makes it available to search via an API.

## Details

- Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using the scrapy crawler framework (http://scrapy.org/) - build the application in Java, Python or Scala.
- The appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc.  Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html
- Store the data in a hosted mongo database, e.g. compose.io/mongo, for subsequent search and retrieval.  Ensure the URL of the article is included to enable comparison to the original.
- Write an API that provides access to the content in the mongo database.  The user should be able to search for articles by keyword

# Bonus point
If you deploy the solution as a public API using an Amazon EC2 instance.
