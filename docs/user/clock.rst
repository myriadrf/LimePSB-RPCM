Reference Clock
###############

The LimePSB RPCM clock system is based on a high stability 30.72 MHz VCOCXO (Voltage Controlled Oven Controlled Crystal Oscillator). Boards v1.3 and newer also have a 10 MHz VCOCXO. The oscillators can be tuned via an external 1PPS reference signal or, on v1.3 and newer, the GPSDO function.

The board provides external synchronization input and output signals, including 1PPS and reference clocks, via SMA and U.FL connectors. Connector designators depend on the board version, as shown in Table 3.

.. tabs::

  .. tab:: v1.4 and v1.5

    .. table:: Table 3. Clock Functions (v1.4 and v1.5)

      +----------------------+-------------------+-------------------------------------+
      |     **Function**     | **Specification** |              **Notes**              |
      +======================+===================+=====================================+
      |  On-board Oscillator | 30.72 MHz VCOCXO  | U7475LF                             |
      |                      +-------------------+-------------------------------------+
      |                      | 10 MHz VCOCXO     | U8073LF                             |
      +----------------------+-------------------+-------------------------------------+
      |  External Sync Input | SMA (J36)         | 1PPS; 30.72 MHz 3.3V CMOS           |
      +----------------------+-------------------+-------------------------------------+
      | External Sync output | SMA (J38)         | 1PPS; 10 MHz or 30.72 MHz 3.3V CMOS |
      +----------------------+-------------------+-------------------------------------+
      |     Clock output     | U.FL (J39)        | 10 MHz 3.3V CMOS                    |
      |                      +-------------------+-------------------------------------+
      |                      | U.FL (J37)        | 30.72 MHz 3.3V CMOS                 |
      +----------------------+-------------------+-------------------------------------+

  .. tab:: v1.3

    .. table:: Table 3. Clock Functions (v1.3)

      +----------------------+-------------------+-------------------------------------+
      |     **Function**     | **Specification** |              **Notes**              |
      +======================+===================+=====================================+
      |  On-board Oscillator | 30.72 MHz VCOCXO  | U7475LF                             |
      |                      +-------------------+-------------------------------------+
      |                      | 10 MHz VCOCXO     | U8073LF                             |
      +----------------------+-------------------+-------------------------------------+
      |  External Sync Input | SMA (J34)         | 1PPS; 30.72 MHz 3.3V CMOS           |
      +----------------------+-------------------+-------------------------------------+
      | External Sync output | SMA (J37)         | 1PPS; 10 MHz or 30.72 MHz 3.3V CMOS |
      +----------------------+-------------------+-------------------------------------+
      |     Clock output     | U.FL (J35)        | 10 MHz 3.3V CMOS                    |
      |                      +-------------------+-------------------------------------+
      |                      | U.FL (J33)        | 30.72 MHz 3.3V CMOS                 |
      +----------------------+-------------------+-------------------------------------+

  .. tab:: v1.1 and v1.2

    .. table:: Table 3. Clock Functions (v1.1 and v1.2)

      +----------------------+-------------------+-------------------------------------+
      |     **Function**     | **Specification** |              **Notes**              |
      +======================+===================+=====================================+
      |  On-board Oscillator | 30.72 MHz VCOCXO  | U7475LF                             |
      +----------------------+-------------------+-------------------------------------+
      |  External Sync Input | SMA (J32)         | 1PPS; 30.72 MHz 3.3V CMOS           |
      +----------------------+-------------------+-------------------------------------+
      | External Sync output | SMA (J35)         | 1PPS; 30.72 MHz 3.3V CMOS           |
      +----------------------+-------------------+-------------------------------------+
      |     Clock output     | U.FL (J33)        | 30.72 MHz 3.3V CMOS                 |
      +----------------------+-------------------+-------------------------------------+

.. warning::
   When using external clock references, ensure signal levels and frequencies match specifications. 
   
   Improper clock signals may cause unstable operation and potential damage to the device.

