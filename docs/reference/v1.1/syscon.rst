System Header
#############

Raspberry Pi CM4 configuration, debug and analog signals can be accessed in system (SYS) header J14. SYS headers pins, schematic signal names and description are given in Table 3.

.. list-table:: Table 3. SYS header pinout
   :header-rows: 1

   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - GND
     - Ground (0V)
   * - 2
     - RPI_nRPIBOOT
     - A low on this pin forces CM4 booting. To enable Raspberry Pi USB boot also place nRPIBOOT jumper on J14 pins 1-2. 
      
       Place jumper on header J28 to switch Raspberry Pi USB from USB hub to USB C connector.
   * - 3
     - GND
     - Ground (0V)
   * - 4
     - RPI_EEPROM_nWP
     - CM4 on-board EEPROM write protect
   * - 5
     - RPI_AIP0
     - Analogue input
   * - 6
     - RPI_AIP1
     - Analogue input
   * - 7
     - GND
     - Ground (0V)
   * - 8
     - RPI_SYNC_IN
     - IEEE1588 SYNC Input
   * - 9
     - RPI_SYNC_OUT
     - IEEE1588 SYNC Output
   * - 10
     - GND
     - Ground (0V)
   * - 11
     - RPI_TVDAC
     - Video DAC output
   * - 12
     - GND
     - Ground (0V)
   * - 13
     - RPI_RUN_PG_BUFF
     - Buffered (5V output) RPI_RUN_PG line. High signal indicates CM4 CPU is running.
   * - 14
     - RPI_GLOBAL_EN
     - Drive low to power off CM4. A button between pins 13-14 can be used to wake up compute module from power down.