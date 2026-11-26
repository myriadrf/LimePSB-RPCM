Board Versions
##############

The LimePSB RPCM has several hardware versions (v1.1–v1.5), with new features added in each version. A summary of the added features is provided in the table below.

.. table:: Table 1. Added features

  +-------------------+------------------------------------------+-----------------------------------------------------+
  | **Board version** | **New Features**                         | **Comment**                                         |
  +===================+==========================================+=====================================================+
  | v1.5              | No new features. Component changes only. | Replaced F2972NEGK RF switches with BGS12WN6        |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Replaced obsolete fan with MF80151V2-1000U-A99      |
  +-------------------+------------------------------------------+-----------------------------------------------------+
  | v1.4              | Digital Clock network path configuration | Replaced clock path selection jumpers with switches |
  |                   +------------------------------------------+-----------------------------------------------------+
  |                   | RF TX output power metering              | Added HHM22152A2 RF couplers                        |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Added LTC5587 RF power detectors                    |
  +-------------------+------------------------------------------+-----------------------------------------------------+
  | v1.3              | GPSDO & IEEE 1588 Sync                   | Added FPGA ICE5LP4K-SG48ITR                         |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Added 10 MHz OCXO clock source                      |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Added GNSS receiver                                 |
  +-------------------+------------------------------------------+-----------------------------------------------------+
  | v1.2              | Compatibility with Raspberry Pi CM5      | Updated CM connector pinout                         |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Added USB 3.0 socket for CM5                        |
  |                   |                                          +-----------------------------------------------------+
  |                   |                                          | Added board configuration 4 bit DIP switch          |
  |                   +------------------------------------------+-----------------------------------------------------+
  |                   | Fan Speed control                        | Added fan speed controller EMC2301                  |
  +-------------------+------------------------------------------+-----------------------------------------------------+

.. warning::
  Before proceeding, verify which features are supported by your specific hardware version.

LimePSB RPCM version identification text is printed on the top side of the board:

 * for versions 1.1 and 1.2 next to one of the mounting holes.
 * for versions 1.3, 1.4 and 1.5 near LEDs.

.. figure:: /images/LimePSB-RPCM_v1.5_3D_top.png
  :width: 600

  Figure 1: LimePSB RPCM v1.5 board top view

.. figure:: /images/LimePSB-RPCM_v1.4_3D_top.png
  :width: 600

  Figure 2: LimePSB RPCM v1.4 board top view

.. figure:: /images/LimePSB-RPCM_v1.3_3D_top.png
  :width: 600

  Figure 3: LimePSB RPCM v1.3 board top view

.. figure:: /images/LimePSB-RPCM_v1.2_3D_top.png
  :width: 600

  Figure 4: LimePSB RPCM v1.2 board top view

.. figure:: /images/LimePSB-RPCM_v1.1_3D_top.png
  :width: 600

  Figure 5: LimePSB RPCM v1.1 board top view