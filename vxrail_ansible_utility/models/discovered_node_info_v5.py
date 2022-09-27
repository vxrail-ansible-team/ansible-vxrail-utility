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

class DiscoveredNodeInfoV5(object):
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
        'id': 'DiscoveredNodeIdInfo',
        'esxi_version': 'str',
        'vxm_system_version': 'str',
        'evo_uuid': 'str',
        'primary_ip': 'str',
        'idrac_ip': 'str',
        'idrac_ipv6': 'str',
        'ip': 'str',
        'ipv6': 'str',
        'asset_tag': 'str',
        'serial_number': 'str',
        'primary': 'bool',
        'ssl_thumbprint': 'str',
        'ssh_thumbprint': 'str',
        'uuid': 'DiscoveredNodeUuidInfo',
        'hardware_profile': 'DiscoveredNodeHardwareProfileInfo',
        'disk_group_config': 'DiscoveredNodeDiskGroupConfigInfo',
        'storage_types': 'list[str]',
        'configuration_state': 'str',
        'model': 'str',
        'violations': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'esxi_version': 'esxi_version',
        'vxm_system_version': 'vxm_system_version',
        'evo_uuid': 'evo_uuid',
        'primary_ip': 'primary_ip',
        'idrac_ip': 'idrac_ip',
        'idrac_ipv6': 'idrac_ipv6',
        'ip': 'ip',
        'ipv6': 'ipv6',
        'asset_tag': 'asset_tag',
        'serial_number': 'serial_number',
        'primary': 'primary',
        'ssl_thumbprint': 'ssl_thumbprint',
        'ssh_thumbprint': 'ssh_thumbprint',
        'uuid': 'uuid',
        'hardware_profile': 'hardware_profile',
        'disk_group_config': 'disk_group_config',
        'storage_types': 'storage_types',
        'configuration_state': 'configuration_state',
        'model': 'model',
        'violations': 'violations'
    }

    def __init__(self, id=None, esxi_version=None, vxm_system_version=None, evo_uuid=None, primary_ip=None, idrac_ip=None, idrac_ipv6=None, ip=None, ipv6=None, asset_tag=None, serial_number=None, primary=None, ssl_thumbprint=None, ssh_thumbprint=None, uuid=None, hardware_profile=None, disk_group_config=None, storage_types=None, configuration_state=None, model=None, violations=None):  # noqa: E501
        """DiscoveredNodeInfoV5 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._esxi_version = None
        self._vxm_system_version = None
        self._evo_uuid = None
        self._primary_ip = None
        self._idrac_ip = None
        self._idrac_ipv6 = None
        self._ip = None
        self._ipv6 = None
        self._asset_tag = None
        self._serial_number = None
        self._primary = None
        self._ssl_thumbprint = None
        self._ssh_thumbprint = None
        self._uuid = None
        self._hardware_profile = None
        self._disk_group_config = None
        self._storage_types = None
        self._configuration_state = None
        self._model = None
        self._violations = None
        self.discriminator = None
        self.id = id
        self.esxi_version = esxi_version
        if vxm_system_version is not None:
            self.vxm_system_version = vxm_system_version
        if evo_uuid is not None:
            self.evo_uuid = evo_uuid
        if primary_ip is not None:
            self.primary_ip = primary_ip
        if idrac_ip is not None:
            self.idrac_ip = idrac_ip
        if idrac_ipv6 is not None:
            self.idrac_ipv6 = idrac_ipv6
        if ip is not None:
            self.ip = ip
        if ipv6 is not None:
            self.ipv6 = ipv6
        self.asset_tag = asset_tag
        self.serial_number = serial_number
        self.primary = primary
        self.ssl_thumbprint = ssl_thumbprint
        self.ssh_thumbprint = ssh_thumbprint
        if uuid is not None:
            self.uuid = uuid
        self.hardware_profile = hardware_profile
        if disk_group_config is not None:
            self.disk_group_config = disk_group_config
        self.storage_types = storage_types
        if configuration_state is not None:
            self.configuration_state = configuration_state
        self.model = model
        if violations is not None:
            self.violations = violations

    @property
    def id(self):
        """Gets the id of this DiscoveredNodeInfoV5.  # noqa: E501


        :return: The id of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: DiscoveredNodeIdInfo
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiscoveredNodeInfoV5.


        :param id: The id of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: DiscoveredNodeIdInfo
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def esxi_version(self):
        """Gets the esxi_version of this DiscoveredNodeInfoV5.  # noqa: E501

        ESXi version of the node  # noqa: E501

        :return: The esxi_version of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._esxi_version

    @esxi_version.setter
    def esxi_version(self, esxi_version):
        """Sets the esxi_version of this DiscoveredNodeInfoV5.

        ESXi version of the node  # noqa: E501

        :param esxi_version: The esxi_version of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if esxi_version is None:
            raise ValueError("Invalid value for `esxi_version`, must not be `None`")  # noqa: E501

        self._esxi_version = esxi_version

    @property
    def vxm_system_version(self):
        """Gets the vxm_system_version of this DiscoveredNodeInfoV5.  # noqa: E501

        VxRail system version  # noqa: E501

        :return: The vxm_system_version of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._vxm_system_version

    @vxm_system_version.setter
    def vxm_system_version(self, vxm_system_version):
        """Sets the vxm_system_version of this DiscoveredNodeInfoV5.

        VxRail system version  # noqa: E501

        :param vxm_system_version: The vxm_system_version of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._vxm_system_version = vxm_system_version

    @property
    def evo_uuid(self):
        """Gets the evo_uuid of this DiscoveredNodeInfoV5.  # noqa: E501

        UUID of the VxRail Manager VM  # noqa: E501

        :return: The evo_uuid of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._evo_uuid

    @evo_uuid.setter
    def evo_uuid(self, evo_uuid):
        """Sets the evo_uuid of this DiscoveredNodeInfoV5.

        UUID of the VxRail Manager VM  # noqa: E501

        :param evo_uuid: The evo_uuid of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._evo_uuid = evo_uuid

    @property
    def primary_ip(self):
        """Gets the primary_ip of this DiscoveredNodeInfoV5.  # noqa: E501

        The IPv6 address of the first virtual NIC (vmk0) of the node  # noqa: E501

        :return: The primary_ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this DiscoveredNodeInfoV5.

        The IPv6 address of the first virtual NIC (vmk0) of the node  # noqa: E501

        :param primary_ip: The primary_ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._primary_ip = primary_ip

    @property
    def idrac_ip(self):
        """Gets the idrac_ip of this DiscoveredNodeInfoV5.  # noqa: E501

        iDRAC IPv4 address of the node  # noqa: E501

        :return: The idrac_ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._idrac_ip

    @idrac_ip.setter
    def idrac_ip(self, idrac_ip):
        """Sets the idrac_ip of this DiscoveredNodeInfoV5.

        iDRAC IPv4 address of the node  # noqa: E501

        :param idrac_ip: The idrac_ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._idrac_ip = idrac_ip

    @property
    def idrac_ipv6(self):
        """Gets the idrac_ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The idrac_ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._idrac_ipv6

    @idrac_ipv6.setter
    def idrac_ipv6(self, idrac_ipv6):
        """Sets the idrac_ipv6 of this DiscoveredNodeInfoV5.

        Internal use only  # noqa: E501

        :param idrac_ipv6: The idrac_ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._idrac_ipv6 = idrac_ipv6

    @property
    def ip(self):
        """Gets the ip of this DiscoveredNodeInfoV5.  # noqa: E501

        IPv4 address of the node  # noqa: E501

        :return: The ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DiscoveredNodeInfoV5.

        IPv4 address of the node  # noqa: E501

        :param ip: The ip of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ipv6(self):
        """Gets the ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this DiscoveredNodeInfoV5.

        Internal use only  # noqa: E501

        :param ipv6: The ipv6 of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """

        self._ipv6 = ipv6

    @property
    def asset_tag(self):
        """Gets the asset_tag of this DiscoveredNodeInfoV5.  # noqa: E501

        Asset tag of the node  # noqa: E501

        :return: The asset_tag of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this DiscoveredNodeInfoV5.

        Asset tag of the node  # noqa: E501

        :param asset_tag: The asset_tag of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if asset_tag is None:
            raise ValueError("Invalid value for `asset_tag`, must not be `None`")  # noqa: E501

        self._asset_tag = asset_tag

    @property
    def serial_number(self):
        """Gets the serial_number of this DiscoveredNodeInfoV5.  # noqa: E501

        Serial number of the node  # noqa: E501

        :return: The serial_number of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this DiscoveredNodeInfoV5.

        Serial number of the node  # noqa: E501

        :param serial_number: The serial_number of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def primary(self):
        """Gets the primary of this DiscoveredNodeInfoV5.  # noqa: E501

        Whether the node is the primary node  # noqa: E501

        :return: The primary of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this DiscoveredNodeInfoV5.

        Whether the node is the primary node  # noqa: E501

        :param primary: The primary of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: bool
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")  # noqa: E501

        self._primary = primary

    @property
    def ssl_thumbprint(self):
        """Gets the ssl_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501

        SSL thumbprint of the node  # noqa: E501

        :return: The ssl_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._ssl_thumbprint

    @ssl_thumbprint.setter
    def ssl_thumbprint(self, ssl_thumbprint):
        """Sets the ssl_thumbprint of this DiscoveredNodeInfoV5.

        SSL thumbprint of the node  # noqa: E501

        :param ssl_thumbprint: The ssl_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if ssl_thumbprint is None:
            raise ValueError("Invalid value for `ssl_thumbprint`, must not be `None`")  # noqa: E501

        self._ssl_thumbprint = ssl_thumbprint

    @property
    def ssh_thumbprint(self):
        """Gets the ssh_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501

        SSH thumbprint of the node  # noqa: E501

        :return: The ssh_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._ssh_thumbprint

    @ssh_thumbprint.setter
    def ssh_thumbprint(self, ssh_thumbprint):
        """Sets the ssh_thumbprint of this DiscoveredNodeInfoV5.

        SSH thumbprint of the node  # noqa: E501

        :param ssh_thumbprint: The ssh_thumbprint of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if ssh_thumbprint is None:
            raise ValueError("Invalid value for `ssh_thumbprint`, must not be `None`")  # noqa: E501

        self._ssh_thumbprint = ssh_thumbprint

    @property
    def uuid(self):
        """Gets the uuid of this DiscoveredNodeInfoV5.  # noqa: E501


        :return: The uuid of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: DiscoveredNodeUuidInfo
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DiscoveredNodeInfoV5.


        :param uuid: The uuid of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: DiscoveredNodeUuidInfo
        """

        self._uuid = uuid

    @property
    def hardware_profile(self):
        """Gets the hardware_profile of this DiscoveredNodeInfoV5.  # noqa: E501


        :return: The hardware_profile of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: DiscoveredNodeHardwareProfileInfo
        """
        return self._hardware_profile

    @hardware_profile.setter
    def hardware_profile(self, hardware_profile):
        """Sets the hardware_profile of this DiscoveredNodeInfoV5.


        :param hardware_profile: The hardware_profile of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: DiscoveredNodeHardwareProfileInfo
        """
        if hardware_profile is None:
            raise ValueError("Invalid value for `hardware_profile`, must not be `None`")  # noqa: E501

        self._hardware_profile = hardware_profile

    @property
    def disk_group_config(self):
        """Gets the disk_group_config of this DiscoveredNodeInfoV5.  # noqa: E501


        :return: The disk_group_config of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: DiscoveredNodeDiskGroupConfigInfo
        """
        return self._disk_group_config

    @disk_group_config.setter
    def disk_group_config(self, disk_group_config):
        """Sets the disk_group_config of this DiscoveredNodeInfoV5.


        :param disk_group_config: The disk_group_config of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: DiscoveredNodeDiskGroupConfigInfo
        """

        self._disk_group_config = disk_group_config

    @property
    def storage_types(self):
        """Gets the storage_types of this DiscoveredNodeInfoV5.  # noqa: E501

        Storage type of the node  # noqa: E501

        :return: The storage_types of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: list[str]
        """
        return self._storage_types

    @storage_types.setter
    def storage_types(self, storage_types):
        """Sets the storage_types of this DiscoveredNodeInfoV5.

        Storage type of the node  # noqa: E501

        :param storage_types: The storage_types of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: list[str]
        """
        if storage_types is None:
            raise ValueError("Invalid value for `storage_types`, must not be `None`")  # noqa: E501
        allowed_values = ["LOCAL", "EXTERNAL", "NONE", "UNKNOWN"]  # noqa: E501
        if not set(storage_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `storage_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(storage_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._storage_types = storage_types

    @property
    def configuration_state(self):
        """Gets the configuration_state of this DiscoveredNodeInfoV5.  # noqa: E501

        Configuration state of the node  # noqa: E501

        :return: The configuration_state of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._configuration_state

    @configuration_state.setter
    def configuration_state(self, configuration_state):
        """Sets the configuration_state of this DiscoveredNodeInfoV5.

        Configuration state of the node  # noqa: E501

        :param configuration_state: The configuration_state of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNCONFIGURED", "CONFIGURING", "CONFIGURED"]  # noqa: E501
        if configuration_state not in allowed_values:
            raise ValueError(
                "Invalid value for `configuration_state` ({0}), must be one of {1}"  # noqa: E501
                .format(configuration_state, allowed_values)
            )

        self._configuration_state = configuration_state

    @property
    def model(self):
        """Gets the model of this DiscoveredNodeInfoV5.  # noqa: E501

        Appliance model of the node  # noqa: E501

        :return: The model of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DiscoveredNodeInfoV5.

        Appliance model of the node  # noqa: E501

        :param model: The model of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def violations(self):
        """Gets the violations of this DiscoveredNodeInfoV5.  # noqa: E501

        Messages about hardware profile violations  # noqa: E501

        :return: The violations of this DiscoveredNodeInfoV5.  # noqa: E501
        :rtype: list[str]
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """Sets the violations of this DiscoveredNodeInfoV5.

        Messages about hardware profile violations  # noqa: E501

        :param violations: The violations of this DiscoveredNodeInfoV5.  # noqa: E501
        :type: list[str]
        """

        self._violations = violations

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
        if issubclass(DiscoveredNodeInfoV5, dict):
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
        if not isinstance(other, DiscoveredNodeInfoV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
