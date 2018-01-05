# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.numbers_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.number_26 import Number26
from ..exceptions.error_exception import ErrorException
from ..exceptions.api_exception import APIException

class NumbersController(BaseController):

    """A Controller to access Endpoints in the flowroutenumbersandmessaging API."""


    def list_available_exchange_codes(self,
                                      limit=None,
                                      offset=None,
                                      max_setup_cost=None,
                                      areacode=None):
        """Does a GET request to /v2/numbers/available/exchanges.

        Returns a list of all Central Office (exchange) codes containing
        purchasable phone numbers.

        Args:
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.
            max_setup_cost (float, optional): Restricts the results to the
                specified maximum non-recurring setup cost.
            areacode (int, optional): Restricts the results to the specified
                area code.

        Returns:
            mixed: Response from the API. A JSON object of Central Office (exchange) codes containing
                    purchasable phone numbers that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/available/exchanges'
        _query_parameters = {
            'limit': limit,
            'offset': offset,
            'max_setup_cost': max_setup_cost,
            'areacode': areacode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def list_available_area_codes(self,
                                  limit=None,
                                  offset=None,
                                  max_setup_cost=None):
        """Does a GET request to /v2/numbers/available/areacodes.

        Returns a list of all Numbering Plan Area (NPA) codes containing
        purchasable phone numbers.

        Args:
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 400 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.
            max_setup_cost (float, optional): Restricts the results to the
                specified maximum non-recurring setup cost.

        Returns:
            mixed: Response from the API. A JSON object of area codes containing
                    purchasable phone numbers that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/available/areacodes'
        _query_parameters = {
            'limit': limit,
            'offset': offset,
            'max_setup_cost': max_setup_cost
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Invalid Query', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def search_for_purchasable_phone_numbers(self,
                                             starts_with=None,
                                             contains=None,
                                             ends_with=None,
                                             limit=None,
                                             offset=None,
                                             rate_center=None,
                                             state=None):
        """Does a GET request to /v2/numbers/available.

        This endpoint lets you search for phone numbers by state or rate
        center, or by your specified search value.

        Args:
            starts_with (int, optional): Retrieve phone numbers that start
                with the specified value.
            contains (int, optional): Retrieve phone numbers containing the
                specified value.
            ends_with (int, optional): Retrieve phone numbers that end with
                the specified value.
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.
            rate_center (string, optional): Filters by and displays phone
                numbers in the specified rate center.
            state (string, optional): Filters by and displays phone numbers in
                the specified state. Optional unless a ratecenter is
                specified.

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/available'
        _query_parameters = {
            'starts_with': starts_with,
            'contains': contains,
            'ends_with': ends_with,
            'limit': limit,
            'offset': offset,
            'rate_center': rate_center,
            'state': state
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def list_account_phone_numbers(self,
                                  starts_with=None,
                                  ends_with=None,
                                  contains=None,
                                  limit=None,
                                  offset=None):
        """Does a GET request to /v2/numbers.

        Returns a list of all phone numbers currently on your Flowroute
        account. The response includes details such as the phone number's rate
        center, state, number type, and whether CNAM Lookup is enabled for
        that number.

        Args:
            starts_with (int, optional): Retrieves phone numbers that start
                with the specified value.
            ends_with (int, optional): Retrieves phone numbers that end with
                the specified value.
            contains (int, optional): Retrieves phone numbers containing the
                specified value.
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.

        Returns:
            mixed: Response from the API. A JSON object of phone numbers in
                your account

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers'
        _query_parameters = {
            'starts_with': starts_with,
            'ends_with': ends_with,
            'contains': contains,
            'limit': limit,
            'offset': offset
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def purchase_a_phone_number(self,
                                       id):
        """Does a POST request to /v2/numbers/{id}.

        Lets you purchase a phone number from available Flowroute inventory.

        Args:
            id (int): Phone number to purchase. Must be in 11-digit E.164
                format; e.g. 12061231234.

        Returns:
            Number26: Response from the API. CREATED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def list_phone_number_details(self,
                                 id):
        """Does a GET request to /v2/numbers/{id}.

        Lists all of the information associated with any of the phone numbers
        in your account, including billing method, primary voice route, and
        failover voice route.

        Args:
            id (int): Phone number to search for which must be a number that
                you own. Must be in 11-digit E.164 format; e.g. 12061231234.

        Returns:
            Number26: Response from the API. A JSON object of phone numbers in
                your account

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized', _context)
        elif _context.response.status_code == 404:
            raise APIException('Not Found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
