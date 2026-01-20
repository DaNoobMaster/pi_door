#Pi_Door
Ths project is a smart door lock created using a raspberry pi zero 2w. This is the cheapest raspberry pi capable of running what i want this project needs.
The door is capable of Face ID, Palm vein recognition, fingerprint and has a 4x4 keypad entry as well. QR codes can be generated for one time use to open the door as well.
It uses high-end secure biometric components in order to keep it reliable and safe. There is a live camera feed as well that would be transmitted from the camera to the local raspberry pi server.

The aim of this project is to make entering my house quicker and more reliable. Due to the fact that its mostly digital, it is less susceptible to intruder attacks and can help catch intruders if an attack does occur. The live camera feed is also helpful in checking who is at your at door. I belive this project would use my skills to the most. Its mechanical and software aspect is perfect for me to improve my skills and learn how to work with such types of hardware.


The 4x3 keypad can be used to enter in a pincode.
The pincode can be set to be however long.
Pressing # enters the code while * resets it. If no user input is present for 10 seconds, the code entry cache resets. If the door unlocks using other means, the code entry cache resets.
The fingerprint sensor has a 



<img width="1467" height="838" alt="image" src="https://github.com/user-attachments/assets/89ca3128-0ba1-494d-8a13-542e06ba3c86" />

### Complete Hardware Wiring (As per Schematic)

| Subsystem | Device Pin / Signal | Connected To | Raspberry Pi Pin | GPIO / Voltage | Notes |
|----------|---------------------|--------------|------------------|----------------|-------|
| **AI Camera (Face / Palm)** | VCC | Pi 5V | Pin 4 | 5V | Camera power |
| AI Camera | GND | Pi GND | Pin 6 | GND | Common ground |
| AI Camera | UART_TX | Pi RX | Pin 10 | GPIO15 (RXD) | Camera → Pi |
| AI Camera | UART_RX | Pi TX | Pin 8 | GPIO14 (TXD) | Pi → Camera |
| **Fingerprint Sensor (via CP2102)** | VIN | CP2102 3V3 | — | 3.3V | Sensor power |
| Fingerprint | GND | CP2102 GND | — | GND | Common ground |
| Fingerprint | RX | CP2102 TXD | — | UART TX |
| Fingerprint | TX | CP2102 RXI | — | UART RX |
| Fingerprint | RST | CP2102 DTR | — | Reset |
| CP2102 | USB | Raspberry Pi | USB | — | USB-UART |
| **3×4 Keypad** | K1 (Row 1) | Pi GPIO | Pin 29 | GPIO5 | Output |
| Keypad | K2 (Row 2) | Pi GPIO | Pin 31 | GPIO6 | Output |
| Keypad | K3 (Row 3) | Pi GPIO | Pin 33 | GPIO13 | Output |
| Keypad | K4 (Row 4) | Pi GPIO | Pin 35 | GPIO19 | Output |
| Keypad | K5 (Col 1) | Pi GPIO | Pin 37 | GPIO26 | Input (PU) |
| Keypad | K6 (Col 2) | Pi GPIO | Pin 38 | GPIO20 | Input (PU) |
| Keypad | K7 (Col 3) | Pi GPIO | Pin 40 | GPIO21 | Input (PU) |
| Keypad | K8 | — | — | NC | Not connected |
| Keypad | K9 | — | — | NC | Not connected |
| Relay | Relay VCC | Pi 5V | Pin 4 | 5V | Coil power |
| Relay | Relay GND | Pi GND | Pin 6 | GND | Ground |
| **Transistor (BC107)** | Base | Pi GPIO (via resistor) | Pin 16 | GPIO23 | Drives relay |
| Transistor | Collector | 5V | — | 5V | From voltage convertor |
| Transistor | Emitter | Relay Coil | — | — | Reference |
| **Solenoid Lock** | + | External Supply | — | +7.5V | Lock power |
| Solenoid | − | Relay NO Contact | — | Switched | Controlled by relay |



### Authentication Accuracy & Error Rates

| Input Method | False Acceptance Rate (FAR) | False Rejection Rate (FRR) | Notes |
|-------------|-----------------------------|-----------------------------|-------|
| Fingerprint (Capacitive) | ~0.001% – 0.01% | ~1% – 3% | High accuracy, may fail with wet or damaged fingers |
| Face Recognition (Offline AI) | ~0.1% – 1% | ~1% – 5% | Affected by lighting, pose, and occlusion |
| Palm Recognition (Offline AI) | ~0.01% – 0.1% | ~0.5% – 2% | Very stable, less affected by lighting |
| Keypad PIN (4-digit) | 0% (if secret) | User-dependent | Security depends on PIN secrecy and length |




BOM

| S.No | Component | Purpose | Estimated Cost (₹) |
|-----:|-----------|---------|-------------------:|
| 1 | Solenoid (Door Lock) | Physically locks/unlocks the door | 800 |
| 2 | Face ID & Palm Vein Sensor | Primary biometric authentication | 5636 |
| 3 | Fingerprint Sensor | Secondary authentication | 2,042.00 |
| 4 | Raspberry Pi Zero 2 W | Main controller & processing unit | 1,587.10 |
| 5 | 18650 Battery | Portable power source | 205.32 |
| 6 | Battery Charger Module | Charging the 18650 battery | 14.00 |
| 7 | Battery Holder | Secure battery mounting | 46.00 |
| 8 | UART Converter (CP2102) | Additional UART interface for fingerprint sensor | 300.00 |
| 9 | USB to Micro-USB Cable | Power & USB connection | 54.00 |
| 10 | Barrel Jack Connector | External power input | 23.00 |
| 11 | 4×3 Keypad | Manual PIN-based fallback access | 188.00 |
| 12 | BC107 Transistor | Solenoid driver / switching | 19.00 |
| 13 | 3D Printed Parts | Enclosure & mounting brackets | — |
| 14 | Acrylic Sheet | Structural housing panels | 75.00 |
| 15 | SRD-05VDC-SL-A Relay | Solenoid isolation & control | 79.00 |
| **—** | **Total Estimated Cost** |  | **11,068.42** |


