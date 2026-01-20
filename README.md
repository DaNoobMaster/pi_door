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


