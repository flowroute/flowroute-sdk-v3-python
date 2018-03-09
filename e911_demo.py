#!/usr/bin/env python
import pprint
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient

# Instantiate API client and create controllers for Numbers and E911s
client = FlowroutenumbersandmessagingClient()
numbers_controller = client.numbers
e911s_controller = client.e911s


print("--List E911 Records")
limit = 10
offset = None
result = e911s_controller.list_e911s(limit, offset)
pprint.pprint(result)

print("--Validate an Address")
result = e911s_controller.validate_address(
                                           label="Test Address",
                                           first_name="Chris",
                                           last_name="Smith",
                                           street_name="3rd Ave",
                                           street_number="1182",
                                           city="Seattle",
                                           state="WA",
                                           country="USA",
                                           zip="98101")
pprint.pprint(result)

print("--Get Details for a specific E911 Record")
result = e911s_controller.get_e911(11476)
pprint.pprint(result)

print("--Create and Validate an Address")
result = e911s_controller.create_address(
                                         label="E911 Test",
                                         first_name="Chris",
                                         last_name="Smith",
                                         street_name="3rd Ave",
                                         street_number="1182",
                                         city="Seattle",
                                         state="WA",
                                         country="USA",
                                         zip="98101")
pprint.pprint(result)

# Pull the ID from the newly created record
record_id = result['data']['id']

print("--Update an E911 Address")
result = e911s_controller.update_address(record_id, last_name='Wiley')
pprint.pprint(result)

# Get our DIDs
did_list = numbers_controller.list_account_phone_numbers()
did = did_list['data'][0]['attributes']['value']

# Get our E911s
e911_list = e911s_controller.list_e911s()
e911_id = e911_list['data'][0]['id']

# Associate them
print("--Associate an E911 Record and a DID")
result = e911s_controller.associate(e911_id, did)
pprint.pprint(result)

print("--List all DIDs associated with an E911 Record")
result = e911s_controller.list_dids_for_e911(e911_id)
pprint.pprint(result)

# Diss-Associate them
print("--Un-associate the address")
result = e911s_controller.disconnect(e911_id, did)
pprint.pprint(result)

print("--Delete an E911 Address")
result = e911s_controller.delete_address(e911_id)
pprint.pprint(result)

