GPIO Connector
##############

Some Raspberry Pi Compute Module 4 GPIOs are connected to 20 pin 0.1” J10 header. Three pins of this connector are dedicated for power (3.3 V and 5V). GPIO header pins (J10) and additional information is given in Table 18.

.. list-table:: Table 18. Raspberry Pi CM4 GPIO header (J10) pins
   :header-rows: 1
   :stub-columns: 1   

   * - Connector pin
     - Schematic signal name
     - CM4 pin
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
     - GND
     -
     -
     - Ground (0V)
   * - 7
     - GND
     -
     -
     - Ground (0V)
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
     - GND
     -
     -
     - Ground (0V)
   * - 13
     - RPI_SPI0_SCLK
     - GPIO11
     - 3.3V
     - General purpose configured as SPI clock
   * - 14
     - GND
     -
     -
     - Ground (0V)
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
     - General purpose
   * - 18
     - RPI_ID_SC
     - ID_SC
     - 3.3V
     - General purpose
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
