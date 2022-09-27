# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.400
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV5Network1(object):
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
        'sfs': 'SystemInitSpecV5Network1Sfs',
        'nic_profile': 'str',
        'systemvm_portgroup_binding_type': 'str',
        'management_portgroup_binding_type': 'str',
        'vds': 'list[SystemInitSpecV5Network1Vds]'
    }

    attribute_map = {
        'sfs': 'sfs',
        'nic_profile': 'nic_profile',
        'systemvm_portgroup_binding_type': 'systemvm_portgroup_binding_type',
        'management_portgroup_binding_type': 'management_portgroup_binding_type',
        'vds': 'vds'
    }

    def __init__(self, sfs=None, nic_profile=None, systemvm_portgroup_binding_type=None, management_portgroup_binding_type=None, vds=None):  # noqa: E501
        """SystemInitSpecV5Network1 - a model defined in Swagger"""  # noqa: E501
        self._sfs = None
        self._nic_profile = None
        self._systemvm_portgroup_binding_type = None
        self._management_portgroup_binding_type = None
        self._vds = None
        self.discriminator = None
        if sfs is not None:
            self.sfs = sfs
        if nic_profile is not None:
            self.nic_profile = nic_profile
        if systemvm_portgroup_binding_type is not None:
            self.systemvm_portgroup_binding_type = systemvm_portgroup_binding_type
        if management_portgroup_binding_type is not None:
            self.management_portgroup_binding_type = management_portgroup_binding_type
        if vds is not None:
            self.vds = vds

    @property
    def sfs(self):
        """Gets the sfs of this SystemInitSpecV5Network1.  # noqa: E501


        :return: The sfs of this SystemInitSpecV5Network1.  # noqa: E501
        :rtype: SystemInitSpecV5Network1Sfs
        """
        return self._sfs

    @sfs.setter
    def sfs(self, sfs):
        """Sets the sfs of this SystemInitSpecV5Network1.


        :param sfs: The sfs of this SystemInitSpecV5Network1.  # noqa: E501
        :type: SystemInitSpecV5Network1Sfs
        """

        self._sfs = sfs

    @property
    def nic_profile(self):
        """Gets the nic_profile of this SystemInitSpecV5Network1.  # noqa: E501

        The NIC profile configuration  # noqa: E501

        :return: The nic_profile of this SystemInitSpecV5Network1.  # noqa: E501
        :rtype: str
        """
        return self._nic_profile

    @nic_profile.setter
    def nic_profile(self, nic_profile):
        """Sets the nic_profile of this SystemInitSpecV5Network1.

        The NIC profile configuration  # noqa: E501

        :param nic_profile: The nic_profile of this SystemInitSpecV5Network1.  # noqa: E501
        :type: str
        """
        allowed_values = ["FOUR_HIGH_SPEED", "TWO_HIGH_SPEED", "FOUR_LOW_SPEED", "TWO_LOW_TWO_HIGH_SPEED", "FOUR_EXTREME_SPEED", "ADVANCED_VXRAIL_SUPPLIED_VDS", "ADVANCED_CUSTOMER_SUPPLIED_VDS"]  # noqa: E501
        if nic_profile not in allowed_values:
            raise ValueError(
                "Invalid value for `nic_profile` ({0}), must be one of {1}"  # noqa: E501
                .format(nic_profile, allowed_values)
            )

        self._nic_profile = nic_profile

    @property
    def systemvm_portgroup_binding_type(self):
        """Gets the systemvm_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501

        The type of portgroup binding for the system VMs  # noqa: E501

        :return: The systemvm_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501
        :rtype: str
        """
        return self._systemvm_portgroup_binding_type

    @systemvm_portgroup_binding_type.setter
    def systemvm_portgroup_binding_type(self, systemvm_portgroup_binding_type):
        """Sets the systemvm_portgroup_binding_type of this SystemInitSpecV5Network1.

        The type of portgroup binding for the system VMs  # noqa: E501

        :param systemvm_portgroup_binding_type: The systemvm_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC_BINDING", "EPHEMERAL"]  # noqa: E501
        if systemvm_portgroup_binding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `systemvm_portgroup_binding_type` ({0}), must be one of {1}"  # noqa: E501
                .format(systemvm_portgroup_binding_type, allowed_values)
            )

        self._systemvm_portgroup_binding_type = systemvm_portgroup_binding_type

    @property
    def management_portgroup_binding_type(self):
        """Gets the management_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501

        The type of portgroup binding for the management server  # noqa: E501

        :return: The management_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501
        :rtype: str
        """
        return self._management_portgroup_binding_type

    @management_portgroup_binding_type.setter
    def management_portgroup_binding_type(self, management_portgroup_binding_type):
        """Sets the management_portgroup_binding_type of this SystemInitSpecV5Network1.

        The type of portgroup binding for the management server  # noqa: E501

        :param management_portgroup_binding_type: The management_portgroup_binding_type of this SystemInitSpecV5Network1.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC_BINDING", "EPHEMERAL"]  # noqa: E501
        if management_portgroup_binding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `management_portgroup_binding_type` ({0}), must be one of {1}"  # noqa: E501
                .format(management_portgroup_binding_type, allowed_values)
            )

        self._management_portgroup_binding_type = management_portgroup_binding_type

    @property
    def vds(self):
        """Gets the vds of this SystemInitSpecV5Network1.  # noqa: E501

        Information about network vSwitches  # noqa: E501

        :return: The vds of this SystemInitSpecV5Network1.  # noqa: E501
        :rtype: list[SystemInitSpecV5Network1Vds]
        """
        return self._vds

    @vds.setter
    def vds(self, vds):
        """Sets the vds of this SystemInitSpecV5Network1.

        Information about network vSwitches  # noqa: E501

        :param vds: The vds of this SystemInitSpecV5Network1.  # noqa: E501
        :type: list[SystemInitSpecV5Network1Vds]
        """

        self._vds = vds

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
        if issubclass(SystemInitSpecV5Network1, dict):
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
        if not isinstance(other, SystemInitSpecV5Network1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
