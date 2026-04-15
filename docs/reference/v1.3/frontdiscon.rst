Front Display Connector
#######################

LimePSB RPCM board has 5-pin 0.1” pitch header J8 with friction lock (Molex 0022112052) dedicated for front screen connection. Front display connector J8 contains signals for I2C interface, button and power rail. More detailed information about the front display connector is provided in table 16.

.. list-table:: Table 16. Front screen connector (J8) pinout
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - GND
     - Ground (0V)
   * - 2
     - VCC3P3 / VCC5P0
     - Power 3.3V (default) or 5V
   * - 3
     - RPI_ID_SD
     - I2C data
   * - 4
     - RPI_ID_SC
     - I2C clock
   * - 5
     - RPI_BTN2
     - User button 2 (debounced)