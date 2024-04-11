# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IdracUserUpdateSpecV2(object):
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
        'name': 'str',
        'current_password': 'str',
        'new_password': 'str',
        'privilege': 'str'
    }

    attribute_map = {
        'name': 'name',
        'current_password': 'current_password',
        'new_password': 'new_password',
        'privilege': 'privilege'
    }

    def __init__(self, name=None, current_password=None, new_password=None, privilege=None):  # noqa: E501
        """IdracUserUpdateSpecV2 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._current_password = None
        self._new_password = None
        self._privilege = None
        self.discriminator = None
        self.name = name
        self.current_password = current_password
        self.new_password = new_password
        self.privilege = privilege

    @property
    def name(self):
        """Gets the name of this IdracUserUpdateSpecV2.  # noqa: E501

        The iDRAC user name  # noqa: E501

        :return: The name of this IdracUserUpdateSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdracUserUpdateSpecV2.

        The iDRAC user name  # noqa: E501

        :param name: The name of this IdracUserUpdateSpecV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def current_password(self):
        """Gets the current_password of this IdracUserUpdateSpecV2.  # noqa: E501

        The iDRAC user current password  # noqa: E501

        :return: The current_password of this IdracUserUpdateSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this IdracUserUpdateSpecV2.

        The iDRAC user current password  # noqa: E501

        :param current_password: The current_password of this IdracUserUpdateSpecV2.  # noqa: E501
        :type: str
        """
        if current_password is None:
            raise ValueError("Invalid value for `current_password`, must not be `None`")  # noqa: E501

        self._current_password = current_password

    @property
    def new_password(self):
        """Gets the new_password of this IdracUserUpdateSpecV2.  # noqa: E501

        The iDRAC user new password  # noqa: E501

        :return: The new_password of this IdracUserUpdateSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this IdracUserUpdateSpecV2.

        The iDRAC user new password  # noqa: E501

        :param new_password: The new_password of this IdracUserUpdateSpecV2.  # noqa: E501
        :type: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

    @property
    def privilege(self):
        """Gets the privilege of this IdracUserUpdateSpecV2.  # noqa: E501

        The permissions (privilege) of the iDRAC user  # noqa: E501

        :return: The privilege of this IdracUserUpdateSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this IdracUserUpdateSpecV2.

        The permissions (privilege) of the iDRAC user  # noqa: E501

        :param privilege: The privilege of this IdracUserUpdateSpecV2.  # noqa: E501
        :type: str
        """
        if privilege is None:
            raise ValueError("Invalid value for `privilege`, must not be `None`")  # noqa: E501

        self._privilege = privilege

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
        if issubclass(IdracUserUpdateSpecV2, dict):
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
        if not isinstance(other, IdracUserUpdateSpecV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other