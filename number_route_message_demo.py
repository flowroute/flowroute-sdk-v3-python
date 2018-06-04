#!/usr/bin/env python
import datetime
import pprint
import random
import string
from flowroutenumbersandmessaging.configuration import Configuration
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import \
    FlowroutenumbersandmessagingClient
from dateutil.relativedelta import relativedelta

print("Number/Route Management v2 & Messaging v2.1 Demo")

# Set up your api credentials and test mobile number for outbound SMS or MMS
# basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
# basic_auth_password = os.environ.get('FR_SECRET_KEY')
mobile_number = "YOUR MOBILE NUMBER HERE"


# Instantiate API client and create controllers for Numbers,
# Messages, and Routes
client = FlowroutenumbersandmessagingClient(Configuration.basic_auth_user_name,
                                            Configuration.basic_auth_password)
numbers_controller = client.numbers
routes_controller = client.routes
messages_controller = client.messages
porting_controller = client.porting

# --------------------- Numbering -----------------------------------------

print("--List Available Area Codes, specifying a maximum setup cost.")
max_setup_cost = 3.25
limit = 3
offset = None
result = numbers_controller.list_available_area_codes(limit,
                                                      offset,
                                                      max_setup_cost)
pprint.pprint(result)

print("--List Available Exchange Codes")
limit = 3
offset = None
max_setup_cost = None
areacode = 347
result = numbers_controller.list_available_exchange_codes(limit,
                                                          offset,
                                                          max_setup_cost,
                                                          areacode)
pprint.pprint(result)

print("--Search for Purchasable Phone Numbers")
starts_with = 206
contains = 3
ends_with = None
limit = 3
offset = None
rate_center = None
state = None
result = numbers_controller.search_for_purchasable_phone_numbers(starts_with,
                                                                 contains,
                                                                 ends_with,
                                                                 limit,
                                                                 offset,
                                                                 rate_center,
                                                                 state)
pprint.pprint(result)

purchasable_number = None
if len(result['data']):
    print("--Purchase a Phone Number")
    print("NOTE: This demo has been disabled as it pulls credit from your account")
    # purchasable_number = result['data'][0]['id']
    # result = numbers_controller.purchase_a_phone_number(purchasable_number)
    # pprint.pprint(result)

print("--List Account Phone Numbers")
starts_with = None
ends_with = None
contains = None
limit = 3
offset = None
result = numbers_controller.list_account_phone_numbers(starts_with, ends_with,
                                                       contains, limit, offset)
pprint.pprint(result)

print("--List Phone Number Details")
number_id = result['data'][0]['id']
result = numbers_controller.list_phone_number_details(number_id)
pprint.pprint(result)

if purchasable_number is not None:
    print("--Release a DID")
    result = numbers_controller.release_a_did(purchasable_number)
    pprint.pprint(result)

print("--Update an Alias for a DID")
result = numbers_controller.set_did_alias(number_id, "New Test")
pprint.pprint(result)
result = numbers_controller.list_phone_number_details(number_id)
pprint.pprint(result)

print("--Set a callback for a DID")
result = numbers_controller.set_did_callback(number_id,
                                             'http://www.example.com/test')
pprint.pprint(result)

# --------------------- Routes -----------------------------------------

print("---List all available edge strategies")
result = routes_controller.list_edge_strategies()
pprint.pprint(result)


# Function to generate six-charac random string
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print("---Create an Inbound Route")
new_route = '{}.sonsofodin.com'.format(id_generator())
alias = id_generator()
for i in range(10): 
    alias += str(i)
request_body = '{ \
  "data": { \
    "type": "route", \
    "attributes": { \
      "route_type": "host", \
      "value": "' + new_route + '", \
      "alias": "' + alias + '", \
      "edge_strategy": "1" \
    } \
  } \
}'
result = routes_controller.create_an_inbound_route(request_body)
pprint.pprint(result)

print ("---List Inbound Routes")
limit = 10
result = routes_controller.list_inbound_routes(limit)
pprint.pprint(result)

primary_routeid = result['data'][1]['id']
secondary_routeid = result['data'][2]['id']

request_body = '{ \
  "data": { \
    "type": "route", \
    "id": "' + str(primary_routeid) + '" \
  } \
}'

print("---Update Primary Voice Route")
result = routes_controller.update_primary_voice_route(number_id, request_body)
if result is None:
    print("204: No Content")
else:
    print (result)

request_body = '{ \
  "data": { \
    "type": "route", \
    "id": "' + str(secondary_routeid) + '" \
  } \
}'

print("---Update Failover Voice Route")
result = routes_controller.update_failover_voice_route(number_id, request_body)
if result is None:
    print("204: No Content")
else:
    print (result)

# --------------------- Messaging -----------------------------------------

body = "Hello there how are you?"

request_body = '{ \
  "data": { \
    "type": "message", \
    "attributes": { \
      "to": "' + str(mobile_number) + '", \
      "from": "' + str(number_id) + '", \
      "body": "' + str(body) + '", \
      "is_mms": "false" \
    } \
  } \
}'

request_body_mms = '{ \
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

request_body_with_dlr = '{ \
  "data": { \
    "type": "message", \
    "attributes": { \
      "to": "' + str(mobile_number) + '", \
      "from": "' + str(number_id) + '", \
      "body": "' + str(body) + '", \
      "is_mms": "false", \
      "dlr_callback": "http://httpbin.org/status/:code" \
    } \
  } \
}'

print("---Send an SMS Message")
result = messages_controller.send_a_message(request_body)
pprint.pprint(result)

print("---Send an MMS Message")
result = messages_controller.send_a_message(request_body_mms)
pprint.pprint(result)

print("---Send A Message with a DLR")
sms_url = 'http://example.com/sms/special'
result = messages_controller.send_a_message(request_body_with_dlr)
pprint.pprint(result)

print("---Look Up A Set Of Messages")
start_date = datetime.datetime.now() - relativedelta(days=30)
end_date = datetime.datetime.now()

start_date_string = start_date.strftime("%Y-%m-%d")
end_date_string = end_date.strftime("%Y-%m-%d")

limit = 10
result = messages_controller.look_up_a_set_of_messages(start_date_string,
                                                       end_date_string,
                                                       limit)
pprint.pprint(result)

print ("\n---Look Up A Message Detail Record")
message_id = result['data'][0]['id']
result = messages_controller.look_up_a_message_detail_record(message_id)
pprint.pprint(result)

print("\n---Set an Account Level SMS Callback URL")
sms_url = 'http://example.com/sms'
result = messages_controller.set_account_level_sms_callback(sms_url)
pprint.pprint(result)

print("\n---Set an Account Level MMS Callback URL")
mms_url = 'http://example.com/mms'
result = messages_controller.set_account_level_mms_callback(mms_url)
pprint.pprint(result)

print("\n---Set an Account Level DLR Callback URL")
dlr_url = 'http://example.com/dlr'
result = messages_controller.set_account_level_dlr_callback(dlr_url)
pprint.pprint(result)

print("\n---Set a DID Level DLR Callback URL")
dlr_url = 'http://example.com/did/dlr'
result = messages_controller.set_did_level_dlr_callback(number_id, dlr_url)
pprint.pprint(result)

# --------------------- Porting -----------------------------------------

print("\n---Check Number Portability")
numbers = ['14254664444', '18827833439']
result = porting_controller.checkPortability(numbers)
pprint.pprint(result)
