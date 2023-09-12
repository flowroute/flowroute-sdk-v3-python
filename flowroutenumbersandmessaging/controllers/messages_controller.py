# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.messages_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.mdr_2 import MDR2
import json


class MessagesController(BaseController):

    """A Controller to access Endpoints in the
    flowroutenumbersandmessaging API."""

    def look_up_a_set_of_messages(self,
                                  start_date,
                                  end_date=None,
                                  limit=None,
                                  offset=None):
        """Does a GET request to /v2.1/messages.

        Retrieves a list of Message Detail Records (MDRs) within a specified
        date range. Date and time is based on Coordinated Universal Time
        (UTC).

        Args:
            start_date (datetime): The beginning date and time, in UTC, on
                which to perform an MDR search. The DateTime can be formatted
                as YYYY-MM-DDor YYYY-MM-DDTHH:mm:ss.SSZ.
            end_date (datetime, optional): The ending date and time, in UTC,
                on which to perform an MDR search. The DateTime can be
                formatted as YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss.SSZ.
            limit (int, optional): The number of MDRs to retrieve at one time.
                You can set as high of a number as you want, but the number
                cannot be negative and must be greater than 0 (zero).
            offset (int, optional): The number of MDRs to skip when performing
                a query. The number must be 0 (zero) or greater, but cannot be
                negative.

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        parsed_end_date = None

        if end_date is not None:
            parsed_end_date = APIHelper.RFC3339DateTime(end_date)

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages'
        _query_parameters = {
            'start_date': APIHelper.RFC3339DateTime(start_date),
            'end_date': parsed_end_date,
            'limit': limit,
            'offset': offset
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters,
            Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def look_up_a_message_detail_record(self,
                                            id):
        """Does a GET request to /v2.1/messages/{id}.

        Searches for a specific message record ID and returns a Message Detail
        Record (in MDR2 format).

        Args:
            id (string): The unique message detail record identifier (MDR ID)
                of any message. When entering the MDR ID, the number should
                include the mdr2- preface.

        Returns:
            MDR2: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(
            _query_builder, {
                'id': id
            })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def send_a_message(self, body):
        """Does a POST request to /v2.1/messages.

        Sends an SMS or MMS from a Flowroute long code or toll-free phone
        number to another valid phone number.

        Args:
            body (Message): The SMS or MMS message to send.

        Returns:
            mixed: Response from the API. ACCEPTED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json',
            'content-type': 'application/vnd.api+json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url,
                                         headers=_headers,
                                         parameters=APIHelper.json_serialize(body))

        return self.handle_request_and_response(_request)

    def set_account_level_sms_callback(self, url):
        """Does a PUT request to /v2.1/messages/sms_callback.

        Sets the callback url for all sms messages.

        Args:
            url (string): The callback url to be hit.

        Returns:
            mixed: Response from the API. ACCEPTED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages/sms_callback'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json',
            'content-type': 'application/vnd.api+json; charset=utf-8'
        }

        body = {
            'data': {
                'attributes': {
                    'callback_url': url
                }
            }
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url,
                                        headers=_headers,
                                        parameters=APIHelper.json_serialize(body))

        return self.handle_request_and_response(_request)

    def set_account_level_mms_callback(self, url):
        """Does a PUT request to /v2.1/messages/mms_callback.

        Sets the callback url for all mms messages.

        Args:
            url (string): The callback url to be hit.

        Returns:
            mixed: Response from the API. ACCEPTED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages/mms_callback'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json',
            'content-type': 'application/vnd.api+json; charset=utf-8'
        }

        body = {
            'data': {
                'attributes': {
                    'callback_url': url
                }
            }
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url,
                                        headers=_headers,
                                        parameters=APIHelper.json_serialize(
                                             body))

        return self.handle_request_and_response(_request)

    def set_account_level_dlr_callback(self, url):
        """Does a PUT request to /v2.1/messages/dlr_callback.

        Sets the callback url for all delivery receipts (dlrs)

        Args:
            url (string): The callback url to be hit.

        Returns:
            mixed: Response from the API. ACCEPTED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2.1/messages/dlr_callback'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json',
            'content-type': 'application/vnd.api+json; charset=utf-8'
        }

        body = {
            'data': {
                'attributes': {
                    'callback_url': url
                }
            }
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url,
                                        headers=_headers,
                                        parameters=APIHelper.json_serialize(
                                             body))

        return self.handle_request_and_response(_request)

    def set_did_level_dlr_callback(self, number_id, dlr_url):
        """Does a POST request to /v2/numbers/number_id/relationships/dlr_callback

        Sets the callback url for all delivery receipts (dlrs) for the
            specified did

        Args:
            number_id (integer): pk of the DID record
            url (string): The callback url to be hit.

        Returns:
            mixed: Response from the API. ACCEPTED

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/dlr_callback'.format(number_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json',
            'content-type': 'application/vnd.api+json; charset=utf-8'
        }

        body = {
            'data': {
                'attributes': {
                    'callback_url': dlr_url
                }
            }
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url,
                                         headers=_headers,
                                         parameters=APIHelper.json_serialize(
                                             body))

        return self.handle_request_and_response(_request)