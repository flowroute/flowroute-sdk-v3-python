Flowroute Python Library v3
=====================

The Flowroute Python Library v3 provides methods for interacting with [Numbers v2](https://developer.flowroute.com/api/numbers/v2.0/) &endash; which includes inbound voice routes, E911 addresses, CNAM storage &endash; and [Messages v2.1](https://developer.flowroute.com/api/messages/v2.1/) and [CDR v2.0](https://developer.flowroute.com/api/cdrs/v2.0/) of the [Flowroute](https://www.flowroute.com) API.

**Topics**

*   [Requirements](#requirements)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [Controllers](#controllers)
        * [Numbers Controller](#numberscontroller)
        * [Routes Controller](#routescontroller)
        * [Messages Controller](#messagescontroller)
        * [E911s Controller](#e911scontroller)
        * [CNAMs Controller](#cnamscontroller)
    *   [Credentials](#credentials)
    *   [Methods](#methods)
        *   [Number Management](#number-management)
            *   [list_available_area_codes](#list_available_area_codes)
            *   [list_available_exchange_codes](#list_available_exchange_codes)
            *   [search_for_purchasable_phone_numbers](#search_for_purchasable_phone_numbers)
            *   [purchase_a_phone_number](#purchase_a_phone_numberpurchasable_number)
            *   [list_account_phone_numbers](#list_account_phone_numbers)
            *   [list_phone_number_details](#list_phone_number_detailsnumber_id)

        *   [Route Management](#route-management)
            *   [create_an_inbound_route](#create_an_inbound_routeroute_body)
            *   [list_inbound_routes](#list_inbound_routes)
            *   [update_primary_voice_route](#update_primary_voice_routenumber_id-route_body)
            *   [update_failover_voice_route](#update_failover_voice_routenumber_id-route_body)

        *   [Messaging](#messaging)
            *   [send_a_message](#send_a_messagemessage_body)
            *   [look_up_a_set_of_messagesstart_date](#look_up_a_set_of_messagesstart_date)
            *   [look_up_a_message_detail_record](#look_up_a_message_detail_recordmessage_id)

        *   [E911 Address Management](#e911-address-management)
            *   [list_e911s](#list_e911s)
            *   [get_e911](#get_e911e911_id)
            *   [validate_address](#validate_addresse911_attributes)
            *   [create_address](#create_addresse911_attributes)
            *   [update_address](#update_addresse911_id-e911_attributes)
            *   [associate](#associatee911_id-number_id)
            *   [list_dids_for_e911](#list_dids_for_e911e911_id)
            *   [disconnect](#disconnectnumber_id)
            *   [delete_address](#delete_addresse911_id)

        *   [CNAM Record Management](#cnam-management)
            *   [list_cnams](#list_cnams)
            *   [get_cnam](#get_cnamcnam_id)
            *   [create_cnam_record](#create_cnam_recordcnam_value)
            *   [associate_cnam](#associate_cnamcnam_id-number_id)
            *   [unassociate_cnam](#unassociate_cnamnumber_id)
            *   [remove_cnam](#remove_cnamcnam_id)

        *   [Call Detail Record (CDR)](#call-detail-record)
            *   [list_cdr_exports](#list_cdr_exports)
            *   [create_cdr_export](#create_cdr_export)
            *   [get_cdr_export_status](#get_cdr_export_status)
            *   [download_cdr_export](#download_cdr_export)

    *   [Errors](#errors)
    *   [Testing](#testing)

* * *
Requirements
------------

*   Flowroute [API credentials](https://manage.flowroute.com/accounts/preferences/api/)
*   [Python](https://www.python.org/downloads/): `Python 2 >=2.7.9` or `Python 3 >=3.4`


* * *
Installation
------------

1. First, start a shell session and clone the Python library:
    * via HTTPS: `git clone https://github.com/flowroute/flowroute-sdk-v3-python.git`

    * via SSH: `git@github.com:flowroute/flowroute-sdk-v3-python.git`

2. Switch to the newly-created `flowroute-sdk-v3-python` directory. This version of the library comes with a requirements file listing the required Python libraries. See [Installing Packages](https://packaging.python.org/tutorials/installing-packages/) to learn more about different ways to install Python packages. 

`pip` is already installed if you're using `Python 2 >=2.7.9` or `Python 3 >=3.4`. This version of the library has been tested with both `Python 2.7.9` and `Python 3.6.4` for Mac OS X. To see which version of `pip` is installed on your machine, run the following:

`pip --version`

Depending on your `pip` permissions, you may be required to preface each `pip` command with `sudo`. 

`pip3 install -r requirements.txt`

* * *
Usage
------------
In Flowroute's approach to building the Python Library v3, HTTP requests are handled by controllers named after the API resources they represent: **Numbers**, **Routes**, **E911s**, **CNAMs**, and **Messages**. These controllers contain the methods used to perform messaging, number management, route management, E911 address management, and CNAM record management within the Python library.

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

### E911sController

Contains all of the methods necessary to create, update, and validate new and existing E911 addresses, retrieve all of the E911 records, activate and deactive E911 service for long code and toll-free numbers on your account, view all of the phone numbers associated with an E911 record, and remove an E911 address from your account once it is no longer associated with any of your Flowroute phone numbers.

*   [list\_e911s()](#list_e911s) \- Returns a list of all E911 records on your account by default. All request parameters are optional. If you don't specify a limit, results are limited to the first 10 items.
*   [get\_e911(e911\_id)](#get_e911e911_id) \- Returns details on a specified E911 record.
*   [validate\_address(e911\_attributes)](#validate_addresse911_attributes) \- Lets you validate new and existing E911 addresses on your account.
*   [create\_address(e911\_attributes)](#create_addresse911_attributes) \- Lets you create and validate an E911 address within the US and Canada which can then be assigned to any of the long code or toll­free numbers on your account. To assign an E911 address to your number, see the [associate](#associatee911_id-number_id) method.
*   [update\_address(e911\_id, e911\_attributes)](#update_addresse911_id-e911_attributes) \- Lets you update and validate an existing E911 address on your account. You must create the E911 address first by following the [create\_address](#create_address) method. 
*   [associate(e911\_id, number\_id)](#associatee911_id-number_id) \- Lets you assign a valid E911 address to a specific long code or toll-free phone number in your account. This method calls an endpoint which does not return an error for subsequent attempts at associating a phone number with the same E911 record. The E911 record assignment charge only occurs on the first successful attempt. Note that you can later assign a different `e911_id` to the same phone number and will be charged accordingly.
*   [list\_dids\_for\_e911(e911\_id)](#list_dids_for_e911e911_id) \- Returns a list of your Flowroute long code or toll-free phone numbers associated with a specified E911 record.
*   [disconnect(number\_id)](#disconnectnumber_id) \- Lets you deactivate the current E911 service for your phone number.
*   [delete\_address(e911\_id)](#delete_addresse911_id) \- Lets you delete an E911 address associated with your account. You must remove all phone number associations first before you can successfully delete the specified E911 record.

### CNAMsController

Contains all of the methods necessary to create and delete CNAM records, view all of the CNAM records associated with your account, filter for specific CNAM records by status, review CNAM record details, and assign and unassign CNAM records to your Flowroute long code phone numbers.
*   [list\_cnams()](#list_cnams) \- Returns a list of all CNAM records on your account by default. You can apply search filters using any of the available query parameters.
*   [get\_cnam(cnam\_id)](#get_cnamcnam_id) \- Returns details pertaining to a specific CNAM record on your account, including long code numbers that are associated with the record.
*   [create\_cnam\_record(cnam\_value)](#create_cnam_recordcnam_value) \- Lets you create a Caller ID record for your account which can then be assigned to any of your long code numbers. To assign a CNAM record to your number, see the [associate\_cnam](#associate_cnamcnam_id-number_id) method.
*   [associate\_cnam(cnam\_id, number\_id)](#associate_cnamcnam_id-number_id) \- Lets you associate a CNAM record with a specified long code number on your account. Note that a CNAM record takes 1-2 days to be approved.
*   [unassociate(number\_id)](#unassociate_cnamnumber_id) \- Lets you unassign a CNAM record associated with a specified long code number on your account without deleting the CNAM record itself.
*   [remove\_cnam(cnam\_id)](#remove_cnamcnam_id) \- Lets you delete a CNAM record from your account. Note that this will automatically disassociate all numbers associated with the deleted CNAM record.

### CDRsController

Contains all of the methods necessary to create and retrieve CDR exports.
*   [list\_cdr\_exports](#list_cdr_exports) \- Returns a list of all CDR Exports that have been created on your account.
*   [create\_cdr\_export](#create_cdr_export) \- Create a CDR Export with a list of filter parameters.  When this asynchronous job is done running,
Flowroute's servers will post to a callback URL if one is provided.
*   [get\_cdr\_export\_status(cdr\_export\_id)](#get_cdr_export_status) \- Returns details pertaining to a specific CDR Export, including the download_url that
is required to retrieve the CDR Export data.
*   [download\_cdr\_export(cdr\_export\_id)](#download_cdr_export) \- Downloads the CDR Export CSV file or GZIPPED CSV file from the Flowroute servers.


The following shows an example of a single Python file that imports the Flowroute API client and all the required modules. The Python Library v3 comes with three example demo files &mdash; **number_route_message_demo.py**, **e911_demo.py**, **cnam_demo.py** &mdash; files that you can edit and run for demonstration and testing purposes.

```python
import pprint
import os
import json
import random
import string
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
```    
#### Credentials

Let's take **number_route_message_demo.py** as an example. In the file, replace `basic_auth_user_name` with your API Access Key and `basic_auth_password` with your API Secret Key from the [Flowroute Manager](https://manage.flowroute.com/accounts/preferences/api/). Note that in our example, we are accessing your Flowroute credentials as environment variables. To learn more about setting environment variables, see [How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps).

```python
# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')
mobile_number = "YOUR_MOBILE_NUMBER"
```
#### Instantiate API Client and Controllers
Next, instantiate the API Client and its controllers. In the following example, we are only instantiating the necessary controllers for the Numbers,Messages, and Routes resources. The E911 and CNAM demo files come with their own set of required controllers to interact with the associated methods for E911 and CNAM record management.

```python
# Instantiate API client and create controllers for Numbers, Messages, and Routes
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)
numbers_controller = client.numbers
routes_controller = client.routes
messages_controller = client.messages
```
## Methods
The following section will demonstrate the capabilities of Numbers v2, Messaging v2.1, E911 v2, and CNAM v2 that are wrapped in our Python library. Note that the example responses have been formatted using Mac's `pbpaste` and `jq`. To learn more, see [Quickly Tidy Up JSON from the Command Line](http://onebigfunction.com/vim/2015/02/02/quickly-tidying-up-json-from-the-command-line-and-vim/). 

### Number Management

The Flowroute Python Library v3  allows you to make HTTP requests to the `numbers` resource of Flowroute API v2: `https://api.flowroute.com/v2/numbers`.

All of the number management methods are encapsulated in `number_route_message_demo.py`.

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

The Flowroute Python Library v3 allows you to make HTTP requests to the `routes` resource of Flowroute API v2: `https://api.flowroute.com/v2/routes`.

All of the route management methods are encapsulated in `number_route_message_demo.py`.
    
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
The Flowroute Python Library v3 allows you to make HTTP requests to the `messages` resource of Flowroute API v2.1: `https://api.flowroute.com/v2.1/messages`.

All of the messaging methods are encapsulated in `number_route_message_demo.py`.

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
### E911 Address Management

The Flowroute Python Library v3  allows you to make HTTP requests to the `e911s` resource of Flowroute API v2: `https://api.flowroute.com/v2/e911s`.

All of the E911 address management methods are encapsulated in `e911_demo.py`.

#### list\_e911s()

The method accepts `limit`, `offset`, and `state` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-account-e911-addresses/).
    
##### Example Request
```python
print("--List E911 Records")
limit = 2
offset = None
result = e911s_controller.list_e911s(limit, offset)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of e911 objects in JSON format.

```
--List E911 Records
{'data': [{'attributes': {'address_type': 'Lobby',
                          'address_type_number': '12',
                          'city': 'Seattle',
                          'country': 'USA',
                          'first_name': 'Maria',
                          'label': 'Example E911',
                          'last_name': 'Bermudez',
                          'state': 'WA',
                          'street_name': '20th Ave SW',
                          'street_number': '7742',
                          'zip': '98106'},
           'id': '20930',
           'links': {'self': 'https://api.flowroute.com/v2/e911s/20930'},
           'type': 'e911'},
          {'attributes': {'address_type': 'Apartment',
                          'address_type_number': '12',
                          'city': 'Seattle',
                          'country': 'US',
                          'first_name': 'Something',
                          'label': '5th E911',
                          'last_name': 'Someone',
                          'state': 'WA',
                          'street_name': 'Main St',
                          'street_number': '645',
                          'zip': '98104'},
           'id': '20707',
           'links': {'self': 'https://api.flowroute.com/v2/e911s/20707'},
           'type': 'e911'}],
 'links': {'next': 'https://api.flowroute.com/v2/e911s?limit=2&offset=2',
           'self': 'https://api.flowroute.com/v2/e911s?limit=2&offset=0'}}
```

#### get\_e911(e911\_id)

The method accepts an `e911_id` as a path parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-e911-record-details/).
    
##### Example Request
```python
e911_id = None
# If the user has any E911 records, pull one up
for e in result['data']:
    e911_id = e['id']
    break

if e911_id:
    print("\n--Get Details for a specific E911 Record")
    result = e911s_controller.get_e911(e911_id)
    pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains a detailed e911 object in JSON format.

```
--Get Details for a specific E911 Record
{
  "data": {
    "attributes": {
      "address_type": "Suite",
      "address_type_number": "333",
      "city": "Seattle",
      "country": "US",
      "first_name": "Albus",
      "label": "Office Space III",
      "last_name": "Rasputin, Jr.",
      "state": "WA",
      "street_name": "Main St",
      "street_number": "666",
      "zip": "98101"
    },
    "id": "21845",
    "links": {
      "self": "https://api.flowroute.com/v2/e911s/21845"
    },
    "type": "e911"
  }
}
```

#### validate_address(e911_attributes)

The method accepts the different attributes of an E911 address as parameters: `label`, `first_name`, `last_name`, `street_name`, `street_number`, optional `address_type` and `address_type_number`, `city`, `state`, `country`, and `zipcode`. Learn more about the different E911 attributes in the [API reference](https://developer.flowroute.com/api/e911s/v2.0/validate-e911-address/). 
    
##### Example Request
```
print("\n--Validate an Address")
try:
    result = e911s_controller.validate_address(
                                               label="Test Address",
                                               first_name="Chris",
                                               last_name="Smith",
                                               street_name="3rd Ave",
                                               street_number="1182",
                                               city="Seattle",
                                               state="WA",
                                               country="CA",
                                               zipcode="98101")
    pprint.pprint(result)
except Exception as e:
    print(str(e))
```

##### Example Response

On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content. On error, a printable representation of the detailed API response is displayed.

```
--Validate an Address
HTTP response not OK.
{"errors":[{"detail":"Could not geocode this address. Please check the validity of your address.","id":"7fcfd1cd-486b-4159-8484-b710bd4bbab4","status":400,"title":"Client Error"}]}
```
#### create_address(e911_attributes)

The method accepts the different attributes of an E911 address as parameters: `label`, `first_name`, `last_name`, `street_name`, `street_number`, optional `address_type` and `address_type_number`, `city`, `state`, `country`, and `zipcode`. Learn more about the different E911 attributes in the [API reference](https://developer.flowroute.com/api/e911s/v2.0/create-and-validate-new-e911-address/). 
    
##### Example Request
```
print("\n--Create and Validate an Address")
try:
    result = e911s_controller.create_address(
                                             label="E911 Test",
                                             first_name="Chris",
                                             last_name="Smith",
                                             street_name="3rd Ave",
                                             street_number="1218",
                                             city="Seattle",
                                             state="WA",
                                             country="US",
                                             zipcode="98101")
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
```

##### Example Response

On success, the HTTP status code in the response header is `201 Created` and the response body contains the newly created e911 object in JSON format. On error, a printable representation of the detailed API response is displayed.

```
--Create and Validate an Address
{'data': {'attributes': {'city': 'Seattle',
                         'country': 'US',
                         'first_name': 'Chris',
                         'label': 'E911 Test',
                         'last_name': 'Smith',
                         'state': 'WA',
                         'street_name': '3rd Ave',
                         'street_number': '1218',
                         'zip': '98101'},
          'id': '21301',
          'links': {'self': 'https://api.flowroute.com/v2/e911s/21301'},
          'type': 'e911'}}
```
#### update_address(e911_id, e911_attributes)

The method accepts an E911 record id and the different attributes of an E911 address as parameters: `label`, `first_name`, `last_name`, `street_name`, `street_number`, optional `address_type` and `address_type_number`, `city`, `state`, `country`, and `zipcode`. Learn more about the different E911 attributes that you can update in the [API reference](https://developer.flowroute.com/api/e911s/v2.0/update-and-validate-existing-e911-address/). In the following example, we will retrieve the record ID of our newly created E911 address and assign it to a variable, `record_id`. We then update the `last_name` of our selected E911 address to "Wiley".
    
##### Example Request
```
# Pull the ID from the newly created record
if len(result):
    record_id = result['data']['id']

    print("\n--Update an E911 Address")
    try:
        result = e911s_controller.update_address(record_id, last_name='Wiley')
        pprint.pprint(result)
    except Exception as e:
        print(str(e))
        print(e.context.response.raw_body)
```
##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains the newly updated e911 object in JSON format. On error, a printable representation of the detailed API response is displayed.

```
--Update an E911 Address
{'data': {'attributes': {'city': 'Seattle',
                         'country': 'US',
                         'first_name': 'Chris',
                         'label': 'E911 Test 2',
                         'last_name': 'Wiley',
                         'state': 'WA',
                         'street_name': '3rd Ave',
                         'street_number': '1218',
                         'zip': '98104'},
          'id': '21306',
          'links': {'self': 'https://api.flowroute.com/v2/e911s/21306'},
          'type': 'e911'}}
```
#### associate(e911_id, number_id)

The method accepts an E911 record id and a phone number as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/assign-valid-e911-address-to-phone-number/). In the following example, we call the [list_account_phone_numbers](#list_account_phone_numbers) covered under Number Management and [list_e911s](#list_e911s), extract the values of the first items in the returned JSON arrays into variables `e911_id` and `did` then make the association between them.
    
##### Example Request
```
# Get our DIDs
did_list = numbers_controller.list_account_phone_numbers()
did = did_list['data'][0]['attributes']['value']

# Get our E911s
e911_list = e911s_controller.list_e911s()
e911_id = e911_list['data'][0]['id']

# Associate them
print("--Associate an E911 Record and a DID")
try:
    result = e911s_controller.associate(e911_id, did)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
```
##### Example Response

On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

```
--Associate an E911 Record and a DID
204: No Content
```

#### list_dids_for_e911(e911_id)

The method accepts an E911 record id as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-phone-numbers-associated-with-e911-record/). In the following example, we retrieve the list of phone numbers associated with our previously assigned `e911_id`.
    
##### Example Request
```
print("\n--List all DIDs associated with an E911 Record")
result = e911s_controller.list_dids_for_e911(e911_id)
pprint.pprint(result)
```
##### Example Response
On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of related number objects in JSON format.
```
--List all DIDs associated with an E911 Record
{
  "data": [
    {
      "attributes": {
        "alias": null,
        "value": "12062011682"
      },
      "id": "12062011682",
      "links": {
        "self": "https://api.flowroute.com/v2/numbers/12062011682"
      },
      "type": "number"
    }
  ],
  "links": {
    "self": "https://api.flowroute.com/v2/e911s/21330/relationships/numbers?limit=10&offset=0"
  }
}
```

#### disconnect(number_id)

The method accepts a phone number as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/deactivate-e911-service-for-phone-number/). In the following example, we deactivate the E911 service for our previously assigned `did`.

##### Example Request
```
# Dis-Associate them
try:
    print("\n--Un-associate the address")
    result = e911s_controller.disconnect(12062011682)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
```
##### Example Response
On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

```
--Un-associate the address
''
```
#### delete_address(e911_id)

The method accepts an E911 record ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/remove-e911-address-from-account/). Note that all phone number associations must be removed first before you are able to delete the specified `e911_id`. In the following example, we will attempt to delete the previously assigned `e911_id`.

##### Example Request
```
try:
    print("\n--Delete an E911 Address")
    result = e911s_controller.delete_address(e911_id)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
```
##### Example Response
On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

```
--Delete an E911 Address
''
```
### CNAM Record Management

The Flowroute Python Library v3  allows you to make HTTP requests to the `cnams` resource of Flowroute API v2: `https://api.flowroute.com/v2/cnams`.

All of the CNAM record management methods are encapsulated in `cnam_demo.py`.

#### list\_cnams()

The method accepts `limit`, `offset`, and `is_approved` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-account-cnam-records/).
    
##### Example Request
```python
print("--List CNAM Records")
limit = 10
offset = None
result = cnams_controller.list_cnams(limit, offset)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of cnam objects in JSON format.

```
--List CNAM Records
{'data': [{'attributes': {'approval_datetime': None,
                          'creation_datetime': None,
                          'is_approved': True,
                          'rejection_reason': '',
                          'value': 'TEST, MARIA'},
           'id': '17604',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/17604'},
           'type': 'cnam'},
          {'attributes': {'approval_datetime': '2018-04-16 '
                                               '16:20:32.939166+00:00',
                          'creation_datetime': '2018-04-12 '
                                               '19:08:39.062539+00:00',
                          'is_approved': True,
                          'rejection_reason': None,
                          'value': 'REGENCE INC'},
           'id': '22671',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/22671'},
           'type': 'cnam'},
          {'attributes': {'approval_datetime': '2018-04-23 '
                                               '17:04:30.829341+00:00',
                          'creation_datetime': '2018-04-19 '
                                               '21:03:04.932192+00:00',
                          'is_approved': True,
                          'rejection_reason': None,
                          'value': 'BROWN BAG'},
           'id': '22790',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/22790'},
           'type': 'cnam'},
          {'attributes': {'approval_datetime': '2018-05-23 '
                                               '18:58:46.052602+00:00',
                          'creation_datetime': '2018-05-22 '
                                               '23:38:27.794911+00:00',
                          'is_approved': True,
                          'rejection_reason': None,
                          'value': 'LEATHER REBEL'},
           'id': '23221',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/23221'},
           'type': 'cnam'},
          {'attributes': {'approval_datetime': '2018-05-23 '
                                               '18:58:46.052602+00:00',
                          'creation_datetime': '2018-05-22 '
                                               '23:39:24.447054+00:00',
                          'is_approved': True,
                          'rejection_reason': None,
                          'value': 'LEATHER REBELZ'},
           'id': '23223',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/23223'},
           'type': 'cnam'},
          {'attributes': {'approval_datetime': '2018-05-23 '
                                               '18:58:46.052602+00:00',
                          'creation_datetime': '2018-05-22 '
                                               '23:42:00.786818+00:00',
                          'is_approved': True,
                          'rejection_reason': None,
                          'value': 'MORBO'},
           'id': '23224',
           'links': {'self': 'https://api.flowroute.com/v2/cnams/23224'},
           'type': 'cnam'}],
 'links': {'self': 'https://api.flowroute.com/v2/cnams?limit=10&offset=0'}}
```
#### get_cnam(cnam_id)

The method accepts a CNAM record ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/list-cnam-record-details/). In the following example, we query for approved CNAM records on your account and then extract the ID of the first record returned and retrieve the details of that specific CNAM record. 
    
##### Example Request
```
print("\n--List Approved CNAM Records")
result = cnams_controller.list_cnams(is_approved=True)
pprint.pprint(result)
if len(result['data']):
    cnam_id = result['data'][0]['id']

    print("\n--List CNAM Detail")
    result = cnams_controller.get_cnam(cnam_id)
    pprint.pprint(result)
```
##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains a detailed cnam object in JSON format. For the sake of brevity, we will omit the response to the approved CNAM record query.
```
--List CNAM Detail
{'data': {'attributes': {'approval_datetime': None,
                         'creation_datetime': None,
                         'is_approved': True,
                         'rejection_reason': '',
                         'value': 'TEST, MARIA'},
          'id': '17604',
          'links': {'self': 'https://api.flowroute.com/v2/cnams/17604'},
          'type': 'cnam'}}
```
#### create_cnam_record(cnam_value)

The method accepts a Caller ID value as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/create-a-new-cnam-record/). In the following example, we reuse the `random_generator()` function to generate a four-character random string which we will concatenate with FR and assign as our CNAM value.

| CNAM Storage Rules |
| ------------------- |
| You can enter up to 15 characters for your CNAM value at least one of which is a letter. |
| While most CNAM presets can be approved, the following are not allowed and must be rejected: |
|    -  Consist of curse words and/or is inappropriate. |
|    -  A phone number (CNAM must be a name not a number) |
|    -  If the CNAM preset which the customer has submitted appears to be misleading such as: |
|       - Political Figures or Places (Obama, Barack or The White House) |
|       - False or fake CNAM (Seattle Police) |
    
##### Example Request
```
# Helper function for random strings
def random_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

print("\n--Create a CNAM Record")
cnam_value = 'FR ' + random_generator()
result = cnams_controller.create_cnam_record(cnam_value)
pprint.pprint(result)
print("\nNOTE: Newly created CNAM records need to be approved first before they can be associated with your long code number.")
```

##### Example Response

On success, the HTTP status code in the response header is `201 Created` and the response body contains the newly created cnam object in JSON format. Note that CNAM records take up to 48 hours to be approved on your account and further association with a phone number takes 5-7 business days.

```
--Create a CNAM Record
{'data': {'attributes': {'approval_datetime': None,
                         'creation_datetime': '2018-06-01 '
                                              '00:09:52.513092+00:00',
                         'is_approved': False,
                         'rejection_reason': None,
                         'value': 'FR H5K8'},
          'id': '23454',
          'links': {'self': 'https://api.flowroute.com/v2/cnams/23454'},
          'type': 'cnam'}}

NOTE: Newly created CNAM records need to be approved first before they can be associated with your long code number.
```
#### associate_cnam(cnam_id, number_id)

The method accepts a CNAM record ID and a phone number as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/assign-cnam-record-to-phone-number/). In the following example, we will call `list_account_phone_numbers()` and associate the first number in the returned array with our previously assigned `cnam_id`.
    
##### Example Request
```
print("\n--Associate a CNAM Record to a DID")
our_numbers = numbers_controller.list_account_phone_numbers()
did_id = our_numbers['data'][0]['id']

if cnam_id is None:
    print("Create some CNAM records and wait for approval before trying"
          " to associate them with a DID")
else:
    result = cnams_controller.associate_cnam(cnam_id, did_id)
    pprint.pprint(result)
```

##### Example Response
On success, the HTTP status code in the response header is `202 Accepted` and the response body contains an attributes dictionary containing the `date_created` field and the assigned cnam object in JSON format. This request will fail if the CNAM you are trying to associate has not yet been approved.
```
--Associate a CNAM Record to a DID
{'data': {'attributes': {'date_created': 'Fri, 01 Jun 2018 00:17:52 GMT'},
          'id': 17604,
          'type': 'cnam'}}
```
#### unassociate_cnam(number_id)

The method accepts a phone number as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/unassign-a-cnam-record-from-phone-number/). In the following example, we will disassociate the same phone number that we've used in `associate_cnam()`.
    
##### Example Request
```
print("\n--Unassociate a CNAM Record from a DID")
result = cnams_controller.unassociate_cnam(did_id)
pprint.pprint(result)
```

##### Example Response
On success, the HTTP status code in the response header is `202 Accepted` and the response body contains an attributes object with the date the CNAM was requested to be deleted, and the updated cnam object in JSON format.

```
--Unassociate a CNAM Record from a DID
{'data': {'attributes': {'date_created': 'Fri, 01 Jun 2018 00:17:52 GMT'},
          'id': None,
          'type': 'cnam'}}
```
#### remove_cnam(cnam_id)

The method accepts a CNAM record ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/numbers/v2.0/remove-cnam-record-from-account/). In the following example, we will be deleting our previously extracted `cnam_id` from the "List Approved CNAM Records" function call.
    
##### Example Request
```
print("\n--Remove a CNAM Record from your account")
result = cnams_controller.remove_cnam(cnam_id)
pprint.pprint(result)
```

##### Example Response
On success, the HTTP status code in the response header is `204 No Content` which means that the server successfully processed the request and is not returning any content.

```
--Remove a CNAM Record from your account
''
```

### Call Detail Record Export API

The Flowroute Python Library v3 allows you to make HTTP requests to the `cdrs` resource of Flowroute API v2: `https://api.flowroute.com/v2/cdrs`.

All of the CDR export methods are encapsulated in `cdr_demo.py`.

#### list_cdr_exports

The method accepts `status`, `limit`, and `offset` as parameters which you can learn more about in the [API reference](https://developer.flowroute.com/api/cdrexports/v2.0/list-cdrs/).

##### Example Request
```python
print("--List Completed CDR Exports")
status = 'completed'
limit = 10
offset = None
result = cdrs_controller.list_cdr_exports(status, limit, offset)
pprint.pprint(result)
```

##### Example Response

On success, the HTTP status code in the response header is `200 OK` and the response body contains an array of CDR Export objects in JSON format.

```
{
  "data": [
    {
      "data": {
        "attributes": {
          "billed_minutes": 0,
          "callback_url": null,
          "ccrf": "0.0",
          "created_at": "2019-03-18T23:20:30+00:00",
          "download_url": "https://s3.us-west-2.amazonaws.com/flowroute-cdrexports/40375/2019/3/18/e55f474c3154a14cd2cec842f79ca6a8000.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential;=ASIA2DG5LFSOIDMMFUVW%2F20190318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date;=20190318T232030Z&X-Amz-Expires;=259200&X-Amz-SignedHeaders;=host&X-Amz-Security-Token;=FQoGZXIvYXdzEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDBB4u7fdwDGKfgWUSyKZBF6fKcf16poJprJr9imLeVtLmQCcWKWnJjmmkRLz%2FQKjaMUvHTnTo4drHg8KWAbvvbpwoC3NOgFsn28nw1fHlgBjVODuIDeMJxFHROUZAPTbayDsUttyO%2BqbcluTENh3ESJoZGoXi3sGwHDvvtcYTtHr0MQMw7cvEEKgKvaMp7KgliTpwJzzquAPeMQg2LD5C%2FR36nI%2BZNXrqp64ZovMrtVV1IR9KLXTkRZs3%2Ft%2Bvt7CzhM8Fopc96cKhu%2FpX7eVR%2BBJfTeUD%2FPvz19KWuKWsM9V%2FEqNptPTADIg6LtupuainAJVhvBaatHOdGe7aUt2ABkvsCZVs5uFbdy79aHVMMtZgN886E1TsVR%2FDwbg1AhfsxLBujEumIn9bJAkr1RJpHakrC67gm%2FyTsU64huC%2BGCqQrd5CHIAQsbDCV8tMPw5K%2B3SonWV2TLusiOg%2FWZikSMqgDrexj7KQo7utXWGAAt2W4INKGSpwY1BoOWJGl6rBMJ1rWpERJ2lxagHeAPd8tOPiKVvkytscHH1vEgM4S1wOApspud5tMsvtkhyAWGwfsbkn1ZiF5PoqUbBjHXH9m%2Bq8p4oLUEI2aozdrLEqdQxELSlleQna0U1VsxyRa%2BXRjxDU7oOpmqETzUEx3NKELDGOb%2FwzO%2F8HH%2BqPcC8OVaox2KdLvAFwHGulKLwRrtSlblZopzZqrBmd0R5X60tZ4u2KIUH3lLeiSiGvb%2FkBQ%3D%3D&X-Amz-Signature;=beb0e34bbd48cac63ce1db887de6f783238acddcfd7675b3a525ae49003d2cb7",
          "expires_at": "2019-03-21T23:20:30+00:00",
          "filter_parameters": {
            "number_aliases": [
              "Home Phone"
            ],
            "start_call_end_time": "2019-01-01T00:00:00+00:00",
            "start_call_start_time": "2018-12-01T00:00:00+00:00"
          },
          "num_calls": 0,
          "requested_at": "2019-03-18T23:20:17+00:00",
          "status": "completed",
          "total_cost": "0.0",
          "call_subtotal": "0.0",
          "connect_fees": "0.0",
          "cnamlookup_fees": "0.0",
          "usf_fees": "0.0"
        },
        "id": 203485,
        "type": "cdrexport"
      }
    },
    {
      "data": {
        "attributes": {
          "billed_minutes": 0,
          "callback_url": null,
          "ccrf": "0.0",
          "created_at": "2019-03-18T23:16:47+00:00",
          "download_url": "https://s3.us-west-2.amazonaws.com/flowroute-cdrexports/40375/2019/3/18/8294b10fd18846d61ab1de8535f05b55000.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential;=ASIA2DG5LFSOIDMMFUVW%2F20190318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date;=20190318T231647Z&X-Amz-Expires;=259200&X-Amz-SignedHeaders;=host&X-Amz-Security-Token;=FQoGZXIvYXdzEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDBB4u7fdwDGKfgWUSyKZBF6fKcf16poJprJr9imLeVtLmQCcWKWnJjmmkRLz%2FQKjaMUvHTnTo4drHg8KWAbvvbpwoC3NOgFsn28nw1fHlgBjVODuIDeMJxFHROUZAPTbayDsUttyO%2BqbcluTENh3ESJoZGoXi3sGwHDvvtcYTtHr0MQMw7cvEEKgKvaMp7KgliTpwJzzquAPeMQg2LD5C%2FR36nI%2BZNXrqp64ZovMrtVV1IR9KLXTkRZs3%2Ft%2Bvt7CzhM8Fopc96cKhu%2FpX7eVR%2BBJfTeUD%2FPvz19KWuKWsM9V%2FEqNptPTADIg6LtupuainAJVhvBaatHOdGe7aUt2ABkvsCZVs5uFbdy79aHVMMtZgN886E1TsVR%2FDwbg1AhfsxLBujEumIn9bJAkr1RJpHakrC67gm%2FyTsU64huC%2BGCqQrd5CHIAQsbDCV8tMPw5K%2B3SonWV2TLusiOg%2FWZikSMqgDrexj7KQo7utXWGAAt2W4INKGSpwY1BoOWJGl6rBMJ1rWpERJ2lxagHeAPd8tOPiKVvkytscHH1vEgM4S1wOApspud5tMsvtkhyAWGwfsbkn1ZiF5PoqUbBjHXH9m%2Bq8p4oLUEI2aozdrLEqdQxELSlleQna0U1VsxyRa%2BXRjxDU7oOpmqETzUEx3NKELDGOb%2FwzO%2F8HH%2BqPcC8OVaox2KdLvAFwHGulKLwRrtSlblZopzZqrBmd0R5X60tZ4u2KIUH3lLeiSiGvb%2FkBQ%3D%3D&X-Amz-Signature;=8b4dab6a349ecc98905d949d026889035101ee8acb34055efb87ca2c299e4ba4",
          "expires_at": "2019-03-21T23:16:47+00:00",
          "filter_parameters": {
            "number_aliases": [
              "Home Phone"
            ],
            "start_call_end_time": "2018-10-01T00:00:00+00:00",
            "start_call_start_time": "2018-10-01T00:00:00+00:00"
          },
          "num_calls": 0,
          "requested_at": "2019-03-18T23:16:46+00:00",
          "status": "completed",
          "total_cost": "0.0",
          "call_subtotal": "0.0",
          "connect_fees": "0.0",
          "cnamlookup_fees": "0.0",
          "usf_fees": "0.0"
        },
        "id": 203484,
        "type": "cdrexport"
      }
    }
  ],
  "links": {
    "next": "http://cdr-api/cdrs/exports?offset=2&limit;=2",
    "self": "http://cdr-api/cdrs/exports?offset=0&limit;=2"
  }
}
```

#### create_cdr_export

The method accepts a many query parameters, such as `start_call_start_time`, `start_call_end_time`, and `number_aliases`. Learn more about the different CDR export filter parameters in the [API reference](https://developer.flowroute.com/api/cdrexports/v2.0/query-cdrs/).

##### Example Request
```
print("\n--Create a CDR Export where the call started between a certain time from a list of number alises")
try:
    filters = {
        "start_call_start_time": "2019-01-01 00:00:00",
        "start_call_end_time": "2019-02-01 00:00:00",
        "number_aliases": ["Office 221", "Office 888"]
    }
    callback_url = "https://myserver.com/cdrs"
    result = cdrs_controller.create_cdr(filters, callback_url)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
```

##### Example Response

On success, the HTTP status code in the response header is `201 Created` and the response body contains the newly created CDR export object in JSON format. On error, a printable representation of the detailed API response is displayed.

```

{
  "data": {
    "type": "cdrexport",
    "id": "38647",
    "links": {
        "self": "https://api.flowroute.com/v2/cdrs/exports/38647"
      },
    "attributes": {
      "number_aliases": [
        "Office 221",
        "Office 888"
      ],
      "start_call_start_time": "2019-01-01 00:00:00",
      "start_call_end_time": "2019-02-01 00:00:00",
      "callback_url": "https://myserver.com/cdrs",
      "status": "processing",
      "download_url": None,
      "requested_at": "2019-03-18T16:43:00+00:00",
      "created_at": "2019-03-18T16:43:01+03:00",
      "expires_at": None,
      "total_cost": None,
      "call_subtotal": None,
      "connect_fees": None,
      "cnamlookup_fees": None,
      "usf_fees": None,
      "ccrf": None,
      "billed_minutes": None,
      "filter_parameters": {
        "number_aliases": [
          "Office 221",
          "Office 888"
        ],
      }
    }
  }
}
```

#### get_cdr_export_status(cdrexport_id)

The method accepts a CDR Export ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/cdrexports/v2.0/cdr-status/). In the following example, we will be retrieving the Detail Status of the CDR Export we created in the previous query.

##### Example Request
```
print("\n--Get CDR Export Detail Status")
result = cdrs_controller.get_cdr_export_status(cdrexport_id)
pprint.pprint(result)
```

##### Example Response
On success, the HTTP status code in the response header is `200 OK` and the response body contains a CDR export JSON object.

```
{'data':
	'type': 'cdrexport',
	'id': '38647',
	'attributes': {
		'callback_url': 'http://myserver.com/webhook',
		'status': 'completed',
		'download_url': ('https://s3.us-east-2.amazonaws.com/uiuc-presigned-url-example/secret.'
			'txt?X-Amz-Date=20170720T182534Z&X-Amz-SignedHeaders;=host&X-Amz-Creden;'
			'tial=ASIAIYLQNVRRFNZOCFBA%2F20170720%2Fus-east-2%2Fs3%2Faws4_request&'
			'X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires;=604800&X-Amz-Security-;'
			'Token=FQoDYXdzEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDOLWx95j90zPxGh7WSL'
			'dAVnoYoKC4gjrrR1xbokFWRRwutmuAmOxaIVcQqOy%2Fqxy%2FXQt3Iz%2FohuEEmI7%2'
			'FHPzShy%2BfgQtvfUeDaojrAx5q8fG9P1KuIfcedfkiU%2BCxpM2foyCGlXzoZuNlcF8o'
			'hm%2BaM3wh4%2BxQ%2FpShLl18cKiKEiw0QF1UQGj%2FsiEqzoM81vOSUVWL9SpTTkVq8'
			'EQHY1chYKBkBWt7eIQcxjTI2dQeYOohlrbnZ5Y1%2F1cxPgrbk6PkNFO3whAoliSjyRC8'
			'e4TSjIY2j3V6d9fUy4%2Fp6nLZIf9wuERL7xW9PjE6eZbKOHnw8sF&X-Amz-Signature;'
			'=a14b3065ab822105e8d7892eb5dcc455ddd603c61e47520774a7289178af9ecc'),
		 'requested_at': '2018-09-11T23:21:20+00:00'
		 'created_at': '2018-09-11T23:23:23+00:00'
		 'expires_at': '2018-09-14T23:23:29+00:00',
		 'total_cost': '34.321300',
		 'usf_fees': '5.93190',
		 'ccrf': '0.0',
		 'num_calls': 301,
		 'billed_minutes': 10,
		 'filter_parameters': {
			"start_call_start_time": "2019-01-01 00:00:00",
			"start_call_end_time": "2019-02-01 00:00:00",
			"number_aliases": "['Office 221', 'Office 888']"
		 }
	},
	'links': {
		'self': 'http://cdr-api/cdrs/exports/38647'
    }
}
```

#### #download_cdr_export(cdrexport_id)

The method accepts a CDR Export ID as a parameter which you can learn more about in the [API reference](https://developer.flowroute.com/api/cdrexports/v2.0/cdr-status/). In the following example, we will be retrieving the file of the CDR Export we created in the previous query.
You can learn more about the format of the CDR Export Data in the [API results reference](https://developer.flowroute.com/api/cdrexports/v2.0/cdr-results/).

##### Example Request
```
print("\n--Get CDR Export Data")
result = cdrs_controller.download_cdr_export(cdrexport_id, filename)
pprint.pprint(result)
```

##### Example Response
On success, the HTTP status code in the response header is `200 OK` and a file is written to the local computer using the provided filename.

```
direction,start_time,end_time,destination,number_alias,callerid,total_cost,destination_name,callerid_country,line_information,result,call_fail_sip_code,call_fail_reason,duration,billed_duration,rate,first_increment,subsequent_increment,cost_subtotal,connect_fee,usf_fee,ccrf,cnam_lookup_fee,custom_x_tag,customer_ip
Outbound,2019-06-25 18:18:54+00,2019-06-25 18:19:31+00,18774551500,Office Line 2,+12063389999,0.00000000,UNITED STATES - TOLL FREE,N/A,,completed,200,OK,37,42,0.000000,6,6,0.00000000,0.0000,0.00000000,0.00000000,0.00000000,,53.186.152.52:5080
Inbound,2019-06-25 18:18:00+00,2019-06-25 18:18:29+00,12063389999,Office Line 2,+12069928999,0.00474784,UNITED STATES,UNITED STATES,61,completed,200,OK,29,30,0.001500,6,6,0.00075000,0.0000,0.00000000,0.00009784,0.00390000,,53.186.152.52
Outbound,2019-06-25 18:15:38+00,2019-06-25 18:17:24+00,12069928999,Office Line 1,+12063389998,0.01994112,UNITED STATES,N/A,,completed,200,OK,106,108,0.009800,6,6,0.01764000,0.0000,0.00000000,0.00230112,0.00000000,,53.186.151.52:5080
```


#### Errors

In cases of method errors, the Python library raises an exception which includes an error message and the HTTP body that was received in the request. 

##### Example Error
` raise ErrorException('403 Forbidden – The server understood the request but refuses to authorize it.', _context) `
 
## Testing

Once you are done configuring your Flowroute API credentials and updating the function parameters, you can run any of the demo files to see them in action. The Flowroute library demo files are named after the resource they represent: `<resource_name>_demo.py`.

` python cnam_demo.py `
` python e911_demo.py `
` python cdrs_demo.py `