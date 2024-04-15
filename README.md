# CS429-Project Oriana Zup

**Abstract- Development summary, objectives, and next steps.** 

**Overview- Solution outline, relevant literature, proposed system.**

**Design- System capabilities, interactions, integration.** 

**Architecture- Software components, interfaces, implementation.** 

**Operation- Software commands, inputs, installation.** 

**Conclusion- Success/Failure results, outputs, caveats/cautions.** 

**Data Sources- Links, downloads, access information.** 

**Test Cases- Framework, harness, coverage.** 

**Source Code- Listings, documentation, dependencies (open-source).** 

**Bibliography- Reference citations (Chicago style- AMS/AIP or ACM/IEEE)** 

usages in order <br>
python crawlerRun.py scrapy https://example.com 3 2 <br>
python index.py <br>
python query.py <br>

Process: <br>
Started new project in VScode on my computer <br>
Installed the latest version of python 3.12.3 <br>
Created a github repository for this project <br>
- initialized this project with a license and a ReadME file <br>
  - put the contents to be the headers given on the project info document <br> <br>

Started with the first objective <br>
- installed scrapy
- created a new scrapy project <br>
- created a spider that will take inputs URL/Domain, Max Pages, Max Depth <br>
- makes sure spider crawled the information correctly  <br>
- Created a python file to run the crawler <br>
  - made sure that the user can specify each of the variables URL/Domain, Max Pages, Max Depth <br>
  - made sure that it correctly imitates the crawler, and has correct uage requirements met (will not error out)<br>
  - Usage: python crawlerRun.py scrapy https://example.com 3 2 <br> <br>
 
Moved onto second objective <br>
- installed sklearn, pickle <br>
- started to try and import sklearn <br>
- ran into issues of it not recognizing the import <br>
- spent a lot of time troubleshooting, to no avail <br>
- decided on my own to try and downgrade my python verson from 3.12.3 to 3.10.7 as that was the 'global version' indicated on my computer and within VScode <br>
  - so uninstalled python on computer, and reinstalled 3.10.7 <br>
- Installed sklearn, pickle <br>
- starting to think about writing the code for the indexer. realized I needed to store the crawled documents somewhere <br> <br>

Went back to modify first objective <br>
- had to reinstalled scrapy, <br>
- recreated the project with an updated name <br>
- decided to store the crawled documents to a folder called 'Crawled Documents' <br>
- decided to save each crawled page in a separate html file fo easier reading <br>
- updated naming convention to acknowledge the specific command run <br>
- fixed the files saving to the right place <br> <br>

Resume with second objective  <br>
- decided that functionality will be to take all the pages that are in the 'CrawledDocuments' Folder and index them <br>
  - Usage: python index.py <br>
- needed functionality, for:  <br>
  - getting(collecting) the documents  <br>
  - correctly parsing the documents  <br>
  - building the actual indexes  <br>
  - saving them in pkl format.  <br>
- created those functionalities.  <br>
  - needed additional imports: numpy, beautifulsoup4
  - Since I was just focusing on Indexes decided to wait to implement Cosine similarity until working on part 3  <br>
- since there were differently stored html files I decided to follow the same format for the indexes. Each index was stories, so each file contained the 'vocabulary'(terms) and the TF-IDF matrix for each term.  <br>
- Then decided to store a separate file created with the full TF-IDF matrix for each term within all the documents  <br>
- Stored each of these files in a separate folder called 'IndexedDocuments'  <br>
- Since the .pkl files where not 'readable' I wanted a way to authenticate it is working properly therefore added a separate functionality to save to txt files as well.  <br>
- in order to not conflict with requirements these files were stored in a separate folder.  <br>
  - Decided to keep this functionality for post-testing because I like it, and gives the user the ability to see specific documents  <br>  <br>
 
Moved on to third objective   <br>
- installed Flask <br>
- looked up what flask was /how to implement since I have not used it before <br>
  - used page: https://ask.replit.com/t/how-should-i-go-about-learning-flask/58130 <br>
    - used subsequent links on this page as well <br>
- Attempted implementation of flask app, <br>
- went back to the index file to create a 'search' function for the query <br>
  - Therefore now implementing the cosine_similarity <br>
- created a function in flask app to handle the query as well as make sure it is using the indexed documents. <br>
- tried running flask app, realized needed other functionality to handle user input <br>
- created another file to handle this <br>
  - Usage: python query.py  <br>
  - this file will run the flask app, so the user does not have to do that separately and then prompt user for a query <br>
  - also allows the user to exit, by typing 'exit' <br>
  - this file also will output the top ranked documents based on the Similarity score to the query (as calculated in the search function) <br> <br>

Fixes and Improvements: <br>
- user can now specify the number of results they want retrieved y tagging the end of there query with a k number 'k=#' <br>
  - it will default to 10 items retrieved <br>
    - decided this because there could be ALOT of indexed documents. <br>
- fixed the usage in the CrawlerRun document to reflect the name changes,  <br>
- Spelling Corrections Here <br> <br>

Future ideas: <br>
- 1 command that will run the Crawl, Index, and then prompt a query input by the user <br>
