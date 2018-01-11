#!/usr/bin/env python
import pprint
import os
import json
import random
import string
import requests
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
from flowroutenumbersandmessaging.models import *
from flowroutenumbersandmessaging.models.new_route import NewRoute

print("Number/Route Management v2 & Messaging v2.1 Demo")

# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')
mobile_number = "YOUR_MOBILE_NUMBER"


# Instantiate API client and create controllers for Numbers, Messages, and Routes
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)
numbers_controller = client.numbers
routes_controller = client.routes
messages_controller = client.messages

print("--List Available Area Codes")
max_setup_cost = 3.25
limit = 3
offset = None
result = numbers_controller.list_available_area_codes(limit, offset, max_setup_cost)
pprint.pprint(result)

print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 347
result = numbers_controller.list_available_exchange_codes(limit, offset, max_setup_cost, areacode)
pprint.pprint(result)

print("--Search for Purchasable Phone Numbers")
starts_with = 646
contains = 3
ends_with = 7
limit = 3
offset = None
rate_center = None
state = None
result = numbers_controller.search_for_purchasable_phone_numbers(starts_with, contains, ends_with, limit, offset, rate_center, state)
pprint.pprint(result)

print("--Purchase a Phone Number")
purchasable_number = result['data'][0]['id']
#result = numbers_controller.purchase_a_phone_number(purchasable_number)

print("--List Account Phone Numbers")
starts_with = 201
ends_with = None
contains = None
limit = 3
offset = None
result = numbers_controller.list_account_phone_numbers(starts_with, ends_with, contains, limit, offset)
pprint.pprint(result)


print("--List Phone Number Details")
number_id = result['data'][0]['id']
result = numbers_controller.list_phone_number_details(number_id)
pprint.pprint(result)

print ("---Create an Inbound Route")
# Function to generate six-charac random string
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
new_route = id_generator() + '.sonsofodin.com'
alias = id_generator()
for i in range(10): 
    alias += str(i)
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
pprint.pprint(result)

print ("---List Inbound Routes")
limit = 3
result = routes_controller.list_inbound_routes(limit)
pprint.pprint(result)


prirouteid = result['data'][1]['id']
secrouteid = result['data'][2]['id']
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
#result = messages_controller.send_a_message(request_body)
#pprint.pprint(result)

print ("---Look Up A Set Of Messages")
start_date = "2017-12-01"
end_date = "2018-01-08"
limit = 2
result = messages_controller.look_up_a_set_of_messages(start_date, end_date, limit)
pprint.pprint(result)

print ("---Look Up A Message Detail Record")
message_id = result['data'][0]['id']
result = messages_controller.look_up_a_message_detail_record(message_id)
pprint.pprint(result)


