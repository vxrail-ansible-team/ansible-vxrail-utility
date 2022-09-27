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

class DiscoveredNodeIdInfo(object):
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
        'appliance_id': 'str',
        'position': 'int',
        'total_supported_nodes': 'int'
    }

    attribute_map = {
        'appliance_id': 'appliance_id',
        'position': 'position',
        'total_supported_nodes': 'total_supported_nodes'
    }

    def __init__(self, appliance_id=None, position=None, total_supported_nodes=None):  # noqa: E501
        """DiscoveredNodeIdInfo - a model defined in Swagger"""  # noqa: E501
        self._appliance_id = None
        self._position = None
        self._total_supported_nodes = None
        self.discriminator = None
        self.appliance_id = appliance_id
        if position is not None:
            self.position = position
        if total_supported_nodes is not None:
            self.total_supported_nodes = total_supported_nodes

    @property
    def appliance_id(self):
        """Gets the appliance_id of this DiscoveredNodeIdInfo.  # noqa: E501

        PSNT/appliance ID of the node  # noqa: E501

        :return: The appliance_id of this DiscoveredNodeIdInfo.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this DiscoveredNodeIdInfo.

        PSNT/appliance ID of the node  # noqa: E501

        :param appliance_id: The appliance_id of this DiscoveredNodeIdInfo.  # noqa: E501
        :type: str
        """
        if appliance_id is None:
            raise ValueError("Invalid value for `appliance_id`, must not be `None`")  # noqa: E501

        self._appliance_id = appliance_id

    @property
    def position(self):
        """Gets the position of this DiscoveredNodeIdInfo.  # noqa: E501

        The node position in the chassis. For G Series appliances, this parameter indicates the position of the node in the chassis. A G Series appliance can fit up to 4 nodes in a chassis. For all other appliance models, the position value is 1.  # noqa: E501

        :return: The position of this DiscoveredNodeIdInfo.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DiscoveredNodeIdInfo.

        The node position in the chassis. For G Series appliances, this parameter indicates the position of the node in the chassis. A G Series appliance can fit up to 4 nodes in a chassis. For all other appliance models, the position value is 1.  # noqa: E501

        :param position: The position of this DiscoveredNodeIdInfo.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def total_supported_nodes(self):
        """Gets the total_supported_nodes of this DiscoveredNodeIdInfo.  # noqa: E501

        Total number of supported nodes  # noqa: E501

        :return: The total_supported_nodes of this DiscoveredNodeIdInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_supported_nodes

    @total_supported_nodes.setter
    def total_supported_nodes(self, total_supported_nodes):
        """Sets the total_supported_nodes of this DiscoveredNodeIdInfo.

        Total number of supported nodes  # noqa: E501

        :param total_supported_nodes: The total_supported_nodes of this DiscoveredNodeIdInfo.  # noqa: E501
        :type: int
        """

        self._total_supported_nodes = total_supported_nodes

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
        if issubclass(DiscoveredNodeIdInfo, dict):
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
        if not isinstance(other, DiscoveredNodeIdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
