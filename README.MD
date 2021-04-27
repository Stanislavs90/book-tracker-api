Intro:
    An api that allows users keep track of books, authors, and characters. 


Setup:

   python3 -m venv venv
   
   source env/bin/activate

   pip install -r requirements.txt

   cd into directory 

   python manage.py createsuperuser

   python manage.py runserver

Overview: 

    Navigate to http://127.0.0.1:8000/api/books/ to view or create books

    Since django does not support nested fields, postman is ideal for viewing and adding to this api. 

    The following fields can be entered:
    
    Title
    Description 
    Pirce
    Publish date
    Characters of the book - nested
    Authors - nested

    Please see example below: 
    

        {
        "title": "For Whom the Bell Tolls",
        "description": "The novel graphically describes the brutality of the Spanish Civil War.",
        "price": "0.01",
        "published": "1940-10-21",
        "characters": [
            {
          
                "name": "Robert Jordan",
              
            }
        ],
        "authors": [
            {
          
                "name": "Ernest Hemingway",
             
            }
        ]
    }

    To view authors separately navigate to http://localhost:8000/api/authors/

   
   To view characters separatley http://localhost:8000/api/Characters/
   
   
   
   
