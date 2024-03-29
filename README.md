# Luizalabs Employee Manager

## Django Coding Test
The purpose of this coding test is to evaluate your skills using Python and the Django web
framework.

## The Problem
Luizalabs' team is growing every month and now we need to have some application to manage
employees' information, such as name, e-mail and department. As any application written at
Luizalabs, it must have an API to allow integrations.

## Deliverables
"Luizalabs Employee Manager" app must have:
- A Django Admin panel to manage employees' data
- An API to list, add and remove employees

## API example (list)
## Request

curl -H "Content-Type: application/javascript" http://localhost:8000/employee/

Response

  [
  
        {
                "name": "Arnaldo Pereira",
                "email": "arnaldo@luizalabs.com",
                "department": "Architecture"
         },
  
        {
               "name": "Renato Pedigoni",
               "email": "renato@luizalabs.com",
               "department": "E-commerce"
         },
  
        {
               "name": "Thiago Catoto",
               "email": "catoto@luizalabs.com",
               "department": "Mobile"
         }
  
  ]
