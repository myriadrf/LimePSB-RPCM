Board Versions
##############

The LimePSB RPCM has several hardware versions (v1.1–v1.4), with new features added in each version. A summary of the added features is provided in the table below.

.. table:: Table 1. Added features
      
  +-------------------+--------------------------------------------------------+
  | **Board version** | **Added Features**                                     |
  +===================+========================================================+
  | v1.2              | Raspberry Pi connector compatibility with CM5          |
  |                   +--------------------------------------------------------+
  |                   | USB 3.0 socket (CM5)                                   |
  |                   +--------------------------------------------------------+
  |                   | Configuration 4 bit DIP switch                         |
  |                   +--------------------------------------------------------+
  |                   | Fan controller EMC2301                                 |
  +-------------------+--------------------------------------------------------+
  | v1.3              | FPGA ICE5LP4K-SG48ITR                                  |
  |                   +--------------------------------------------------------+
  |                   | 10 MHz OCXO (GPSDO)                                    |
  |                   +--------------------------------------------------------+
  |                   | GNSS receiver (GPSDO)                                  |
  +-------------------+--------------------------------------------------------+
  | v1.4              | HDMI connectors changed to type D (Micro)              |
  |                   +--------------------------------------------------------+
  |                   | Clock path configuration jumpers changed to  switches  |
  |                   +--------------------------------------------------------+
  |                   | RF transmit power detectors                            |
  +-------------------+--------------------------------------------------------+

.. warning::
  Before proceeding, verify which features are supported by your specific hardware version.

LimePSB RPCM version identification text is printed on the top side of the board:

 * for versions 1.1 and 1.2 next to one of the mounting holes.
 * for versions 1.3 and 1.4 near LEDs.

.. figure:: /images/LimePSB-RPCM_v1.4_3D_top.png
  :width: 600

  Figure 1: LimePSB RPCM v1.4 board top view

.. figure:: /images/LimePSB-RPCM_v1.3_3D_top.png
  :width: 600

  Figure 2: LimePSB RPCM v1.3 board top view

.. figure:: /images/LimePSB-RPCM_v1.2_3D_top.png
  :width: 600

  Figure 3: LimePSB RPCM v1.2 board top view

.. figure:: /images/LimePSB-RPCM_v1.1_3D_top.png
  :width: 600

  Figure 4: LimePSB RPCM v1.1 board top view