RF Front End
############

LimePSB RPCM RF path features power amplifiers, low noise amplifiers, SPDT switches, Couplers and power detectors as shown in Figure 6.

.. figure:: /images/LimePSB-RPCM_v1.2_diagrams_RFFE.png
  :width: 600

  Figure 6: LimePSB RPCM v1.2 RFFE diagram

A single control signal (RF_SW_TDD) is used to control all RF switches simultaneously for both A and B channels to change between TDD and FDD modes as shown in Table 7.

.. table:: Table 7. RF path truth table

  +--------------------------------+----------------+----------------+
  | **Control signal (RF_SW_TDD)** | **TRXA/B       | **RXA/B        |
  |                                | connected to** | connected to** |
  +================================+================+================+
  | High                           | TXA/B_IN       | RXA/B_OUT      |
  +--------------------------------+----------------+----------------+
  | Low                            | RXA/B_OUT      | NC             |
  +--------------------------------+----------------+----------------+

By default RF switches may be controlled from mPCIe expansion board pin 17 (via resistor R39). Optional control source may be RFFE TDD control header (J19) or CM4/5 GPIO6 (resistor R40 must be soldered).

RF path contains two types of connectors: board edge SMA connectors (J42, J43, J46, J47) used for external connections (antennas or cables) and U.FL connectors (J40, J41, J44, J45) used for internal connections (for example to connect to XTRX mini PCIe expansion board). 
Signal frequency range of TX and RX paths are listed in Table 8.

.. table:: Table 8. RF path signal frequency range

  +---------------+---------------------+
  | **Direction** | **Frequency range** |
  +===============+=====================+
  | TX            | 100 MHz - 4 GHz     |
  +---------------+---------------------+
  | RX            | 100 MHz - 4 GHz     |
  +---------------+---------------------+

More detailed RF path component parameters are given in Table 9.

.. table:: Table 9. RF path components parameters

  +---------------+--------------+--------------------------------------+----------------------+------------------+
  | **Component** | **Function** | **Gain, dB**                         | **Output P1dB, dBm** | **NF, dB**       |
  +---------------+--------------+--------------------------------------+----------------------+------------------+
  | SBB-5089      | TX amplifier | 20.5dB (850 MHz)   19.0dB (1950 MHz) | 20.5dBm (850 MHz)    | 3.8dB (850 MHz)  |
  |               |              +--------------------------------------+----------------------+------------------+
  |               |              | 15.5dB   (6000 MHz)                  | 20.4dBm (1950 MHz)   | 4.1dB (1950 MHz) |
  |               |              +--------------------------------------+----------------------+------------------+
  |               |              |                                      | 14.7dBm (4000 MHz)   | 4.6dB (4000 MHz) |
  +---------------+--------------+--------------------------------------+----------------------+------------------+
  | SPF5043Z      | RX amplifier | 18.2dB (900 MHz)                     | 22.6dBm (900 MHz)    | 0.8dB (900 MHz)  |
  |               |              +--------------------------------------+----------------------+------------------+
  |               |              | 12.9dB   (1960 MHz)                  | 22.7dBm (1900 MHz)   | 0.8dB (1900 MHz) |
  |               |              +--------------------------------------+----------------------+------------------+
  |               |              | 7.0dB   (3800 MHz)                   | 22.8dBm (3800 MHz)   | 1.5dB (3800 MHz) |
  +---------------+--------------+--------------------------------------+----------------------+------------------+
  | SKY13286      | RF switch    | -0.7dB (1000 MHz)                    | 30.dBm (2000 MHz)    |                  |
  |               |              +--------------------------------------+                      |                  |
  |               |              | -0.8dB   (2000 MHz)                  |                      |                  |
  |               |              +--------------------------------------+                      |                  |
  |               |              | -1.6dB   (6000 MHz)                  |                      |                  |
  +---------------+--------------+--------------------------------------+----------------------+------------------+

