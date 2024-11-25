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

class SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm(object):
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
        'hostname': 'str',
        'management_ip': 'str',
        'witness_ip': 'str',
        'netmask': 'str',
        'accounts': 'SystemInitSpecV6VxrailManagedWitnessNodeWitnessVmAccounts'
    }

    attribute_map = {
        'hostname': 'hostname',
        'management_ip': 'management_ip',
        'witness_ip': 'witness_ip',
        'netmask': 'netmask',
        'accounts': 'accounts'
    }

    def __init__(self, hostname=None, management_ip=None, witness_ip=None, netmask=None, accounts=None):  # noqa: E501
        """SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm - a model defined in Swagger"""  # noqa: E501
        self._hostname = None
        self._management_ip = None
        self._witness_ip = None
        self._netmask = None
        self._accounts = None
        self.discriminator = None
        if hostname is not None:
            self.hostname = hostname
        self.management_ip = management_ip
        if witness_ip is not None:
            self.witness_ip = witness_ip
        if netmask is not None:
            self.netmask = netmask
        if accounts is not None:
            self.accounts = accounts

    @property
    def hostname(self):
        """Gets the hostname of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501

        Name of the witness vm.  # noqa: E501

        :return: The hostname of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.

        Name of the witness vm.  # noqa: E501

        :param hostname: The hostname of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def management_ip(self):
        """Gets the management_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501

        Management IP address for the witness VM.  # noqa: E501

        :return: The management_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.

        Management IP address for the witness VM.  # noqa: E501

        :param management_ip: The management_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :type: str
        """
        if management_ip is None:
            raise ValueError("Invalid value for `management_ip`, must not be `None`")  # noqa: E501

        self._management_ip = management_ip

    @property
    def witness_ip(self):
        """Gets the witness_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501

        Witness traffic IP address for the witness VM  # noqa: E501

        :return: The witness_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :rtype: str
        """
        return self._witness_ip

    @witness_ip.setter
    def witness_ip(self, witness_ip):
        """Sets the witness_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.

        Witness traffic IP address for the witness VM  # noqa: E501

        :param witness_ip: The witness_ip of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :type: str
        """

        self._witness_ip = witness_ip

    @property
    def netmask(self):
        """Gets the netmask of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501

        Subnet mask for the witness traffic IP address  # noqa: E501

        :return: The netmask of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.

        Subnet mask for the witness traffic IP address  # noqa: E501

        :param netmask: The netmask of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def accounts(self):
        """Gets the accounts of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501


        :return: The accounts of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :rtype: SystemInitSpecV6VxrailManagedWitnessNodeWitnessVmAccounts
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.


        :param accounts: The accounts of this SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm.  # noqa: E501
        :type: SystemInitSpecV6VxrailManagedWitnessNodeWitnessVmAccounts
        """

        self._accounts = accounts

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
        if issubclass(SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm, dict):
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
        if not isinstance(other, SystemInitSpecV6VxrailManagedWitnessNodeWitnessVm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other