# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import clever
from clever.rest import ApiException
from clever.apis.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    """ EventsApi unit test stubs """

    def setUp(self):
        self.api = clever.apis.events_api.EventsApi()
        self.api.api_client.configuration.access_token = 'TEST_TOKEN'

    def tearDown(self):
        pass

    def test_get_event(self):
        """
        Test case for get_event

        
        """
        pass

    def test_get_events(self):
        """
        Test case for get_events


        """

        # Check event class is properly set
        response = self.api.get_events(limit=1)
        event = response.data[0]
        event_class = type(event.data).__name__
        self.assertTrue(event_class != 'Event')
        self.assertTrue(event_class.endswith('Created') or event_class.endswith('Updated') or event_class.endswith('Deleted'))

    def test_get_events_for_school(self):
        """
        Test case for get_events_for_school


        """
        pass

    def test_get_events_for_school_admin(self):
        """
        Test case for get_events_for_school_admin

        
        """
        pass

    def test_get_events_for_section(self):
        """
        Test case for get_events_for_section

        
        """
        pass

    def test_get_events_for_student(self):
        """
        Test case for get_events_for_student

        
        """
        pass

    def test_get_events_for_teacher(self):
        """
        Test case for get_events_for_teacher

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
