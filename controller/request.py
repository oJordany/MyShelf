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


def request(isbn):
    try:
        urllib.request.urlopen('http://google.com')
    except:
        return "Error: Connection Failure"
    try:
        language = info(isbn) # Isso contém o país 
        bibtex = bibformatters["json"]
        metadata = json.loads(bibtex(meta(isbn)))
        metadata['language'] = language
        metadata['type'] = metadata['type']
        metadata['language'] = metadata['language']
        authors = list()
        for author in metadata['author']:
            authors.append(author['name'])
        metadata['author'] = str(authors)
        metadata['identifier'] = int(metadata['identifier'][0]['id'])
        pattern = re.compile(r"\[|\'|\'|\]")
        metadata['author'] = re.sub(pattern, '', metadata['author'])
        return metadata

    except:
        msgError = "Error: non-existent isbn"
        return msgError

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

        try:
            link = decoded[i]["selfLink"]
            infos["selfLink"] = link
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
            isbn = decoded[i]["volumeInfo"]["industryIdentifiers"][0]["identifier"]
            infos["isbn"] = isbn
        except:
            pass

        response.append(copy.deepcopy(infos))
        del infos
    
    return response