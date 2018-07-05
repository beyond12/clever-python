# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Name(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first': 'str',
        'last': 'str',
        'middle': 'str'
    }

    attribute_map = {
        'first': 'first',
        'last': 'last',
        'middle': 'middle'
    }

    def __init__(self, first=None, last=None, middle=None):
        """
        Name - a model defined in Swagger
        """

        self._first = None
        self._last = None
        self._middle = None
        self.discriminator = None

        if first is not None:
          self.first = first
        if last is not None:
          self.last = last
        if middle is not None:
          self.middle = middle

    @property
    def first(self):
        """
        Gets the first of this Name.

        :return: The first of this Name.
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this Name.

        :param first: The first of this Name.
        :type: str
        """

        self._first = first

    @property
    def last(self):
        """
        Gets the last of this Name.

        :return: The last of this Name.
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this Name.

        :param last: The last of this Name.
        :type: str
        """

        self._last = last

    @property
    def middle(self):
        """
        Gets the middle of this Name.

        :return: The middle of this Name.
        :rtype: str
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        """
        Sets the middle of this Name.

        :param middle: The middle of this Name.
        :type: str
        """

        self._middle = middle

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Name):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other