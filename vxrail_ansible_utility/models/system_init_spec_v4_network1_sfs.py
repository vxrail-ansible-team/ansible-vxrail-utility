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

class SystemInitSpecV4Network1Sfs(object):
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
        'rest_user_password': 'str',
        'sfs_disabled': 'bool'
    }

    attribute_map = {
        'rest_user_password': 'REST_USER_password',
        'sfs_disabled': 'sfs_disabled'
    }

    def __init__(self, rest_user_password=None, sfs_disabled=None):  # noqa: E501
        """SystemInitSpecV4Network1Sfs - a model defined in Swagger"""  # noqa: E501
        self._rest_user_password = None
        self._sfs_disabled = None
        self.discriminator = None
        if rest_user_password is not None:
            self.rest_user_password = rest_user_password
        if sfs_disabled is not None:
            self.sfs_disabled = sfs_disabled

    @property
    def rest_user_password(self):
        """Gets the rest_user_password of this SystemInitSpecV4Network1Sfs.  # noqa: E501

        User password  # noqa: E501

        :return: The rest_user_password of this SystemInitSpecV4Network1Sfs.  # noqa: E501
        :rtype: str
        """
        return self._rest_user_password

    @rest_user_password.setter
    def rest_user_password(self, rest_user_password):
        """Sets the rest_user_password of this SystemInitSpecV4Network1Sfs.

        User password  # noqa: E501

        :param rest_user_password: The rest_user_password of this SystemInitSpecV4Network1Sfs.  # noqa: E501
        :type: str
        """

        self._rest_user_password = rest_user_password

    @property
    def sfs_disabled(self):
        """Gets the sfs_disabled of this SystemInitSpecV4Network1Sfs.  # noqa: E501

        SmartFabric disable flag. Set sfs_disabled to true to indicate SmartFabric is not used. Set sfs_disabled to false to indicate SmartFabric Services are enabled. The default is false (enabled).  # noqa: E501

        :return: The sfs_disabled of this SystemInitSpecV4Network1Sfs.  # noqa: E501
        :rtype: bool
        """
        return self._sfs_disabled

    @sfs_disabled.setter
    def sfs_disabled(self, sfs_disabled):
        """Sets the sfs_disabled of this SystemInitSpecV4Network1Sfs.

        SmartFabric disable flag. Set sfs_disabled to true to indicate SmartFabric is not used. Set sfs_disabled to false to indicate SmartFabric Services are enabled. The default is false (enabled).  # noqa: E501

        :param sfs_disabled: The sfs_disabled of this SystemInitSpecV4Network1Sfs.  # noqa: E501
        :type: bool
        """

        self._sfs_disabled = sfs_disabled

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
        if issubclass(SystemInitSpecV4Network1Sfs, dict):
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
        if not isinstance(other, SystemInitSpecV4Network1Sfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
