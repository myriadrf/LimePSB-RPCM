Hardware Setup
##############

Host Device
***********

The Raspberry Pi Compute Module serves as the system host device. The LimePSB RPCM is compatible with Raspberry Pi Compute Module 4 and 5.

Before installing the Compute Module, ensure that the fourth bit of the configuration DIP switch (SW1) is set to the correct position.
 
 * Compute Module 5 - CM5 USB (ON) position.
 * Compute Module 4 - CM4 USB (OFF) position.

.. warning::
  Raspberry Pi Compute Module 5 is supported by LimePSB RPCM version 1.2 and newer. 

Cooling
*******

Depending on the application, host system and ambient temperature, additional cooling may be required to ensure reliable operation of the LimePSB RPCM board. This may be in the form of airflow through the host system, or a dedicated heatsink fitted to the board.

In standard applications, an 80 mm × 80 mm fan with a 4-pin, 3-pin, or 2-pin connector can be mounted using M3 spacers with a recommended length of 12 mm. This configuration provides sufficient cooling for systems operating with both a Compute Module and an mPCIe expansion card simultaneously.

.. note::
   In the event of errors, instability or reduced performance, check the board temperature to ensure that it is within the specified operating range.

RF Connections
**************

.. figure:: /images/LimePSB-RPCM_v1.4_RFCON.png
  :width: 600
  
  Figure 8: LimePSB RPCM board top with RF connector positions

.. list-table:: Table 1. RF Connectors
    :header-rows: 1
    :stub-columns: 1

    * - Connector
      - Frequency Range
      - Notes
    * - J46 (SMA)
      - 0.1 GHz - 4 GHz
      - Channel A receive input
    * - J42 (SMA)
      - 0.1 GHz - 4 GHz
      - Channel A transmit output or receive input (TDD)
    * - J47 (SMA)
      - 0.1 GHz - 4 GHz
      - Channel B receive input 
    * - J43 (SMA)
      - 0.1 GHz - 4 GHz
      - Channel B transmit output or receive input (TDD)
    * - J49 (U.FL)
      - 0.1 GHz - 4 GHz
      - Channel B Receive output 
    * - J45 (U.FL)
      - 0.1 GHz - 4 GHz
      - Channel B transmit input
    * - J44 (U.FL)
      - 0.1 GHz - 4 GHz
      - Channel A transmit input
    * - J48 (U.FL)
      -  0.1 GHz - 4 GHz
      - Channel A receive output
    * - J20 (Header), J21 (SMA), J22 (U.FL)
      - up to 6 GHz
      - U.FL to SMA adapter (INT to EXT 1)
    * - J23 (header), J24 (SMA), J25 (U.FL)
      - up to 6 GHz
      - U.FL to SMA adapter (INT to EXT 2)

.. warning::
   Care should be taken when connecting external RF signals to the TX and RX inputs, to ensure that the maximum safe input power of +10 dBm is not exceeded, as this may cause permanent damage to the device.

