import re

from django.test import TestCase
from frontend.time_to_string_converter import TimeConverter


class LastUsageString(TestCase):

    minute = 60
    hour = 3600

    def test_text_formater_gets_initial_value(self):
        initial_value = TimeConverter
        self.assertIsNotNone(initial_value)

    def test_last_usage_zero_seconds_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(0)

        self.assertEqual(reply_text, "less than second")

    def test_last_usage_second_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(1)

        self.assertEqual(reply_text, "1 second")

    def test_last_usage_seconds_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(5)

        self.assertEqual(reply_text, "5 seconds")

    def test_last_usage_minute_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(65)

        self.assertEqual(reply_text, "about a minute")

    def test_last_usage_minutes_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(5 * self.minute)

        self.assertEqual(reply_text, "5 minutes")

    def test_last_usage_hour_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(75 * self.minute)

        self.assertEqual(reply_text, "more than hour")

    def test_last_usage_hours_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(3 * self.hour)

        self.assertEqual(reply_text, "3 hours")

    def test_last_usage_too_long_returned_correctly(self):
        reply_text = TimeConverter.time_ago_seconds_to_text(25 * self.hour)

        self.assertEqual(reply_text, "way too long")

    def test_last_usage_full_text(self):
        reply_text = TimeConverter.get_last_usage_string()

        regex_pattern = "(less than|second|seconds|minute) ago"

        match_found = re.search(regex_pattern, reply_text)

        self.assertTrue(match_found)
