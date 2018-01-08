Flowroute SDK for Python (v3)
=====================

The Flowroute SDK v3 for Python provides methods for interacting with [Numbers v2](https://developer.flowroute.com/api/numbers/v2.0/ and [Messages v2.1](https://developer.flowroute.com/api/messages/v2.1/) of the [Flowroute](https://www.flowroute.com) API.

**Topics**

*   [Requirements](#requirements)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [Controllers](#controllers)
        * [Numbers Controller](#numberscontroller)
        * [Routes Controller](#routescontroller)
        * [Messages Controller](#messagescontroller)
    *   [Credentials](#credentials)
    *   [Methods](#methods)
    *   [Errors](#errors)

* * *
Requirements
------------

*   Flowroute [API credentials](https://manage.flowroute.com/accounts/preferences/api/)
*   [Python](https://www.python.org/downloads/) 2.x or higher

* * *
Installation
------------

1. First, start a shell session and clone the SDK:
    * via HTTPS: `git clone https://github.com/flowroute/flowroute-numbers-messaging-python.git`

    * via SSH: `git@github.com:flowroute/flowroute-numbers-messaging-python.git`

2. Switch to the newly-created `flowroute-numbers-messaging-python` directory. Version 3 of the Flowroute SDK for Python comes with a requirements file listing the required Python libraries. Click [here](https://packaging.python.org/installing/#requirements-files) to learn more about different ways to install Python packages. Depending on your `pip` permissions, you may be required to preface each `pip` command with `sudo`.

`pip install -r requirements.txt`

* * *
Usage
------------
In Flowroute's approach to building SDK v3 for Python, HTTP requests are handled by controllers named after the API resources they represent: **Numbers**, **Routes**, and **Messages**. These controllers contain the methods used to perform messaging, number management, and route management within the Python SDK.

### Controllers

#### NumbersController

Contains all of the methods necessary to search through Flowroute's phone number inventory, purchase a phone number, and review details of your account phone numbers.

*   [list\_available\_area\_codes()](#list_available_area_codes) \- Returns a list of all Numbering Plan Area (NPA) codes containing purchasable phone numbers. All request parameters are optional. If you don't specify a limit, results are limited to the first 10 items.
*   [list\_available\_exchange\_codes()](#list_available_exchange_codes) \- Returns a list of all Central Office (exchange) codes containing purchasable phone numbers. All request parameters are optional.
*   [search\_for\_purchasable\_phone\_numbers()](#search_for_purchasable_phone_numbers) \- Searches for purchasable phone numbers by state or rate center, or by your specified search value.
*   [purchase\_a\_phone\_number(number\_id)](#purchase_a_phone_numbernumber_id) \- Lets you purchase a phone number from available Flowroute inventory.
*   [list\_account\_phone\_numbers()](#list_account_phone_numbers) \- Returns a list of all phone numbers currently on your Flowroute account. 
*   [list\_phone\_number\_details(numberid)](#list_phone_number_detailsnumber_id) \- Returns details on a specific phone number associated with your account, including primary voice route, and failover voice route if previously configured.

#### RoutesController
    
Contains the methods required to create new inbound routes, view all of your account routes, and update primary and failover voice routes for your phone numbers.
    
*   [create\_an\_inbound\_route(route\_body)](#create_an_inbound_routeroute_body) \- Creates a new inbound route which can then be assigned as either a primary or a failover voice route for a phone number on your account.
*   [list\_inbound\_routes()](#list_inbound_routes) \- Returns a list of your inbound routes. From the list, you can then select routes to use as the primary and failover voice routes for phone numbers on your account.
*   [update\_primary\_voice\_route(number\_id, route\_body)](#update_primary_voice_routenumber_id-route_body) \- Updates the primary voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.
*   [update\_failover\_voice\_route(number\_id, route\_body)](#update_failover_voice_routenumber_id-route_body) \- Updates the failover voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.

####   MessagesController
    
Contains the methods required to send an MMS or SMS, and review a specific Message Detail Record (MDR) or a set of messages.
    
*   [send\_a\_message(message\_body)](#send_a_messagemessage_body) \- Sends an SMS or MMS from a Flowroute long code or toll-free phone number to another valid phone number.
*   [look\_up\_a\_message\_detail\_record()](#look_up_a_message_detail_recordmessage_id) \- Searches for a specific message record ID and returns a Message Detail Record (in MDR2 format).
*   [look\_up\_a\_set\_of\_messages()](#look_up_a_set_of_messagesstart_date) \- Retrieves a list of Message Detail Records (MDRs) within a specified date range. Date and time is based on Coordinated Universal Time (UTC).

The following shows an example of a single Python file that imports the Flowroute API client and all the required modules. The Python SDK comes with a **demo.py** file that you can edit and run as an example.

```python
import pprint
import os
import json
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
```    
#### Credentials

In **demo.py**, replace `basic_auth_user_name` with your API Access Key and `basic_auth_password` with your API Secret Key from the [Flowroute Manager](https://manage.flowroute.com/accounts/preferences/api/). Note that in our example, we are accessing your Flowroute credentials as environment variables. To learn more about setting environment variables, see [How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps).

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

Flowroute SDK version 3 for Python allows you to make HTTP requests to the `numbers` resource of Flowroute API v2: `https://api.flowroute.com/v2/numbers`

#### list\_available\_area\_codes()

The method accepts `limit`, `offset`, and `max_setup_cost` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-available-area-codes/).
    
##### Example Request
```python
print("--List Available Area Codes")
max_setup_cost = 3.25
limit = 3
offset = None
result = numbers_controller.list_available_area_codes(limit, offset, max_setup_cost)
pprint.pprint(result)
```

##### Example Response
```
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

#### list\_available\_exchange\_codes()

The method accepts `limit`, `offset`, `max_setup_cost`, and `areacode` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-available-exchanges/). 

##### Example Request
```python
print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 347
result = numbers_controller.list_available_exchange_codes(limit, offset, max_setup_cost, areacode)
pprint.pprint(result)
```
##### Example Response
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

#### search\_for\_purchasable\_phone\_numbers()

The method accepts `starts_with`, `contains`, `ends_with`, `limit`, `offset`, `rate_center`, and `state` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/search-for-purchasable-phone-numbers/).

##### Example Request
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

##### Example Response
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

#### purchase\_a\_phone\_number(number\_id)

The method is used to purchase a telephone number from Flowroute's inventory and accepts the phone number `id` as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/purchase-a-phone-number/).

##### Example Request
```python
print("--Purchase a Phone Number")
numberid = result['data'][0]['id']
result = numbers_controller.purchase_a_phone_number(numberid)
```

In the example above, we have assigned the `id` of the first phone number in the resulting JSON array as the phone number to be purchased.

#### Example Response
```
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
```

#### list\_account\_phone\_numbers()

The method accepts `starts_with`, `ends_with`, `contains`, `limit`, and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-account-phone-numbers/). 
    

##### Example Request
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

##### Example Response
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

#### list\_phone\_number\_details(number\_id)

The method accepts the `number_id` as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-phone-number-details/). In the following example, we request the details of our newly purchased phone number above.

##### Example Request
```python
print("--List Phone Number Details")
result = numbers_controller.list_phone_number_details(numberid)
pprint.pprint(result)
```

##### Example Response
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

Flowroute SDK version 3 for Python allows you to make HTTP requests to the `routes` resource of Flowroute API v2: `https://api.flowroute.com/v2/routes`
    
#### create\_an\_inbound\_route(route\_body) 
WIP

The method accepts the route object in JSON format as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/create-an-inbound-route/).

##### Example Request
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

##### Example Response
```
```
Currently has some issues with POST and PATCH requests via the SDK methods provided.

#### list\_inbound\_routes()

The method accepts `limit` and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-inbound-routes/).

##### Example Request
```python
print ("---List Inbound Routes")
result = routes_controller.list_inbound_routes()
pprint.pprint(result)
```

##### Example Response
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

#### update\_primary\_voice\_route(number\_id, route\_body)
WIP

The method accepts a phone number `id` and a route record object in JSON format as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/update-number-primary-voice-route/).

##### Example Request
```python
print ("---Update Primary Voice Route for a Phone Number")
```

##### Example Response
`204 NO CONTENT`

On success, the HTTP status code in the response header is `204 NO CONTENT` which means that the server successfully processed the request and is not returning any content.

#### update\_failover\_voice\_route(number\_id, route\_body)
WIP

The method accepts a phone number `id` and a route record object in JSON format as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/update-number-failover-voice-route/).

##### Example Request
```python
print ("---Update Failover Voice Route for a Phone Number")
```

##### Example Response
`204 NO CONTENT`

On success, the HTTP status code in the response header is `204 NO CONTENT` which means that the server successfully processed the request and is not returning any content.

### Messaging
Flowroute SDK version 3 for Python allows you to make HTTP requests to the `messages` resource of Flowroute API v2.1: `https://api.flowroute.com/v2.1/messages`

#### send\_a\_message(message\_body)
WIP

The method accepts a message object in JSON format as a parameter which you can learn more about in the API References for [MMS](https://developer.flowroute.com/api/messages/v2.1/send-an-mms/) and [SMS](https://developer.flowroute.com/api/messages/v2.1/send-an-sms/).

##### Example Request
```python
print ("---Send a Message")
```

##### Example Response
`202 ACCEPTED`

On success, the HTTP status code in the response header is `202 Accepted` and the response body contains the message record ID with `mdr2` prefix.

#### look\_up\_a\_message\_detail\_record(message\_id)

The method accepts a message `id` in MDR2 format as a parameter which you can learn more about in the [API Reference](https://developer.flowroute.com/api/messages/v2.1/look-up-a-message-detail-record/).

##### Example Request
```python
print ("---Look Up a Message Detail Record")
message_id = "mdr2-ca82be46e6ba11e79d08862d092cf73d"
result = messages_controller.look_up_a_message_detail_record(message_id)
pprint.pprint(result)
```

##### Example Response
```
{
  "data": {
    "attributes": {
      "body": "Hello are you there? ",
      "status": "delivered",
      "direction": "inbound",
      "amount_nanodollars": 4000000,
      "to": "12012673227",
      "message_encoding": 0,
      "timestamp": "2017-12-22T01:52:39.39Z",
      "delivery_receipts": [],
      "amount_display": "$0.0040",
      "from": "12067392634",
      "is_mms": false,
      "message_type": "longcode"
    },
    "type": "message",
    "id": "mdr2-ca82be46e6ba11e79d08862d092cf73d"
  }
}
```

#### look\_up\_a\_set\_of\_messages(start\_date)
WIP
The method accepts `start_date`, `end_date`, `limit`, and `offset` as a parameters which you can learn more about in the [API Reference](https://developer.flowroute.com/api/messages/v2.1/look-up-set-of-messages/).

##### Example Request
```python
print ("---Look Up a Set of Messages")
```

##### Example Response
`202 ACCEPTED`
On success, the HTTP status code in the response header is `202 Accepted` and the response body contains the message record ID with `mdr2` prefix.
#### Errors

In cases of method errors, the API Controller returns an error object with the same fields as our [API's error response](https://developer.flowroute.com/api/errors).

##### Example Error
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
  
