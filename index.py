import os
import pickle
import numpy as np
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def parse_html_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text()
    return text
  
def collect_document_texts(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            text = parse_html_document(file_path)
            documents.append((filename, text)) 
    return documents
  
def build_index(document):
    filename, text = document
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    return vectorizer, tfidf_matrix, filename

  
def save_indexer(vectorizer, matrix, filename, output_directory):
    index_filename = os.path.splitext(filename)[0] + '-index.pkl'
    output_file = os.path.join(output_directory, index_filename)
    
    with open(output_file, 'wb') as file:
        index_data = {
            'vectorizer': vectorizer,
            'tfidf_matrix': matrix,
            'filename': filename
        }
        pickle.dump(index_data, file)
    
def save_to_text(vectorizer, matrix, filename, output_directory_2):
    txt_filename = os.path.splitext(filename)[0] + '-index.txt'
    txt_output_directory = output_directory_2
    if not os.path.exists(txt_output_directory):
        os.makedirs(txt_output_directory)
    
    feature_names = vectorizer.get_feature_names_out()
    tfidf_values = matrix.toarray()[0]
    
    txt_filepath = os.path.join(txt_output_directory, txt_filename)
    with open(txt_filepath, 'w', encoding='utf-8') as file:
        file.write("Vocabulary:\n")
        file.write("\n".join(feature_names) + "\n\n")
        
        file.write("TF-IDF Matrix:\n")
        for feature, value in zip(feature_names, tfidf_values):
            file.write(f"{feature}: {value:.6f}\n")
    
def save_completed_tfidf(documents, output_directory, output_directory_2):
    term_tfidf_dict = {}
    
    for filename, _ in documents:
        index_filename = os.path.splitext(filename)[0] + '-index.pkl'
        index_file = os.path.join(output_directory, index_filename)
        
        with open(index_file, 'rb') as file:
            index_data = pickle.load(file)
            feature_names = index_data['vectorizer'].get_feature_names_out()
            tfidf_values = index_data['tfidf_matrix'].toarray()[0]
        
        for feature, value in zip(feature_names, tfidf_values):
            if feature not in term_tfidf_dict:
                term_tfidf_dict[feature] = {}
            term_tfidf_dict[feature][filename] = value
    
    completed_tfidf_pickle_file = os.path.join(output_directory, 'completed-TFIDF.pkl')
    with open(completed_tfidf_pickle_file, 'wb') as file:
        pickle.dump(term_tfidf_dict, file)
        
    completed_tfidf_txt_file = os.path.join(output_directory_2, 'completed-TFIDF.txt')
    with open(completed_tfidf_txt_file, 'w', encoding='utf-8') as file:
        file.write("        ")
        for filename, _ in documents:
            file.write(f"{filename.ljust(12)}")
        file.write("\n")
        
        for term, doc_values in term_tfidf_dict.items():
            file.write(f"{term.ljust(10)}")
            for _, value in doc_values.items():
                file.write(f"{value:.6f}".ljust(12))
            file.write("\n")      

def search(query, indexed_documents):
    results = []
    
    for filename, doc_info in indexed_documents.items():
        vectorizer = doc_info['vectorizer']
        doc_tfidf_matrix = doc_info['tfidf_matrix']
        
        query_tfidf_matrix = vectorizer.transform([query])
        
        similarity = cosine_similarity(query_tfidf_matrix, doc_tfidf_matrix)
        
        results.append({
            'filename': filename,
            'similarity_score': similarity[0][0]
        })
    
    results.sort(key=lambda x: x['similarity_score'], reverse=True)
    
    return results
    
def main():
    input_directory = 'CrawledDocuments'
    output_directory = 'IndexedDocuments'
    output_directory_2 = 'IndexedDocumentsTXT'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    if not os.path.exists(output_directory_2):
        os.makedirs(output_directory_2)
    
    documents = collect_document_texts(input_directory)
    
    for document in documents:
        vectorizer, tfidf_matrix, filename = build_index(document)
        save_indexer(vectorizer, tfidf_matrix, filename, output_directory)
        save_to_text(vectorizer, tfidf_matrix, filename, output_directory_2)
    
    save_completed_tfidf(documents, output_directory, output_directory_2)

if __name__ == "__main__":
    main()


#usage
#python index.py
    
#python 3.12.3 does not work!!! wont recognize sklearn
#installed python on my device 3.10.7 same as global

#needed installed things
#pip install scikit-learn
#pip install pickle
#pip install numpy
#pip install beautifulsoup4