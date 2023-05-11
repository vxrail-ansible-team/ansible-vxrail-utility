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

class StigInfoV1(object):
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
        'vmware': 'StigInfoV1Vmware',
        'ntp_servers': 'list[str]',
        'syslog_servers': 'list[str]'
    }

    attribute_map = {
        'vmware': 'vmware',
        'ntp_servers': 'ntp_servers',
        'syslog_servers': 'syslog_servers'
    }

    def __init__(self, vmware=None, ntp_servers=None, syslog_servers=None):  # noqa: E501
        """StigInfoV1 - a model defined in Swagger"""  # noqa: E501
        self._vmware = None
        self._ntp_servers = None
        self._syslog_servers = None
        self.discriminator = None
        if vmware is not None:
            self.vmware = vmware
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if syslog_servers is not None:
            self.syslog_servers = syslog_servers

    @property
    def vmware(self):
        """Gets the vmware of this StigInfoV1.  # noqa: E501


        :return: The vmware of this StigInfoV1.  # noqa: E501
        :rtype: StigInfoV1Vmware
        """
        return self._vmware

    @vmware.setter
    def vmware(self, vmware):
        """Sets the vmware of this StigInfoV1.


        :param vmware: The vmware of this StigInfoV1.  # noqa: E501
        :type: StigInfoV1Vmware
        """

        self._vmware = vmware

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this StigInfoV1.  # noqa: E501

        IP address or hostnames of NTP servers.  # noqa: E501

        :return: The ntp_servers of this StigInfoV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this StigInfoV1.

        IP address or hostnames of NTP servers.  # noqa: E501

        :param ntp_servers: The ntp_servers of this StigInfoV1.  # noqa: E501
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def syslog_servers(self):
        """Gets the syslog_servers of this StigInfoV1.  # noqa: E501

        IP address or hostnames of syslog servers.  # noqa: E501

        :return: The syslog_servers of this StigInfoV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._syslog_servers

    @syslog_servers.setter
    def syslog_servers(self, syslog_servers):
        """Sets the syslog_servers of this StigInfoV1.

        IP address or hostnames of syslog servers.  # noqa: E501

        :param syslog_servers: The syslog_servers of this StigInfoV1.  # noqa: E501
        :type: list[str]
        """

        self._syslog_servers = syslog_servers

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
        if issubclass(StigInfoV1, dict):
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
        if not isinstance(other, StigInfoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other