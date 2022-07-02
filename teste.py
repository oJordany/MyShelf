from base64 import decode
import requests 
import copy
import json
import re

def request_open_library(isbn):
    try:
        result = requests.get(
            f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
        )
    except:
        return "Connection Failure"
    books = result.json()
    pattern = re.compile(r"\[|\'|\'|\"|\"|\]")
    
    encoded = json.dumps(books)
    decoded = json.loads(encoded)
    decoded = decoded[f'ISBN:{isbn}']

    metadata = dict()
    metadata["type"] = 'book'
    listAuthors = list()
    listPublishers = list()
    listLanguages = list()
    try:
        metadata["title"] = decoded["title"]+" - "+decoded["subtitle"]
    except:
        metadata["title"] = decoded["title"]
    try:
        for author in decoded['authors']:
            listAuthors.append(author['name'])
        metadata["author"] = re.sub(pattern,'', str(listAuthors))
    except:
        metadata["author"] = 'NULL'
    try:
        metadata['year'] = decoded["publish_date"]
    except:
        metadata['year'] = 'NULL'
    metadata['identifier'] = isbn 
    try:
        for publisher in decoded['publishers']:
            listPublishers.append(publisher['name'])
        metadata['publisher'] = re.sub(pattern, '', str(listPublishers))
    except:
        metadata['publisher'] = 'NULL'
    try:
        for language in decoded['subject_places']:
            listLanguages.append(language['name'])
        metadata["language"] = re.sub(pattern,'', str(listLanguages))
    except:
        metadata["language"] = 'NULL'

    print(metadata)

    return metadata

request_open_library('9788575413708')