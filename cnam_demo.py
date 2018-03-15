#!/usr/bin/env python
import pprint
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient

# Instantiate API client and create controllers for Numbers and E911s
client = FlowroutenumbersandmessagingClient()
numbers_controller = client.numbers
cnams_controller = client.cnams


print("--List CNAM Records")
limit = 10
offset = None
result = cnams_controller.list_cnams(limit, offset)
pprint.pprint(result)


print("\n--List Approved CNAM Records")
result = cnams_controller.list_cnams(limit, offset, is_approved=True)
pprint.pprint(result)
cnam_id = result['data'][0]['id']

print("\n--List CNAM Detail")
cnam_id = result['data'][0]['id']
result = cnams_controller.get_cnam(cnam_id)
pprint.pprint(result)

print("\n--Search for CNAM Record")
result = cnams_controller.search_cnams(contains='CHRIS')
pprint.pprint(result)

# print("\n--Create a CNAM Record")
# result = cnams_controller.create_cnam_record('CJL')
# pprint.pprint(result)
# cnam_id = result['data']['id']

print("\n--Associate a CNAM Record to a DID")
result = cnams_controller.associate_cnam(cnam_id, '12066417659')
pprint.pprint(result)

print("\n--Unassociate a CNAM Record from a DID")
result = cnams_controller.unassociate_cnam('12066417659')
pprint.pprint(result)

print("\n--Remove a CNAM Record from your account")
result = cnams_controller.remove_cnam(cnam_id)
pprint.pprint(result)
