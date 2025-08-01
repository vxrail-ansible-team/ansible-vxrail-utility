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

class ReportCustomizeComponentData(object):
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
        'key': 'str',
        'component_name': 'str',
        'component_version': 'str',
        'component_status': 'str',
        'component_current_version': 'list[str]',
        'component_bundle': 'str',
        'type': 'str',
        'component_display_name': 'str',
        'support_deleted': 'bool',
        'reboot_flag': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'component_name': 'component_name',
        'component_version': 'component_version',
        'component_status': 'component_status',
        'component_current_version': 'component_current_version',
        'component_bundle': 'component_bundle',
        'type': 'type',
        'component_display_name': 'component_display_name',
        'support_deleted': 'support_deleted',
        'reboot_flag': 'reboot_flag'
    }

    def __init__(self, key=None, component_name=None, component_version=None, component_status=None, component_current_version=None, component_bundle=None, type=None, component_display_name=None, support_deleted=None, reboot_flag=None):  # noqa: E501
        """ReportCustomizeComponentData - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._component_name = None
        self._component_version = None
        self._component_status = None
        self._component_current_version = None
        self._component_bundle = None
        self._type = None
        self._component_display_name = None
        self._support_deleted = None
        self._reboot_flag = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if component_name is not None:
            self.component_name = component_name
        if component_version is not None:
            self.component_version = component_version
        if component_status is not None:
            self.component_status = component_status
        if component_current_version is not None:
            self.component_current_version = component_current_version
        if component_bundle is not None:
            self.component_bundle = component_bundle
        if type is not None:
            self.type = type
        if component_display_name is not None:
            self.component_display_name = component_display_name
        if support_deleted is not None:
            self.support_deleted = support_deleted
        if reboot_flag is not None:
            self.reboot_flag = reboot_flag

    @property
    def key(self):
        """Gets the key of this ReportCustomizeComponentData.  # noqa: E501


        :return: The key of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ReportCustomizeComponentData.


        :param key: The key of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def component_name(self):
        """Gets the component_name of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_name of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ReportCustomizeComponentData.


        :param component_name: The component_name of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

    @property
    def component_version(self):
        """Gets the component_version of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_version of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._component_version

    @component_version.setter
    def component_version(self, component_version):
        """Sets the component_version of this ReportCustomizeComponentData.


        :param component_version: The component_version of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._component_version = component_version

    @property
    def component_status(self):
        """Gets the component_status of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_status of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._component_status

    @component_status.setter
    def component_status(self, component_status):
        """Sets the component_status of this ReportCustomizeComponentData.


        :param component_status: The component_status of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._component_status = component_status

    @property
    def component_current_version(self):
        """Gets the component_current_version of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_current_version of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: list[str]
        """
        return self._component_current_version

    @component_current_version.setter
    def component_current_version(self, component_current_version):
        """Sets the component_current_version of this ReportCustomizeComponentData.


        :param component_current_version: The component_current_version of this ReportCustomizeComponentData.  # noqa: E501
        :type: list[str]
        """

        self._component_current_version = component_current_version

    @property
    def component_bundle(self):
        """Gets the component_bundle of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_bundle of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._component_bundle

    @component_bundle.setter
    def component_bundle(self, component_bundle):
        """Sets the component_bundle of this ReportCustomizeComponentData.


        :param component_bundle: The component_bundle of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._component_bundle = component_bundle

    @property
    def type(self):
        """Gets the type of this ReportCustomizeComponentData.  # noqa: E501


        :return: The type of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportCustomizeComponentData.


        :param type: The type of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def component_display_name(self):
        """Gets the component_display_name of this ReportCustomizeComponentData.  # noqa: E501


        :return: The component_display_name of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: str
        """
        return self._component_display_name

    @component_display_name.setter
    def component_display_name(self, component_display_name):
        """Sets the component_display_name of this ReportCustomizeComponentData.


        :param component_display_name: The component_display_name of this ReportCustomizeComponentData.  # noqa: E501
        :type: str
        """

        self._component_display_name = component_display_name

    @property
    def support_deleted(self):
        """Gets the support_deleted of this ReportCustomizeComponentData.  # noqa: E501


        :return: The support_deleted of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: bool
        """
        return self._support_deleted

    @support_deleted.setter
    def support_deleted(self, support_deleted):
        """Sets the support_deleted of this ReportCustomizeComponentData.


        :param support_deleted: The support_deleted of this ReportCustomizeComponentData.  # noqa: E501
        :type: bool
        """

        self._support_deleted = support_deleted

    @property
    def reboot_flag(self):
        """Gets the reboot_flag of this ReportCustomizeComponentData.  # noqa: E501


        :return: The reboot_flag of this ReportCustomizeComponentData.  # noqa: E501
        :rtype: bool
        """
        return self._reboot_flag

    @reboot_flag.setter
    def reboot_flag(self, reboot_flag):
        """Sets the reboot_flag of this ReportCustomizeComponentData.


        :param reboot_flag: The reboot_flag of this ReportCustomizeComponentData.  # noqa: E501
        :type: bool
        """

        self._reboot_flag = reboot_flag

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
        if issubclass(ReportCustomizeComponentData, dict):
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
        if not isinstance(other, ReportCustomizeComponentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
