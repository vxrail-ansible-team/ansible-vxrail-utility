# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV4Network1Vds(object):
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
        'name': 'str',
        'mtu': 'int',
        'nic_mappings': 'list[SystemInitSpecV4Network1NicMappings]',
        'portgroups': 'list[SystemInitSpecV4Network1Portgroups]'
    }

    attribute_map = {
        'name': 'name',
        'mtu': 'mtu',
        'nic_mappings': 'nic_mappings',
        'portgroups': 'portgroups'
    }

    def __init__(self, name=None, mtu=None, nic_mappings=None, portgroups=None):  # noqa: E501
        """SystemInitSpecV4Network1Vds - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._mtu = None
        self._nic_mappings = None
        self._portgroups = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if mtu is not None:
            self.mtu = mtu
        if nic_mappings is not None:
            self.nic_mappings = nic_mappings
        if portgroups is not None:
            self.portgroups = portgroups

    @property
    def name(self):
        """Gets the name of this SystemInitSpecV4Network1Vds.  # noqa: E501

        Name of the defined vSphere Distributed Switch. This property is only for ADVANCED_CUSTOMER_SUPPLIED_VDS nic_profile.  # noqa: E501

        :return: The name of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInitSpecV4Network1Vds.

        Name of the defined vSphere Distributed Switch. This property is only for ADVANCED_CUSTOMER_SUPPLIED_VDS nic_profile.  # noqa: E501

        :param name: The name of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mtu(self):
        """Gets the mtu of this SystemInitSpecV4Network1Vds.  # noqa: E501

        The MTU value of the vSphere Distributed Switch. This value must be in the [1500, 9000] range. This property is only supported for the V-VDS or Multi-VDS portgroup types. This property is not supported for customer-supplied VDS or vSAN 2-node clusters.  # noqa: E501

        :return: The mtu of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this SystemInitSpecV4Network1Vds.

        The MTU value of the vSphere Distributed Switch. This value must be in the [1500, 9000] range. This property is only supported for the V-VDS or Multi-VDS portgroup types. This property is not supported for customer-supplied VDS or vSAN 2-node clusters.  # noqa: E501

        :param mtu: The mtu of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def nic_mappings(self):
        """Gets the nic_mappings of this SystemInitSpecV4Network1Vds.  # noqa: E501

        This property is only used for a ADVANCED_VXRAIL_SUPPLIED_VDS and ADVANCED_CUSTOMER_SUPPLIED_VDS nic_profile  # noqa: E501

        :return: The nic_mappings of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :rtype: list[SystemInitSpecV4Network1NicMappings]
        """
        return self._nic_mappings

    @nic_mappings.setter
    def nic_mappings(self, nic_mappings):
        """Sets the nic_mappings of this SystemInitSpecV4Network1Vds.

        This property is only used for a ADVANCED_VXRAIL_SUPPLIED_VDS and ADVANCED_CUSTOMER_SUPPLIED_VDS nic_profile  # noqa: E501

        :param nic_mappings: The nic_mappings of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :type: list[SystemInitSpecV4Network1NicMappings]
        """

        self._nic_mappings = nic_mappings

    @property
    def portgroups(self):
        """Gets the portgroups of this SystemInitSpecV4Network1Vds.  # noqa: E501


        :return: The portgroups of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :rtype: list[SystemInitSpecV4Network1Portgroups]
        """
        return self._portgroups

    @portgroups.setter
    def portgroups(self, portgroups):
        """Sets the portgroups of this SystemInitSpecV4Network1Vds.


        :param portgroups: The portgroups of this SystemInitSpecV4Network1Vds.  # noqa: E501
        :type: list[SystemInitSpecV4Network1Portgroups]
        """

        self._portgroups = portgroups

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
        if issubclass(SystemInitSpecV4Network1Vds, dict):
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
        if not isinstance(other, SystemInitSpecV4Network1Vds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
