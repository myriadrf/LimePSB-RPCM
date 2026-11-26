RF Front End
############

LimePSB RPCM RF path features power amplifiers, low noise amplifiers, SPDT switches, Couplers and power detectors as shown in Figure 6.

.. figure:: /images/LimePSB-RPCM_v1.5_diagrams_RFFE.png
  :width: 600

  Figure 6: LimePSB RPCM v1.5 RFFE diagram

A single control signal (RF_SW_TDD) is used to control all RF switches simultaneously for both A and B channels to change between TDD and FDD modes as shown in Table 8.

.. table:: Table 8. RF path truth table

  +--------------------------------+----------------+----------------+
  | **Control signal (RF_SW_TDD)** | **TRXA/B       | **RXA/B        |
  |                                | connected to** | connected to** |
  +================================+================+================+
  | High                           | RXA/B_OUT      | NC             |
  +--------------------------------+----------------+----------------+
  | Low                            | TXA/B_IN       | RXA/B_OUT      |
  +--------------------------------+----------------+----------------+

By default RF switches may be controlled from FPGA pin 13 (via resistor R43). Optional control source may be RFFE TDD control header J18 (not fitted by default).

RF_SW_TDD is pulled low by resistor R44. If RF_SW_TDD is not driven, TRXA/B is connected to TXA/B_IN and RXA/B is connected to RXA/B_OUT.

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
  | BGS12WN6      | RF switch    | -0.16 dB (699-960 MHz)               | 30 dBm (P0.1dB, min) |                   |
  |               |              +--------------------------------------+                      |                   |
  |               |              | -0.19 dB (1200-2170 MHz)             |                      |                   |
  |               |              +--------------------------------------+                      |                   |
  |               |              | -0.30 dB (3300-4200 MHz)             |                      |                   |
  +---------------+--------------+--------------------------------------+----------------------+-------------------+

Both channels TX PAs `TQP3M9018`_ outputs are coupled by `HHM22152A2`_ (IC53, IC55) to RF power detectors `LTC5587`_ (IC72, IC73). The power detectors are read by Raspberry Pi CM4/5 over SPI (RPI_SPI0): RPI_SPI0_SCLK is connected to the detector SCK pins and RPI_SPI0_MISO to the SDO pins. Conversion and readout of each detector is controlled by its own CONV signal: RFPDA_CONV (RPI GPIO25) for channel A and RFPDB_CONV (RPI GPIO26) for channel B.

To enable the power detectors, drive I/O expander EXP1 (IC15) pin GPB3 (RFPD_EN) high.

.. _LTC5587: https://www.analog.com/en/products/ltc5587.html
.. _HHM22152A2: https://product.tdk.com/en/search/rf/rf/coupler/info?part_no=hhm22152a2
.. _TQP3M9018: https://www.qorvo.com/products/p/TQP3M9018
