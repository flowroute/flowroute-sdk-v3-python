#!/usr/bin/env python

import pprint
import os
import json
import random
import string
from flowroutenumbersandmessaging.configuration import *
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import (
    FlowroutenumbersandmessagingClient,
)

print("Number/Route Management v2 & Messaging v2.1 Demo")


# Use configuration.py for user-dependent variables.
basic_auth_user_name = Configuration().basic_auth_user_name
basic_auth_password = Configuration().basic_auth_password

# If testing SMS functionality, fill in the following variables
test_from_number = None
test_to_number = None


# Instantiate API client and create controllers for Numbers, Messages, and Routes.
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)
numbers_controller = client.numbers
routes_controller = client.routes
messages_controller = client.messages


# Use the numbers controller to list available area codes currently in inventory.
print("--List Available Area Codes")
max_setup_cost = 3.25
limit = 3
offset = None
result = numbers_controller.list_available_area_codes(limit, offset, max_setup_cost)
pprint.pprint(result)


# Use the numbers controller to list numbers in the specified area code that are currently in inventory.
print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 206
result = numbers_controller.list_available_exchange_codes(
    limit, offset, max_setup_cost, areacode
)
pprint.pprint(result)


# Search for vanity and/or local numbers in numbers currently in inventory.
print("--Search for Purchasable Phone Numbers")
starts_with = 1
contains = 0
ends_with = "007"
limit = 3
offset = None
rate_center = None
state = None
print("Searching for vanity numbers with the specified patterns")
result = numbers_controller.search_for_purchasable_phone_numbers(
    starts_with, contains, ends_with, limit, offset, rate_center, state
)
pprint.pprint(result)


# Use the numbers controller to purchase a phone number from inventory.
print("--Purchase a Phone Number")
"""
Uncomment the result line below to allow the demo script to purchase the first number returned by the query above.
If you are not running the number search above, please specify
a purchasable_number before running the purchase a number request.
"""
purchasable_number = result["data"][0]["id"]
if purchasable_number is None:
    print(
        "Please assign purchasable_number to an available number you wish to purchase"
    )
else:
    print("Uncomment the result line below to allow the demo to purchase a number")
    # result = numbers_controller.purchase_a_phone_number(purchasable_number)


# Use the numbers controller to list phone numbers currently on your account
print("--List Account Phone Numbers")
starts_with = 1
ends_with = None
contains = None
limit = 5
offset = None
result = numbers_controller.list_account_phone_numbers(
    starts_with, ends_with, contains, limit, offset
)
pprint.pprint(result)


# Use the numbers controller to list the details for a number on your account.
print("--List Phone Number Details")
# You can only get details for a number currently on your account.
number_id = result["data"][0]["id"]
if number_id is None:
    print("Please assign number_id to a number to get details for")
else:
    result = numbers_controller.list_phone_number_details(number_id)
    pprint.pprint(result)


# Use the numbers controller to create an inbound route.
# Each inbound route created has a unique id, even if the route is identical.
print("---Create an Inbound Route")


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # Function to generate six-character random string.
    # If you attempt to create a route already on your account you will receive a 403 error.
    return "".join(random.choice(chars) for _ in range(size))


new_route = id_generator() + ".sonsofodin.com"
alias = id_generator()
for i in range(10):
    alias += str(i)

# request_body is what a JSON body looks like!
request_body = {
  "data": {
    "type": "route",
    "attributes": {
      "route_type": "host",
      "value": new_route,
      "alias": alias,
    }
  }
}

result = routes_controller.create_an_inbound_route(request_body)
pprint.pprint(result)


# Use the numbers controller to list inbound routes currently on your account.
print("---List Inbound Routes")
limit = 3
result = routes_controller.list_inbound_routes(limit)
pprint.pprint(result)

# assigns your primary_inbound_route_id variable to be the [0] first result from the querey above.
# The first result will always be sip-reg with a route id of 0.
primary_inbound_route_id = result["data"][0]["id"]
if primary_inbound_route_id is None:
    print("Please assign a primary_inbound_route_id")

# assigns the failover_route_id variable to be the [1] second result from the querey above.
failover_route_id = result["data"][1]["id"]
if failover_route_id is None:
    print("Please assign a failover_route_id")


# Use the routes controller to assign a primary route to a number currently on your account.
# create the primary route JSON request:
request_body = {
  "data": {
    "type": "route",
    "id": str(primary_inbound_route_id),
  }
}

# update the route!
print("---Update Primary Voice Route")
result = routes_controller.update_primary_voice_route(number_id, request_body)
if result is None:
    print("204: No Content")
else:
    print(result)


# Use the routes controller to assign a failover route to a number currently on your account.
# create the failover route JSON request:
request_body = {
  "data": {
    "type": "route",
    "id": str(failover_route_id),
  }
}

# update the route!
print("---Update Failover Voice Route")
result = routes_controller.update_failover_voice_route(number_id, request_body)
if result is None:
    print("204: No Content")
else:
    print(result)


if test_to_number and test_from_number:
    # Use the messaging controller to send a MMS message using a number currently on your account.
    # Create the JSON request:
    request_body = {
      "data": {
        "type": "message",
        "attributes": {
          "to": str(test_to_number),
          "from": str(test_from_number),
          "body": "greetings hooman!!",
          "is_mms": "true",
          "media_urls": ["http://s3.amazonaws.com/barkpost-assets/50+GIFs/37.gif"]
        }
      }
    }

    # send the message!
    print("---Send A Message")
    result = messages_controller.send_a_message(request_body)
    pprint.pprint(result)


# Use the messages controller to look up the MDRs for a set of messages.
print("---Look Up A Set Of Messages")
start_date = "2018-12-01"
end_date = "2021-01-08"
limit = 2
result = messages_controller.look_up_a_set_of_messages(start_date, end_date, limit)
pprint.pprint(result)


# Use the messages controller to look up the report for an MDR.
print("---Look Up A Message Detail Record")
message_id = result["data"][0]["id"]
if message_id is None:
    print(
        "You need to have sent a message within the specified date range to get its MDR."
    )
result = messages_controller.look_up_a_message_detail_record(message_id)
pprint.pprint(result)
