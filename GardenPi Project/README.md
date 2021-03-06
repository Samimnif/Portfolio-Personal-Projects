# GardenPi Project
## Problem
I like growing my vegetables during the summer and it neeeds to be watered regulary because of the hot weather. I usually work everyday and sometimes I come home tired and I feel lazy going to my garden.
## Idea
GardenPi is multisensor watering device that is smart amd efficient. It has multiple sensors like soil moisture sensor, temperature sensor, motion sensor and a camera. It also includes a screen, remote control and a water pump.
## Objective
My garden is located 200m from my apartment building. There are no electric outlets for power and since the water hose is shared between neighbours, it is not possible to setup a direct water supply from the tap.
## Solution
### 1. Board
Fpr this project I am going to use a rasoberry pi zero w. Raspberry pi is a great board since it can interact with teh GPIO pins using python and its libraries.
### 2. Power solution
Since I am going to use this device during summer, the sun will be my main source of power. That is why I am going to use a solar panel to power my raspberry pi.<br>
The solar panel supplies 5v and 230mAh for the raspberry pi to function. Since we there are no sun during the night, we are going to add batteries so that it can charge during the day and use the batteries at night. The capacity of the batteries are two 2400mAh 3.7V, in total 4800mAh (parallel cells).<br>
To make sure the batteries charge and raspberry pi getting power, we will be using a TP4056 controller that charges the batteries and supply power.<br>
The controller will be supplying 3.7V from the batteries. We will be using a DC to DC converter to increase the voltage to 5V (the working volatage for raspberry pi).<br>
From the converter we will be plugging the Vout+ to the 5V pin in raspberry pi's pins and plug Vout- in the ground pin of raspberry pi.<br>
Now we solved the power issue of the project.<br>
### 3. Sensors and Electronic Components
We have 4 seonsors + a camera all connected to the raspberry pi.<br>
**_I._ Sensors:**
   - **a. Motion Detection sensor**:
This sensor will be helping us to detect movement nearby. Once it detects motion we will instruct raspberry pi to take a picture, store it and send a notification through radio frequency signal.
   - **b. Soil Moisture sensor**:
The soil moisture sensor detects the moisture of the soil. If the soil is dry we will instruct raspberry pi to enable the water pump to water the plants.
   - **c. Temperature & Humidity sensor**:
The sensor will be recording the temperature at the site of the GradenPi and will send us the data through rf signal. This sensor will be more helpful in the future to implement other functionalities.
   - **d. Infrared Signal Receiver**:
This receiver will let us controlm the GardenPi manually with a remote controller.
