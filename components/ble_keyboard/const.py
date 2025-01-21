"""BleKeyboard component const."""

# pylint: disable=line-too-long

from __future__ import annotations

from typing import Final

import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.components.number import NumberMode
from esphome.const import (
    CONF_DEVICE_CLASS,
    CONF_DISABLED_BY_DEFAULT,
    CONF_ENTITY_CATEGORY,
    CONF_ICON,
    CONF_ID,
    CONF_INITIAL_VALUE,
    CONF_MAX_VALUE,
    CONF_MIN_VALUE,
    CONF_MODE,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_RESTORE_VALUE,
    CONF_STEP,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_VALUE,
    DEVICE_CLASS_CONNECTIVITY,
    ENTITY_CATEGORY_CONFIG,
    UNIT_MILLISECOND,
    UNIT_PERCENT,
)

DOMAIN: Final = "ble_keyboard"

CONF_TEXT: Final = "text"
CONF_KEYS: Final = "keys"
CONF_RECONNECT: Final = "reconnect"
CONF_BUTTONS: Final = "buttons"
CONF_USE_DEFAULT_LIBS: Final = "use_default_libs"

COMPONENT_CLASS: Final = "Esp32BleKeyboard"
COMPONENT_NUMBER_CLASS: Final = "Esp32BleKeyboardNumber"
COMPONENT_BUTTON_CLASS: Final = "Esp32BleKeyboardButton"

ACTION_START_CLASS: Final = "Esp32BleKeyboardStartAction"
ACTION_STOP_CLASS: Final = "Esp32BleKeyboardStopAction"
ACTION_PRINT_CLASS: Final = "Esp32BleKeyboardPrintAction"
ACTION_PRESS_CLASS: Final = "Esp32BleKeyboardPressAction"
ACTION_RELEASE_CLASS: Final = "Esp32BleKeyboardReleaseAction"
ACTION_COMBINATION_CLASS: Final = "Esp32BleKeyboardCombinationAction"

"""Libraries"""
LIBS_DEFAULT: Final = [
    ("ESP32 BLE Arduino", "1.0.1", None),
]

LIBS_ADDITIONAL: Final = [
    (
        "h2zero/NimBLE-Arduino",
        "1.4.0",
        None,
    ),
    (
        "t-vk/ESP32 BLE Keyboard",
        "0.3.2",
        None,
    ),
]

BUILD_FLAGS: Final = "-D USE_NIMBLE"

"""Binary sensors"""
BINARY_SENSOR_STATE: Final = {
    CONF_ID: cv.declare_id(binary_sensor.BinarySensor)("connected"),
    CONF_NAME: "Connected",
    CONF_DEVICE_CLASS: DEVICE_CLASS_CONNECTIVITY,
    CONF_DISABLED_BY_DEFAULT: False,
}

"""Numbers"""
TYPE_PRESS: Final = 0
TYPE_RELEASE: Final = 1
TYPE_BATTERY_LEVEL: Final = 2

NUMBERS: Final = [
    {
        CONF_ID: "press_delay",
        CONF_NAME: "Delay press",
        CONF_TYPE: TYPE_PRESS,
        CONF_DISABLED_BY_DEFAULT: False,
        CONF_OPTIMISTIC: True,
        CONF_MIN_VALUE: 1.0,
        CONF_MAX_VALUE: 60000.0,
        CONF_STEP: 1.0,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MILLISECOND,
        CONF_RESTORE_VALUE: True,
        CONF_INITIAL_VALUE: 8.0,
        CONF_MODE: NumberMode.NUMBER_MODE_AUTO,
        CONF_ENTITY_CATEGORY: cv.entity_category(ENTITY_CATEGORY_CONFIG),
    },
    {
        CONF_ID: "release_delay",
        CONF_NAME: "Delay release",
        CONF_TYPE: TYPE_RELEASE,
        CONF_DISABLED_BY_DEFAULT: False,
        CONF_OPTIMISTIC: True,
        CONF_MIN_VALUE: 1.0,
        CONF_MAX_VALUE: 60000.0,
        CONF_STEP: 1.0,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MILLISECOND,
        CONF_RESTORE_VALUE: True,
        CONF_INITIAL_VALUE: 8.0,
        CONF_MODE: NumberMode.NUMBER_MODE_AUTO,
        CONF_ENTITY_CATEGORY: cv.entity_category(ENTITY_CATEGORY_CONFIG),
    }
]

"""Buttons"""
BUTTONS_KEY: Final = [
    {
        CONF_NAME: "Next track",
        CONF_ID: "key_media_next_track",
        CONF_ICON: "mdi:skip-next",
        CONF_VALUE: (1, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Previous track",
        CONF_ID: "key_media_previous_track",
        CONF_ICON: "mdi:skip-previous",
        CONF_VALUE: (2, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Stop",
        CONF_ID: "key_media_stop",
        CONF_ICON: "mdi:stop",
        CONF_VALUE: (4, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Play/Pause",
        CONF_ID: "key_media_play_pause",
        CONF_ICON: "mdi:play-pause",
        CONF_VALUE: (8, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Mute",
        CONF_ID: "key_media_mute",
        CONF_ICON: "mdi:volume-mute",
        CONF_VALUE: (16, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume up",
        CONF_ID: "key_media_volume_up",
        CONF_ICON: "mdi:volume-plus",
        CONF_VALUE: (32, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    },
    {
        CONF_NAME: "Volume down",
        CONF_ID: "key_media_volume_down",
        CONF_ICON: "mdi:volume-minus",
        CONF_VALUE: (64, 0),
        CONF_DISABLED_BY_DEFAULT: False,
    }
]
