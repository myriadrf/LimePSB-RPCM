FPGA
####

LimePSB RPCM board houses a Lattice Semiconductor iCE40 Ultra family FPGA (IC17, iCE5LP4K-SG48ITR). The FPGA connects the GNSS receiver (IC40), the XO tuning DACs (IC33, IC35), the RF front end TDD control (FPGA_RF_SW_TDD) and the synchronisation signals (RPI_SYNC_IN, RPI_SYNC_OUT, FPGA_SYNC_OUT) to the Raspberry Pi CM4/5. Clock buffer outputs LMK10_CLK_OUT0 and LMKRF_CLK_OUT4 are connected to FPGA inputs.

CM4/5 communicates with the FPGA over RPI_SPI1 (slave select RPI_SPI1_SS1) and over I2C (FPGA_I2C_SCL and FPGA_I2C_SDA are connected to RPI_I2C0 through resistors R99 and R100). FPGA interface pins are listed in :doc:`peripheralinterfaces`.

The FPGA does not keep its configuration when power is removed. It is configured after every power up or reset, either by CM4/5 (default) or from a configuration flash memory.

Configuration Modes
===================

The FPGA supports two SPI configuration modes:

* **Slave SPI (default).** CM4/5 loads the FPGA configuration over RPI_SPI0 (slave select RPI_SPI0_SS0). Resistor R109 (10k) pulls FPGA_CFG_SPI_CSN low, so the FPGA starts in SPI slave mode.
* **Master SPI.** The FPGA loads its configuration from SPI flash memory IC18 (MX25U1632FM2I02, 16 Mbit). In this mode CM4/5 can program the flash over RPI_SPI0.

The configuration mode is selected by fitting or removing the components listed in Table 3.

.. list-table:: Table 3. FPGA SPI configuration mode selection
   :header-rows: 1

   * - Component
     - Slave SPI (default)
     - Master SPI
   * - R103
     - Fit
     - Fit
   * - R104
     - Not fitted
     - Fit
   * - R105
     - Fit
     - Not fitted
   * - R106
     - Not fitted
     - Fit
   * - R107
     - Fit
     - Not fitted
   * - R108
     - Fit
     - Fit
   * - R109
     - Fit
     - Not fitted
   * - R111
     - Not fitted
     - Fit

Configuration Control and Status
================================

CM4/5 controls FPGA configuration through I/O expander IC13:

* FPGA_CRESET (FPGA pin 8, CRESET_B) is driven by IC13 GPB5. Drive it low to reset the FPGA and high to start configuration.
* FPGA_CDONE (FPGA pin 7, CDONE) goes high when the FPGA is configured. It drives the green LED of LED7.

FPGA_CDONE and FPGA_CRESET are also available on header J25, which is not fitted by default.

Diode D2 supplies the FPGA VPP_2V5 pin (VCC2P5_FPGA) from the 3.3 V rail, as required for programming the FPGA internal non-volatile configuration memory (NVCM).
