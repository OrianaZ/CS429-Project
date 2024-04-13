from flask import Flask, request, jsonify
import os
import pickle
from index import search

app = Flask(__name__)

INDEXED_DOCUMENTS_DIR = 'IndexedDocuments'

@app.route('/query', methods=['POST'])
def query_handler():
    query = request.json['query']

    indexed_documents = load_indexed_documents(INDEXED_DOCUMENTS_DIR)

    if not indexed_documents:
        return jsonify({'error': 'No indexed documents found'}), 500

    if not any('vectorizer' in doc for doc in indexed_documents.values()):
        return jsonify({'error': 'Vectorizers missing in indexed documents'}), 500

    try:
        results = search(query, indexed_documents)
        return jsonify({'results': results}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def load_indexed_documents(directory):
    indexed_documents = {}

    for filename in os.listdir(directory):
        if filename.endswith('-index.pkl'):
            index_file_path = os.path.join(directory, filename)
            with open(index_file_path, 'rb') as file:
                index_data = pickle.load(file)
                indexed_documents[index_data['filename']] = {
                    'vectorizer': index_data['vectorizer'],
                    'tfidf_matrix': index_data['tfidf_matrix']
                }

    print(f"Loaded {len(indexed_documents)} indexed documents")
    return indexed_documents

if __name__ == '__main__':
    app.run(debug=True)

#needed installed things
#pip install Flask