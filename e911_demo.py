#!/usr/bin/env python
import pprint
import os
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient

# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')

# Instantiate API client and create controllers for Numbers and E911s
client = FlowroutenumbersandmessagingClient(basic_auth_user_name,
                                            basic_auth_password)
numbers_controller = client.numbers
e911s_controller = client.e911s


print("--List E911 Records")
limit = 10
offset = None
result = e911s_controller.list_e911s(limit, offset)
pprint.pprint(result)

e911_id = None
# If the user has any E911 records, pull one up
for e in result['data']:
    e911_id = e['id']
    break

if e911_id:
    print("\n--Get Details for a specific E911 Record")
    result = e911s_controller.get_e911(e911_id)
    pprint.pprint(result)

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
                                               country="US",
                                               zipcode="98101")
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)

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

print("\n--List all DIDs associated with an E911 Record")
result = e911s_controller.list_dids_for_e911(e911_id)
pprint.pprint(result)

# Dis-Associate them
try:
    print("\n--Un-associate the address")
    result = e911s_controller.disconnect(did)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)

try:
    print("\n--Delete an E911 Address")
    result = e911s_controller.delete_address(e911_id)
    pprint.pprint(result)
except Exception as e:
    print(str(e))
    print(e.context.response.raw_body)
