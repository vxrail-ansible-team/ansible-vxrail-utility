# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Layer3ManagementNetworkHostSpec(object):
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
        'sn': 'str',
        'psnt': 'str',
        'hostname': 'str',
        'management_ip': 'str'
    }

    attribute_map = {
        'sn': 'sn',
        'psnt': 'psnt',
        'hostname': 'hostname',
        'management_ip': 'managementIp'
    }

    def __init__(self, sn=None, psnt=None, hostname=None, management_ip=None):  # noqa: E501
        """Layer3ManagementNetworkHostSpec - a model defined in Swagger"""  # noqa: E501
        self._sn = None
        self._psnt = None
        self._hostname = None
        self._management_ip = None
        self.discriminator = None
        self.sn = sn
        self.psnt = psnt
        self.hostname = hostname
        self.management_ip = management_ip

    @property
    def sn(self):
        """Gets the sn of this Layer3ManagementNetworkHostSpec.  # noqa: E501


        :return: The sn of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this Layer3ManagementNetworkHostSpec.


        :param sn: The sn of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :type: str
        """
        if sn is None:
            raise ValueError("Invalid value for `sn`, must not be `None`")  # noqa: E501

        self._sn = sn

    @property
    def psnt(self):
        """Gets the psnt of this Layer3ManagementNetworkHostSpec.  # noqa: E501


        :return: The psnt of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this Layer3ManagementNetworkHostSpec.


        :param psnt: The psnt of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :type: str
        """
        if psnt is None:
            raise ValueError("Invalid value for `psnt`, must not be `None`")  # noqa: E501

        self._psnt = psnt

    @property
    def hostname(self):
        """Gets the hostname of this Layer3ManagementNetworkHostSpec.  # noqa: E501


        :return: The hostname of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Layer3ManagementNetworkHostSpec.


        :param hostname: The hostname of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def management_ip(self):
        """Gets the management_ip of this Layer3ManagementNetworkHostSpec.  # noqa: E501


        :return: The management_ip of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this Layer3ManagementNetworkHostSpec.


        :param management_ip: The management_ip of this Layer3ManagementNetworkHostSpec.  # noqa: E501
        :type: str
        """
        if management_ip is None:
            raise ValueError("Invalid value for `management_ip`, must not be `None`")  # noqa: E501

        self._management_ip = management_ip

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
        if issubclass(Layer3ManagementNetworkHostSpec, dict):
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
        if not isinstance(other, Layer3ManagementNetworkHostSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
