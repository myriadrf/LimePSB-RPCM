Introduction
############

.. toctree::
   :maxdepth: 3
   :hidden:
   
   Introduction <self>
   user/index
   reference/index
   developer

.. figure:: /images/limepsb-rpcm-04_jpg_gallery-lg.jpg
      :align: center


The LimePSB RPCM is a carrier board designed for the Raspberry Pi Computes Module 4 and 5. In addition to providing access to all interfaces of the Raspberry Pi Compute Modules, the LimePSB RPCM features an onboard 2T2R TDD-capable RF front end.

This combination delivers a versatile hardware platform for the development and prototyping of high-performance systems based on the Raspberry Pi Compute Modules 4 and 5, integrating an RF front end, clock distribution network, and mPCIe connectivity.

Specifications
**************

RF Front-end
============

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Value
     - Notes
   * - Configuration
     - MIMO (2T2R)
     - 2 Full-duplex channels
   * - Frequency Range
     - 100 MHz – 4 GHz
     - Continuos coverage
   * - Tx Gain
     - 16 dB - 20 dB
     - Depended on frequency
   * - Rx Gain
     - 6 dB - 17 dB
     - Depended on frequency
   * - TX NF
     - 1.9 dB - 3.4 dB
     - Depended on frequency
   * - RX NF
     - 1.8 dB - 2.5 dB
     - Depended on frequency
   * - TX P1dB
     - 18.2 dBm - 20.4 dBm
     - Depended on frequency
   * - RX P1dB
     - 21.6 dBm - 21.8 dBm
     - Depended on frequency

.. note::
   RF front-end parameters may vary depending on the board version.

Digital Interfaces
==================

Raspbery Pi compute module (system host) interfaces:
   
   * PCIe 2.0 x1 (Mini PCIe expansion card slot)
   * 2x HDMI 2.0
   * 2x USB 2.0 or 1 x USB 2.0 + 1 x USB 3.0 (top socket) 
   * Audio 
   * MIPI DSI and CSI
   * Wifi and bluetooth
   * Gigabit Ethernet

.. note::
   USB 3.0 is available if Raspberry Pi Compute Module 5 is used.


Power Supply
============

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Value
     - Notes
   * - Input Voltage (DC Barrel)
     - 9 V - 14 V DC
     - Inner diameter 2 mm outer, outer diameter 6.5 mm
   * - Input Voltage (USB PD)
     - 9 V - 12 V DC
     - Via USB type C connector
   * - Input Voltage (PoE+)
     - 40V - 57 V DC
     - Class 4 IEEE802.3 PD
   * - Maximum Power
     - 24 W
     - Applicable to all three power sources

.. note::
   Power consumption depends on configuration.

.. warning::
   Incorrect voltage or inadequate current capacity may cause damage or unstable operation.

Environmental
=============

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Value
     - Notes
   * - Operating Temperature
     - 0 °C to +70 °C
     - Commercial-grade
   * - Storage Temperature
     - -40 °C to +85 °C
     - N/A
   * - Operating Humidity
     - 10% to 90% RH  
     - Non-condensing

Mechanical
==========

Board size 170 × 110 mm.

Features
********

.. note::
   Features may vary depending on board version.

Devices
=======

* Lattice iCE40 Ultra family FPGA (iCE5LP4K)
* Board temperature sensor
* FAN controller
* EEPROM
* Secure key storage, I/O expander
* RTC, ADC
* USB 2.0 hub

Clock System
============

* GNSS receiver
* 30.72MHz and 10 MHz (default) on board VCOCXOs and 30.72/38.4/40.00MHz (optional) VCTCXOs
* Possibility to tune on board XO by on-board DAC or by phase detector to match a reference clock input (e.g. 10MHz).
* Reference clock/PPS input and output SMA connectors (EXT_SYNC_IN and EXT_SYNC_OUT)
* Possibility to synchronize multiple boards using coaxial SMA connectors  (EXT_SYNC_IN and EXT_SYNC_OUT)

Configuration
=============

* Configuration dip switch
* Clock system path switches

General user inputs/outputs
===========================

* 4x general purpose Dual colour (RG) LEDs 
* 20 pin CM4/5 GPIO header (3.3V)
* Front button
* Buzzer

Connectors
==========

* Raspberry CM4 and CM5 connector (dual row)
* USB 2.0 Type-C socket (USB boot and power delivery)
* Dual USB 3.0 (type A) socket and USB header (downstream ports) or Front Panel USB 2.0 header (unpopulated)
* Ethernet jack (Gigabit Ethernet with PoE)
* mini PCIe x1 Gen 2 (5Gbps)
* 2x Micro HDMI 2.0 receptacle (up to 4Kp60 supported)
* 2x 15-pin FPC connectors for MIPI DSI display and CSI camera
* 3.5 mm 4-pin jack for analog audio and composite video
* uSD card socket
* Nano-SIM socket
* Coaxial RF (4x SMA female + 4x U.FL female) connectors for RF front end
* External synchronization (2x SMA female) connectors for input and output
* 2x Coaxial pass-through U.FL to external SMA connectors
* 20-pin Raspberry CM4/5 GPIO header (3.3V)
* 14-pin Raspberry CM4/5 SYS header
* 5-pin front display connector (power, I2C, button)
* Raspberry CM4/5 UART0 header (unpopulated)
* 2-pin and 4-pin FAN connector (5V default or 3.3V or VCC_INT voltage)
  


