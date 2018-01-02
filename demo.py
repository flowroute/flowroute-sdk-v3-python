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
