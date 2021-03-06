# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.models.attributes

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from flowroutenumbersandmessaging.api_helper import APIHelper
import flowroutenumbersandmessaging.models.delivery_receipt

class Attributes(object):

    """Implementation of the 'Attributes' model.

    TODO: type model description here.

    Attributes:
        amount_display (float): TODO: type description here.
        amount_nanodollars (float): TODO: type description here.
        body (string): TODO: type description here.
        delivery_receipts (list of DeliveryReceipt): TODO: type description
            here.
        direction (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        is_mms (bool): TODO: type description here.
        message_encoding (int): TODO: type description here.
        message_type (MessageTypeEnum): TODO: type description here.
        status (string): TODO: type description here.
        timestamp (datetime): TODO: type description here.
        to (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_display" : "amount_display",
        "amount_nanodollars" : "amount_nanodollars",
        "body" : "body",
        "delivery_receipts" : "delivery_receipts",
        "direction" : "direction",
        "mfrom" : "from",
        "is_mms" : "is_mms",
        "message_encoding" : "message_encoding",
        "message_type" : "message_type",
        "status" : "status",
        "timestamp" : "timestamp",
        "to" : "to"
    }

    def __init__(self,
                 amount_display=None,
                 amount_nanodollars=None,
                 body=None,
                 delivery_receipts=None,
                 direction=None,
                 mfrom=None,
                 is_mms=None,
                 message_encoding=None,
                 message_type=None,
                 status=None,
                 timestamp=None,
                 to=None):
        """Constructor for the Attributes class"""

        # Initialize members of the class
        self.amount_display = amount_display
        self.amount_nanodollars = amount_nanodollars
        self.body = body
        self.delivery_receipts = delivery_receipts
        self.direction = direction
        self.mfrom = mfrom
        self.is_mms = is_mms
        self.message_encoding = message_encoding
        self.message_type = message_type
        self.status = status
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None
        self.to = to


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        amount_display = dictionary.get("amount_display")
        amount_nanodollars = dictionary.get("amount_nanodollars")
        body = dictionary.get("body")
        delivery_receipts = None
        if dictionary.get("delivery_receipts") != None:
            delivery_receipts = list()
            for structure in dictionary.get("delivery_receipts"):
                delivery_receipts.append(flowroutenumbersandmessaging.models.delivery_receipt.DeliveryReceipt.from_dictionary(structure))
        direction = dictionary.get("direction")
        mfrom = dictionary.get("from")
        is_mms = dictionary.get("is_mms")
        message_encoding = dictionary.get("message_encoding")
        message_type = dictionary.get("message_type")
        status = dictionary.get("status")
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        to = dictionary.get("to")

        # Return an object of this model
        return cls(amount_display,
                   amount_nanodollars,
                   body,
                   delivery_receipts,
                   direction,
                   mfrom,
                   is_mms,
                   message_encoding,
                   message_type,
                   status,
                   timestamp,
                   to)


