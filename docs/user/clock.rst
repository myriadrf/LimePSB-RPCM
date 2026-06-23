Reference Clock
###############

The LimeSDR USB clock system is based on a high stability 30.72 MHz and 10 MHz VCOCXOs (Voltage Controlled Temperature Compensated Crystal Oscillators) which can be tuned via an external 1PPS reference signal or GPSDO function.


The board provides external synchronization input and output signals, including 1PPS and reference clocks, via SMA and U.FL connectors. 

.. table:: Table 2. Clock Functions

  +----------------------+-------------------+-------------------------------------+
  |     **Function**     | **Specification** |              **Notes**              |
  +======================+===================+=====================================+
  |  On-board Oscillator | 30.72 MHz VCOCXO  | U7475LF                             |
  |                      +-------------------+-------------------------------------+
  |                      | 10 MHz VCOCXO     | U8073LF                             |
  +----------------------+-------------------+-------------------------------------+
  |  External Sync Input | SMA (J36)         | 1PPS; 30,72 MHz 3,3V CMOS           |
  +----------------------+-------------------+-------------------------------------+
  | External Sync output | SMA (J38)         | 1PPS; 10 MHz or 30,72 MHz 3.3V CMOS |
  +----------------------+-------------------+-------------------------------------+
  |     Clock output     | U.FL (J39)        | 10 MHz 3.3V CMOS                    |
  |                      +-------------------+-------------------------------------+
  |                      | U.FL (J37)        | 30,72 MHz3.3V CMOS                  |
  +----------------------+-------------------+-------------------------------------+

.. note::
  10 MHz VCOCXO is available in LimePSB RPCM v1.3 and newer.

.. warning::
   When using external clock references, ensure signal levels and frequencies match specifications. 
   
   Improper clock signals may cause unstable operation and potential damage to the device.

