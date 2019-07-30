# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.cdrs_controller

"""

from csv import DictReader
import gzip
import json
import StringIO
import urllib2

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from .numbers_controller import NumbersController
from ..exceptions.api_exception import APIException

class CDRsController(BaseController):

    """A Controller to access Endpoints in the CDR API."""

    def list_cdrs(self,
                   limit=None,
                   offset=None,
                   status=None):
        """Does a GET request to /v2/cdrs/exports.

        Returns a list of all CDR Exports created by the user.

        Args:
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of CDR exports by your
                specified value. For example, if you have 4 CDR exports and
                you entered 1 as your offset value, then only 3 of your
                CDR exports will be displayed in the response.
            status: Display only requests whose status matches the specified
                value. Possible values are processing, completed or failed

        Returns:
            mixed: Response from the API. A JSON object of CDR Export Records
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cdrs/exports'
        _query_parameters = {
            'limit': limit,
            'offset': offset
        }
        if status is not None:
            _query_parameters['status'] = status

        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters,
            Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def get_cdr_export_status(self, cdrexport_id):
        """Does a GET request to /v2/cdrs/exports/<cdrexport_id>.

        Returns a record detail for the CDR Export Record Id specified

        Args:
            cdrexport_id (int, required): The ID of the CDR Export to retrieve

        Returns:
            mixed: Response from the API. A JSON object of of an CDR Export record
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cdrs/exports/{}'.format(cdrexport_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def create_cdr_export(self, filters, callback_url=None):
        """Does a POST request to /v2/cdrs/export.

        Searches for CDR Records that match the criteria

        Args:
            filters (dictionary, required): The dictionary of filter parameters
               https://developer.flowroute.com/api/cdrexports/v2.0/query-cdrs/
            callback_url (string, optional): A string to use as a URI for sending
               callback events

        Returns:
            mixed: Response from the API. A JSON object of of a CNAM record
                with the new data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        body = {
            "data": {
                "type": "cdrexport",
                "attributes": {
                    "filter_parameters": filters
                }
            }
        }

        if callback_url is not None:
            body['data']['attributes']['callback_url'] = callback_url
        json_body = json.dumps(body)

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cdrs/exports'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=json_body)
        return self.handle_request_and_response(_request)


    def download_cdr_export(self, cdrexport_id, filename):
        """Does a GET request to /v2/cdrs/exports/<cdrexport_id>.

        Returns the filename that was written

        Args:
            cdrexport_id (int, required): The ID of the CDR Export to retrieve
            filename (string, required):  The filename to write the CDR Export data

        Returns:
            mixed: Response from the API and filename

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cdrs/exports/{}'.format(cdrexport_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        _response = self.handle_request_and_response(_request)
 
        if (_response.get('data') and _response['data'].get('attributes') and _response['data']['attributes'].get('download_url')):
            print("fetching {}".format(_response['data']['attributes']['download_url']))
            export_url = _response['data']['attributes']['download_url']
            #urllib.urlretrieve(export_url, filename)
            try:
                response = urllib2.urlopen(export_url)
                compressedFile = StringIO.StringIO(response.read())
                decompressedFile = gzip.GzipFile(fileobj=compressedFile)
                with open(filename, 'w') as outfile:
                    outfile.write(decompressedFile.read())
                return {'filename': filename}
            except Exception as e:
                raise APIException("Error fetching CDR Export data {}".format(e),
                    _response.context)


    def parse_cdr_export(self, filename):
        """Parses a CDR export file and returns a dictionary


        Args:
            filename (string, required):  The filename to write the CDR Export data

        Returns:
            mixed: dictionary of file contents

        Raises:
            Exception: When an error occurs parsing data

        """

        try:
            with open(filename, 'r') as infile:
                fileinfo = DictReader(infile)
                return list(fileinfo)
        except Exception as e:
            raise Exception("Error parsing CDR Export data {}".format(e))