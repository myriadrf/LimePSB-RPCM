User Interface
##############

LimePSB RPCM board features button, buzzer, 6 dual colour (red and green (RG)) LEDs, 1 green indication LED, and 2 Ethernet activity LEDs (yellow and green). All board user interface components are highlighted in Figure 9.

.. figure:: /images/LimePSB-RPCM_v1.3_user_interface_components.png
  :width: 600

  Figure 9: LimePSB RPCM v1.3 user interface components
  
Dual color LEDs (LED1-LED4) are connected to I/O expander (IC13). Their function may be programmed according to the user requirements. Dual color LED5 indicates Raspberry Pi status. Green LED6 indicates board power. These LEDs are mounted on the front side of the board.
 
Ethernet connector J9 has two LEDs: yellow and green. LEDs indicate wired network activity and speed. 

Default function of LEDs and related information is listed in Table 20. 


.. table:: Table 20. Default LEDs functions

  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | **Board Reference**     | **Schematic      | **I/O expander**        | **Description**                                                                          |                                          
  |                         | name**           |                         |                                                                                          |
  |                         |                  | **(IC13) pin**          |                                                                                          |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED1                    | RPI_LED1_R       | GPA0                    | User defined.                                                                            |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | RPI_LED1_G       | GPA1                    |                                                                                          |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED2                    | RPI_LED2_R       | GPA2                    | User defined.                                                                            |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | RPI_LED2_G       | GPA3                    |                                                                                          |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED3                    | RPI_LED3_R       | GPA4                    | User defined.                                                                            |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | RPI_LED3_G       | GPA5                    |                                                                                          |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED4                    | RPI_LED4_R       | GPA6                    | User defined.                                                                            |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | RPI_LED4_G       | GPA7                    |                                                                                          |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED5                    | RPI_STATUS_LED_R |                         | Green is connected to CM4/5 PI_LED_nPWR (Power On)                                       |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | RPI_STATUS_LED_G |                         | and red is connected to Pi_nLED_Activity (Activity)                                      |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED6                    | VCC3P3           |                         | Board power. Connected to 3.3 V power rail.                                              |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | LED7                    | FPGA_LED_R       |                         | User defined                                                                             |
  |                         +------------------+-------------------------+                                                                                          |
  |                         | FPGA_CDONE       |                         | Indictes FPGA configuration status                                                       |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+
  | Ethernet   connector J9 | ETH_LED_Y        |                         | Green is connected to Ethernet_nLED2 (Ethernet speed   indicator: 1Gbit or 100Mbit Link) |
  |                         +------------------+-------------------------+                                                                                          |
  | LEDs                    | ETH_LED_G        |                         | and yellow is connected to Ethernet_nLED3   (Ethernet activity indicator).               |
  +-------------------------+------------------+-------------------------+------------------------------------------------------------------------------------------+

A user button (BTN1) and buzzer (BZ1) are mounted on the front side of the board and can be used for various purposes. The button is connected to Raspberry Pi CM4/5 GPIO24 (default)/CM5 RUN_PG, has external pull up resistors and is hardware debounced. Buzzer control circuit is connected to GPIO5.
