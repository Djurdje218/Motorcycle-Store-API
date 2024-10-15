# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.motorcycle import Motorcycle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_motorcycles_get(self):
        """Test case for motorcycles_get

        Get a list of all motorcycles
        """
        response = self.client.open(
            '/motorcycles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_motorcycles_id_delete(self):
        """Test case for motorcycles_id_delete

        Delete a motorcycle by ID
        """
        response = self.client.open(
            '/motorcycles/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_motorcycles_id_get(self):
        """Test case for motorcycles_id_get

        Get a specific motorcycle by ID
        """
        response = self.client.open(
            '/motorcycles/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_motorcycles_id_put(self):
        """Test case for motorcycles_id_put

        Update a motorcycle by ID
        """
        body = Motorcycle()
        response = self.client.open(
            '/motorcycles/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_motorcycles_post(self):
        """Test case for motorcycles_post

        Add a new motorcycle to the store
        """
        body = Motorcycle()
        response = self.client.open(
            '/motorcycles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
