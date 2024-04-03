
#running scrappy crawler
import os
import sys

def run_spider(url, max_pages, max_depth):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_folder = os.path.join(script_dir, "ScrappyCS429Project")
    os.chdir(project_folder)

    os.system(f'scrapy crawl myspider -a url={url} -a max_pages={max_pages} -a max_depth={max_depth}')

if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] != "scrappy":
        print("Usage: python projectRunFile.py scrappy <url> <max_pages> <max_depth>")
    else:
        url = sys.argv[2]
        max_pages = sys.argv[3]
        max_depth = sys.argv[4]
        run_spider(url, max_pages, max_depth)
        
        
#python projectRunFile.py scrappy https://example.com 1 1



