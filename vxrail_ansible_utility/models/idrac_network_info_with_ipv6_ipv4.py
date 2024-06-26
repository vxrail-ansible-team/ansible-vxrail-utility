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

class IdracNetworkInfoWithIPv6Ipv4(object):
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
        'ip_address': 'str',
        'netmask': 'str',
        'gateway': 'str',
        'dhcp_enabled': 'bool'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'netmask': 'netmask',
        'gateway': 'gateway',
        'dhcp_enabled': 'dhcp_enabled'
    }

    def __init__(self, ip_address=None, netmask=None, gateway=None, dhcp_enabled=None):  # noqa: E501
        """IdracNetworkInfoWithIPv6Ipv4 - a model defined in Swagger"""  # noqa: E501
        self._ip_address = None
        self._netmask = None
        self._gateway = None
        self._dhcp_enabled = None
        self.discriminator = None
        if ip_address is not None:
            self.ip_address = ip_address
        if netmask is not None:
            self.netmask = netmask
        if gateway is not None:
            self.gateway = gateway
        if dhcp_enabled is not None:
            self.dhcp_enabled = dhcp_enabled

    @property
    def ip_address(self):
        """Gets the ip_address of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501

        The static IPv4 address of the IDRAC. To configure the IPv4 address, set the property of dhcp_enabled as false. The IPv4 address information is not required to configure the IPv4 address through DHCP.  # noqa: E501

        :return: The ip_address of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this IdracNetworkInfoWithIPv6Ipv4.

        The static IPv4 address of the IDRAC. To configure the IPv4 address, set the property of dhcp_enabled as false. The IPv4 address information is not required to configure the IPv4 address through DHCP.  # noqa: E501

        :param ip_address: The ip_address of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def netmask(self):
        """Gets the netmask of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501

        The netmask of the iDRAC  # noqa: E501

        :return: The netmask of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IdracNetworkInfoWithIPv6Ipv4.

        The netmask of the iDRAC  # noqa: E501

        :param netmask: The netmask of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def gateway(self):
        """Gets the gateway of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501

        The gateway address of the iDRAC  # noqa: E501

        :return: The gateway of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IdracNetworkInfoWithIPv6Ipv4.

        The gateway address of the iDRAC  # noqa: E501

        :param gateway: The gateway of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def dhcp_enabled(self):
        """Gets the dhcp_enabled of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501

        The flag indicates whether or not DHCP is enabled to obtain an IPv4 address. If this property is set to false, the IPv4 address property is configured. Otherwise, an IPv4 address is configured through DHCP.  # noqa: E501

        :return: The dhcp_enabled of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp_enabled

    @dhcp_enabled.setter
    def dhcp_enabled(self, dhcp_enabled):
        """Sets the dhcp_enabled of this IdracNetworkInfoWithIPv6Ipv4.

        The flag indicates whether or not DHCP is enabled to obtain an IPv4 address. If this property is set to false, the IPv4 address property is configured. Otherwise, an IPv4 address is configured through DHCP.  # noqa: E501

        :param dhcp_enabled: The dhcp_enabled of this IdracNetworkInfoWithIPv6Ipv4.  # noqa: E501
        :type: bool
        """

        self._dhcp_enabled = dhcp_enabled

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
        if issubclass(IdracNetworkInfoWithIPv6Ipv4, dict):
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
        if not isinstance(other, IdracNetworkInfoWithIPv6Ipv4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
