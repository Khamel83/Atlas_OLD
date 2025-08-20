"""
Unit tests for contextual capture functionality
"""

import os
import sys
import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from apple_shortcuts.contextual_capture import (
    ContextualCaptureManager,
    LocationContext,
    TimeContext,
    ActivityContext,
    CalendarContext,
    FocusModeContext,
)


class TestContextualCaptureManager(unittest.TestCase):
    """Test cases for ContextualCaptureManager"""

    def setUp(self):
        """Set up test fixtures"""
        self.manager = ContextualCaptureManager("test_context_data")

    def tearDown(self):
        """Clean up test fixtures"""
        # Remove test directory
        import shutil

        if os.path.exists("test_context_data"):
            shutil.rmtree("test_context_data")

    def test_get_current_time_context(self):
        """Test getting current time context"""
        with patch("apple_shortcuts.contextual_capture.datetime") as mock_datetime:
            # Mock morning time
            mock_datetime.now.return_value = datetime(
                2023, 6, 15, 8, 30, 0
            )  # Thursday, June 15, 8:30 AM
            mock_datetime.weekday.return_value = 3  # Thursday

            time_context = self.manager.get_current_time_context()

            self.assertIsInstance(time_context, TimeContext)
            self.assertEqual(time_context.hour, 8)
            self.assertEqual(time_context.day_of_week, 3)
            self.assertFalse(time_context.is_weekend)
            self.assertEqual(time_context.time_of_day, "morning")
            self.assertEqual(time_context.season, "summer")

    def test_get_contextual_categories(self):
        """Test getting contextual categories"""
        # This test uses the stub implementations which return mock data
        categories = self.manager.get_contextual_categories()
        self.assertIsInstance(categories, list)
        self.assertIn("work", categories)  # From mock location context
        self.assertIn("tasks", categories)  # From mock time context

    def test_get_contextual_priority(self):
        """Test getting contextual priority"""
        # This test uses the stub implementations which return mock data
        priority = self.manager.get_contextual_priority()
        self.assertIn(priority, ["low", "medium", "high"])
        # Based on mock data, should be "high" (work context)
        self.assertEqual(priority, "high")

    def test_create_contextual_shortcut_templates(self):
        """Test creating contextual shortcut templates"""
        templates = self.manager.create_contextual_shortcut_templates()
        self.assertIsInstance(templates, list)
        self.assertGreater(len(templates), 0)

        # Check that we have different types of templates
        template_names = [t["name"] for t in templates]
        self.assertIn("log_home_activity", template_names)
        self.assertIn("morning_routine", template_names)
        self.assertIn("commute_thought", template_names)
        self.assertIn("meeting_note", template_names)

    def test_save_and_load_context_data(self):
        """Test saving and loading context data"""
        test_data = {
            "location": {
                "latitude": 37.7749,
                "longitude": -122.4194,
                "place_name": "San Francisco",
            },
            "time": {
                "hour": 10,
                "day_of_week": 1,
                "is_weekend": False,
                "time_of_day": "morning",
            },
            "activity": {"activity_type": "working", "confidence": 0.85},
        }

        # Save data
        filepath = self.manager.save_context_data(test_data, "test_context.json")
        self.assertTrue(os.path.exists(filepath))

        # Load data
        loaded_data = self.manager.load_context_data("test_context.json")
        self.assertEqual(test_data, loaded_data)


if __name__ == "__main__":
    unittest.main()
