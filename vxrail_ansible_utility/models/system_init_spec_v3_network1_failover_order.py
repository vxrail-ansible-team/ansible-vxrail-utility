# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SystemInitSpecV3Network1FailoverOrder(object):
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
        'active': 'list[str]',
        'standby': 'list[str]'
    }

    attribute_map = {
        'active': 'active',
        'standby': 'standby'
    }

    def __init__(self, active=None, standby=None):  # noqa: E501
        """SystemInitSpecV3Network1FailoverOrder - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._standby = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if standby is not None:
            self.standby = standby

    @property
    def active(self):
        """Gets the active of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501

        A list of active uplinks  # noqa: E501

        :return: The active of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501
        :rtype: list[str]
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SystemInitSpecV3Network1FailoverOrder.

        A list of active uplinks  # noqa: E501

        :param active: The active of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501
        :type: list[str]
        """

        self._active = active

    @property
    def standby(self):
        """Gets the standby of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501

        A list of standby uplinks  # noqa: E501

        :return: The standby of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501
        :rtype: list[str]
        """
        return self._standby

    @standby.setter
    def standby(self, standby):
        """Sets the standby of this SystemInitSpecV3Network1FailoverOrder.

        A list of standby uplinks  # noqa: E501

        :param standby: The standby of this SystemInitSpecV3Network1FailoverOrder.  # noqa: E501
        :type: list[str]
        """

        self._standby = standby

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
        if issubclass(SystemInitSpecV3Network1FailoverOrder, dict):
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
        if not isinstance(other, SystemInitSpecV3Network1FailoverOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
