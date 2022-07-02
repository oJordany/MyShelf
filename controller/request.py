from base64 import decode
import json
from isbnlib import info
from isbnlib import meta
from tkinter import Label, StringVar, FLAT
from isbnlib.registry import bibformatters
import requests
import copy
import re
import urllib.request
import asyncio

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
    try:
        decoded = decoded[f'ISBN:{isbn}']
    except:
        return "Error: non-existent ISBN"

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
        metadata["author"] = re.sub(pattern, '', str(listAuthors))
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
        metadata["language"] = re.sub(pattern, '', str(listLanguages))
    except:
        metadata["language"] = 'NULL'
    print('pela segunda api')
    print(metadata)

    return metadata
    
def request(isbn):
    try:
        urllib.request.urlopen('http://google.com')
    except:
        return "Error: Connection Failure"
    try:
        language = info(isbn)  # Isso contém o país
        bibtex = bibformatters["json"]
        metadata = json.loads(bibtex(meta(isbn)))
        metadata['language'] = language
        authors = list()
        for author in metadata['author']:
            authors.append(author['name'])
        print(authors)
        if authors != ['']:
            metadata['author'] = str(authors)
        else:
            metadata['author'] = 'NULL'
        metadata['identifier'] = int(metadata['identifier'][0]['id'])
        pattern = re.compile(r"\[|\'|\'|\]")
        metadata['author'] = re.sub(pattern, '', metadata['author'])
        print('pela primeira api')
        return metadata

    except:
        try:
            metadata = request_open_library(isbn)
            return metadata
        except:
            return "Error: non-existent ISBN"

async def request_google_books(keyword):
    keywordTreated = re.sub(r'\s', '+', keyword)
    try:
        result = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={keywordTreated}"
        )
    except:
        return "Connection Failure"

    books = result.json()

    try:
        items = books["items"]
    except:
        return f"nothing found for {keyword}"
    
    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    response = list()

    if len(decoded) < 8:
        count_max = len(decoded)
    else:
        count_max = 8

    for i in range(0, count_max):
        infos = dict()
        print(decoded[i]['selfLink'])
        try:
            link = decoded[i]["volumeInfo"]["previewLink"]  
            infos["previewLink"] = link
        except:
            pass
        try:
            title = decoded[i]["volumeInfo"]["title"]
            infos["title"] = title
        except:
            pass
        try:
            subtitle = decoded[i]["volumeInfo"]["subtitle"]
            infos["subtitle"] = subtitle
        except:
            pass
        try:
            authors = decoded[i]["volumeInfo"]["authors"]
            authors_str = str(authors)
            authors_str = re.sub(r"\[|\'|\]", '', authors_str)
            infos["authors"] = authors_str
        except:
            pass
        try:
            publisher = decoded[i]["volumeInfo"]["publisher"]
            infos["publisher"] = publisher
        except:
            pass
        try:
            categories = decoded[i]["volumeInfo"]["categories"]
            categories_str = str(categories)
            categories_str = re.sub(r"\[|\'|\]", '', categories_str)
            infos["categories"] = categories_str
        except:
            pass
        try:
            imageLink = decoded[i]["volumeInfo"]["imageLinks"]["thumbnail"]
            infos["imageLink"] = imageLink
        except:
            pass
        try:
            if decoded[i]["volumeInfo"]["industryIdentifiers"][0]["type"] == "OTHER":
                isbn = "ISBN Not Registred"
                infos['isbn'] = isbn
            else:
                isbn = decoded[i]["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                infos["isbn"] = isbn
        except:
            pass

        response.append(copy.deepcopy(infos))
        del infos
    
    return response