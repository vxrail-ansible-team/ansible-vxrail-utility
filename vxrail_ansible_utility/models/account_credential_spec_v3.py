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

class AccountCredentialSpecV3(object):
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
        'component': 'str',
        'hostname': 'str',
        'username': 'str',
        'current_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'component': 'component',
        'hostname': 'hostname',
        'username': 'username',
        'current_password': 'current_password',
        'new_password': 'new_password'
    }

    def __init__(self, component=None, hostname=None, username=None, current_password=None, new_password=None):  # noqa: E501
        """AccountCredentialSpecV3 - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._hostname = None
        self._username = None
        self._current_password = None
        self._new_password = None
        self.discriminator = None
        self.component = component
        if hostname is not None:
            self.hostname = hostname
        self.username = username
        self.current_password = current_password
        self.new_password = new_password

    @property
    def component(self):
        """Gets the component of this AccountCredentialSpecV3.  # noqa: E501

        The type of component to be updated.  # noqa: E501

        :return: The component of this AccountCredentialSpecV3.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this AccountCredentialSpecV3.

        The type of component to be updated.  # noqa: E501

        :param component: The component of this AccountCredentialSpecV3.  # noqa: E501
        :type: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")  # noqa: E501
        allowed_values = ["VC", "ESXI"]  # noqa: E501
        if component not in allowed_values:
            raise ValueError(
                "Invalid value for `component` ({0}), must be one of {1}"  # noqa: E501
                .format(component, allowed_values)
            )

        self._component = component

    @property
    def hostname(self):
        """Gets the hostname of this AccountCredentialSpecV3.  # noqa: E501

        The hostname of the vCenter or ESXi host  # noqa: E501

        :return: The hostname of this AccountCredentialSpecV3.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this AccountCredentialSpecV3.

        The hostname of the vCenter or ESXi host  # noqa: E501

        :param hostname: The hostname of this AccountCredentialSpecV3.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def username(self):
        """Gets the username of this AccountCredentialSpecV3.  # noqa: E501

        The username for the management account  # noqa: E501

        :return: The username of this AccountCredentialSpecV3.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AccountCredentialSpecV3.

        The username for the management account  # noqa: E501

        :param username: The username of this AccountCredentialSpecV3.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def current_password(self):
        """Gets the current_password of this AccountCredentialSpecV3.  # noqa: E501

        The current password for the management account stored in VxRail Manager  # noqa: E501

        :return: The current_password of this AccountCredentialSpecV3.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this AccountCredentialSpecV3.

        The current password for the management account stored in VxRail Manager  # noqa: E501

        :param current_password: The current_password of this AccountCredentialSpecV3.  # noqa: E501
        :type: str
        """
        if current_password is None:
            raise ValueError("Invalid value for `current_password`, must not be `None`")  # noqa: E501

        self._current_password = current_password

    @property
    def new_password(self):
        """Gets the new_password of this AccountCredentialSpecV3.  # noqa: E501

        The password for the management account to be stored in VxRail Manager  # noqa: E501

        :return: The new_password of this AccountCredentialSpecV3.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this AccountCredentialSpecV3.

        The password for the management account to be stored in VxRail Manager  # noqa: E501

        :param new_password: The new_password of this AccountCredentialSpecV3.  # noqa: E501
        :type: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

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
        if issubclass(AccountCredentialSpecV3, dict):
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
        if not isinstance(other, AccountCredentialSpecV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
