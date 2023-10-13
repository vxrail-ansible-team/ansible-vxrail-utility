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

class UpgradeUploadbundleBody(object):
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
        'component_bundle': 'str'
    }

    attribute_map = {
        'component_bundle': 'component_bundle'
    }

    def __init__(self, component_bundle=None):  # noqa: E501
        """UpgradeUploadbundleBody - a model defined in Swagger"""  # noqa: E501
        self._component_bundle = None
        self.discriminator = None
        if component_bundle is not None:
            self.component_bundle = component_bundle

    @property
    def component_bundle(self):
        """Gets the component_bundle of this UpgradeUploadbundleBody.  # noqa: E501

        Indicates the file path on the local machine.  # noqa: E501

        :return: The component_bundle of this UpgradeUploadbundleBody.  # noqa: E501
        :rtype: str
        """
        return self._component_bundle

    @component_bundle.setter
    def component_bundle(self, component_bundle):
        """Sets the component_bundle of this UpgradeUploadbundleBody.

        Indicates the file path on the local machine.  # noqa: E501

        :param component_bundle: The component_bundle of this UpgradeUploadbundleBody.  # noqa: E501
        :type: str
        """

        self._component_bundle = component_bundle

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
        if issubclass(UpgradeUploadbundleBody, dict):
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
        if not isinstance(other, UpgradeUploadbundleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
