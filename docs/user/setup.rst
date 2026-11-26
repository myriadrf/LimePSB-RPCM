Hardware Setup
##############

Host Device
***********

The Raspberry Pi Compute Module serves as the system host device. The LimePSB RPCM is compatible with Raspberry Pi Compute Module 4 and 5.

On LimePSB RPCM v1.2 and newer, before installing the Compute Module, ensure that the fourth bit of the configuration DIP switch (SW1 on v1.2 and v1.3, DSW1 on v1.4 and newer) is set to the correct position.
 
 * Compute Module 5 - CM5 USB (ON) position.
 * Compute Module 4 - CM4 USB (OFF) position.

.. warning::
  Raspberry Pi Compute Module 5 is supported by LimePSB RPCM version 1.2 and newer. LimePSB RPCM v1.1 supports Compute Module 4 only.

Cooling
*******

Depending on the application, host system and ambient temperature, additional cooling may be required to ensure reliable operation of the LimePSB RPCM board. This may be in the form of airflow through the host system, or a dedicated heatsink fitted to the board.

In standard applications, an 80 mm x 80 mm fan with a 4-pin, 3-pin, or 2-pin connector can be mounted using M3 spacers with a recommended length of 12 mm. This configuration provides sufficient cooling for systems operating with both a Compute Module and an mPCIe expansion card simultaneously.

To use the PWM speed control input of a 4-pin fan, board resistor options must be changed. See the Board Temperature Control page of the :doc:`/reference/index` for your board version.

.. note::
   In the event of errors, instability or reduced performance, check the board temperature to ensure that it is within the specified operating range.

RF Connections
**************

RF connector designators depend on the board version. Select your board version in Table 2. Figure 6 shows the RF connector positions on a v1.4 board.

.. figure:: /images/LimePSB-RPCM_v1.4_RFCON.png
  :width: 600
  
  Figure 6: LimePSB RPCM v1.4 board top with RF connector positions

.. tabs::

  .. tab:: v1.4 and v1.5

    .. list-table:: Table 2. RF Connectors (v1.4 and v1.5)
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
        - Channel B receive output
      * - J45 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B transmit input
      * - J44 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A transmit input
      * - J48 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A receive output
      * - J20 (Header), J21 (SMA), J22 (U.FL)
        - up to 6 GHz
        - U.FL to SMA adapter (INT to EXT 1).

          Header J20 is not fitted by default.
      * - J23 (Header), J24 (SMA), J25 (U.FL)
        - up to 6 GHz
        - U.FL to SMA adapter (INT to EXT 2).

          By default J24 is connected to the GNSS receiver antenna input.

          J23 and J25 are not fitted by default.

  .. tab:: v1.3

    .. list-table:: Table 2. RF Connectors (v1.3)
      :header-rows: 1
      :stub-columns: 1

      * - Connector
        - Frequency Range
        - Notes
      * - J52 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A receive input
      * - J48 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A transmit output or receive input (TDD)
      * - J51 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B receive input
      * - J47 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B transmit output or receive input (TDD)
      * - J49 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B receive output
      * - J45 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B transmit input
      * - J46 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A transmit input
      * - J50 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A receive output
      * - J20 (Header), J21 (SMA), J22 (U.FL)
        - up to 6 GHz
        - U.FL to SMA adapter (INT to EXT).

          Header J20 is not fitted by default.

  .. tab:: v1.2

    .. list-table:: Table 2. RF Connectors (v1.2)
      :header-rows: 1
      :stub-columns: 1

      * - Connector
        - Frequency Range
        - Notes
      * - J47 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A receive input
      * - J43 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A transmit output or receive input (TDD)
      * - J46 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B receive input
      * - J42 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B transmit output or receive input (TDD)
      * - J44 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B receive output
      * - J40 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B transmit input
      * - J41 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A transmit input
      * - J45 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A receive output
      * - J20 (Header), J21 (SMA), J22 (U.FL)
        - up to 6 GHz
        - U.FL to SMA adapter (INT to EXT).

          Header J20 is not fitted by default.

  .. tab:: v1.1

    .. list-table:: Table 2. RF Connectors (v1.1)
      :header-rows: 1
      :stub-columns: 1

      * - Connector
        - Frequency Range
        - Notes
      * - J47 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A receive input
      * - J43 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel A transmit output or receive input (TDD)
      * - J46 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B receive input
      * - J42 (SMA)
        - 0.1 GHz - 4 GHz
        - Channel B transmit output or receive input (TDD)
      * - J44 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B receive output
      * - J40 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel B transmit input
      * - J41 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A transmit input
      * - J45 (U.FL)
        - 0.1 GHz - 4 GHz
        - Channel A receive output
      * - J22 (Header), J23 (SMA), J24 (U.FL)
        - up to 6 GHz
        - U.FL to SMA adapter (INT to EXT).

          Header J22 is not fitted by default.

.. warning::
   Care should be taken when connecting external RF signals to the TX and RX inputs, to ensure that the maximum safe input power of +10 dBm is not exceeded, as this may cause permanent damage to the device.

