```python
# ============================================================
# Project: 12-Key Macro Keyboard
# Firmware: KMK + CircuitPython
# Controller: Raspberry Pi Pico
# ============================================================

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306


# ------------------------------------------------------------
# 1. KEYBOARD INITIALIZATION
# ------------------------------------------------------------

keyboard = KMKKeyboard()

# EXAMPLE PINS ONLY — CHANGE TO MATCH YOUR SCHEMATIC.
# Four columns and three rows = 12 switches.

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
)

keyboard.row_pins = (
    board.GP4,
    board.GP5,
    board.GP6,
)

# Verify diode orientation against the actual PCB.
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# ------------------------------------------------------------
# 2. MEDIA KEY SUPPORT
# ------------------------------------------------------------

keyboard.extensions.append(MediaKeys())


# ------------------------------------------------------------
# 3. ROTARY ENCODER
# ------------------------------------------------------------

encoder_handler = EncoderHandler()

# EXAMPLE PINS ONLY. Verify against your schematic.
# The encoder push switch is not assigned.
encoder_handler.pins = (
    (board.GP8, board.GP9, None),
)

# Order: anticlockwise, clockwise, push.
# The push action is intentionally unassigned.
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),)
]

keyboard.modules.append(encoder_handler)


# ------------------------------------------------------------
# 4. OLED DISPLAY
# ------------------------------------------------------------

# EXAMPLE I2C PINS ONLY.
# First argument is SCL; second argument is SDA.
i2c_bus = busio.I2C(board.GP21, board.GP20)

display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    entries=[
        TextEntry(
            text="hellow rishav",
            x=0,
            y=0,
        ),
        TextEntry(
            text="the omp boy",
            x=0,
            y=16,
        ),
    ],
)

keyboard.extensions.append(display)


# ------------------------------------------------------------
# 5. SHORTCUT MAPPINGS
# ------------------------------------------------------------

# SW1: Copy                  Ctrl + C
SW1 = KC.LCTL(KC.C)

# SW2: Paste                 Ctrl + V
SW2 = KC.LCTL(KC.V)

# SW3: Undo                  Ctrl + Z
SW3 = KC.LCTL(KC.Z)

# SW4: Screenshot tool       Win + Shift + S
SW4 = KC.LGUI(KC.LSFT(KC.S))

# SW5: Windows Search        Win + S
SW5 = KC.LGUI(KC.S)

# SW6: Switch between apps   Alt + Tab
SW6 = KC.LALT(KC.TAB)

# SW7: Save                  Ctrl + S
SW7 = KC.LCTL(KC.S)

# SW8: Select all            Ctrl + A
SW8 = KC.LCTL(KC.A)

# SW9: File Explorer         Win + E
SW9 = KC.LGUI(KC.E)

# SW10: VS Code Command Palette
# Ctrl + Shift + P
SW10 = KC.LCTL(KC.LSFT(KC.P))

# SW11: Play/Pause media
SW11 = KC.MPLY

# SW12: Open Run dialog      Win + R
SW12 = KC.LGUI(KC.R)


# ------------------------------------------------------------
# 6. KEY MATRIX
# ------------------------------------------------------------

# Assumes:
# Row 1: SW1, SW2, SW3, SW4
# Row 2: SW5, SW6, SW7, SW8
# Row 3: SW9, SW10, SW11, SW12
#
# Change this order if your physical matrix differs.

keyboard.keymap = [
    [SW1, SW2, SW3, SW4],
    [SW5, SW6, SW7, SW8],
    [SW9, SW10, SW11, SW12],
]


# ------------------------------------------------------------
# 7. START KEYBOARD
# ------------------------------------------------------------

keyboard.go()
```
