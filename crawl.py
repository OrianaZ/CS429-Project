import os
import sys

def run_spider(url, max_pages, max_depth):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_folder = os.path.join(script_dir, "ScrapyCrawler")
    os.chdir(project_folder)

    os.system(f'scrapy crawl myspider -a url={url} -a max_pages={max_pages} -a max_depth={max_depth}')
    
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python crawl.py <url> <max_pages> <max_depth>")
    else:
        url = sys.argv[1]
        max_pages = sys.argv[2]
        max_depth = sys.argv[3]
        run_spider(url, max_pages, max_depth)
        
#usage        
#python crawl.py https://example.com 1 1

#needed installed things
#pip install scrapy

#commands done
#scrapy startproject ScrapyCrawler