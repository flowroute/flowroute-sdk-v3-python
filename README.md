# flowroute-numbers-messaging-python
Flowroute SDK for Python (v3)
=====================

The Flowroute Python API Wrapper v3 provides methods for interacting with **[Numbers v2](#numbers)** and **[Messages v2.1](#messaging)** of the [Flowroute](https://www.flowroute.com) API.

**Topics**

*   [Requirements](#requirements)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [Controllers](#controllers)
    *   [Credentials](#credentials)
    *   [Methods](#methods)
    *   [Errors](#errors)

* * *
Requirements
------------

*   Flowroute [API credentials](https://manage.flowroute.com/accounts/preferences/api/)
*   [Python](https://www.python.org/downloads/) 2.x or higher


[View Repo](https://github.com/flowroute/flowroute-numbers-messaging-python)

### Installation

1. First, start a shell session and clone the SDK:
    * via HTTPS	

`git clone https://github.com/flowroute/flowroute-numbers-python.git`

    * via SSH

`git@github.com:flowroute/flowroute-numbers-messaging-python.git`
    

2. Switch to the newly-created `flowroute-numbers-messaging-python` directory. The Flowroute SDK for Python v3 comes with a requirements file listing the required Python libraries. Click [here](https://packaging.python.org/installing/#requirements-files) to learn more about different ways to install Python packages. Depending on your `pip` permissions, you may be required to preface each `pip` command with `sudo`.

`pip install -r requirements.txt`

### Usage
In Flowroute's approach to building Python API Wrapper 3, HTTP requests are handled by controllers named after the API resources they represent: **Numbers**, **Routes**, and **Messages**. These controllers contain the methods used to perform tasks with the Python SDK.

#### Controllers

*   NumbersController
    
    Contains all of the methods necessary to search through Flowroute's phone number inventory, purchase a phone number, and review details of your account phone numbers.
    
    *   [list\_available\_area\_codes()](#listareacodes) \- Returns a list of all Numbering Plan Area (NPA) codes containing purchasable phone numbers.
    *   [list\_available\_exchange\_codes()](#listexchanges) \- Returns a list of all Central Office (exchange) codes containing purchasable phone numbers.
    *   [search\_for\_purchasable\_phone\_numbers()](#search) \- Searches for purchasable phone numbers by state or rate center, or by your specified search value.
    *   [purchase\_a\_phone\_number(number\_id)](#purchase) \- Lets you purchase a phone number from available Flowroute inventory.
    *   [list\_account\_phone\_numbers()](#listaccountnumbers) \- Returns a list of all phone numbers currently on your Flowroute account. The response includes details such as the phone number's rate center, state, number type, and whether CNAM Lookup is enabled for that number.
    *   [list\_phone\_number\_details(numberid)](#numberdetails) \- Lists all of the information associated with any of the phone numbers in your account, including billing method, primary voice route, and failover voice route.

*   RoutesController
    
    Contains the methods required to create new inbound routes, view all of your account routes, and update primary and failover voice routes for your phone numbers.
    
    *   [create\_an\_inbound\_route(route\_body)](#createnewroute) \- Create a new inbound route that can then be assigned as either a primary or failover voice route for a phone number.
    *   [list\_inbound\_routes()](#listroutes) \- Returns a list of your inbound routes. From the list, you can then select routes to use as the primary and failover voice routes for your phone number.
    *   [update\_primary\_voice\_route(number\_id, route\_body)](#updateprimaryvoiceroute) \- Updates the primary voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.
    *   [update\_failover\_voice\_route(number\_id, route\_body)](#updatefailovervoiceroute) \- Updates the failover voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.

*   MessagesController
    
    Contains the methods required to send an MMS or SMS, and review a specific Message Detail Record (MDR) or a set of messages.
    
    *   [send\_a\_message(message\_body)](#sendmessage) \- Sends an SMS or MMS from a Flowroute long code or toll-free phone number to another valid phone number.
    *   [look\_up\_a\_message\_detail\_record()](#lookupmessage) \- Searches for a specific message record ID and returns a Message Detail Record (in MDR2 format).
    *   [look\_up\_a\_message\_detail\_record()](#lookupmessage) \- Searches for a specific message record ID and returns a Message Detail Record (in MDR2 format).

The following shows an example of a single Python file that imports the Flowroute API client and all the required modules. The Python SDK comes with a **demo.py** file that you can edit and run as an example.

```python
import pprint
import os
import json
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
```    
#### Credentials

In **demo.py**, replace `basic_auth_user_name` with your API Access Key and `basic_auth_password` with your API Secret Key from the [Flowroute Manager](https://manage.flowroute.com/accounts/preferences/api/). Note that in our example, we are accessing them as environment variables. To learn more about setting environment variables, see [How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps).

```python
# Set up your api credentials
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')
```
#### Instantiate API Client and Controllers
Next, instantiate the API Client and its controllers.

```python
# Instantiate API client and create controllers for Numbers, Messages, and Routes
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)
numbers_controller = client.numbers
routes_controller = client.routes
messages_controller = client.messages
```
#### Methods

### Number Management

##### list\_available\_area\_codes()

The method accepts `limit`, `offset`, and `max_setup_cost` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-available-area-codes/).
    
###### Example Request

```python
print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 347
result = numbers_controller.list_available_exchange_codes(limit, offset, max_setup_cost, areacode)
pprint.pprint(result)
```

###### Example Response

```
{
  "data": [
    {
      "type": "exchange",
      "id": "347215",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347215"
      }
    },
    {
      "type": "exchange",
      "id": "347325",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347325"
      }
    },
    {
      "type": "exchange",
      "id": "347331",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347331"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=347&limit=3&offset=0",
    "next": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=347&limit=3&offset=3"
  }
}
Marias-MacBook-Pro:~ mbermudez$ pbpaste | jq .
{
  "data": [
    {
      "type": "areacode",
      "id": "201",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=201"
      }
    },
    {
      "type": "areacode",
      "id": "202",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=202"
      }
    },
    {
      "type": "areacode",
      "id": "203",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=203"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/available/areacodes?max_setup_cost=3&limit=3&offset=0",
    "next": "https://api.flowroute.com/v2/numbers/available/areacodes?max_setup_cost=3&limit=3&offset=3"
  }
}
```

##### list\_available\_area\_codes()

The method accepts `limit`, `offset`, `max_setup_cost`, and `areacode` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-available-exchanges/). 

###### Example Request

```python
print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 347
result = numbers_controller.list_available_exchange_codes(limit, offset, max_setup_cost, areacode)
pprint.pprint(result)
```
###### Example Response

```
{
  "data": [
    {
      "type": "exchange",
      "id": "347215",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347215"
      }
    },
    {
      "type": "exchange",
      "id": "347325",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347325"
      }
    },
    {
      "type": "exchange",
      "id": "347331",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/available?starts_with=1347331"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=347&limit=3&offset=0",
    "next": "https://api.flowroute.com/v2/numbers/available/exchanges?areacode=347&limit=3&offset=3"
  }

}
```

##### search\_for\_purchasable\_phone\_numbers

The method accepts `starts_with`. `contains`, `ends_with`, `limit`, `offset`, `rate_center`, and `state` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v1.0/search-for-purchasable-phone-numbers/).

###### Example Request

```python
print("--Search for Purchasable Phone Numbers")
starts_with = 646
contains = 3
ends_with = 7
limit = 3
offset = None
rate_center = None
state = None
result = numbers_controller.search_for_purchasable_phone_numbers(starts_with, contains, ends_with, limit, offset, rate_center, state)

```

###### Example Response
```
{
  "data": [
    {
      "attributes": {
        "rate_center": "nwyrcyzn01",
        "value": "16463439507",
        "monthly_cost": 1.25,
        "state": "ny",
        "number_type": "standard",
        "setup_cost": 1
      },
      "type": "number",
      "id": "16463439507",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/16463439507"
      }
    },
    {
      "attributes": {
        "rate_center": "nwyrcyzn01",
        "value": "16463439617",
        "monthly_cost": 1.25,
        "state": "ny",
        "number_type": "standard",
        "setup_cost": 1
      },
      "type": "number",
      "id": "16463439617",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/16463439617"
      }
    },
    {
      "attributes": {
        "rate_center": "nwyrcyzn01",
        "value": "16463439667",
        "monthly_cost": 1.25,
        "state": "ny",
        "number_type": "standard",
        "setup_cost": 3.99
      },
      "type": "number",
      "id": "16463439667",
      "links": {
        "related": "https://api.flowroute.com/v2/numbers/16463439667"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/available?contains=3&ends_with=7&starts_with=1646&limit=3&offset=0",
    "next": "https://api.flowroute.com/v2/numbers/available?contains=3&ends_with=7&starts_with=1646&limit=3&offset=3"
  }
}
```
##### purchase\_a\_phone\_number(number\_id)

The method is used to purchase a telephone number from Flowroute's inventory and accepts the phone number ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/purchase-a-phone-number/).

###### Example Request

```python
print("--Purchase a Phone Number")
numberid = result['data'][0]['id'])
result = numbers_controller.purchase_a_phone_number(numberid)
```
In our example above, we have assigned the `id` of the first phone number in the resulting JSON array as the phone number to be purchased.

##### Example Response
{
  "data": {
    "attributes": {
      "alias": null,
      "cnam_lookups_enabled": true,
      "number_type": "standard",
      "rate_center": "millbrae",
      "state": "ca",
      "value": "16502390214"
    },
    "id": "16502390214",
    "links": {
      "self": "https://api.flowroute.com/v2/numbers/16502390214"
    },
    "relationships": {
      "cnam_preset": {
        "data": null
      },
      "e911_address": {
        "data": null
      },
      "failover_route": {
        "data": null
      },
      "primary_route": {
        "data": {
          "id": "0",
          "type": "route"
        }
      }
    },
    "type": "number"
  },
  "included": [
    {
      "attributes": {
        "alias": "sip-reg",
        "route_type": "sip-reg",
        "value": null
      },
      "id": "0",
      "links": {
        "self": "https://api.flowroute.com/v2/routes/0"
      },
      "type": "route"
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/16502390214"
  }
}

##### list\_account\_phone\_numbers()

The method accepts `starts_with`, `ends_with`, `contains`, `limit`, and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-account-phone-numbers/). 
    

###### Example Request

```python
print("--List Account Phone Numbers")
starts_with = 201
ends_with = None
contains = None
limit = 3
offset = None
result = numbers_controller.list_account_phone_numbers(starts_with, ends_with, contains, limit, offset)
pprint.pprint(result)
```

###### Example Response
```
{
  "data": [
    {
      "attributes": {
        "rate_center": "oradell",
        "value": "12012673227",
        "alias": null,
        "state": "nj",
        "number_type": "standard",
        "cnam_lookups_enabled": true
      },
      "type": "number",
      "id": "12012673227",
      "links": {
        "self": "https://api.flowroute.com/v2/numbers/12012673227"
      }
    },
    {
      "attributes": {
        "rate_center": "jerseycity",
        "value": "12014845220",
        "alias": null,
        "state": "nj",
        "number_type": "standard",
        "cnam_lookups_enabled": true
      },
      "type": "number",
      "id": "12014845220",
      "links": {
        "self": "https://api.flowroute.com/v2/numbers/12014845220"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/numbers?starts_with=1201&limit=3&offset=0"
  }
}
```
##### list\_phone\_number\_details(number\_id)

The method accepts the `number_id` as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-phone-number-details/). In the following example, we request the details of our newly purchased phone number above.

###### Example Request

```python
print("--List Phone Number Details")
result = numbers\_controller.list\_phone\_number\_details(numberid)
pprint.pprint(result)
```

###### Example Response
```
{
  "included": [
    {
      "attributes": {
        "route_type": "sip-reg",
        "alias": "sip-reg",
        "value": null
      },
      "type": "route",
      "id": "0",
      "links": {
        "self": "https://api.flowroute.com/v2/routes/0"
      }
    }
  ],
  "data": {
    "relationships": {
      "cnam_preset": {
        "data": null
      },
      "e911_address": {
        "data": null
      },
      "failover_route": {
        "data": null
      },
      "primary_route": {
        "data": {
          "type": "route",
          "id": "0"
        }
      }
    },
    "attributes": {
      "rate_center": "millbrae",
      "value": "16502390214",
      "alias": null,
      "state": "ca",
      "number_type": "standard",
      "cnam_lookups_enabled": true
    },
    "type": "number",
    "id": "16502390214",
    "links": {
      "self": "https://api.flowroute.com/v2/numbers/16502390214"
    }
  },
  "links": {
    "self": "https://api.flowroute.com/v2/numbers/16502390214"
  }
}
```
### Route Management
    
##### create\_an\_inbound\_route(route\_body) - WIP

The method accepts the route object in JSON format as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/create-an-inbound-route/).

###### Example Request
```python
#print ("---Create an Inbound Route")
#request_body = '{
#  "data": {
#    "type": "route",
#    "attributes": {
#      "route_type": "host",
#      "value": "www.example.com",
#      "alias": "new_route_id"
#    }
#  }
#}'

#routepost = NewRoute(json.dumps({"data": {"type": "route", "attributes": {"route_type": "host", "value": "13471654563", "alias": "new_route_56"}}}))
#result = routes_controller.create_an_inbound_route(routepost)
result = routes_controller.create_an_inbound_route(request_body)
pprint.pprint(result)
```
Currently has some issues with POST and PATCH requests via the SDK methods provided.

##### list\_inbound\_routes()

The method accepts `limit` and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-inbound-routes/).

###### Example Response
```python
print ("---List Inbound Routes")
result = routes_controller.list_inbound_routes()
pprint.pprint(result)
```

###### Example Response
```
{
  "data": [
    {
      "attributes": {
        "route_type": "sip-reg",
        "alias": "sip-reg",
        "value": null
      },
      "type": "route",
      "id": "0",
      "links": {
        "self": "https://api.flowroute.com/v2/routes/0"
      }
    },
    {
      "attributes": {
        "route_type": "number",
        "alias": "PSTNroute1",
        "value": "12065551212"
      },
      "type": "route",
      "id": "83834",
      "links": {
        "self": "https://api.flowroute.com/v2/routes/83834"
      }
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/routes?limit=2&offset=0",
    "next": "https://api.flowroute.com/v2/routes?limit=2&offset=2"
  }
}
```
#### Errors

In cases of method errors, the API Controller returns an error object with the same fields as our [API's error response](https://developer.flowroute.com/api/errors).

###### Example Error
```
{
  "errors": [
    {
      "detail": "Error fetching media: File at \"https://s3-us-west-2.amazonaws.com/testing/1503617641_12067392634\" is over 767840 byte limit.",
      "id": "8f20a349-ebc0-4246-81ae-b4e7caef324c",
      "status": 422
    }
  ]
}
```
  
