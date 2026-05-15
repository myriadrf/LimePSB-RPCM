User Interface
##############

LimePSB RPCM board features button, buzzer, 5 dual colour (red and green (RG)) LEDs, 1 green indication LED and 2 Ethernet activity LEDs (yellow and green). All board user interface components are highlighted in Figure 8.

.. figure:: /images/LimePSB-RPCM_v1.2_user_interface_components.png
  :width: 600

  Figure 9: LimePSB RPCM v1.2 user interface components
   
Dual color LEDs (LED1-LED4) are connected to shift register (IC14). Their function may be programmed according to the user requirements. Dual color LED5 indicates Raspberry Pi status. Green LED6 indicates board power. These LEDs are mounted on the front side of the board.
Ethernet connector J9 has two LEDs: yellow and green. LEDs indicate wired network activity and speed. 

Default function of LEDs and related information is listed in Table 18. 


.. table:: Table 18. Default LEDs functions

  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | **Board Reference** | **Schematic name** | **Shift register**    | **Description**                                                                           |
  |                     |                    |                       |                                                                                           |
  |                     |                    | **(IC14) pin**        |                                                                                           |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED1                | RPI_LED1_R         | Q0                    | User defined.                                                                             |
  |                     +--------------------+-----------------------+                                                                                           |
  |                     | RPI_LED1_G         | Q1                    |                                                                                           |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED2                | RPI_LED2_R         | Q2                    | User defined.                                                                             |
  |                     +--------------------+-----------------------+                                                                                           |
  |                     | RPI_LED2_G         | Q3                    |                                                                                           |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED3                | RPI_LED3_R         | Q4                    | User defined.                                                                             |
  |                     +--------------------+-----------------------+                                                                                           |
  |                     | RPI_LED3_G         | Q5                    |                                                                                           |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED4                | RPI_LED4_R         | Q6                    | User defined.                                                                             |
  |                     +--------------------+-----------------------+                                                                                           |
  |                     | RPI_LED4_G         | Q7                    |                                                                                           |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED5                | RPI_STATUS_LED_R   |                       | Green is connected to CM4 PI_LED_nPWR (Power On)                                          |
  |                     +--------------------+-----------------------+                                                                                           |
  |                     | RPI_STATUS_LED_G   |                       | and red is connected to Pi_nLED_Activity (Activity).                                      |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | LED6                | VCC3P3             |                       | Board power. Connected to 3.3 V power rail                                                |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+
  | Ethernet connector  | ETH_LED_Y          |                       | Green is connected to Ethernet_nLED2 (Ethernet speed   indicator: 1Gbit or 100Mbit Link)  |
  |                     +--------------------+-----------------------+                                                                                           |
  | J9 LEDs             | ETH_LED_G          |                       | and yellow is connected to Ethernet_nLED3   (Ethernet activity indicator).                |
  +---------------------+--------------------+-----------------------+-------------------------------------------------------------------------------------------+

A user button (BTN1) and buzzer (BZ1) are mounted on the front side of the board and can be used for various purposes. The button is connected to Raspberry Pi CM4/5 GPIO24 (default)/CM5 RUN_PG, has external pull up resistors and is hardware debounced. Buzzer control circuit is connected to GPIO5.
