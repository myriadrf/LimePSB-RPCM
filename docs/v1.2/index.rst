*****
LimePSB RPCM v1.2 Board
*****

Introduction
============

LimePSB RPCM v1.2 Board Key Features
-------------------------------

The LimePSB RPCM is carrier board for Raspberry Pi Compute Module 4 or 5 (CM4 or CM5) and mPCIe card (by default LimeSDR XTRX board). LimePSB RPCM carrier board provides a hardware platform for developing and prototyping high-performance designs based on Raspberry Pi CM4 or CM5, RF front end, clock network and mPCIe card. It allows user to use the board in SDR, LoRa and other applications.

.. figure:: images/LimePSB-RPCM_v1.2_3D_top.png
  :width: 600
  
  Figure 1. LimePSB-RPCM v1.2 board top view

.. figure:: images/LimePSB-RPCM_v1.2_3D_bot.png
  :width: 600
  
  Figure 2. LimePSB-RPCM v1.2 board bottom view

LimePSB RPCM board features:

* Connectors:

  * Raspberry CM4 and CM5 connector (dual row)
  * USB 2.0 Type-C socket (USB boot and power delivery)
  * Dual USB 3.0 (type A) socket (downstream ports) or Front Panel USB 2.0 header (unpopulated)
  * Ethernet jack (Gigabit Ethernet with PoE)
  * mini PCIe x1 Gen 2 (5Gbps)
  * 2x HDMI 2.0 receptacle (up to 4Kp60 supported)
  * 2x 15-pin FPC connectors for MIPI DSI display and CSI camera
  * 3.5 mm 4-pin jack for analog audio and composite video
  * uSD card socket
  * Nano-SIM socket
  * Coaxial RF (4x SMA female + 4x U.FL female) connectors for RF front end
  * Coaxial pass-through U.FL to external SMA connector
  * 20-pin Raspberry CM4 GPIO header (3.3V)
  * 14-pin Raspberry CM4 SYS header
  * 5-pin front display connector (power, I2C, button)
  * Raspberry CM4 UART0 header (unpopulated)
  * 2-pin and 4-pin FAN connector (5V default or 3.3V or VCC_INT voltage)

* RF front end:

  * Configuration: MIMO (2x TRX, 2x RX)
  * LNAs, PAs, RF switches, power and mode control (TDD and FDD)

* Miscellaneous:

  * Board temperature sensor
  * FAN controller
  * EEPROM
  * Secure key storage, shift registers
  * RTC, ADC
  * USB 2.0 hub
  * Configuration dip switch

* General user inputs/outputs:

  * 4x general purpose Dual colour (RG) LEDs 
  * 20 pin CM4/5 GPIO header (3.3V)
  * Front button
  * Buzzer

* Clock system:

  * 30.72MHz (default) on board VCOCXO and 30.72/38.4/40.00MHz (optional) VCTCXOs
  * Possibility to tune on board XO by on-board DAC or by phase detector to match a reference clock input (e.g. 10MHz).
  * Reference clock/PPS input and output SMA connectors (EXT_SYNC_IN and EXT_SYNC_OUT)
  * Possibility to synchronize multiple boards using coaxial SMA connectors  (EXT_SYNC_IN and EXT_SYNC_OUT)

* Board size: 170mm x 110mm

* Board power sources:

  * Barrel (9-14V, 2-3A)
  * USB Power Delivery (12V 1.5A or 2.5A)
  * PoE (12V, 2A)

For more information on the following topics, refer to the folowing documents:

* `Raspberry Pi CM4  <http://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf>`_
* `Raspberry Pi CM5  <https://pip.raspberrypi.com/categories/944-raspberry-pi-compute-module-5>`_
* `LimeSDR XTRX  <https://limesdr-xtrx.myriadrf.org/>`_

