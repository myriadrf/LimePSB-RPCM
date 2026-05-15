FPGA Configuration
##################

LimePSB RPCM board houses Lattice Semiconductor ICE40 Ultra family FPGA ICE5LP4K. It can be copnfigured by RPI CM4/5 (RPI_SPI0) or by external source (JTAG). By default FPGA is set to SPI slave mode and PRi module is in master mode to configure it during boot up. Also FPGA can be set to SPI master mode (FPGA_CFG) while CM4/5 (RPI_SPI0) is disconnected. In this case FPGA configuration information is stored in flash IC19 (NF). Hardware configuration for both modes are shown table 7.

.. list-table:: Table 7. FPGA SPI mode selection 
   :header-rows: 1

   * - Component id
     - Slave SPI
     - Master SPI
   * - R113
     - populate
     - populate
   * - R114
     - remove
     - populate
   * - R115
     - populate
     - remove
   * - R116
     - remove
     - populate
   * - R118
     - populate
     - remove
   * - R119
     - populate
     - populate
   * - R120
     - populate
     - remove
   * - R122
     - remove
     - populate
   * - R124
     - remove
     - populate
   * - IC19
     - remove
     - populate
   * - C63
     - remove
     - populate
