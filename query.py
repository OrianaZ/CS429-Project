import requests
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

def display_results(results):
    if not results:
        print("No results found.")
    else:
        print("Top-ranked documents:")
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. Filename: {result['filename']}, Similarity Score: {result['similarity_score']:.4f}")

def main():
    start_flask_server()
    
    print("Welcome to the Interactive Query System!")
    print("Type 'exit' to quit at any time.")

    while True:
        query = input("Enter your query: ")

        if query.lower() == 'exit':
            print("Exiting Interactive Query System. Goodbye!")
            break

        results = send_query(query)

        display_results(results)

if __name__ == '__main__':
    main()


#usage python query.py