GPIO Connector
##############

Some Raspberry Pi Compute Module 4/5 and FPGA GPIOs are connected to 21 pin 0.1” J10 header. Several pins of this connector are dedicated for power (1 pin for 3.3 V and 2 pins for 5V). GPIO header pins (J10) and additional information is given in table 20.

.. list-table:: Table 21. Raspberry Pi CM4/5 GPIO header (J10) pins
   :header-rows: 1
   :stub-columns: 1   

   * - Pin
     - Schematic signal name
     - CM4/5 pin
     - I/O standard
     - Comment
   * - 1
     - VCC3P3
     - 
     - 3.3V
     - 3.3V power rail
   * - 2
     - VCC5P0
     - 
     - 5.0V
     - 5.0V power rail
   * - 3
     - RPI_GPIO22
     - GPIO22
     - 3.3V
     - General purpose
   * - 4
     - VCC5P0
     - 
     - 5.0V
     - 5.0V power rail
   * - 5
     - RPI_GPIO27
     - GPIO27
     - 3.3V
     - General purpose
   * - 6
     - RPI_GPIO3
     - GPIO3
     - 3.3V
     - General purpose
   * - 7
     - RPI_GPIO6
     - GPIO6
     - 3.3V
     - General purpose
   * - 8
     - RPI_UART0_TX
     - GPIO14
     - 3.3V
     - General purpose configured as UART output
   * - 9
     - RPI_SPI0_MOSI
     - GPIO10
     - 3.3V
     - General purpose configured as SPI output
   * - 10
     - RPI_UART0_RX
     - GPIO15
     - 3.3V
     - General purpose configured as UART input
   * - 11
     - RPI_SPI0_MISO
     - GPIO9
     - 3.3V
     - General purpose configured as SPI input
   * - 12
     - FPGA_GPIO0
     - 
     - 
     - FPGA 45 pin (IOB_5B)
   * - 13
     - RPI_SPI0_SCLK
     - GPIO11
     - 3.3V
     - General purpose configured as SPI clock
   * - 14
     - FPGA_GPIO1
     - 
     - 
     - FPGA 21 pin (IOB_23B)
   * - 15
     - RPI_GPIO2
     - GPIO2
     - 3.3V
     - General purpose
   * - 16
     - RPI_GPIO4
     - GPIO4
     - 3.3V
     - General purpose
   * - 17
     - RPI_ID_SD
     - ID_SD
     - 3.3V
     - I2C interface SD for HATs (ID EEPROM)
   * - 18
     - RPI_ID_SC
     - ID_SC
     - 3.3V
     - I2C interface SC for HATs (ID EEPROM)
   * - 19
     - GND
     - 
     - 
     - Ground (0V)
   * - 20
     - GND
     - 
     - 
     - Ground (0V)
