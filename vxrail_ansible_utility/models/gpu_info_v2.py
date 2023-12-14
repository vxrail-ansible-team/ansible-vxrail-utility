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

class GpuInfoV2(object):
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
        'type': 'str',
        'slot': 'int',
        'vendor_description': 'str',
        'supplier': 'str',
        'marketing_name': 'str',
        'firmware_version': 'str',
        'gpu_health': 'str',
        'gpu_part_number': 'str',
        'gpu_state': 'str',
        'last_update_time': 'int',
        'serial_number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'slot': 'slot',
        'vendor_description': 'vendor_description',
        'supplier': 'supplier',
        'marketing_name': 'marketing_name',
        'firmware_version': 'firmware_version',
        'gpu_health': 'gpu_health',
        'gpu_part_number': 'gpu_part_number',
        'gpu_state': 'gpu_state',
        'last_update_time': 'last_update_time',
        'serial_number': 'serial_number'
    }

    def __init__(self, type=None, slot=None, vendor_description=None, supplier=None, marketing_name=None, firmware_version=None, gpu_health=None, gpu_part_number=None, gpu_state=None, last_update_time=None, serial_number=None):  # noqa: E501
        """GpuInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._slot = None
        self._vendor_description = None
        self._supplier = None
        self._marketing_name = None
        self._firmware_version = None
        self._gpu_health = None
        self._gpu_part_number = None
        self._gpu_state = None
        self._last_update_time = None
        self._serial_number = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if slot is not None:
            self.slot = slot
        if vendor_description is not None:
            self.vendor_description = vendor_description
        if supplier is not None:
            self.supplier = supplier
        if marketing_name is not None:
            self.marketing_name = marketing_name
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if gpu_health is not None:
            self.gpu_health = gpu_health
        if gpu_part_number is not None:
            self.gpu_part_number = gpu_part_number
        if gpu_state is not None:
            self.gpu_state = gpu_state
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if serial_number is not None:
            self.serial_number = serial_number

    @property
    def type(self):
        """Gets the type of this GpuInfoV2.  # noqa: E501

        Device type of the GPU.  # noqa: E501

        :return: The type of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GpuInfoV2.

        Device type of the GPU.  # noqa: E501

        :param type: The type of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def slot(self):
        """Gets the slot of this GpuInfoV2.  # noqa: E501

        Slot number of the GPU device.  # noqa: E501

        :return: The slot of this GpuInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this GpuInfoV2.

        Slot number of the GPU device.  # noqa: E501

        :param slot: The slot of this GpuInfoV2.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def vendor_description(self):
        """Gets the vendor_description of this GpuInfoV2.  # noqa: E501

        Vendor description of the GPU device.  # noqa: E501

        :return: The vendor_description of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._vendor_description

    @vendor_description.setter
    def vendor_description(self, vendor_description):
        """Sets the vendor_description of this GpuInfoV2.

        Vendor description of the GPU device.  # noqa: E501

        :param vendor_description: The vendor_description of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._vendor_description = vendor_description

    @property
    def supplier(self):
        """Gets the supplier of this GpuInfoV2.  # noqa: E501

        Supplier name of the GPU device.  # noqa: E501

        :return: The supplier of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this GpuInfoV2.

        Supplier name of the GPU device.  # noqa: E501

        :param supplier: The supplier of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def marketing_name(self):
        """Gets the marketing_name of this GpuInfoV2.  # noqa: E501


        :return: The marketing_name of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._marketing_name

    @marketing_name.setter
    def marketing_name(self, marketing_name):
        """Sets the marketing_name of this GpuInfoV2.


        :param marketing_name: The marketing_name of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._marketing_name = marketing_name

    @property
    def firmware_version(self):
        """Gets the firmware_version of this GpuInfoV2.  # noqa: E501

        Firmware version of the GPU device.  # noqa: E501

        :return: The firmware_version of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this GpuInfoV2.

        Firmware version of the GPU device.  # noqa: E501

        :param firmware_version: The firmware_version of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def gpu_health(self):
        """Gets the gpu_health of this GpuInfoV2.  # noqa: E501

        Health status of the GPU.  # noqa: E501

        :return: The gpu_health of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._gpu_health

    @gpu_health.setter
    def gpu_health(self, gpu_health):
        """Sets the gpu_health of this GpuInfoV2.

        Health status of the GPU.  # noqa: E501

        :param gpu_health: The gpu_health of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._gpu_health = gpu_health

    @property
    def gpu_part_number(self):
        """Gets the gpu_part_number of this GpuInfoV2.  # noqa: E501

        Part number of the GPU.  # noqa: E501

        :return: The gpu_part_number of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._gpu_part_number

    @gpu_part_number.setter
    def gpu_part_number(self, gpu_part_number):
        """Sets the gpu_part_number of this GpuInfoV2.

        Part number of the GPU.  # noqa: E501

        :param gpu_part_number: The gpu_part_number of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._gpu_part_number = gpu_part_number

    @property
    def gpu_state(self):
        """Gets the gpu_state of this GpuInfoV2.  # noqa: E501

        State of the GPU.  # noqa: E501

        :return: The gpu_state of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._gpu_state

    @gpu_state.setter
    def gpu_state(self, gpu_state):
        """Sets the gpu_state of this GpuInfoV2.

        State of the GPU.  # noqa: E501

        :param gpu_state: The gpu_state of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._gpu_state = gpu_state

    @property
    def last_update_time(self):
        """Gets the last_update_time of this GpuInfoV2.  # noqa: E501

        Last updated time of the GPU.   # noqa: E501

        :return: The last_update_time of this GpuInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this GpuInfoV2.

        Last updated time of the GPU.   # noqa: E501

        :param last_update_time: The last_update_time of this GpuInfoV2.  # noqa: E501
        :type: int
        """

        self._last_update_time = last_update_time

    @property
    def serial_number(self):
        """Gets the serial_number of this GpuInfoV2.  # noqa: E501

        Serial number of the GPU.  # noqa: E501

        :return: The serial_number of this GpuInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this GpuInfoV2.

        Serial number of the GPU.  # noqa: E501

        :param serial_number: The serial_number of this GpuInfoV2.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

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
        if issubclass(GpuInfoV2, dict):
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
        if not isinstance(other, GpuInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
