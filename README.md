# CS429-Project Oriana Zup

## Abstract
The objective of this project was to develop a comprehensive web document retrieval and search system using Python along with specialized libraries including Scikit-Learn, Scrapy, and Flask. The system contains a web crawler for document retrieval, an indexer for creating an inverted index, and a query processor to handle user queries effectively. Key functionalities such as TF-IDF scoring and cosine similarity were implemented to enhance document retrieval and ranking. This report outlines the design, implementation, and operation of the system, detailing its capabilities and interactions.

## Overview
The project consists of three main components: a Scrapy-based web crawler for document retrieval, a Scikit-Learn-based indexer for constructing an inverted index, and a Flask-based query processor for handling user queries. The system architecture leverages each component to facilitate efficient web crawling, indexing, and query processing. Relevant literature in information retrieval and search engine technologies guided the design and implementation of the system.

## Design
### Crawler Design
The web crawler utilizes Scrapy to download web documents in HTML format. It initializes with a seed URL/Domain, maximum pages, and maximum depth parameters, allowing concurrent crawling for scalability. The crawler extracts text content from web pages and stores them as HTML files for further processing.

### Indexer Design
The indexer implements TF-IDF scoring using Scikit-Learn, constructing an inverted index stored in pickle format. Each document's TF-IDF matrix is computed and indexed, enabling efficient cosine similarity calculations for query processing.

### Query Processor Design
The query processor is developed using Flask, providing an API endpoint to handle user queries. It validates and processes input queries, retrieves relevant documents based on cosine similarity scores, and returns top-ranked results.

## Architecture
The system architecture comprises the following components and interactions:
### Web Crawler (Scrapy):
- Initiates document retrieval from specified URLs.
- Concurrent crawling and depth limitation for efficient data acquisition.

### Indexer (Scikit-Learn):
- Computes TF-IDF scores for document indexing.
- Constructs an inverted index and stores it in pickle format for efficient retrieval.

### Query Processor (Flask):
- Provides a API for query handling.
- Validates and processes user queries, returning ranked document results.

## Operation
This respository should be cloned/downloaded in order to use commands. All commands should done from the root folder. (CS429-Project) <br>
The web document retrieval and search system can be operated in two distinct ways to accommodate different user needs: independent execution of specific tasks or streamlined execution using a single script.
### Independent Execution 
#### Crawling Documents
- Execute the following command to initiate the web crawler:
`python crawl.py <url> <max_pages> <max_depth>`
- Replace <url> with the seed URL or domain from which to start crawling.
- Replace <max_pages> with the maximum number of pages to crawl.
- Replace <max_depth> with the maximum depth of crawling (number of links away from the seed URL).

#### Indexing Documents
- Run the following command to index the crawled documents:
`python index.py`

#### Query Processing
- Start the Flask app to handle user queries:
`python query.py`
- Users will then be prompted to input queries and the program will retrieve relevant document results using the Flask-based query processor.
- The progem will default to showing the top 10 results. However the user can specify the number of ranked documents they wish to retrieve by taggin `k=#` at the end of there query. Where # is replaced by the number of documents wished to be retrieved.

### Streamlined Execution
#### Automated Workflow
- Execute the run.py script with the following command:
`python run.py <url> <max_pages> <max_depth>`
- Replace <url> with the seed URL or domain from which to start crawling.
- Replace <max_pages> with the maximum number of pages to crawl.
- Replace <max_depth> with the maximum depth of crawling (number of links away from the seed URL).
- The run.py script orchestrates the following sequence of tasks:
  - Initiates web crawling (crawl.py) to download web documents.
  - Performs document indexing (index.py) using TF-IDF scoring.
  - Starts the Flask app (query.py) for user query processing and document retrieval.

## Conclusion
The implemented web document retrieval and search system successfully achieves its objectives of crawling, indexing, and query processing. The system demonstrates efficient retrieval and ranking of web documents based on user queries using TF-IDF scoring and cosine similarity. Future enhancements could include incorporating advanced search techniques such as Query spelling-correction/suggestion (NLTK) or query expansion.

## Data Sources
The development and execution of this project involved various tools, libraries, and resources to facilitate web document retrieval, indexing, and query processing. The following data sources were used in the implementation and testing of the project components:
1. Scrapy Documentation
- Link: [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
- Description: Scrapy, a powerful web crawling and scraping framework, was utilized to build the web crawler component of the project. The official Scrapy documentation provided essential guidance on initializing crawlers, handling responses, and managing concurrent crawling.

2. Scikit-Learn Documentation
- Link: Scikit-Learn: [Machine Learning in Python](https://www.researchgate.net/publication/51969319_Scikit-learn_Machine_Learning_in_Python)
- Description: Scikit-Learn, a popular machine learning library in Python, played a crucial role in implementing the document indexer using TF-IDF scoring. The documentation offered insights into vectorization techniques, TF-IDF calculation, and cosine similarity computation.

3. Python Documentation
- Link: [Python Documentation](https://docs.python.org/3/)
- Description: The official Python documentation was referenced to understand language syntax, standard libraries, and best practices. It provided necessary information on Python version compatibility, module imports, and file operations.

4. Beautiful Soup Documentation
- Link: [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Description: Beautiful Soup, a library for parsing HTML and XML documents, was used to extract text content from crawled web pages. The documentation assisted in navigating document trees, extracting data, and handling malformed HTML.

5. Flask Documentation
- Link: [Flask Documentation](https://ask.replit.com/t/how-should-i-go-about-learning-flask/58130)
- Description: Flask, a lightweight and versatile web framework, was employed to develop the query processor component. The Flask documentation provided guidelines for creating RESTful APIs, handling HTTP requests, and rendering dynamic web pages.

6. Ask Replit Discussion
- Link: [How should I go about learning Flask?](https://ask.replit.com/t/how-should-i-go-about-learning-flask/58130)
- Description: The Ask Replit discussion forum served as a valuable resource for learning Flask and obtaining practical advice on web development using Flask. Discussions on Flask tutorials, learning paths, and community experiences informed the implementation of the Flask-based query processor.

7. Flask Quickstart Guide
- Link: [Flask Quickstart](https://flask-docs.readthedocs.io/en/latest/quickstart/)
- Description: The Flask Quickstart guide provided step-by-step instructions for setting up Flask applications, defining routes, and handling request/response cycles. It served as a foundational resource for developing the query processor and integrating Flask with other project components.

8. Additional References
- Python Software Foundation: Official resources and documentation from the Python Software Foundation offered comprehensive insights into Python development, package management, and community contributions.
- Other Online Tutorials and Forums: Various online tutorials, forums, and community-driven resources were consulted throughout the project for troubleshooting. Such as why sklearn was not working on original python version.

## Test Cases
### Crawling Test Scenarios
Different combinations of URLs, pages, and depths were used to test the crawling functionality:
- urls:
  - https://example.com
  - https://www.bbc.com/
- Pages: 1-10
- Depths: 1-10

A few examples of combinations that were used are:
- https://example.com 3 2
- https://example.com 1 1
- https://example.com 10 10
- https://www.bbc.com/ 1 1
- https://www.bbc.com/ 10 10
- https://www.bbc.com/ 3 2

### Indexing and Query Processing Test Scenarios
After crawling the specified URLs with different page and depth configurations, the system was tested for indexing and query processing using the indexed documents.
- Indexing and query processing were tested on the crawled documents for each URL and configuration.

### Automated Workflow Test Scenarios (Using run.py)
The automated workflow (run.py) facilitated the execution of multiple combinations of crawling, indexing, and query processing seamlessly.
- Various combinations of URLs, pages, and depths were used to validate the end-to-end workflow.

## Source Code
###  Listings and documentation
This Project was developed in Visual Studio Code <br>
Please see this [respository](https://github.com/OrianaZ/CS429-Project) for full code works, and documentation outline.

### Dependencies
Python version 3.10+. <br>
*note that this project was originally created in Python 3.12.3, However there were issues with it recongizing sklearn. Therefore Python version was downgraded to 3.10.7. Other versions of python have not been tested* <br>
Dependencies needed for this project are:  <br>
`pip install scrapy`  *2.11+* <br> 
`pip install scikit-learn` *1.2+* <br>
`pip install pickle`  <br>
`pip install numpy`  <br>
`pip install beautifulsoup4`  <br>
`pip install Flask` *2.2+* <br>

## Bibliography
1. Scrapy. "Scrapy Documentation." Retrieved from https://docs.scrapy.org/en/latest/.
2. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... Duchesnay, É. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
3. Grinberg, M. "Flask Documentation." Retrieved from https://flask.palletsprojects.com/en/2.0.x/.
4. Python Software Foundation. "Python Documentation." Retrieved from https://docs.python.org/3/.
5. Richardson, L. "Beautiful Soup Documentation." Retrieved from https://www.crummy.com/software/BeautifulSoup/bs4/doc/.
6. Ask Replit. "How should I go about learning Flask?" Retrieved from https://ask.replit.com/t/how-should-i-go-about-learning-flask/58130.
7. Flask Documentation. "Flask Quickstart." Retrieved from https://flask-docs.readthedocs.io/en/latest/quickstart/.
8. Flask. "Flask Documentation." Retrieved from https://flask.palletsprojects.com/en/latest/#.
