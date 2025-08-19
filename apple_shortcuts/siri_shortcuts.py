"""
Siri Shortcuts functionality for Atlas
"""

import json
import os
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
from enum import Enum


class ActionType(Enum):
    """Supported action types for Siri shortcuts"""

    LOG_ENTRY = "log_entry"
    START_TIMER = "start_timer"
    CREATE_NOTE = "create_note"
    CAPTURE_URL = "capture_url"
    VOICE_MEMO = "voice_memo"


@dataclass
class SiriShortcut:
    """Dataclass for Siri shortcut definitions"""

    name: str
    phrase: str
    action: ActionType
    parameters: Dict[str, Any]
    content_types: List[str]  # Supported content types (URL, text, voice, image, file)

    def __post_init__(self):
        """Validate parameters after initialization"""
        self.validate_parameters()

    def validate_parameters(self):
        """Validate parameters based on action type"""
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(self.phrase, str) or not self.phrase.strip():
            raise ValueError("Phrase must be a non-empty string")

        if not isinstance(self.action, ActionType):
            raise ValueError("Action must be an ActionType enum")

        if not isinstance(self.parameters, dict):
            raise ValueError("Parameters must be a dictionary")

        if not isinstance(self.content_types, list):
            raise ValueError("Content types must be a list")

        # Validate content types
        valid_content_types = ["URL", "text", "voice", "image", "file"]
        for content_type in self.content_types:
            if content_type not in valid_content_types:
                raise ValueError(
                    f"Invalid content type: {content_type}. Valid types: {valid_content_types}"
                )

        # Action-specific parameter validation
        if self.action == ActionType.LOG_ENTRY:
            if "type" not in self.parameters:
                raise ValueError("LOG_ENTRY action requires 'type' parameter")
        elif self.action == ActionType.START_TIMER:
            if "duration" in self.parameters and not isinstance(
                self.parameters["duration"], (int, float)
            ):
                raise ValueError("START_TIMER duration must be a number")
        elif self.action == ActionType.CREATE_NOTE:
            if "title" in self.parameters and not isinstance(
                self.parameters["title"], str
            ):
                raise ValueError("CREATE_NOTE title must be a string")
        elif self.action == ActionType.VOICE_MEMO:
            # Voice memo specific validation
            if "transcription" in self.parameters and not isinstance(
                self.parameters["transcription"], bool
            ):
                raise ValueError("VOICE_MEMO transcription parameter must be a boolean")

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data["action"] = self.action.value
        return data


class ShortcutTemplate:
    """Template class for .shortcut file generation"""

    def __init__(self):
        pass

    def generate_shortcut_file(self, shortcut: SiriShortcut) -> Dict[str, Any]:
        """Generate a .shortcut file structure"""
        # This represents a more complete .shortcut file structure
        shortcut_data = {
            "WFWorkflowActions": [
                {
                    "WFWorkflowActionIdentifier": f"is.workflow.actions.{shortcut.action.value}",
                    "WFWorkflowActionParameters": {
                        "phrase": shortcut.phrase,
                        "parameters": shortcut.parameters,
                    },
                }
            ],
            "WFWorkflowIcon": {
                "WFWorkflowIconGlyphNumber": 59845,
                "WFWorkflowIconStartColor": 2071128575,
            },
            "WFWorkflowImportQuestions": [],
            "WFWorkflowInputContentItemClasses": [
                "WFAppStoreAppContentItem",
                "WFArticleContentItem",
                "WFContactContentItem",
                "WFDateContentItem",
                "WFEmailAddressContentItem",
                "WFGenericFileContentItem",
                "WFImageContentItem",
                "WFIMessageAttachmentContentItem",
                "WFMediaContentItem",
                "WFNumberContentItem",
                "WFPhoneNumberContentItem",
                "WFPhotoMediaContentItem",
                "WFReminderContentItem",
                "WFSafariWebPageContentItem",
                "WFStringContentItem",
                "WFURLContentItem",
            ],
            "WFWorkflowTypes": ["WatchKit", "ActionExtension"],
            "WFWorkflowClientVersion": "1040.24",
            "WFWorkflowClientRelease": "2.1",
            "WFWorkflowMinimumClientVersion": 900,
            "WFWorkflowMinimumClientRelease": "2.0",
        }
        return shortcut_data

    def generate_voice_capture_template(self) -> Dict[str, Any]:
        """Generate a template for voice-activated content capture"""
        template = {
            "WFWorkflowActions": [
                {
                    "WFWorkflowActionIdentifier": "is.workflow.actions.recordaudio",
                    "WFWorkflowActionParameters": {
                        "WFRecordingCompression": "Medium",
                        "WFRecordingStart": "Immediately",
                        "WFRecordingEnd": "After Time",
                        "WFRecordingTimeInterval": 300,  # 5 minutes
                    },
                },
                {
                    "WFWorkflowActionIdentifier": "is.workflow.actions.sendtoapp",
                    "WFWorkflowActionParameters": {
                        "WFAppName": "Atlas",
                        "WFInput": "Recorded Audio",
                    },
                },
            ],
            "WFWorkflowIcon": {
                "WFWorkflowIconGlyphNumber": 59845,
                "WFWorkflowIconStartColor": 2071128575,
            },
            "WFWorkflowImportQuestions": [],
            "WFWorkflowInputContentItemClasses": ["WFMediaContentItem"],
            "WFWorkflowTypes": ["WatchKit"],
            "WFWorkflowClientVersion": "1040.24",
            "WFWorkflowClientRelease": "2.1",
            "WFWorkflowMinimumClientVersion": 900,
            "WFWorkflowMinimumClientRelease": "2.0",
            "WFWorkflowName": "Hey Siri, save to Atlas",
            "WFWorkflowDescription": "Voice-activated content capture for Atlas",
        }
        return template

    def save_shortcut_file(self, shortcut: SiriShortcut, filepath: str) -> str:
        """Save a shortcut to a .shortcut file"""
        shortcut_data = self.generate_shortcut_file(shortcut)
        with open(filepath, "w") as f:
            json.dump(shortcut_data, f, indent=2)
        return filepath

    def save_voice_template(self, filepath: str) -> str:
        """Save the voice capture template to a .shortcut file"""
        template_data = self.generate_voice_capture_template()
        with open(filepath, "w") as f:
            json.dump(template_data, f, indent=2)
        return filepath


class SiriShortcutManager:
    """Manage Siri shortcuts for Atlas"""

    def __init__(self, shortcuts_dir: str = "shortcuts"):
        self.shortcuts_dir = shortcuts_dir
        os.makedirs(shortcuts_dir, exist_ok=True)
        self.template_generator = ShortcutTemplate()

    def create_shortcut(
        self,
        name: str,
        phrase: str,
        action: ActionType,
        parameters: Optional[Dict[str, Any]] = None,
        content_types: Optional[List[str]] = None,
    ) -> str:
        """Create a new Siri shortcut"""
        try:
            shortcut = SiriShortcut(
                name=name,
                phrase=phrase,
                action=action,
                parameters=parameters or {},
                content_types=content_types or ["text"],
            )
        except ValueError as e:
            raise ValueError(f"Invalid shortcut parameters: {e}")
        except Exception as e:
            raise Exception(f"Failed to create shortcut: {e}")

        # Save as JSON for internal use
        json_filepath = os.path.join(self.shortcuts_dir, f"{name}.json")
        try:
            with open(json_filepath, "w") as f:
                json.dump(shortcut.to_dict(), f, indent=2)
        except Exception as e:
            raise Exception(f"Failed to save shortcut JSON file: {e}")

        # Save as .shortcut file for iOS import
        shortcut_filepath = os.path.join(self.shortcuts_dir, f"{name}.shortcut")
        try:
            self.template_generator.save_shortcut_file(shortcut, shortcut_filepath)
        except Exception as e:
            raise Exception(f"Failed to save shortcut file: {e}")

        return json_filepath

    def create_voice_capture_shortcut(self) -> str:
        """Create the "Hey Siri, save to Atlas" voice capture shortcut"""
        filepath = os.path.join(self.shortcuts_dir, "hey_siri_save_to_atlas.shortcut")
        try:
            self.template_generator.save_voice_template(filepath)
            return filepath
        except Exception as e:
            raise Exception(f"Failed to create voice capture shortcut: {e}")

    def execute_shortcut(self, name: str) -> Dict[str, Any]:
        """Execute a Siri shortcut by name"""
        filepath = os.path.join(self.shortcuts_dir, f"{name}.json")
        if not os.path.exists(filepath):
            return {"error": f"Shortcut '{name}' not found"}

        try:
            with open(filepath, "r") as f:
                shortcut_data = json.load(f)
        except json.JSONDecodeError as e:
            return {"error": f"Malformed shortcut file for '{name}': {e}"}
        except Exception as e:
            return {"error": f"Failed to read shortcut file for '{name}': {e}"}

        # In a real implementation, this would actually execute the action
        # For now, we'll just return the shortcut data
        return {"status": "executed", "shortcut": shortcut_data}

    def list_shortcuts(self) -> Dict[str, Any]:
        """List all available shortcuts"""
        shortcuts = {}
        for filename in os.listdir(self.shortcuts_dir):
            if filename.endswith(".json"):
                name = filename[:-5]  # Remove .json extension
                filepath = os.path.join(self.shortcuts_dir, filename)
                try:
                    with open(filepath, "r") as f:
                        shortcuts[name] = json.load(f)
                except json.JSONDecodeError:
                    # Skip malformed files
                    continue
                except Exception:
                    # Skip files with other errors
                    continue
        return shortcuts

    def validate_shortcut_file(self, name: str) -> Dict[str, Any]:
        """Validate a shortcut file for errors"""
        filepath = os.path.join(self.shortcuts_dir, f"{name}.json")
        if not os.path.exists(filepath):
            return {"valid": False, "error": f"Shortcut '{name}' not found"}

        try:
            with open(filepath, "r") as f:
                data = json.load(f)

            # Validate required fields
            required_fields = ["name", "phrase", "action"]
            for field in required_fields:
                if field not in data:
                    return {"valid": False, "error": f"Missing required field: {field}"}

            # Validate action
            try:
                ActionType(data["action"])
            except ValueError:
                return {"valid": False, "error": f"Invalid action: {data['action']}"}

            return {"valid": True, "message": "Shortcut file is valid"}

        except json.JSONDecodeError as e:
            return {"valid": False, "error": f"Malformed JSON: {e}"}
        except Exception as e:
            return {"valid": False, "error": f"Validation error: {e}"}

    def process_voice_memo(
        self, audio_data: bytes, metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process a voice memo with transcription (stub implementation)"""
        # This is a stub implementation - in a real implementation, this would:
        # 1. Save the audio data to a file
        # 2. Call the VoiceProcessor from voice_processing.py
        # 3. Return the transcription and analysis results

        # For now, we'll return a placeholder result
        return {
            "status": "processed",
            "transcript": "[Voice memo processed - transcription would appear here]",
            "confidence": 0.95,
            "language": "en",
            "duration": len(audio_data) / (44100 * 2),  # Rough estimate
            "speaker_count": 1,
            "emotional_tone": "neutral",
            "key_topics": ["voice_memo"],
            "action_items": [],
            "summary": "Voice memo captured via Siri shortcut",
            "processing_time": 0.1,
            "audio_quality": "good",
        }
