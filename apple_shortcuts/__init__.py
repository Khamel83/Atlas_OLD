"""
Atlas Enhanced Apple Features (Block 7)
Advanced iOS integration with contextual capture and smart processing
"""

__version__ = "1.0.0"
__author__ = "Atlas Team"

from .contextual_capture import ContextualCaptureEngine
from .voice_processing import VoiceProcessor
from .reading_list_import import ReadingListImporter
from .ios_extension import IOSShareExtension
from .siri_shortcuts import SiriShortcutManager

__all__ = [
    "ContextualCaptureEngine",
    "VoiceProcessor",
    "ReadingListImporter",
    "IOSShareExtension",
    "SiriShortcutManager",
]
