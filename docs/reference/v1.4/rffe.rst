RF Front End
############

LimePSB RPCM RF path features power amplifiers, low noise amplifiers, SPDT switches, Couplers and power detectors as shown in Figure 6.

.. figure:: /images/LimePSB-RPCM_v1.4_diagrams_r3_RFFE.png
  :width: 600

  Figure 6: LimePSB RPCM v1.4 RFFE diagram

A single control signal (RF_SW_TDD) is used to control all RF switches simultaneously for both A and B channels to change between TDD and FDD modes as shown in Table 8.

.. table:: Table 8. RF path truth table

  +--------------------------------+----------------+----------------+
  | **Control signal (RF_SW_TDD)** | **TRXA/B       | **RXA/B        |
  |                                | connected to** | connected to** |
  +================================+================+================+
  | High                           | TXA/B_IN       | RXA/B_OUT      |
  +--------------------------------+----------------+----------------+
  | Low                            | RXA/B_OUT      | NC             |
  +--------------------------------+----------------+----------------+

By default RF switches may be controlled from FPGA pin 13 (via resistor R43). Optional control source may be RFFE TDD control header (J18).

RF path contains two types of connectors: board edge SMA connectors (J42, J43, J46, J47) used for external connections (antennas or cables) and U.FL connectors (J44, J45, J48, 49) used for internal connections (for example to connect to XTRX mini PCIe expansion board). 

Signal frequency range of TX and RX paths are listed in Table 9.

.. table:: Table 9. RF path signal frequency range

  +---------------+---------------------+
  | **Direction** | **Frequency range** |
  +===============+=====================+
  | TX            | 100 MHz - 4 GHz     |
  +---------------+---------------------+
  | RX            | 100 MHz - 4 GHz     |
  +---------------+---------------------+

More detailed RF path component parameters are given in Table 10.

.. table:: Table 10. RF path components parameters

  +---------------+--------------+--------------------------------------+----------------------+-------------------+
  | **Component** | **Function** | **Gain, dB**                         | **Output P1dB, dBm** | **NF, dB**        |
  +===============+==============+======================================+======================+===================+
  | TQP3M9018     | TX amplifier | 21.9 dB (900 MHz)                    | 21.4 dBm (900 MHz)   | 1.1 dB (900 MHz)  |
  |               |              +--------------------------------------+----------------------+-------------------+
  |               |              | 20.5 dB (1900 MHz)                   | 21.4 dBm (1900 MHz)  | 1.3 dB (1900 MHz) |
  |               |              +--------------------------------------+----------------------+-------------------+
  |               |              | 17 dB   (4000 MHz)                   | 19.2 dBm (4000 MHz)  | 2.5 dB (4000 MHz) |
  +---------------+--------------+--------------------------------------+----------------------+-------------------+
  | SPF5043Z      | RX amplifier | 18.2 dB (900 MHz)                    | 22.6 dBm (900 MHz)   | 0.74 dB (900 MHz) |
  |               |              +--------------------------------------+----------------------+-------------------+
  |               |              | 13.1 dB   (1900 MHz)                 | 22.7 dBm (1900 MHz)  | 0.78 dB (1900 MHz)|
  |               |              +--------------------------------------+----------------------+-------------------+
  |               |              | 7.0 dB   (3800 MHz)                  | 22.8 dBm (3800 MHz)  | 1.49 dB (3800 MHz)|
  +---------------+--------------+--------------------------------------+----------------------+-------------------+
  | F2972NEGK     | RF switch    | -0.53 dB (1000 MHz)                  | 38dBm (1800 MHz)     |                   |
  |               |              +--------------------------------------+                      |                   |
  |               |              | -0.4 dB   (2000 MHz)                 |                      |                   |
  |               |              +--------------------------------------+                      |                   |
  |               |              | -0.55 B   (6000 MHz)                 |                      |                   |
  +---------------+--------------+--------------------------------------+----------------------+-------------------+

Both channels TX PAs `TQP3M9018`_ outputs are coupled by `HHM22152A2`_ (IC53, IC55) to RF power detectors `LTC5587`_ (IC72, IC73). Power detector is connected to RPi CM4/5 SPI (RPI_SPI0). To enable it drive GPPIO expanders EXP1 GPB3 pin high.

.. _LTC5587: https://www.analog.com/en/products/ltc5587.html
.. _HHM22152A2: https://product.tdk.com/en/search/rf/rf/coupler/info?part_no=hhm22152a2
.. _TQP3M9018: https://www.qorvo.com/products/p/TQP3M9018
