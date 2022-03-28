# CarFixInventory

# Endpoints
https://nesinvent.herokuapp.com/swagger/<br>
it has 4 endpoint-<br>
https://nesinvent.herokuapp.com/inventoryView --lists all the repair shop inventory<br>

#### sample respone
[
  {
    "name_of_part": "tyre",<br>
    "price_of_part": "8000.00",<br>
    "car_make": "toyota",<br>
    "car_model": "sss"<br>
  },
  {
    "name_of_part": "Wheel",<br>
    "price_of_part": "10000.00",<br>
    "car_make": "toyota",<br>
    "car_model": "sss"<br>
  }
]

https://nesinvent.herokuapp.com/inventoryView/id/<br>
#### sample response
{
  "name_of_part": "tyre",<br>
  "price_of_part": "8000.00",<br>
  "car_make": "toyota",<br>
  "car_model": "sss"<br>
}


mechanicandservicespost/mechanicandservicespost/

#### sample response
{<br>
  "mechanic_name": "string",<br>
  "garage_name": "string",<br>
  "services": [<br>
    {<br>
      "complexity": 0,<br>
      "title": "string",<br>
      "duration": 0<br>
    }
  ]
}
mechanicandservicespost
#### sample response 
<br>
 {
    "mechanic_name": "peter",<br>
    "garage_name": "isuzu",<br>
    "services": [<br>
      {
        "complexity": 5,<br>
        "title": "Tyre replacement",<br>
        "duration": 5<br>
      },
      {
        "complexity": 5,<br>
        "title": "Tyre repair",<br>
        "duration": 5<br>
      },
      {
        "complexity": 10,<br>
        "title": "Full car service",<br>
        "duration": 5<br>
      }
    ]
  }


# Response code 200-ok get the response
# Response code 500-internal server error-problem with the code



## To try out the swagger api 
https://nesinvent.herokuapp.com/swagger/ <br>

click try out-then execute



copyright:mwasheberit:2022





