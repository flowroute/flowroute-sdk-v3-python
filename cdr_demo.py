#!/usr/bin/env python
import pprint
import os
import random
import string
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client \
    import FlowroutenumbersandmessagingClient


# Helper function for random strings
def random_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# Set up your api credentials and test mobile number for outbound SMS or MMS
basic_auth_user_name = os.environ.get('FR_ACCESS_KEY')
basic_auth_password = os.environ.get('FR_SECRET_KEY')

# Instantiate API client and create controllers for Numbers and E911s
client = FlowroutenumbersandmessagingClient(basic_auth_user_name,
                                            basic_auth_password)
numbers_controller = client.numbers
cdrs_controller = client.cdrs
cdr_id = None

print("\n--Create a CDR Export Record")
filters = {
        "start_call_start_time": "2019-01-01 00:00:00",
        "start_call_end_time": "2019-02-01 00:00:00",
        "number_aliases": ["Office 221", "Office 888"]
    }
callback_url = "https://myserver.com/cdrs"
result = cdrs_controller.create_cdr_export(filters, callback_url)
pprint.pprint(result)


print("--List CDR Records")
limit = 10
offset = None
result = cdrs_controller.list_cdrs(limit, offset)
pprint.pprint(result)

print("\n--List Completed CDR Exports")
result = cdrs_controller.list_cdrs(limit, offset, "completed")
pprint.pprint(result)
if len(result['data']):
    cdr_id = result['data'][0]['data']['id']

    print("\n--List CDR Export Detail {}".format(cdr_id))
    result = cdrs_controller.get_cdr_export_status(cdr_id)
    pprint.pprint(result)

    filename = "temp_cdr_file.csv"
    print("\n--Download CDR Export Data {} to {}".format(cdr_id, filename))

    result = cdrs_controller.download_cdr_export(cdr_id, filename)
    print("\n--Downloaded CDR Export data to {}".format(result['filename']))

    # https://developer.flowroute.com/api/cdrexports/v2.0/cdr-results/
    fileinfo = cdrs_controller.parse_cdr_export(filename)
    for row in fileinfo:
        print("{} called {} for {} starting at {}".format(
            row['callerid'], row['destination'], row['total_cost'], row['start_time'])
        )