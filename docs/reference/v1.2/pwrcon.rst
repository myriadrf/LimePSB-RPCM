Power Control Header
####################

Raspberry Pi CM4/5 power state can be controlled using J5 header. By default the CM4/5 power control header is not populated. 

.. list-table:: Table 4 Raspberry Pi CM4/5 power control (J5) header
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - RPI_GLOBAL_EN
     - Drive low to power off CM4/5
   * - 2
     - GND
     - Ground (0V)
   * - 3
     - RPI_RUN_PG
     - Drive low to reset CM4/5 CPU; high signal indicates CM4/5 CPU is running