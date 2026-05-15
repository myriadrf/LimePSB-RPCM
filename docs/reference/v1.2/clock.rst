Clock Distribution
##################


LimePSB-RPCM board clock network comprises of on-board voltage controlled crystal oscillators, phase detector, clock buffers, GNSS receiver, clock source selection analog muxes, reference clock input and output connectors.
Board clock distribution block diagram is as shown in figure 7.

.. figure:: /images/LimePSB-RPCM_v1.2_diagrams_clock.png
  :width: 600

  Figure 7: LimePSB RPCM v1.2 board clock distribution block diagram

LimePSB-RPCM board distributes reference clock to and from Raspberry Pi Compute Module 4/5, mini PCIe connector and external sources. Clock and PPS signals can be sourced from on board XOs and GNSS transceiver or another external source via J36 (EXT_SYNC_IN) connector. Also J38 (EXT_SYNC_OUT) connector can be used as clock signal output thus synchronizing multiple systems.
Clock path may be configured using analog muxes that are controlled by CM4/5 module as described in table 10.

.. table:: Table 10. LimePSB-RPCM clock signals configuration

  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | **Schematic ID** | **Input signal** | **Output signal** | **Description**                                                                     |
  +==================+==================+===================+=====================================================================================+
  | J36              | EXT_SYNC_IN      | REF_CLK_IN        | Phase detector (IC34) input selection                                               |
  |                  +------------------+                   |                                                                                     |
  |                  | RPI_SYNC_OUT     |                   |                                                                                     |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | J37              | RPI_SYNC_OUT     | PCIE_PPS_IN       | PPS signal source selection for mPCIe expansion boards                              |
  |                  +------------------+                   |                                                                                     |
  |                  | EXT_SYNC_IN      |                   |                                                                                     |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | J38              | EXT_SYNC_IN      | RPI_SYNC_IN       | CM4/5 SYNC_IN synchronization input source selection                                |
  |                  +------------------+                   |                                                                                     |
  |                  | PCIE_PPS_OUT     |                   |                                                                                     |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | J39              | EXT_SYNC_IN      | PCIE_UIMC4        | Reference clock selection for mPCIE exanpsion board (XTRX)                          |
  |                  +------------------+                   |                                                                                     |
  |                  | LMK_CLK_OUT2     |                   |                                                                                     |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | J34              | RPI_SYNC_OUT     | EXT_SYNC_OUT      | Synchronization output signal selection                                             |
  |                  +------------------+                   |                                                                                     |
  |                  | PCIE_PPS_OUT     |                   |                                                                                     |
  |                  +------------------+                   |                                                                                     |
  |                  | LMK_CLK_OUT3     |                   |                                                                                     |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | R153             | PCIE_PPS_IN      | PCIE_COEX1        | PPS signal output for mPCIE expansion board (XTRX)                                  |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | R4               | PCIE_PPS_IN      | PCIE_PETn0        | PPS signal output for mPCIE expansion board (LoRa Semtech)                          |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | R2               | PCIE_PPS_IN      | PCIE_COEX2        | PPS signal output for mPCIE expansion board (LoRa n-Fuse) and PPS output for (XTRX) |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | R3               | PCIE_COEX2       | PCIE_PPS_OUT      | PPS signal input from mPCIE expansion board (XTRX)                                  |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
  | R8               | PCIE_SMB_CLK     | PCIE_PPS_OUT      | Clock signal input from mPCIE expansion board (XTRX)                                |
  +------------------+------------------+-------------------+-------------------------------------------------------------------------------------+
 
LimePSB-RPCM board has several on-board crystal oscillator (XO) options that may be used as source for clock buffers (LMK00101). By default voltage controlled oven compensated crystal oscillators (VCOCXO) XO1 and XO6 are populated. Optional voltage controlled temperature compensated crystal oscillators XO2 – XO5 and XO7 – XO10 (VCTCXO) are not populated by default. All these XOs may be tuned by DAC (16-bit IC36 default or 8-bit IC38) or phase detector (IC37).
Clock network components are listed in table 11.

.. list-table:: Table 11. LimePSB-RPCM clock distribution network components
   :header-rows: 1

   * - Designator
     - Function
     - Part number
     - Parameters
     - Description
   * - XO1
     - VCOCXO
     - U7475LF 30.72 MHz
     - 30.72 MHz
     - 
   * - XO2
     - VCTCXO
     - E6245LF 30.72 MHz
     - 30.72 MHz
     - Not mounted
   * - XO3
     - 
     - E5280LF 30.72 MHz
     - 30.72 MHz
     - Not mounted
   * - XO4
     - 
     - RTX5032A 40.00 MHz
     - 40 MHz
     - Not mounted
   * - XO5
     - 
     - ASVTX-12-A-38.400MHz-H10-T
     - 38.4 MHz
     - Not mounted
   * - IC33
     - DAC
     - AD5662
     - 16-bit
     - 
   * - IC36
     - DAC
     - AD5601BKSZ-REEL7
     - 8-bit
     - Not mounted
   * - IC31
     - Clock buffer
     - LMK00105SQ/NOPB
     - 
     - 
   * - IC34
     - Phase detector
     - ADF4002BCPZ-RL7
     - 
     - 

RPI_SYNC mux (IC35) is needed for CM4 and CM5 compatibility purposes.
