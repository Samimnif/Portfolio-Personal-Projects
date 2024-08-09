# Office Sign MicroPython V3
> Date: Aug 9th, 2024

> [!IMPORTANT]
> This Version is completely redesgned comparing to previous versions.
> This version Uses ESP32 microcontroller compared to V2 which is using a Raspi Pico

## Table of Content
1. [Composition](#composition)
2. [Pin Connections For the Sign](#pin-connections-for-the-sign)
   1. [For LED Matrix](#for-led-matrix)
   2. [For Buttons](#for-buttons)
3. [3D Printed Parts](#3d-printed-parts)
4. [Pin Connections For the Controller](#pin-connections-for-the-controller)
   1. [For OLED Screen](#for-oled-screen)
   2. [For Buttons](#for-buttons-1)

## Composition
The office Sign is composed of:
1. (MAIN LED controller) ESP32 PICO - [M5Stamp PICO](https://docs.m5stack.com/en/core/stamp_pico)
2. (Remote Control) ESP32 PICO **ATOM Lite** - [M5Stack ATOM Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
3. Buttons
4. LED Matrix - [MAX7219](https://a.co/d/8e53JXK)

## 3D Printed Parts
1. Main Sign Case &rarr; **office-sign-case v5.stl**
2. Main Sign Gap fillers &rarr; **support and gap fillers.stl**

## Pin Connections For the Sign
### For LED Matrix:
1. CLK &rarr; GP18
2. CS &rarr; GP19
3. DIN &rarr; GP26
4. GND &rarr; GND
5. VCC &rarr; 5V
### For Buttons:
1. WELCOME &rarr; GP25
2. CLOSED &rarr; GP22
3. BACK &rarr; GP21
4. MEETING &rarr; GP36 **(having issues with the wire connection)**

| Esp32 Prototype | Case Design |
|----| ---|
|![Prototype First Idea](/Office Sign Micropython/V3/imgs/IMG_5298.jpeg)| ![Case Design 3d Printed](/Office Sign Micropython/V3/imgs/IMG_5405.jpeg) |

| Back Wiring | Fron Wiring |
|----| ---|
| ![Back Wiring for Buttons](/Office Sign Micropython/V3/imgs/IMG_5407.jpeg) | ![Front Wireing and Connections](/Office Sign Micropython/V3/imgs/IMG_5408.jpeg) |

| Close Up Front Wiring |
|----|
| ![Front wireing for the led matrix](/Office Sign Micropython/V3/imgs/IMG_5409.jpeg)|



## Pin Connections For the Controller
> [!TIP]
> You can use any esp32 microcontroller that supports ESPNOW comms. I had ATOM Lite from M5Stack lating around.

### For OLED Screen:
1. SDA &rarr; GP21
2. SCK &rarr; GP25
3. VCC &rarr; 3v3
4. GND &rarr; GND
### For Buttons:
1. WELCOME &rarr; GP22
2. CLOSED &rarr; GP19
3. BACK &rarr; GP23
4. MEETING &rarr; ButtonA single press __from M5Stack Atom Lite__
5. Unavailable &rarr; ButtonA doublePress

| Front Design Startup | Ready Screen |
| ------------ | ------------ |
| ![startup screen](/V3/imgs/IMG_5411.jpeg) | ![Ready Screen](/V3/imgs/IMG_5412.jpeg) |

| Sent & Received Screen |
| --- |
| ![Sent & Received](/V3/imgs/IMG_5413.jpeg) | 