# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV5Network(object):
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
        'type': 'str',
        'ip': 'str',
        'ipv6': 'str'
    }

    attribute_map = {
        'type': 'type',
        'ip': 'ip',
        'ipv6': 'ipv6'
    }

    def __init__(self, type=None, ip=None, ipv6=None):  # noqa: E501
        """SystemInitSpecV5Network - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._ip = None
        self._ipv6 = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if ip is not None:
            self.ip = ip
        if ipv6 is not None:
            self.ipv6 = ipv6

    @property
    def type(self):
        """Gets the type of this SystemInitSpecV5Network.  # noqa: E501

        The type of component. Supported values include Management, vSAN, Witness, and vMotion.  # noqa: E501

        :return: The type of this SystemInitSpecV5Network.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInitSpecV5Network.

        The type of component. Supported values include Management, vSAN, Witness, and vMotion.  # noqa: E501

        :param type: The type of this SystemInitSpecV5Network.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ip(self):
        """Gets the ip of this SystemInitSpecV5Network.  # noqa: E501

        The IP address of component  # noqa: E501

        :return: The ip of this SystemInitSpecV5Network.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SystemInitSpecV5Network.

        The IP address of component  # noqa: E501

        :param ip: The ip of this SystemInitSpecV5Network.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ipv6(self):
        """Gets the ipv6 of this SystemInitSpecV5Network.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The ipv6 of this SystemInitSpecV5Network.  # noqa: E501
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this SystemInitSpecV5Network.

        Internal use only  # noqa: E501

        :param ipv6: The ipv6 of this SystemInitSpecV5Network.  # noqa: E501
        :type: str
        """

        self._ipv6 = ipv6

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
        if issubclass(SystemInitSpecV5Network, dict):
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
        if not isinstance(other, SystemInitSpecV5Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
