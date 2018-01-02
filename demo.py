#!/usr/bin/env python

"""
demo.py

Flowroute-numbers-python is a Python API Wrapper that provides methods for interacting with v1 (version 1)
of the Flowroute API. These methods can be used to accomplish the following:

* Search for purchasable phone numbers
* Purchase phone numbers
* View the phone numbers you own, as well as their related details
* Create a new inbound route
* Update the primary and failover route on a phone number


Copyright Flowroute, Inc.  2016

"""

import pprint
import os
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient

print("Number Control Demo")

# Setup your api credentials
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')

# Create our controller
client = FlowroutenumbersandmessagingClient(basic_auth_user_name, basic_auth_password)

numbers_controller = client.numbers

starts_with = 201
ends_with = None
contains = None
limit = 3
offset = None

print("--List Account Phone Numbers")
result = numbers_controller.get_account_phone_numbers(starts_with, ends_with, contains, limit, offset)
pprint.pprint(result)

limit = 3
offset = None
max_setup_cost = None
areacode = 347
print("--List Available Exchange Codes")
result = numbers_controller.list_available_exchange_codes(limit, offset, max_setup_cost, areacode)
pprint.pprint(result)

limit = 3
offset = None
max_setup_cost = 3.25
print("--List Available Area Codes")
result = numbers_controller.list_available_area_codes(limit, offset, max_setup_cost)
pprint.pprint(result)

starts_with = 646
contains = 3
ends_with = 7
limit = 3
offset = None
rate_center = None
state = 'WA'
print("--Search for Purchasable Phone Numbers")
result = numbers_controller.search_for_purchasable_phone_numbers(starts_with, contains, ends_with, limit, offset, rate_center, state)
pprint.pprint(result)
