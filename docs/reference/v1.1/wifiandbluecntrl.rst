WiFi and Bluetooth Control Header
#################################

Raspberry Pi Compute Module 4 on board WiFi and Bluetooth disable signals may be controlled from header J6 (not fitted) as shown in Table 5.


.. list-table:: Table 5. Raspberry Pi CM4 J6 WiFi and Bluetooth control header pinout
   :header-rows: 1
  
   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - RPI_WL_nDISABLE
     - Drive low to disable wireless interface
   * - 2
     - GND
     - Ground (0V)
   * - 3
     - RPI_BT_nDISABLE
     - Drive low to disable Bluetooth interface