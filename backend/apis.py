#LLamadas a las APIs públicas
#-Google Books
#-OpenLibrary

import requests #Llamadas HTTP a las APIs

#Método de llamada a Google Books
def get_googleBooks(search, maxResults=3):
    #La f delante de la url convierte la cadena en string (de los recursos de Volumen)
    url = f'https://www.googleapis.com/books/v1/volumes?q={search}&maxResults={maxResults}'
    result = requests.get(url)
    books = []

    if result.status_code == 200: #Si el estado de la API es correcto "OK"
        data = result.json()
        for item in data.get('items', []): #REVISAR
            volume = item.get('volumeInfo', {}) 
            #Lista de datos (Título, Autores, Descripción, Portada)
            books.append({ #Cada elemento se añade al final de la lista
                #Título-->Title
                "title": volume.get('title'),
                #Autor/es-->Authors
                "authors": volume.get('authors', []),
                #Sinopsis/descripción-->description
                "description": volume.get('description', "Descripción no disponible"),
                #Portada/imagen-->imageLinks(thumbnail)
                "thumbnail": volume.get('imageLinks', {}).get('thumbnail')     
            })
    
    return books

#Método de llamada a Open Library
def get_openLibrary(search, maxResults=3):
    #La f delante de la url convierte la cadena en string (de los recursos de Volumen)
    url = f'https://openlibrary.org/search.json?q={search}&limit={maxResults}'
    result = requests.get(url)
    books = []

    if result.status_code == 200: #Si el estado de la API es correcto "OK"
        data = result.json()
        for item in data.get('docs', []):
            #Identificador de la portada-->cover_i
            cover_id = item.get('cover_id')
            work_key = item.get('key')

            #Descripción del libro
            description = "Descripción no disponible"
            if work_key:
                work_url=f"https://openlibrary.org{work_key}.json/"
                work_data=requests.get(work_url).json()
                desc=work_data.get("description","")
                if isinstance(desc, dict):
                    description=desc.get("value", "Descripción no disponible")
                elif isinstance(desc, str):
                    description=desc
            
            #Lista de datos
            books.append({
                "title": item.get('title'),
                "authors": item.get('author_name', []),
                "description": description,
                "thumbnail": f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else None
            })

    return books