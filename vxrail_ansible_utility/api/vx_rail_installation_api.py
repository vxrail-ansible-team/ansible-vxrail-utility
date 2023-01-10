# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class VxRailInstallationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_system_initialize_customer_supplied_hosts_post(self, body, **kwargs):  # noqa: E501
        """Return nodes by customer supplied management IP  # noqa: E501

        Return nodes by the customer supplied node management IP address and ESXi root password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_customer_supplied_hosts_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[CustomerSuppliedHostInfo] body: Management IP and password for all customer supplied hosts (required)
        :return: list[DiscoveredNodeInfoV2]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_customer_supplied_hosts_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_customer_supplied_hosts_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_system_initialize_customer_supplied_hosts_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Return nodes by customer supplied management IP  # noqa: E501

        Return nodes by the customer supplied node management IP address and ESXi root password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_customer_supplied_hosts_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[CustomerSuppliedHostInfo] body: Management IP and password for all customer supplied hosts (required)
        :return: list[DiscoveredNodeInfoV2]
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
                    " to method v1_system_initialize_customer_supplied_hosts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_initialize_customer_supplied_hosts_post`")  # noqa: E501

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
            '/v1/system/initialize/customer-supplied-hosts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DiscoveredNodeInfoV2]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_disk_slot_mappings_get(self, body, **kwargs):  # noqa: E501
        """Get disk slot mappings for hosts  # noqa: E501

        Retrieve disk slots and usage mappings from the initial configuration for a set of hosts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_disk_slot_mappings_get(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InitializeDiskslotmappingsBody body: Information needed to retrieve disk slot usage for a host (required)
        :return: list[HostDiskSlotMappingsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_disk_slot_mappings_get_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_disk_slot_mappings_get_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_system_initialize_disk_slot_mappings_get_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get disk slot mappings for hosts  # noqa: E501

        Retrieve disk slots and usage mappings from the initial configuration for a set of hosts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_disk_slot_mappings_get_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InitializeDiskslotmappingsBody body: Information needed to retrieve disk slot usage for a host (required)
        :return: list[HostDiskSlotMappingsResponse]
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
                    " to method v1_system_initialize_disk_slot_mappings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_initialize_disk_slot_mappings_get`")  # noqa: E501

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
            '/v1/system/initialize/disk-slot-mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HostDiskSlotMappingsResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_nodes_get(self, **kwargs):  # noqa: E501
        """Return nodes by auto discovery  # noqa: E501

        Return nodes discovered by auto discovery.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_nodes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DiscoveredNodeInfoV2]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_initialize_nodes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Return nodes by auto discovery  # noqa: E501

        Return nodes discovered by auto discovery.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_nodes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DiscoveredNodeInfoV2]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_nodes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/initialize/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DiscoveredNodeInfoV2]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_post(self, body, **kwargs):  # noqa: E501
        """Configure and deploy a new VxRail cluster  # noqa: E501

        Configure and deploy a new VxRail cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemInitSpecV5 body: JSON configuration parameters to initialize the VxRail system (required)
        :param bool dryrun: Performs a validation of the initial input configuration. Set true to cause a dry run and false to configure and deploy a new cluster. The default value is false.
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_system_initialize_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Configure and deploy a new VxRail cluster  # noqa: E501

        Configure and deploy a new VxRail cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemInitSpecV5 body: JSON configuration parameters to initialize the VxRail system (required)
        :param bool dryrun: Performs a validation of the initial input configuration. Set true to cause a dry run and false to configure and deploy a new cluster. The default value is false.
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'dryrun']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_initialize_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dryrun' in params:
            query_params.append(('dryrun', params['dryrun']))  # noqa: E501

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
            '/v1/system/initialize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse202',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_status_get(self, **kwargs):  # noqa: E501
        """Get VxRail cluster configuration and deployment status  # noqa: E501

        Retrieve VxRail cluster configuration and deployment status information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_status_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Day1RequestInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_status_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_status_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_initialize_status_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get VxRail cluster configuration and deployment status  # noqa: E501

        Retrieve VxRail cluster configuration and deployment status information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_status_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Day1RequestInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_status_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/initialize/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Day1RequestInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_system_initialize_customer_supplied_hosts_post(self, body, **kwargs):  # noqa: E501
        """Return nodes by customer supplied management IP  # noqa: E501

        Return nodes by the customer supplied node management IP address and ESXi root password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_system_initialize_customer_supplied_hosts_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[CustomerSuppliedHostInfo] body: Management IP and password for all customer supplied hosts (required)
        :return: DiscoveredNodesInfoV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_system_initialize_customer_supplied_hosts_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_system_initialize_customer_supplied_hosts_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v2_system_initialize_customer_supplied_hosts_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Return nodes by customer supplied management IP  # noqa: E501

        Return nodes by the customer supplied node management IP address and ESXi root password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_system_initialize_customer_supplied_hosts_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[CustomerSuppliedHostInfo] body: Management IP and password for all customer supplied hosts (required)
        :return: DiscoveredNodesInfoV3
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
                    " to method v2_system_initialize_customer_supplied_hosts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_system_initialize_customer_supplied_hosts_post`")  # noqa: E501

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
            '/v2/system/initialize/customer-supplied-hosts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscoveredNodesInfoV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_system_initialize_nodes_get(self, **kwargs):  # noqa: E501
        """Return nodes by auto discovery  # noqa: E501

        Return nodes discovered by auto discovery.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_system_initialize_nodes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DiscoveredNodesInfoV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_system_initialize_nodes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Return nodes by auto discovery  # noqa: E501

        Return nodes discovered by auto discovery.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_system_initialize_nodes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DiscoveredNodesInfoV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_system_initialize_nodes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/system/initialize/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscoveredNodesInfoV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
