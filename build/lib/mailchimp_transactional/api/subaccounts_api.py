# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.20
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class SubaccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_key='', api_client = None):
        self.api_key = api_key
        if api_client:
            self.api_client = api_client
        else:
            self.api_client = ApiClient()

    def add(self, body = {}, **kwargs):  # noqa: E501
        """Add subaccount  # noqa: E501

        Add a new subaccount.  # noqa: E501
        """
        (data) = self.add_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add subaccount  # noqa: E501

        Add a new subaccount.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/add', 'POST',
            body=body_params,
            response_type='InlineResponse20048') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete subaccount  # noqa: E501

        Delete an existing subaccount. Any email related to the subaccount will be saved, but stats will be removed and any future sending calls to this subaccount will fail.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete subaccount  # noqa: E501

        Delete an existing subaccount. Any email related to the subaccount will be saved, but stats will be removed and any future sending calls to this subaccount will fail.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20051') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get subaccount info  # noqa: E501

        Given the ID of an existing subaccount, return the data about it.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get subaccount info  # noqa: E501

        Given the ID of an existing subaccount, return the data about it.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method info" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/info', 'POST',
            body=body_params,
            response_type='InlineResponse20049') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List subaccounts  # noqa: E501

        Get the list of subaccounts defined for the account, optionally filtered by a prefix.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List subaccounts  # noqa: E501

        Get the list of subaccounts defined for the account, optionally filtered by a prefix.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20047]') # noqa: E501

    def pause(self, body = {}, **kwargs):  # noqa: E501
        """Pause subaccount  # noqa: E501

        Pause a subaccount's sending. Any future emails delivered to this subaccount will be queued for a maximum of 3 days until the subaccount is resumed.  # noqa: E501
        """
        (data) = self.pause_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def pause_with_http_info(self, body, **kwargs):  # noqa: E501
        """Pause subaccount  # noqa: E501

        Pause a subaccount's sending. Any future emails delivered to this subaccount will be queued for a maximum of 3 days until the subaccount is resumed.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pause" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/pause', 'POST',
            body=body_params,
            response_type='InlineResponse20052') # noqa: E501

    def resume(self, body = {}, **kwargs):  # noqa: E501
        """Resume subaccount  # noqa: E501

        Resume a paused subaccount's sending.  # noqa: E501
        """
        (data) = self.resume_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def resume_with_http_info(self, body, **kwargs):  # noqa: E501
        """Resume subaccount  # noqa: E501

        Resume a paused subaccount's sending.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resume" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/resume', 'POST',
            body=body_params,
            response_type='InlineResponse20053') # noqa: E501

    def update(self, body = {}, **kwargs):  # noqa: E501
        """Update subaccount  # noqa: E501

        Update an existing subaccount.  # noqa: E501
        """
        (data) = self.update_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def update_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update subaccount  # noqa: E501

        Update an existing subaccount.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/subaccounts/update', 'POST',
            body=body_params,
            response_type='InlineResponse20050') # noqa: E501
