# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DiskInfoV2(object):
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
        'id': 'str',
        'sn': 'str',
        'guid': 'str',
        'manufacturer': 'str',
        'model': 'str',
        'disk_type': 'str',
        'protocol': 'str',
        'max_capable_speed': 'str',
        'enclosure': 'int',
        'bay': 'int',
        'slot': 'int',
        'disk_state': 'str',
        'led_status': 'str',
        'missing': 'bool',
        'capacity': 'str',
        'write_endurance': 'str',
        'write_endurance_status': 'str',
        'remaining_write_endurance_rate': 'str',
        'firmware_revision': 'str',
        'disk_claim_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
        'guid': 'guid',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'disk_type': 'disk_type',
        'protocol': 'protocol',
        'max_capable_speed': 'max_capable_speed',
        'enclosure': 'enclosure',
        'bay': 'bay',
        'slot': 'slot',
        'disk_state': 'disk_state',
        'led_status': 'led_status',
        'missing': 'missing',
        'capacity': 'capacity',
        'write_endurance': 'write_endurance',
        'write_endurance_status': 'write_endurance_status',
        'remaining_write_endurance_rate': 'remaining_write_endurance_rate',
        'firmware_revision': 'firmware_revision',
        'disk_claim_type': 'disk_claim_type'
    }

    def __init__(self, id=None, sn=None, guid=None, manufacturer=None, model=None, disk_type=None, protocol=None, max_capable_speed=None, enclosure=None, bay=None, slot=None, disk_state=None, led_status=None, missing=None, capacity=None, write_endurance=None, write_endurance_status=None, remaining_write_endurance_rate=None, firmware_revision=None, disk_claim_type=None):  # noqa: E501
        """DiskInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
        self._guid = None
        self._manufacturer = None
        self._model = None
        self._disk_type = None
        self._protocol = None
        self._max_capable_speed = None
        self._enclosure = None
        self._bay = None
        self._slot = None
        self._disk_state = None
        self._led_status = None
        self._missing = None
        self._capacity = None
        self._write_endurance = None
        self._write_endurance_status = None
        self._remaining_write_endurance_rate = None
        self._firmware_revision = None
        self._disk_claim_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
        if guid is not None:
            self.guid = guid
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if disk_type is not None:
            self.disk_type = disk_type
        if protocol is not None:
            self.protocol = protocol
        if max_capable_speed is not None:
            self.max_capable_speed = max_capable_speed
        if enclosure is not None:
            self.enclosure = enclosure
        if bay is not None:
            self.bay = bay
        if slot is not None:
            self.slot = slot
        if disk_state is not None:
            self.disk_state = disk_state
        if led_status is not None:
            self.led_status = led_status
        if missing is not None:
            self.missing = missing
        if capacity is not None:
            self.capacity = capacity
        if write_endurance is not None:
            self.write_endurance = write_endurance
        if write_endurance_status is not None:
            self.write_endurance_status = write_endurance_status
        if remaining_write_endurance_rate is not None:
            self.remaining_write_endurance_rate = remaining_write_endurance_rate
        if firmware_revision is not None:
            self.firmware_revision = firmware_revision
        if disk_claim_type is not None:
            self.disk_claim_type = disk_claim_type

    @property
    def id(self):
        """Gets the id of this DiskInfoV2.  # noqa: E501

        ID of the disk  # noqa: E501

        :return: The id of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiskInfoV2.

        ID of the disk  # noqa: E501

        :param id: The id of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this DiskInfoV2.  # noqa: E501

        Serial number of the disk  # noqa: E501

        :return: The sn of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this DiskInfoV2.

        Serial number of the disk  # noqa: E501

        :param sn: The sn of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def guid(self):
        """Gets the guid of this DiskInfoV2.  # noqa: E501

        Guid of the disk  # noqa: E501

        :return: The guid of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this DiskInfoV2.

        Guid of the disk  # noqa: E501

        :param guid: The guid of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def manufacturer(self):
        """Gets the manufacturer of this DiskInfoV2.  # noqa: E501

        Manufacturer of the disk  # noqa: E501

        :return: The manufacturer of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this DiskInfoV2.

        Manufacturer of the disk  # noqa: E501

        :param manufacturer: The manufacturer of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this DiskInfoV2.  # noqa: E501

        Model of the disk  # noqa: E501

        :return: The model of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DiskInfoV2.

        Model of the disk  # noqa: E501

        :param model: The model of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def disk_type(self):
        """Gets the disk_type of this DiskInfoV2.  # noqa: E501

        Type of disk drive  # noqa: E501

        :return: The disk_type of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this DiskInfoV2.

        Type of disk drive  # noqa: E501

        :param disk_type: The disk_type of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def protocol(self):
        """Gets the protocol of this DiskInfoV2.  # noqa: E501

        Type of transport protocol  # noqa: E501

        :return: The protocol of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DiskInfoV2.

        Type of transport protocol  # noqa: E501

        :param protocol: The protocol of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def max_capable_speed(self):
        """Gets the max_capable_speed of this DiskInfoV2.  # noqa: E501

        Maximum capable speed of the disk  # noqa: E501

        :return: The max_capable_speed of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._max_capable_speed

    @max_capable_speed.setter
    def max_capable_speed(self, max_capable_speed):
        """Sets the max_capable_speed of this DiskInfoV2.

        Maximum capable speed of the disk  # noqa: E501

        :param max_capable_speed: The max_capable_speed of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._max_capable_speed = max_capable_speed

    @property
    def enclosure(self):
        """Gets the enclosure of this DiskInfoV2.  # noqa: E501

        Enclosure where the disk is installed  # noqa: E501

        :return: The enclosure of this DiskInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._enclosure

    @enclosure.setter
    def enclosure(self, enclosure):
        """Sets the enclosure of this DiskInfoV2.

        Enclosure where the disk is installed  # noqa: E501

        :param enclosure: The enclosure of this DiskInfoV2.  # noqa: E501
        :type: int
        """

        self._enclosure = enclosure

    @property
    def bay(self):
        """Gets the bay of this DiskInfoV2.  # noqa: E501

        Bay number of the disk  # noqa: E501

        :return: The bay of this DiskInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._bay

    @bay.setter
    def bay(self, bay):
        """Sets the bay of this DiskInfoV2.

        Bay number of the disk  # noqa: E501

        :param bay: The bay of this DiskInfoV2.  # noqa: E501
        :type: int
        """

        self._bay = bay

    @property
    def slot(self):
        """Gets the slot of this DiskInfoV2.  # noqa: E501

        Slot where the disk is installed  # noqa: E501

        :return: The slot of this DiskInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this DiskInfoV2.

        Slot where the disk is installed  # noqa: E501

        :param slot: The slot of this DiskInfoV2.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def disk_state(self):
        """Gets the disk_state of this DiskInfoV2.  # noqa: E501

        Health state of the disk  # noqa: E501

        :return: The disk_state of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._disk_state

    @disk_state.setter
    def disk_state(self, disk_state):
        """Sets the disk_state of this DiskInfoV2.

        Health state of the disk  # noqa: E501

        :param disk_state: The disk_state of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._disk_state = disk_state

    @property
    def led_status(self):
        """Gets the led_status of this DiskInfoV2.  # noqa: E501

        State of the LED indicator for the disk  # noqa: E501

        :return: The led_status of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._led_status

    @led_status.setter
    def led_status(self, led_status):
        """Sets the led_status of this DiskInfoV2.

        State of the LED indicator for the disk  # noqa: E501

        :param led_status: The led_status of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._led_status = led_status

    @property
    def missing(self):
        """Gets the missing of this DiskInfoV2.  # noqa: E501

        Whether the disk health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :return: The missing of this DiskInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this DiskInfoV2.

        Whether the disk health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :param missing: The missing of this DiskInfoV2.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def capacity(self):
        """Gets the capacity of this DiskInfoV2.  # noqa: E501

        Capacity of the disk  # noqa: E501

        :return: The capacity of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this DiskInfoV2.

        Capacity of the disk  # noqa: E501

        :param capacity: The capacity of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def write_endurance(self):
        """Gets the write_endurance of this DiskInfoV2.  # noqa: E501

        Write endurance of the disk (usage percentage)  # noqa: E501

        :return: The write_endurance of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._write_endurance

    @write_endurance.setter
    def write_endurance(self, write_endurance):
        """Sets the write_endurance of this DiskInfoV2.

        Write endurance of the disk (usage percentage)  # noqa: E501

        :param write_endurance: The write_endurance of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._write_endurance = write_endurance

    @property
    def write_endurance_status(self):
        """Gets the write_endurance_status of this DiskInfoV2.  # noqa: E501

        Status of the write endurance of the disk  # noqa: E501

        :return: The write_endurance_status of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._write_endurance_status

    @write_endurance_status.setter
    def write_endurance_status(self, write_endurance_status):
        """Sets the write_endurance_status of this DiskInfoV2.

        Status of the write endurance of the disk  # noqa: E501

        :param write_endurance_status: The write_endurance_status of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._write_endurance_status = write_endurance_status

    @property
    def remaining_write_endurance_rate(self):
        """Gets the remaining_write_endurance_rate of this DiskInfoV2.  # noqa: E501

        Remaining write endurance of the disk (percentage remaining)  # noqa: E501

        :return: The remaining_write_endurance_rate of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._remaining_write_endurance_rate

    @remaining_write_endurance_rate.setter
    def remaining_write_endurance_rate(self, remaining_write_endurance_rate):
        """Sets the remaining_write_endurance_rate of this DiskInfoV2.

        Remaining write endurance of the disk (percentage remaining)  # noqa: E501

        :param remaining_write_endurance_rate: The remaining_write_endurance_rate of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._remaining_write_endurance_rate = remaining_write_endurance_rate

    @property
    def firmware_revision(self):
        """Gets the firmware_revision of this DiskInfoV2.  # noqa: E501

        Version of the firmware for the disk  # noqa: E501

        :return: The firmware_revision of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._firmware_revision

    @firmware_revision.setter
    def firmware_revision(self, firmware_revision):
        """Sets the firmware_revision of this DiskInfoV2.

        Version of the firmware for the disk  # noqa: E501

        :param firmware_revision: The firmware_revision of this DiskInfoV2.  # noqa: E501
        :type: str
        """

        self._firmware_revision = firmware_revision

    @property
    def disk_claim_type(self):
        """Gets the disk_claim_type of this DiskInfoV2.  # noqa: E501

        Type of storage claimed for the disk. Disks can be claimed as non-vSAN or vSAN storage  # noqa: E501

        :return: The disk_claim_type of this DiskInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._disk_claim_type

    @disk_claim_type.setter
    def disk_claim_type(self, disk_claim_type):
        """Sets the disk_claim_type of this DiskInfoV2.

        Type of storage claimed for the disk. Disks can be claimed as non-vSAN or vSAN storage  # noqa: E501

        :param disk_claim_type: The disk_claim_type of this DiskInfoV2.  # noqa: E501
        :type: str
        """
        allowed_values = ["non-vSAN", "vSAN", "unmanaged"]  # noqa: E501
        if disk_claim_type not in allowed_values:
            raise ValueError(
                "Invalid value for `disk_claim_type` ({0}), must be one of {1}"  # noqa: E501
                .format(disk_claim_type, allowed_values)
            )

        self._disk_claim_type = disk_claim_type

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
        if issubclass(DiskInfoV2, dict):
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
        if not isinstance(other, DiskInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
