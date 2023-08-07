# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StigInfoV1Vmware(object):
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
        'server_management_host': 'str',
        'virtualization_systems': 'list[VirtualizationSystemInfo]',
        'configured_hosts': 'list[HypervisorHostInfo]',
        'satellite_node_hosts': 'list[HypervisorHostInfo]'
    }

    attribute_map = {
        'server_management_host': 'server_management_host',
        'virtualization_systems': 'virtualization_systems',
        'configured_hosts': 'configured_hosts',
        'satellite_node_hosts': 'satellite_node_hosts'
    }

    def __init__(self, server_management_host=None, virtualization_systems=None, configured_hosts=None, satellite_node_hosts=None):  # noqa: E501
        """StigInfoV1Vmware - a model defined in Swagger"""  # noqa: E501
        self._server_management_host = None
        self._virtualization_systems = None
        self._configured_hosts = None
        self._satellite_node_hosts = None
        self.discriminator = None
        if server_management_host is not None:
            self.server_management_host = server_management_host
        if virtualization_systems is not None:
            self.virtualization_systems = virtualization_systems
        if configured_hosts is not None:
            self.configured_hosts = configured_hosts
        if satellite_node_hosts is not None:
            self.satellite_node_hosts = satellite_node_hosts

    @property
    def server_management_host(self):
        """Gets the server_management_host of this StigInfoV1Vmware.  # noqa: E501

        IP address or hostname of a vCenter server appliance.  # noqa: E501

        :return: The server_management_host of this StigInfoV1Vmware.  # noqa: E501
        :rtype: str
        """
        return self._server_management_host

    @server_management_host.setter
    def server_management_host(self, server_management_host):
        """Sets the server_management_host of this StigInfoV1Vmware.

        IP address or hostname of a vCenter server appliance.  # noqa: E501

        :param server_management_host: The server_management_host of this StigInfoV1Vmware.  # noqa: E501
        :type: str
        """

        self._server_management_host = server_management_host

    @property
    def virtualization_systems(self):
        """Gets the virtualization_systems of this StigInfoV1Vmware.  # noqa: E501

        Information about VMs in this cluster.  # noqa: E501

        :return: The virtualization_systems of this StigInfoV1Vmware.  # noqa: E501
        :rtype: list[VirtualizationSystemInfo]
        """
        return self._virtualization_systems

    @virtualization_systems.setter
    def virtualization_systems(self, virtualization_systems):
        """Sets the virtualization_systems of this StigInfoV1Vmware.

        Information about VMs in this cluster.  # noqa: E501

        :param virtualization_systems: The virtualization_systems of this StigInfoV1Vmware.  # noqa: E501
        :type: list[VirtualizationSystemInfo]
        """

        self._virtualization_systems = virtualization_systems

    @property
    def configured_hosts(self):
        """Gets the configured_hosts of this StigInfoV1Vmware.  # noqa: E501

        Information about nodes in this cluster.  # noqa: E501

        :return: The configured_hosts of this StigInfoV1Vmware.  # noqa: E501
        :rtype: list[HypervisorHostInfo]
        """
        return self._configured_hosts

    @configured_hosts.setter
    def configured_hosts(self, configured_hosts):
        """Sets the configured_hosts of this StigInfoV1Vmware.

        Information about nodes in this cluster.  # noqa: E501

        :param configured_hosts: The configured_hosts of this StigInfoV1Vmware.  # noqa: E501
        :type: list[HypervisorHostInfo]
        """

        self._configured_hosts = configured_hosts

    @property
    def satellite_node_hosts(self):
        """Gets the satellite_node_hosts of this StigInfoV1Vmware.  # noqa: E501

        Information about satellite nodes in this cluster.  # noqa: E501

        :return: The satellite_node_hosts of this StigInfoV1Vmware.  # noqa: E501
        :rtype: list[HypervisorHostInfo]
        """
        return self._satellite_node_hosts

    @satellite_node_hosts.setter
    def satellite_node_hosts(self, satellite_node_hosts):
        """Sets the satellite_node_hosts of this StigInfoV1Vmware.

        Information about satellite nodes in this cluster.  # noqa: E501

        :param satellite_node_hosts: The satellite_node_hosts of this StigInfoV1Vmware.  # noqa: E501
        :type: list[HypervisorHostInfo]
        """

        self._satellite_node_hosts = satellite_node_hosts

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
        if issubclass(StigInfoV1Vmware, dict):
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
        if not isinstance(other, StigInfoV1Vmware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
