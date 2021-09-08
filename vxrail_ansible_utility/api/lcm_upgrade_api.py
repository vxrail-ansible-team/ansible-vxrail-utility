# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class LCMUpgradeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def upgrade_v1(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v1)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 4.5.3xx+, 4.7.x, 7.0.x. [NOTE] When upgrading from VxRail 4.7.515 or earlier to VxRail 7.0.200 or later, you must upload the upgrade bundle to a folder that is not part of the root file system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v1(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV1 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upgrade_v1_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upgrade_v1_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upgrade_v1_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v1)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 4.5.3xx+, 4.7.x, 7.0.x. [NOTE] When upgrading from VxRail 4.7.515 or earlier to VxRail 7.0.200 or later, you must upload the upgrade bundle to a folder that is not part of the root file system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v1_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV1 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upgrade_v1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lcm/upgrade', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncLcmRequestSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upgrade_v2(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v2)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 4.7.410+, 7.0.x. [NOTE] When upgrading from VxRail 4.7.515 or earlier to VxRail 7.0.200 or later, you must upload the upgrade bundle to a folder that is not part of the root file system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v2(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV2 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upgrade_v2_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upgrade_v2_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upgrade_v2_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v2)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 4.7.410+, 7.0.x. [NOTE] When upgrading from VxRail 4.7.515 or earlier to VxRail 7.0.200 or later, you must upload the upgrade bundle to a folder that is not part of the root file system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v2_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV2 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upgrade_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/lcm/upgrade', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncLcmRequestSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upgrade_v3(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v3)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 7.0.100+.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v3(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV3 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upgrade_v3_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upgrade_v3_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upgrade_v3_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a full upgrade of the VxRail system (v3)  # noqa: E501

        Perform a full upgrade for all VxRail software and hardware. Supported in VxRail versions 7.0.100+.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v3_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV3 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_v3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upgrade_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/lcm/upgrade', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncLcmRequestSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upgrade_v4(self, body, **kwargs):  # noqa: E501
        """Perform a partial upgrade of vLCM-enabled VxRail system (v4)  # noqa: E501

        Perform a partial upgrade of all VxRail software and hardware. Version 4 of this API includes the optional property \"target_hosts\", which indicates the nodes to be upgraded. If \"target_hosts\" is empty or not provided, this API upgrades all nodes in the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v4(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV4 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upgrade_v4_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upgrade_v4_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upgrade_v4_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a partial upgrade of vLCM-enabled VxRail system (v4)  # noqa: E501

        Perform a partial upgrade of all VxRail software and hardware. Version 4 of this API includes the optional property \"target_hosts\", which indicates the nodes to be upgraded. If \"target_hosts\" is empty or not provided, this API upgrades all nodes in the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upgrade_v4_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeSpecV4 body: Input parameters needed for the upgrade (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_v4" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upgrade_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v4/lcm/upgrade', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncLcmRequestSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
