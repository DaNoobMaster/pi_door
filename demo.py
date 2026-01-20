#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import serial
import RPi.GPIO as GPIO
from DFRobot_AI10 import DFRobot_AI10_UART

# =========================================================
# ======================== CONFIG =========================
# =========================================================

PIN_CODE = "1234"          # CHANGE THIS
PIN_TIMEOUT = 10           # seconds
UNLOCK_TIME = 5            # seconds door stays unlocked

# =========================================================
# ======================== GPIO ===========================
# =========================================================

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Keypad pins (FROM YOUR SCHEMATIC)
KEYPAD_ROWS = [5, 6, 13, 19]
KEYPAD_COLS = [26, 20, 21]

KEYPAD_MAP = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['*','0','#']
]

for r in KEYPAD_ROWS:
    GPIO.setup(r, GPIO.OUT)
    GPIO.output(r, GPIO.HIGH)

for c in KEYPAD_COLS:
    GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# =========================================================
# ====================== KEYPAD ===========================
# =========================================================

def get_key():
    for r_idx, r in enumerate(KEYPAD_ROWS):
        GPIO.output(r, GPIO.LOW)
        for c_idx, c in enumerate(KEYPAD_COLS):
            if GPIO.input(c) == GPIO.LOW:
                time.sleep(0.2)  # debounce
                GPIO.output(r, GPIO.HIGH)
                return KEYPAD_MAP[r_idx][c_idx]
        GPIO.output(r, GPIO.HIGH)
    return None


def check_pin():
    entered = ""
    last_key_time = time.time()

    print("Enter PIN (* = clear, # = enter):")

    while True:
        if time.time() - last_key_time > PIN_TIMEOUT:
            if entered:
                print("\nPIN timeout → reset")
            return False

        key = get_key()
        if key:
            last_key_time = time.time()

            if key == '*':
                entered = ""
                print("\nPIN cleared")

            elif key == '#':
                print("\nPIN submitted")
                return entered == PIN_CODE

            else:
                entered += key
                print("*", end="", flush=True)

        time.sleep(0.1)

# =========================================================
# =============== FINGERPRINT (WAVESHARE) =================
# =========================================================

ACK_SUCCESS = 0x00
ACK_NO_USER = 0x05

CMD_HEAD = 0xF5
CMD_TAIL = 0xF5

CMD_ADD_1    = 0x01
CMD_ADD_3    = 0x03
CMD_MATCH    = 0x0C
CMD_USER_CNT = 0x09

USER_MAX_CNT = 1000

fp_ser = serial.Serial("/dev/ttyUSB0", 19200, timeout=1)
fp_rx_buf = []


def fp_txrx(cmd, rx_len, timeout):
    global fp_rx_buf
    checksum = 0
    packet = [CMD_HEAD]

    for b in cmd:
        packet.append(b)
        checksum ^= b

    packet.append(checksum)
    packet.append(CMD_TAIL)

    fp_ser.flushInput()
    fp_ser.write(bytes(packet))

    fp_rx_buf = []
    start = time.time()

    while time.time() - start < timeout and len(fp_rx_buf) < rx_len:
        if fp_ser.in_waiting:
            fp_rx_buf += list(fp_ser.read(fp_ser.in_waiting))

    if len(fp_rx_buf) != rx_len:
        return False

    if fp_rx_buf[0] != CMD_HEAD or fp_rx_buf[-1] != CMD_TAIL:
        return False

    return True


def fp_get_user_count():
    cmd = [CMD_USER_CNT, 0, 0, 0, 0]
    if fp_txrx(cmd, 8, 0.2) and fp_rx_buf[4] == ACK_SUCCESS:
        return fp_rx_buf[3]
    return -1


def register_fingerprint():
    print("Place finger to REGISTER...")
    time.sleep(1)

    count = fp_get_user_count()
    if count < 0 or count >= USER_MAX_CNT:
        return False

    cmd = [CMD_ADD_1, 0, count + 1, 3, 0]
    if fp_txrx(cmd, 8, 6) and fp_rx_buf[4] == ACK_SUCCESS:
        cmd[0] = CMD_ADD_3
        return fp_txrx(cmd, 8, 6) and fp_rx_buf[4] == ACK_SUCCESS

    return False


def check_fingerprint():
    print("Checking FINGERPRINT...")
    time.sleep(1)

    cmd = [CMD_MATCH, 0, 0, 0, 0]
    if not fp_txrx(cmd, 8, 5):
        return False

    return fp_rx_buf[4] != ACK_NO_USER

# =========================================================
# ================= AI10 CAMERA (FACE/PALM) ================
# =========================================================

ai10 = DFRobot_AI10_UART(115200)
ai10.begin()


def register_biometric(user_name="User", admin=False, timeout=10):
    print("Present FACE or PALM to REGISTER...")
    time.sleep(1)

    result = ai10.enroll_user(
        admin=ai10.ADMIN if admin else ai10.NORMAL,
        user_name=user_name,
        timeout=timeout
    )
    return result.result == ai10.Success


def check_biometric(timeout=5):
    print("Checking FACE or PALM...")
    data = ai10.get_recognition_result(timeout)
    return data.result == ai10.Success

# =========================================================
# ===================== AUTH LOGIC ========================
# =========================================================

def authenticate():
    # Biometric camera
    if check_biometric():
        print("Biometric success → PIN reset")
        return True

    # Fingerprint
    if check_fingerprint():
        print("Fingerprint success → PIN reset")
        return True

    # Keypad PIN
    if check_pin():
        print("PIN success")
        return True

    return False

# =========================================================
# ====================== MAIN LOOP =========================
# =========================================================

if __name__ == "__main__":
    try:
        print("🔐 Smart Door Lock Ready")

        while True:
            if authenticate():
                print("🔓 DOOR UNLOCKED")
                time.sleep(UNLOCK_TIME)
            else:
                print("❌ ACCESS DENIED")

            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        fp_ser.close()
        print("\nSystem stopped")
