#!/usr/bin/env python
import pprint
import os
import random
import string
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient


# Helper function for random strings
def random_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')

# Instantiate API client and create controllers for Numbers and E911s
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)
numbers_controller = client.numbers
cnams_controller = client.cnams
cnam_id = None
'''
print("--List CNAM Records")
limit = 10
offset = None
result = cnams_controller.list_cnams(limit, offset)
pprint.pprint(result)

print("\n--List Approved CNAM Records")
result = cnams_controller.list_cnams(limit, offset, is_approved=True)
pprint.pprint(result)
if len(result['data']):
    cnam_id = result['data'][0]['id']

    print("\n--List CNAM Detail")
    result = cnams_controller.get_cnam(cnam_id)
    pprint.pprint(result)
    if len(result['data']):
        cnam_id = result['data'][0]['id']
'''
print("\n--Search for CNAM Record")
result = cnams_controller.search_cnams(contains='CHRIS')
pprint.pprint(result)
'''
print("\n--Create a CNAM Record")
cnam_value = 'FR ' + random_generator()
result = cnams_controller.create_cnam_record(cnam_value)
pprint.pprint(result)
print("\nNOTE: Newly created CNAM records need to be approved first before they can be associated with your long code number.")

print("\n--Associate a CNAM Record to a DID")
our_numbers = numbers_controller.list_account_phone_numbers()
did_id = our_numbers['data'][0]['id']

if cnam_id is None:
    print("Create some CNAM records and wait for approval before trying"
          " to associate them with a DID")
else:
    result = cnams_controller.associate_cnam(cnam_id, did_id)
    pprint.pprint(result)

    print("\n--Unassociate a CNAM Record from a DID")
    result = cnams_controller.unassociate_cnam(did_id)
    pprint.pprint(result)

    print("\n--Remove a CNAM Record from your account")
    result = cnams_controller.remove_cnam(cnam_id)
    pprint.pprint(result)
'''    
