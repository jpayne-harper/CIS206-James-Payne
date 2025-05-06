import json
import xml.etree.ElementTree as ET

def load_json_books(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['books']

def load_xml_books(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    books = []
    for book in root.findall('book'):
        books.append({
            "title": book.find('title').text,
            "author": book.find('author').text,
            "year": int(book.find('year').text),
            "available": book.find('available').text == 'true'
        })
    return books

def search_books(books, title):
    for book in books:
        if book['title'].lower() == title.lower():
            return book
    return None

def run_search_interface(books):
    while True:
        title = input("\nEnter a book title (or 'exit' to quit): ")
        if title.lower() == 'exit':
            break
        result = search_books(books, title)
        if result:
            print(f"Title: {result['title']}")
            print(f"Author: {result['author']}")
            print(f"Year Published: {result['year']}")
        else:
            print(f"'{title}' not found in the collection.")

if __name__ == '__main__':
    print("Choose data source:")
    print("1. JSON")
    print("2. XML")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        books = load_json_books('books.json')
        print("\nLoaded JSON books:")
    elif choice == '2':
        books = load_xml_books('books.xml')
        print("\nLoaded XML books:")
    else:
        print("Invalid choice. Exiting.")
        exit()

    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']})")

    run_search_interface(books)
