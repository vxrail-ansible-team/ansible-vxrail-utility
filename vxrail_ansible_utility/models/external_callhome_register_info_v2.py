# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExternalCallhomeRegisterInfoV2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'site_id': 'str',
        'address_list': 'list[Address]'
    }

    attribute_map = {
        'site_id': 'site_id',
        'address_list': 'address_list'
    }

    def __init__(self, site_id=None, address_list=None):  # noqa: E501
        """ExternalCallhomeRegisterInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._address_list = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        if address_list is not None:
            self.address_list = address_list

    @property
    def site_id(self):
        """Gets the site_id of this ExternalCallhomeRegisterInfoV2.  # noqa: E501


        :return: The site_id of this ExternalCallhomeRegisterInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ExternalCallhomeRegisterInfoV2.


        :param site_id: The site_id of this ExternalCallhomeRegisterInfoV2.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def address_list(self):
        """Gets the address_list of this ExternalCallhomeRegisterInfoV2.  # noqa: E501


        :return: The address_list of this ExternalCallhomeRegisterInfoV2.  # noqa: E501
        :rtype: list[Address]
        """
        return self._address_list

    @address_list.setter
    def address_list(self, address_list):
        """Sets the address_list of this ExternalCallhomeRegisterInfoV2.


        :param address_list: The address_list of this ExternalCallhomeRegisterInfoV2.  # noqa: E501
        :type: list[Address]
        """

        self._address_list = address_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ExternalCallhomeRegisterInfoV2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalCallhomeRegisterInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other