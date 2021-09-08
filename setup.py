# coding: utf-8

"""
    VxRail Cluster,System Management and Day1 bring up

    APIs for cluster management, system management and Day1 bring up # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "vxrail_ansible_utility"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="VxRail Cluster,System Management and Day1 bring up",
    author_email="",
    url="",
    keywords=["Swagger", "VxRail Cluster,System Management and Day1 bring up"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    APIs for cluster management,system management and Day1 bring up # noqa: E501
    """
)
