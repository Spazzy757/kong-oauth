"""
This file was taken from https://github.com/AppointmentGuru/AuthenticationGuru/blob/master/kong_oauth/kong.py
at the time of development this resource was under an MIT license
https://github.com/AppointmentGuru/AuthenticationGuru/blob/master/LICENSE
"""
from django.conf import settings
from kong.resources import API, Resource


class KongAPI(API):
    base_url = getattr(settings, 'KONG_ADMIN_URL', 'https://kong:8001')
    headers = {'content-type': 'application/json'}


class ApiResource(Resource):
    api_class = KongAPI
    resource_path = "/apis"


class ConsumerResource(Resource):
    api_class = KongAPI
    resource_path = "/consumers"


class ConsumerCredentialResource(Resource):
    api_class = KongAPI
    resource_path = "/consumers/{consumer_id}/{plugin}"


class GlobalPluginResource(Resource):
    api_class = KongAPI
    resource_path = "/plugins"


class ApiPluginResource(Resource):
    api_class = KongAPI
    resource_path = "/plugins/{api_id}/plugins"
