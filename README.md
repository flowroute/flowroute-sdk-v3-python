Flowroute SDK for Python (v3)
=====================

The Flowroute SDK for Python (v3) provides methods for interacting with [Numbers v2](https://developer.flowroute.com/api/numbers/v2.0/) and [Messages v2.1](https://developer.flowroute.com/api/messages/v2.1/) of the [Flowroute](https://www.flowroute.com) API.

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
*   [Python](https://www.python.org/downloads/): `Python 2 >=2.7.9` or `Python 3 >=3.4`


* * *
Installation
------------

1. First, start a shell session and clone the SDK:
    * via HTTPS: `git clone https://github.com/flowroute/flowroute-numbers-messaging-python.git`

    * via SSH: `git@github.com:flowroute/flowroute-numbers-messaging-python.git`

2. Switch to the newly-created `flowroute-numbers-messaging-python` directory. To build and install the required modules, run the following:

`python setup.py install`

3. Version 3 of the Flowroute SDK for Python comes with a requirements file listing the required Python libraries. Click [here](https://packaging.python.org/installing/#requirements-files) to learn more about different ways to install Python packages. `pip` is already installed if you're using `Python 2 >=2.7.9` or `Python 3 >=3.4`. This SDK has been tested with both `2.7.9` and `3.6.4`. To see which version of `pip` is installed on your machine, run the following:

`pip --version`

Depending on your `pip` permissions, you may be required to preface each `pip` command with `sudo`.  

`pip3 install -r requirements.txt`

* * *
Usage
------------
In Flowroute's approach to building SDK v3 for Python, HTTP requests are handled by controllers named after the API resources they represent: **Numbers**, **Routes**, and **Messages**. These controllers contain the methods used to perform messaging, number management, and route management within the Python SDK.

## Controllers

### NumbersController

Contains all of the methods necessary to search through Flowroute's phone number inventory, purchase a phone number, and review details of your account phone numbers.

*   [list\_available\_area\_codes()](#list_available_area_codes) \- Returns a list of all Numbering Plan Area (NPA) codes containing purchasable phone numbers. All request parameters are optional. If you don't specify a limit, results are limited to the first 10 items.
*   [list\_available\_exchange\_codes()](#list_available_exchange_codes) \- Returns a list of all Central Office (exchange) codes containing purchasable phone numbers. All request parameters are optional.
*   [search\_for\_purchasable\_phone\_numbers()](#search_for_purchasable_phone_numbers) \- Searches for purchasable phone numbers by state or rate center, or by your specified search value.
*   [purchase\_a\_phone\_number(purchasable\_number)](#purchase_a_phone_numbernumber_id) \- Lets you purchase a phone number from available Flowroute inventory.
*   [list\_account\_phone\_numbers()](#list_account_phone_numbers) \- Returns a list of all phone numbers currently on your Flowroute account. 
*   [list\_phone\_number\_details(number\_id)](#list_phone_number_detailsnumber_id) \- Returns details on a specific phone number associated with your account, including primary voice route, and failover voice route if previously configured.

### RoutesController
    
Contains the methods required to create new inbound routes, view all of your account routes, and update primary and failover voice routes for your phone numbers.
    
*   [create\_an\_inbound\_route(route\_body)](#create_an_inbound_routeroute_body) \- Creates a new inbound route which can then be assigned as either a primary or a failover voice route for a phone number on your account.
*   [list\_inbound\_routes()](#list_inbound_routes) \- Returns a list of your inbound routes. From the list, you can then select routes to use as the primary and failover voice routes for phone numbers on your account.
*   [update\_primary\_voice\_route(number\_id, route\_body)](#update_primary_voice_routenumber_id-route_body) \- Updates the primary voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.
*   [update\_failover\_voice\_route(number\_id, route\_body)](#update_failover_voice_routenumber_id-route_body) \- Updates the failover voice route for a phone number. You must create the route first via the `create_an_inbound_route(routebody)` method.

###   MessagesController
    
Contains the methods required to send an MMS or SMS, and review a specific Message Detail Record (MDR) or a set of messages.
    
*   [send\_a\_message(message\_body)](#send_a_messagemessage_body) \- Sends an SMS or MMS from a Flowroute long code or toll-free phone number to another valid phone number.
*   [look\_up\_a\_message\_detail\_record()](#look_up_a_message_detail_recordmessage_id) \- Searches for a specific message record ID and returns a Message Detail Record (in MDR2 format).
*   [look\_up\_a\_set\_of\_messages()](#look_up_a_set_of_messagesstart_date) \- Retrieves a list of Message Detail Records (MDRs) within a specified date range. Date and time is based on Coordinated Universal Time (UTC).

The following shows an example of a single Python file that imports the Flowroute API client and all the required modules. The Python SDK comes with a **demo.py** file that you can edit and run as an example.

```python
import pprint
import os
import json
import random
import string
import requests
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
```    
#### Credentials

In **demo.py**, replace `basic_auth_user_name` with your API Access Key and `basic_auth_password` with your API Secret Key from the [Flowroute Manager](https://manage.flowroute.com/accounts/preferences/api/). Note that in our example, we are accessing your Flowroute credentials as environment variables. To learn more about setting environment variables, see [How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps).

```python
# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')
mobile_number = "YOUR_MOBILE_NUMBER"
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
## Methods
The following section will demonstrate the capabilities of Numbers v2 and Messages v2.1 that are wrapped in our Python library. Note that the example responses have been formatted using Mac's `pbpaste` and `jq`. To learn more, see [Quickly Tidy Up JSON from the Command Line](http://onebigfunction.com/vim/2015/02/02/quickly-tidying-up-json-from-the-command-line-and-vim/). 

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

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of area code objects in JSON format.

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

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of exchange objects in JSON format.

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

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of phone number objects in JSON format.

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

#### purchase\_a\_phone\_number(purchasable\_number)

The method is used to purchase a telephone number from Flowroute's inventory and accepts the phone number `id` as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/purchase-a-phone-number/). In the following example, we assign the `id` of the first phone number in the resulting JSON array as the phone number to be purchased. Note that this function call is currently commented out. Uncomment to test the `purchase_a_phone_number` method.
##### Example Request
```python
print("--Purchase a Phone Number")
purchasable_number = result['data'][0]['id'] 
result = numbers_controller.purchase_a_phone_number(purchasable_number)
```

#### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains a phone number object in JSON format.

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

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of phone number objects in JSON format.

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

The method accepts the `number_id` as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-phone-number-details/). In the following example, we request the details of the first phone number returned after calling the `list_account_phone_numbers` method.

##### Example Request
```python
print("--List Phone Number Details")
number_id = result['data'][0]['id']
result = numbers_controller.list_phone_number_details(number_id)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains a phone number object in JSON format.

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

The method accepts the route object in JSON format as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/create-an-inbound-route/). In the following example, we define a function to generate a six-character random string for our subdomain which we later concatenate with our example domain and assign as our `host` value. We use the same function to generate a unique `alias`.

##### Example Request
```python
print ("---Create an Inbound Route")
# Function to generate six-charac random string
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
new_route = id_generator() + '.sonsofodin.com'
alias = id_generator()
for i in range(6): alias += str(i)
print new_route
request_body = '{ \
  "data": { \
    "type": "route", \
    "attributes": { \
      "route_type": "host", \
      "value": "' + new_route +'", \
      "alias": "' + alias + '" \
    } \
  } \
}'
result = routes_controller.create_an_inbound_route(request_body)
print result
```

##### Example Response

On success, the HTTP status code in the response header is `201 Created` and the response body contains a route object in JSON format.

```
{
  "data": {
    "attributes": {
      "alias": "new route",
      "route_type": "host",
      "value": "il775u.sonsofodin.com"
    },
    "id": "98396",
    "links": {
      "self": "https://api.flowroute.com/routes/98396"
    },
    "type": "route"
  },
  "links": {
    "self": "https://api.flowroute.com/routes/98396"
  }
}
```
#### list\_inbound\_routes()

The method accepts `limit` and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-inbound-routes/).

##### Example Request
```python
print ("---List Inbound Routes")
limit = 3
result = routes_controller.list_inbound_routes(limit)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of route objects in JSON format. 

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

The method accepts a phone number `id` and a route record object in JSON format as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/update-number-primary-voice-route/). In the following example, we extract the second route in our `list_inbound_routes` search result and assign it as the primary voice route for our previously declared `number_id`.

##### Example Request
```python
prirouteid = result['data'][1]['id']
request_body = '{ \
  "data": { \
    "type": "route", \
    "id": "' + str(prirouteid) +'" \
  } \
}'

print ("---Update Primary Voice Route")
result = routes_controller.update_primary_voice_route(number_id, request_body)
if result is None:
    print "204: No Content"
else:
    print result
```

##### Example Response

On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

`204: No Content`


#### update\_failover\_voice\_route(number\_id, route\_body)

The method accepts a phone number `id` and a route record object in JSON format as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/update-number-failover-voice-route/). In the following example, we extract the third and last route in our `list_inbound_routes` search result and assign it as the failover voice route for our previously declared `number_id`.

##### Example Request
```python
secrouteid = result['data'][2]['id']
request_body = '{ \
  "data": { \
    "type": "route", \
    "id": "' + str(secrouteid) +'" \
  } \
}'

print ("---Update Failover Voice Route")
result = routes_controller.update_failover_voice_route(number_id, request_body)
if result is None:
    print "204: No Content"
else:
    print result
```

##### Example Response

On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

`204: No Content`


### Messaging
Flowroute SDK version 3 for Python allows you to make HTTP requests to the `messages` resource of Flowroute API v2.1: `https://api.flowroute.com/v2.1/messages`

#### send\_a\_message(message\_body)

The method accepts a message object in JSON format as a parameter which you can learn more about in the API References for [MMS](https://developer.flowroute.com/api/messages/v2.1/send-an-mms/) and [SMS](https://developer.flowroute.com/api/messages/v2.1/send-an-sms/). In the following example, we are sending an MMS with a `gif` attachment from the previously declared `number_id` to your mobile number. 

##### Example Request
```python
request_body = '{ \
  "data": { \
    "type": "message", \
    "attributes": { \
      "to": "' + str(mobile_number) + '", \
      "from": "' + str(number_id) + '", \
      "body": "hello there", \
      "is_mms": "true", \
      "media_urls": ["http://s3.amazonaws.com/barkpost-assets/50+GIFs/37.gif"] \
    } \
  } \
}'

print ("---Send A Message")
result = messages_controller.send_a_message(request_body)
pprint.pprint(result)
```
Note that this function call is currently commented out. Uncomment to test the `send_a_message` method.

##### Example Response

On success, the HTTP status code in the response header is `202 Accepted` and the response body contains the message record ID with `mdr2` prefix.

```
{
  "data": {
    "links": {
      "self": "https://api.flowroute.com/v2.1/messages/mdr2-39cadeace66e11e7aff806cd7f24ba2d"
    },
    "type": "message",
    "id": "mdr2-39cadeace66e11e7aff806cd7f24ba2d"
  }
}
```


#### look\_up\_a\_set\_of\_messages(start\_date)

The method accepts `start_date`, `end_date`, `limit`, and `offset` as parameters which you can learn more about in the [API Reference](https://developer.flowroute.com/api/messages/v2.1/look-up-set-of-messages/).

##### Example Request
```python
print ("---Look Up A Set Of Messages")
start_date = "2017-12-01"
end_date = "2018-01-08"
limit = 2
result = messages_controller.look_up_a_set_of_messages(start_date, end_date, limit)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of message objects in JSON format.

```
{
  "data": [
    {
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
        "from": "12061231234",
        "is_mms": false,
        "message_type": "longcode"
      },
      "type": "message",
      "id": "mdr2-ca82be46e6ba11e79d08862d092cf73d"
    },
    {
      "attributes": {
        "body": "test sms on v2",
        "status": "message buffered",
        "direction": "outbound",
        "amount_nanodollars": 4000000,
        "to": "12061232634",
        "message_encoding": 0,
        "timestamp": "2017-12-21T16:44:34.93Z",
        "delivery_receipts": [
          {
            "status": "message buffered",
            "status_code": 1003,
            "status_code_description": "Message accepted by Carrier",
            "timestamp": "2017-12-21T16:44:35.00Z",
            "level": 2
          },
          {
            "status": "smsc submit",
            "status_code": null,
            "status_code_description": "Message has been sent",
            "timestamp": "2017-12-21T16:44:35.00Z",
            "level": 1
          }
        ],
        "amount_display": "$0.0040",
        "from": "12012673227",
        "is_mms": false,
        "message_type": "longcode"
      },
      "type": "message",
      "id": "mdr2-39cadeace66e11e7aff806cd7f24ba2d"
    }
  ],
  "links": {
    "next": "https://api.flowroute.com/v2.1/messages?limit=2&start_date=2017-12-01T00%3A00%3A00%2B00%3A00&end_date=2018-01-08T00%3A00%3A00%2B00%3A00&offset=2"
  }
}
```

#### look\_up\_a\_message\_detail\_record(message\_id)

The method accepts a message `id` in MDR2 format as a parameter which you can learn more about in the [API Reference](https://developer.flowroute.com/api/messages/v2.1/look-up-a-message-detail-record/). In the following example, we retrieve the details of the first message in our `look_up_a_set_of_messages` search result.

##### Example Request
```python
message_id = result['data'][0]['id']
result = messages_controller.look_up_a_message_detail_record(message_id)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains the message object for our specified message `id`.
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
      "from": "12061232634",
      "is_mms": false,
      "message_type": "longcode"
    },
    "type": "message",
    "id": "mdr2-ca82be46e6ba11e79d08862d092cf73d"
  }
}
```
#### Errors

In cases of method errors, the Python library raises an exception which includes the HTTP Response code, an error message, and the HTTP body that was received in the request. 

##### Example Error
```
raise ErrorException('403 Forbidden – The server understood the request but refuses to authorize it.', _context)
```
  
