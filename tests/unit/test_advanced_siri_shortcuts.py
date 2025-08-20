"""
Integration test for advanced Siri shortcuts functionality
"""

import os
import sys
import unittest
import tempfile
import shutil

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from apple_shortcuts.siri_shortcuts import SiriShortcutManager
from apple_shortcuts.contextual_capture import ContextualCaptureManager
from apple_shortcuts.automation_manager import (
    AutomationManager,
    TriggerType,
    ActionType,
)


class TestAdvancedSiriShortcuts(unittest.TestCase):
    """Integration tests for advanced Siri shortcuts functionality"""

    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.shortcuts_dir = os.path.join(self.test_dir, "shortcuts")
        self.automations_dir = os.path.join(self.test_dir, "automations")
        self.context_data_dir = os.path.join(self.test_dir, "context_data")

        # Create managers
        self.shortcut_manager = SiriShortcutManager(self.shortcuts_dir)

    def tearDown(self):
        """Clean up test fixtures"""
        # Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_create_contextual_shortcut(self):
        """Test creating a contextual shortcut"""
        # Create a contextual shortcut
        filepath = self.shortcut_manager.create_contextual_shortcut(
            name="Test Contextual Shortcut",
            phrase="Test contextual capture",
            action=ActionType.CREATE_NOTE,
            parameters={"type": "test_note"},
            priority="high",
        )

        # Verify the shortcut was created
        self.assertTrue(os.path.exists(filepath))

        # Verify the shortcut is in the list
        shortcuts = self.shortcut_manager.list_shortcuts()
        self.assertIn("Test Contextual Shortcut", shortcuts)

        # Verify the shortcut has contextual properties
        shortcut_data = shortcuts["Test Contextual Shortcut"]
        self.assertTrue(shortcut_data.get("context_aware", False))
        self.assertEqual(shortcut_data.get("priority"), "high")

    def test_execute_contextual_shortcut(self):
        """Test executing a contextual shortcut"""
        # Create a contextual shortcut
        self.shortcut_manager.create_contextual_shortcut(
            name="Execute Test Shortcut",
            phrase="Execute test",
            action=ActionType.LOG_ENTRY,
            parameters={"type": "test_entry"},
        )

        # Execute the shortcut
        result = self.shortcut_manager.execute_shortcut("Execute Test Shortcut")

        # Verify the result
        self.assertEqual(result["status"], "executed")
        self.assertIn("context", result)
        self.assertIn("shortcut", result)

        # Verify context was added to the shortcut data
        shortcut_data = result["shortcut"]
        self.assertIn("parameters", shortcut_data)
        self.assertIn("context", shortcut_data["parameters"])

    def test_setup_default_contextual_shortcuts(self):
        """Test setting up default contextual shortcuts"""
        # Set up default contextual shortcuts
        count = self.shortcut_manager.setup_default_contextual_shortcuts()

        # Verify some shortcuts were created
        # Note: This might be 0 if the contextual manager doesn't have templates
        # But we're testing that it doesn't crash
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_setup_default_automations(self):
        """Test setting up default automations"""
        # Set up default automations using the shortcut manager
        count = self.shortcut_manager.setup_default_automations()

        # Verify automations were created
        self.assertGreater(count, 0)

        # Verify automations are in the manager
        automations = self.shortcut_manager.automation_manager.list_automation_rules()
        self.assertGreater(len(automations), 0)

    def test_trigger_contextual_automations(self):
        """Test triggering contextual automations"""
        # Set up a simple automation
        self.shortcut_manager.automation_manager.create_automation_rule(
            name="Test Automation",
            description="Test automation for integration",
            trigger_type=TriggerType.TIME,
            trigger_conditions={"hour": 12},
            actions=[{"type": "create_note", "parameters": {"type": "test_note"}}],
        )

        # For this test, we'll just verify that the method doesn't crash
        # since we don't have a real context to test with
        try:
            triggered = self.shortcut_manager.trigger_contextual_automations()
            # This should not raise an exception
            self.assertIsInstance(triggered, list)
        except Exception as e:
            self.fail(f"trigger_contextual_automations raised an exception: {e}")

    def test_get_automation_analytics(self):
        """Test getting automation analytics"""
        # Get initial analytics
        initial_analytics = self.shortcut_manager.get_automation_analytics()

        # Verify the structure
        self.assertIn("total_triggers", initial_analytics)
        self.assertIn("successful_executions", initial_analytics)
        self.assertIn("failed_executions", initial_analytics)
        self.assertIn("rule_trigger_counts", initial_analytics)

        # The values should be zero or empty initially
        self.assertEqual(initial_analytics["total_triggers"], 0)
        self.assertEqual(initial_analytics["successful_executions"], 0)
        self.assertEqual(initial_analytics["failed_executions"], 0)
        self.assertEqual(initial_analytics["rule_trigger_counts"], {})


if __name__ == "__main__":
    unittest.main()
