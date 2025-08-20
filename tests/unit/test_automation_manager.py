"""
Unit tests for automation manager functionality
"""

import os
import sys
import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from apple_shortcuts.automation_manager import (
    AutomationManager,
    AutomationRule,
    AutomationTrigger,
    AutomationAction,
    TriggerType,
    ActionType,
)


class TestAutomationManager(unittest.TestCase):
    """Test cases for AutomationManager"""

    def setUp(self):
        """Set up test fixtures"""
        self.manager = AutomationManager("test_automations")

    def tearDown(self):
        """Clean up test fixtures"""
        # Remove test directory
        import shutil

        if os.path.exists("test_automations"):
            shutil.rmtree("test_automations")

    def test_create_automation_rule(self):
        """Test creating an automation rule"""
        rule_name = self.manager.create_automation_rule(
            name="Test Rule",
            description="A test automation rule",
            trigger_type=TriggerType.TIME,
            trigger_conditions={"hour": 9},
            actions=[{"type": "create_note", "parameters": {"type": "test_note"}}],
        )

        self.assertEqual(rule_name, "Test Rule")
        self.assertIn("Test Rule", self.manager.automation_rules)

        rule = self.manager.get_automation_rule("Test Rule")
        self.assertIsInstance(rule, AutomationRule)
        self.assertEqual(rule.name, "Test Rule")
        self.assertEqual(rule.description, "A test automation rule")
        self.assertEqual(rule.trigger.trigger_type, TriggerType.TIME)
        self.assertEqual(rule.trigger.conditions, {"hour": 9})
        self.assertEqual(len(rule.actions), 1)
        self.assertEqual(rule.actions[0].action_type, ActionType.CREATE_NOTE)

    def test_save_and_load_automation_rule(self):
        """Test saving and loading an automation rule"""
        # Create a rule
        rule_name = self.manager.create_automation_rule(
            name="Save/Load Test",
            description="Test saving and loading",
            trigger_type=TriggerType.LOCATION,
            trigger_conditions={"category": "home"},
            actions=[{"type": "log_entry", "parameters": {"type": "home_arrival"}}],
        )

        # Get the rule
        original_rule = self.manager.get_automation_rule("Save/Load Test")

        # Create a new manager to test loading
        new_manager = AutomationManager("test_automations")
        loaded_rule = new_manager.get_automation_rule("Save/Load Test")

        # Compare rules
        self.assertIsNotNone(loaded_rule)
        self.assertEqual(loaded_rule.name, original_rule.name)
        self.assertEqual(loaded_rule.description, original_rule.description)
        self.assertEqual(
            loaded_rule.trigger.trigger_type, original_rule.trigger.trigger_type
        )
        self.assertEqual(
            loaded_rule.trigger.conditions, original_rule.trigger.conditions
        )
        self.assertEqual(len(loaded_rule.actions), len(original_rule.actions))
        self.assertEqual(
            loaded_rule.actions[0].action_type, original_rule.actions[0].action_type
        )

    def test_list_automation_rules(self):
        """Test listing automation rules"""
        # Create a few rules
        self.manager.create_automation_rule(
            name="Rule 1",
            description="First rule",
            trigger_type=TriggerType.TIME,
            trigger_conditions={"hour": 9},
            actions=[{"type": "create_note", "parameters": {"type": "note1"}}],
        )

        self.manager.create_automation_rule(
            name="Rule 2",
            description="Second rule",
            trigger_type=TriggerType.LOCATION,
            trigger_conditions={"category": "work"},
            actions=[{"type": "log_entry", "parameters": {"type": "log1"}}],
        )

        # Get list of rules
        rule_names = self.manager.list_automation_rules()
        self.assertIn("Rule 1", rule_names)
        self.assertIn("Rule 2", rule_names)
        self.assertEqual(len(rule_names), 2)

    def test_enable_disable_automation_rule(self):
        """Test enabling and disabling automation rules"""
        # Create a rule
        self.manager.create_automation_rule(
            name="Enable/Disable Test",
            description="Test enabling/disabling",
            trigger_type=TriggerType.TIME,
            trigger_conditions={"hour": 10},
            actions=[{"type": "create_note", "parameters": {"type": "test"}}],
        )

        # Check initial state
        rule = self.manager.get_automation_rule("Enable/Disable Test")
        self.assertTrue(rule.enabled)

        # Disable the rule
        self.manager.disable_automation_rule("Enable/Disable Test")
        rule = self.manager.get_automation_rule("Enable/Disable Test")
        self.assertFalse(rule.enabled)

        # Enable the rule
        self.manager.enable_automation_rule("Enable/Disable Test")
        rule = self.manager.get_automation_rule("Enable/Disable Test")
        self.assertTrue(rule.enabled)

    def test_delete_automation_rule(self):
        """Test deleting an automation rule"""
        # Create a rule
        self.manager.create_automation_rule(
            name="Delete Test",
            description="Test deletion",
            trigger_type=TriggerType.TIME,
            trigger_conditions={"hour": 11},
            actions=[{"type": "create_note", "parameters": {"type": "test"}}],
        )

        # Verify rule exists
        self.assertIn("Delete Test", self.manager.automation_rules)

        # Delete the rule
        self.manager.delete_automation_rule("Delete Test")

        # Verify rule is deleted
        self.assertNotIn("Delete Test", self.manager.automation_rules)
        self.assertIsNone(self.manager.get_automation_rule("Delete Test"))

    def test_evaluate_time_trigger(self):
        """Test evaluating time-based triggers"""
        # Create a time trigger
        trigger = AutomationTrigger(
            trigger_type=TriggerType.TIME,
            conditions={"hour": 9, "day_of_week": 1},  # Tuesday at 9 AM
            enabled=True,
        )

        # Test context that matches
        matching_context = {
            "time": {"hour": 9, "day_of_week": 1, "time_of_day": "morning"}
        }
        self.assertTrue(self.manager.evaluate_trigger(trigger, matching_context))

        # Test context that doesn't match
        non_matching_context = {
            "time": {"hour": 10, "day_of_week": 1, "time_of_day": "morning"}
        }
        self.assertFalse(self.manager.evaluate_trigger(trigger, non_matching_context))

    def test_evaluate_location_trigger(self):
        """Test evaluating location-based triggers"""
        # Create a location trigger
        trigger = AutomationTrigger(
            trigger_type=TriggerType.LOCATION,
            conditions={"category": "work", "place_name": "Office"},
            enabled=True,
        )

        # Test context that matches
        matching_context = {"location": {"category": "work", "place_name": "Office"}}
        self.assertTrue(self.manager.evaluate_trigger(trigger, matching_context))

        # Test context that doesn't match
        non_matching_context = {"location": {"category": "home", "place_name": "Home"}}
        self.assertFalse(self.manager.evaluate_trigger(trigger, non_matching_context))

    def test_evaluate_calendar_trigger(self):
        """Test evaluating calendar-based triggers"""
        # Create a calendar trigger
        trigger = AutomationTrigger(
            trigger_type=TriggerType.CALENDAR,
            conditions={"in_meeting": True, "event_title": "Team Meeting"},
            enabled=True,
        )

        # Test context that matches
        matching_context = {
            "calendar": {"is_ongoing": True, "event_title": "Team Meeting"}
        }
        self.assertTrue(self.manager.evaluate_trigger(trigger, matching_context))

        # Test context that doesn't match
        non_matching_context = {
            "calendar": {"is_ongoing": False, "event_title": "Team Meeting"}
        }
        self.assertFalse(self.manager.evaluate_trigger(trigger, non_matching_context))

    def test_evaluate_focus_mode_trigger(self):
        """Test evaluating focus mode triggers"""
        # Create a focus mode trigger
        trigger = AutomationTrigger(
            trigger_type=TriggerType.FOCUS_MODE,
            conditions={"is_active": True, "mode_name": "work"},
            enabled=True,
        )

        # Test context that matches
        matching_context = {"focus_mode": {"is_active": True, "mode_name": "work"}}
        self.assertTrue(self.manager.evaluate_trigger(trigger, matching_context))

        # Test context that doesn't match
        non_matching_context = {"focus_mode": {"is_active": False, "mode_name": "work"}}
        self.assertFalse(self.manager.evaluate_trigger(trigger, non_matching_context))

    def test_execute_action(self):
        """Test executing automation actions"""
        # Create an action
        action = AutomationAction(
            action_type=ActionType.CREATE_NOTE,
            parameters={"type": "test_note", "title": "Test Note"},
            delay=0,
        )

        # Execute the action
        context = {}
        result = self.manager.execute_action(action, context)

        # Check result
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["action_type"], "create_note")
        self.assertTrue(result["note_created"])
        self.assertEqual(result["note_type"], "test_note")
        self.assertEqual(result["title"], "Test Note")

    def test_create_default_automations(self):
        """Test creating default automation rules"""
        # Create default automations
        self.manager.create_default_automations()

        # Check that default rules were created
        rule_names = self.manager.list_automation_rules()
        self.assertIn("Morning Routine", rule_names)
        self.assertIn("Work Mode", rule_names)
        self.assertIn("Meeting Notes", rule_names)
        self.assertIn("Focus Time", rule_names)

        # Check specific rule details
        morning_rule = self.manager.get_automation_rule("Morning Routine")
        self.assertEqual(morning_rule.trigger.trigger_type, TriggerType.TIME)
        self.assertEqual(morning_rule.trigger.conditions["hour"], 8)
        self.assertEqual(len(morning_rule.actions), 2)
