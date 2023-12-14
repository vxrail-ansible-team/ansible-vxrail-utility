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
from vxrail_ansible_utility.models.host_v10 import HostV10  # noqa: F401,E501

class HostV11(HostV10):
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
        'dpus': 'list[DpuInfoV1]'
    }
    if hasattr(HostV10, "swagger_types"):
        swagger_types.update(HostV10.swagger_types)

    attribute_map = {
        'dpus': 'dpus'
    }
    if hasattr(HostV10, "attribute_map"):
        attribute_map.update(HostV10.attribute_map)

    def __init__(self, dpus=None, *args, **kwargs):  # noqa: E501
        """HostV11 - a model defined in Swagger"""  # noqa: E501
        self._dpus = None
        self.discriminator = None
        if dpus is not None:
            self.dpus = dpus
        HostV10.__init__(self, *args, **kwargs)

    @property
    def dpus(self):
        """Gets the dpus of this HostV11.  # noqa: E501


        :return: The dpus of this HostV11.  # noqa: E501
        :rtype: list[DpuInfoV1]
        """
        return self._dpus

    @dpus.setter
    def dpus(self, dpus):
        """Sets the dpus of this HostV11.


        :param dpus: The dpus of this HostV11.  # noqa: E501
        :type: list[DpuInfoV1]
        """

        self._dpus = dpus

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
        if issubclass(HostV11, dict):
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
        if not isinstance(other, HostV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
