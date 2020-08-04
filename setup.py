# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.9
    Contact: apihelp@mandrill.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "mailchimp_transactional"
VERSION = "1.0.9"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "requests>=2.23",
    "six>=1.10",
    "urllib3>=1.23"
]

setup(
    name=NAME,
    version=VERSION,
    description="Mailchimp Transactional API",
    author_email="apihelp@mandrill.com",
    url="",
    keywords=["Swagger", "Mailchimp Transactional API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """
)