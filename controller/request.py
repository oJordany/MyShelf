import json
from isbnlib import info
from isbnlib import meta
from isbnlib.registry import bibformatters
import re

def request(isbn):
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
        return 'Não foi possível encontrar o isbn fornecido'