import requests # type: ignore
import subprocess
import time

def start_flask_server():
    subprocess.Popen(['python', 'appFlask.py'])

    time.sleep(3)

def send_query(query):
    flask_url = 'http://127.0.0.1:5000/query'
    query_data = {'query': query}

    response = requests.post(flask_url, json=query_data)

    if response.status_code == 200:
        results = response.json().get('results', [])
        return results
    else:
        print(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
        return []

def display_results(results, k):
    if not results:
        print("No results found.")
    else:
        print("Top-ranked documents:")
        for idx, result in enumerate(results[:min(len(results), k)], start=1):
            print(f"{idx}. Document: {result['filename']}, Similarity Score: {result['similarity_score']:.4f}")

def main():
    start_flask_server()
    
    print("Welcome to the Interactive Query System!")
    print("Type your query and append with 'k=#' to return # number of results (default 10)")
    print("Type 'exit' to quit at any time.")

    while True:
        query = input("Enter your query: ")

        if query.lower() == 'exit':
            print("Exiting Interactive Query System. Goodbye!")
            break

        parts = query.split()
        for part in parts:
            if part.lower().startswith('k='):
                try:
                    k = int(part.split('=')[1])
                    query = query.replace(part, '').strip()                    
                    break
                except ValueError:
                    k = 10
                    break
        else:
            k = 10

        results = send_query(query)

        display_results(results, k)

if __name__ == '__main__':
    main()


#usage python query.py
#query usage: 'type any query' k=#
# can omit k= for a default of 10 results