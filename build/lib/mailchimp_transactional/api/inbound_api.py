# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.31
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class InboundApi(object):
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

    def add_domain(self, body = {}, **kwargs):  # noqa: E501
        """Add inbound domain  # noqa: E501

        Add an inbound domain to your account.  # noqa: E501
        """
        (data) = self.add_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add inbound domain  # noqa: E501

        Add an inbound domain to your account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/add-domain', 'POST',
            body=body_params,
            response_type='InlineResponse2006') # noqa: E501

    def add_route(self, body = {}, **kwargs):  # noqa: E501
        """Add mailbox route  # noqa: E501

        Add a new mailbox route to an inbound domain.  # noqa: E501
        """
        (data) = self.add_route_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_route_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add mailbox route  # noqa: E501

        Add a new mailbox route to an inbound domain.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_route" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/add-route', 'POST',
            body=body_params,
            response_type='InlineResponse20010') # noqa: E501

    def check_domain(self, body = {}, **kwargs):  # noqa: E501
        """Check domain settings  # noqa: E501

        Check the MX settings for an inbound domain. The domain must have already been added with the add-domain call.  # noqa: E501
        """
        (data) = self.check_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def check_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Check domain settings  # noqa: E501

        Check the MX settings for an inbound domain. The domain must have already been added with the add-domain call.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/check-domain', 'POST',
            body=body_params,
            response_type='InlineResponse2007') # noqa: E501

    def delete_domain(self, body = {}, **kwargs):  # noqa: E501
        """Delete inbound domain  # noqa: E501

        Delete an inbound domain from the account. All mail will stop routing for this domain immediately.  # noqa: E501
        """
        (data) = self.delete_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete inbound domain  # noqa: E501

        Delete an inbound domain from the account. All mail will stop routing for this domain immediately.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/delete-domain', 'POST',
            body=body_params,
            response_type='InlineResponse2008') # noqa: E501

    def delete_route(self, body = {}, **kwargs):  # noqa: E501
        """Delete mailbox route  # noqa: E501

        Delete an existing inbound mailbox route.  # noqa: E501
        """
        (data) = self.delete_route_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_route_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete mailbox route  # noqa: E501

        Delete an existing inbound mailbox route.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_route" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/delete-route', 'POST',
            body=body_params,
            response_type='InlineResponse20012') # noqa: E501

    def domains(self, body = {}, **kwargs):  # noqa: E501
        """List inbound domains  # noqa: E501

        List the domains that have been configured for inbound delivery.  # noqa: E501
        """
        (data) = self.domains_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def domains_with_http_info(self, body, **kwargs):  # noqa: E501
        """List inbound domains  # noqa: E501

        List the domains that have been configured for inbound delivery.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/domains', 'POST',
            body=body_params,
            response_type='list[InlineResponse2005]') # noqa: E501

    def routes(self, body = {}, **kwargs):  # noqa: E501
        """List mailbox routes  # noqa: E501

        List the mailbox routes defined for an inbound domain.  # noqa: E501
        """
        (data) = self.routes_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def routes_with_http_info(self, body, **kwargs):  # noqa: E501
        """List mailbox routes  # noqa: E501

        List the mailbox routes defined for an inbound domain.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method routes" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/routes', 'POST',
            body=body_params,
            response_type='list[InlineResponse2009]') # noqa: E501

    def send_raw(self, body = {}, **kwargs):  # noqa: E501
        """Send mime document  # noqa: E501

        Take a raw MIME document destined for a domain with inbound domains set up, and send it to the inbound hook exactly as if it had been sent over SMTP.  # noqa: E501
        """
        (data) = self.send_raw_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def send_raw_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send mime document  # noqa: E501

        Take a raw MIME document destined for a domain with inbound domains set up, and send it to the inbound hook exactly as if it had been sent over SMTP.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_raw" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/send-raw', 'POST',
            body=body_params,
            response_type='list[InlineResponse20013]') # noqa: E501

    def update_route(self, body = {}, **kwargs):  # noqa: E501
        """Update mailbox route  # noqa: E501

        Update the pattern or webhook of an existing inbound mailbox route. If null is provided for any fields, the values will remain unchanged.  # noqa: E501
        """
        (data) = self.update_route_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def update_route_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update mailbox route  # noqa: E501

        Update the pattern or webhook of an existing inbound mailbox route. If null is provided for any fields, the values will remain unchanged.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_route" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/inbound/update-route', 'POST',
            body=body_params,
            response_type='InlineResponse20011') # noqa: E501
