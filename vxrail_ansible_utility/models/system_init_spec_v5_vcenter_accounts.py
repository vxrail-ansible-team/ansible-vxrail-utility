# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.350
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV5VcenterAccounts(object):
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
        'root': 'SystemInitSpecV5AccountsRoot',
        'administrator': 'SystemInitSpecV5VcenterAccountsAdministrator',
        'management': 'SystemInitSpecV5AccountsManagement'
    }

    attribute_map = {
        'root': 'root',
        'administrator': 'administrator',
        'management': 'management'
    }

    def __init__(self, root=None, administrator=None, management=None):  # noqa: E501
        """SystemInitSpecV5VcenterAccounts - a model defined in Swagger"""  # noqa: E501
        self._root = None
        self._administrator = None
        self._management = None
        self.discriminator = None
        if root is not None:
            self.root = root
        if administrator is not None:
            self.administrator = administrator
        if management is not None:
            self.management = management

    @property
    def root(self):
        """Gets the root of this SystemInitSpecV5VcenterAccounts.  # noqa: E501


        :return: The root of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :rtype: SystemInitSpecV5AccountsRoot
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this SystemInitSpecV5VcenterAccounts.


        :param root: The root of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :type: SystemInitSpecV5AccountsRoot
        """

        self._root = root

    @property
    def administrator(self):
        """Gets the administrator of this SystemInitSpecV5VcenterAccounts.  # noqa: E501


        :return: The administrator of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :rtype: SystemInitSpecV5VcenterAccountsAdministrator
        """
        return self._administrator

    @administrator.setter
    def administrator(self, administrator):
        """Sets the administrator of this SystemInitSpecV5VcenterAccounts.


        :param administrator: The administrator of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :type: SystemInitSpecV5VcenterAccountsAdministrator
        """

        self._administrator = administrator

    @property
    def management(self):
        """Gets the management of this SystemInitSpecV5VcenterAccounts.  # noqa: E501


        :return: The management of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :rtype: SystemInitSpecV5AccountsManagement
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this SystemInitSpecV5VcenterAccounts.


        :param management: The management of this SystemInitSpecV5VcenterAccounts.  # noqa: E501
        :type: SystemInitSpecV5AccountsManagement
        """

        self._management = management

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
        if issubclass(SystemInitSpecV5VcenterAccounts, dict):
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
        if not isinstance(other, SystemInitSpecV5VcenterAccounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
