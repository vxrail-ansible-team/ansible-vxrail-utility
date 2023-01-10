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

class VcenterEmbeddedPSCSpecV4(object):
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
        'vc_admin_user': 'UserSpec',
        'vcsa_root_user': 'UserSpec',
        'migration_spec': 'VcenterEmbeddedPSCMigrationSpecV4'
    }

    attribute_map = {
        'vc_admin_user': 'vc_admin_user',
        'vcsa_root_user': 'vcsa_root_user',
        'migration_spec': 'migration_spec'
    }

    def __init__(self, vc_admin_user=None, vcsa_root_user=None, migration_spec=None):  # noqa: E501
        """VcenterEmbeddedPSCSpecV4 - a model defined in Swagger"""  # noqa: E501
        self._vc_admin_user = None
        self._vcsa_root_user = None
        self._migration_spec = None
        self.discriminator = None
        self.vc_admin_user = vc_admin_user
        if vcsa_root_user is not None:
            self.vcsa_root_user = vcsa_root_user
        if migration_spec is not None:
            self.migration_spec = migration_spec

    @property
    def vc_admin_user(self):
        """Gets the vc_admin_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501


        :return: The vc_admin_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :rtype: UserSpec
        """
        return self._vc_admin_user

    @vc_admin_user.setter
    def vc_admin_user(self, vc_admin_user):
        """Sets the vc_admin_user of this VcenterEmbeddedPSCSpecV4.


        :param vc_admin_user: The vc_admin_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :type: UserSpec
        """
        if vc_admin_user is None:
            raise ValueError("Invalid value for `vc_admin_user`, must not be `None`")  # noqa: E501

        self._vc_admin_user = vc_admin_user

    @property
    def vcsa_root_user(self):
        """Gets the vcsa_root_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501


        :return: The vcsa_root_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :rtype: UserSpec
        """
        return self._vcsa_root_user

    @vcsa_root_user.setter
    def vcsa_root_user(self, vcsa_root_user):
        """Sets the vcsa_root_user of this VcenterEmbeddedPSCSpecV4.


        :param vcsa_root_user: The vcsa_root_user of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :type: UserSpec
        """

        self._vcsa_root_user = vcsa_root_user

    @property
    def migration_spec(self):
        """Gets the migration_spec of this VcenterEmbeddedPSCSpecV4.  # noqa: E501


        :return: The migration_spec of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :rtype: VcenterEmbeddedPSCMigrationSpecV4
        """
        return self._migration_spec

    @migration_spec.setter
    def migration_spec(self, migration_spec):
        """Sets the migration_spec of this VcenterEmbeddedPSCSpecV4.


        :param migration_spec: The migration_spec of this VcenterEmbeddedPSCSpecV4.  # noqa: E501
        :type: VcenterEmbeddedPSCMigrationSpecV4
        """

        self._migration_spec = migration_spec

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
        if issubclass(VcenterEmbeddedPSCSpecV4, dict):
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
        if not isinstance(other, VcenterEmbeddedPSCSpecV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
