import os
import sys
import time

def run(url, max_pages, max_depth):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_folder = os.path.join(script_dir, "ScrapyCrawler")
    os.chdir(project_folder)
    os.system(f'scrapy crawl myspider -a url={url} -a max_pages={max_pages} -a max_depth={max_depth}')
    
    time.sleep(3)
    
    os.chdir("..")
    os.system("python index.py")
    
    time.sleep(3)
    os.system("python query.py")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python run.py <url> <max_pages> <max_depth>")
        
    else:
        url = sys.argv[1]
        max_pages = sys.argv[2]
        max_depth = sys.argv[3]
        run(url, max_pages, max_depth)
        
#python run.py https://example.com 5 2
        