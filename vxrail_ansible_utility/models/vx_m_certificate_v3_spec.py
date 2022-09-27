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

class VxMCertificateV3Spec(object):
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
        'vc_admin_account': 'str',
        'vc_admin_password': 'str',
        'cert': 'str',
        'root_cert_chain': 'list',
        'private_key': 'str',
        'password': 'str'
    }

    attribute_map = {
        'vc_admin_account': 'vc_admin_account',
        'vc_admin_password': 'vc_admin_password',
        'cert': 'cert',
        'root_cert_chain': 'root_cert_chain',
        'private_key': 'private_key',
        'password': 'password'
    }

    def __init__(self, vc_admin_account=None, vc_admin_password=None, cert=None, root_cert_chain=None, private_key=None, password=None):  # noqa: E501
        """VxMCertificateV3Spec - a model defined in Swagger"""  # noqa: E501
        self._vc_admin_account = None
        self._vc_admin_password = None
        self._cert = None
        self._root_cert_chain = None
        self._private_key = None
        self._password = None
        self.discriminator = None
        self.vc_admin_account = vc_admin_account
        self.vc_admin_password = vc_admin_password
        self.cert = cert
        self.root_cert_chain = root_cert_chain
        if private_key is not None:
            self.private_key = private_key
        if password is not None:
            self.password = password

    @property
    def vc_admin_account(self):
        """Gets the vc_admin_account of this VxMCertificateV3Spec.  # noqa: E501

        VC admin account for invoke VC API to send the new root cert to VC trust store.  # noqa: E501

        :return: The vc_admin_account of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: str
        """
        return self._vc_admin_account

    @vc_admin_account.setter
    def vc_admin_account(self, vc_admin_account):
        """Sets the vc_admin_account of this VxMCertificateV3Spec.

        VC admin account for invoke VC API to send the new root cert to VC trust store.  # noqa: E501

        :param vc_admin_account: The vc_admin_account of this VxMCertificateV3Spec.  # noqa: E501
        :type: str
        """
        if vc_admin_account is None:
            raise ValueError("Invalid value for `vc_admin_account`, must not be `None`")  # noqa: E501

        self._vc_admin_account = vc_admin_account

    @property
    def vc_admin_password(self):
        """Gets the vc_admin_password of this VxMCertificateV3Spec.  # noqa: E501

        VC admin password for invoke VC API to send the new root cert to VC trust store.  # noqa: E501

        :return: The vc_admin_password of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: str
        """
        return self._vc_admin_password

    @vc_admin_password.setter
    def vc_admin_password(self, vc_admin_password):
        """Sets the vc_admin_password of this VxMCertificateV3Spec.

        VC admin password for invoke VC API to send the new root cert to VC trust store.  # noqa: E501

        :param vc_admin_password: The vc_admin_password of this VxMCertificateV3Spec.  # noqa: E501
        :type: str
        """
        if vc_admin_password is None:
            raise ValueError("Invalid value for `vc_admin_password`, must not be `None`")  # noqa: E501

        self._vc_admin_password = vc_admin_password

    @property
    def cert(self):
        """Gets the cert of this VxMCertificateV3Spec.  # noqa: E501

        Content of the new certificate in PEM format. Each line should be followed by an escape character \"\\n\".  # noqa: E501

        :return: The cert of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this VxMCertificateV3Spec.

        Content of the new certificate in PEM format. Each line should be followed by an escape character \"\\n\".  # noqa: E501

        :param cert: The cert of this VxMCertificateV3Spec.  # noqa: E501
        :type: str
        """
        if cert is None:
            raise ValueError("Invalid value for `cert`, must not be `None`")  # noqa: E501

        self._cert = cert

    @property
    def root_cert_chain(self):
        """Gets the root_cert_chain of this VxMCertificateV3Spec.  # noqa: E501

        Contents of the certificate chain in PEM format. The root CA certificate comes first, followed by the intermediate CA certificates (if any).  # noqa: E501

        :return: The root_cert_chain of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: list
        """
        return self._root_cert_chain

    @root_cert_chain.setter
    def root_cert_chain(self, root_cert_chain):
        """Sets the root_cert_chain of this VxMCertificateV3Spec.

        Contents of the certificate chain in PEM format. The root CA certificate comes first, followed by the intermediate CA certificates (if any).  # noqa: E501

        :param root_cert_chain: The root_cert_chain of this VxMCertificateV3Spec.  # noqa: E501
        :type: list
        """
        if root_cert_chain is None:
            raise ValueError("Invalid value for `root_cert_chain`, must not be `None`")  # noqa: E501

        self._root_cert_chain = root_cert_chain

    @property
    def private_key(self):
        """Gets the private_key of this VxMCertificateV3Spec.  # noqa: E501

        Contents of the private key in PEM format. Only an RSA private key is allowed. The private key can be omitted if the provided certificate is issued based on the CSR generated by /v1/certificates/csr.  # noqa: E501

        :return: The private_key of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this VxMCertificateV3Spec.

        Contents of the private key in PEM format. Only an RSA private key is allowed. The private key can be omitted if the provided certificate is issued based on the CSR generated by /v1/certificates/csr.  # noqa: E501

        :param private_key: The private_key of this VxMCertificateV3Spec.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def password(self):
        """Gets the password of this VxMCertificateV3Spec.  # noqa: E501

        Password for the new .pfx file.  # noqa: E501

        :return: The password of this VxMCertificateV3Spec.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VxMCertificateV3Spec.

        Password for the new .pfx file.  # noqa: E501

        :param password: The password of this VxMCertificateV3Spec.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(VxMCertificateV3Spec, dict):
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
        if not isinstance(other, VxMCertificateV3Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
