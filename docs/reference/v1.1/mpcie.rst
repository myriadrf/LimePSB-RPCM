mPCIe Connector
###############


LimePSB RPCM board features mini PCIe x1 specification compatible socket. LimePSB RPCM board mPCIe socket is also compatible with some non-standard expansion boards like LimeSDR-XTRX, LoRaWAN and LoRa Core. More detailed information is listed in Table 19.


.. list-table:: Table 19. LimePSB RPCM board Mini PCIe x1 connector pinout
   :header-rows: 1

   * - Pin
     - Mini PCIe x1 
  
       Specification Reference
     - LimePSB RPCM 
      
       schematic signal name
     - XTRX reference
     - LoRaWAN reference
     - SX1302/03 Corecell 

       schematic signal name
   * - 1
     - Wake#
     - NC
     - Wake#
     - NC
     - NC
   * - 2
     - 3.3 Vaux
     - VCC3P3
     - +3.3V
     - VCC
     - VCC5V_IN
   * - 3
     - COEX1
     - PCIE_COEX1
     - 1PPSI_GPIO1(1N)
     - NC
     - NC
   * - 4
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 5
     - COEX2
     - PCIE_COEX2
     - 1PPSO_GPIO2(1P)
     - PPS_IN
     - NC
   * - 6
     - GND
     - VCC1P5
     - +1.5V
     - NC
     - GPIO(6) (NC)
   * - 7
     - CLKREQ#
     - RPI_PCIE_CLK_nREQ
     - CLKREQ#
     - NC
     - NC
   * - 8
     - UIM PWR
     - UIM_PWR
     - UIM_PWR
     - NC
     - NC
   * - 9
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 10
     - UIM_DATA
     - UIM_DATA
     - UIM_DATA
     - SWDIO
     - NC
   * - 11
     - REFCLK-
     - RPI_PCIE_CLK_N
     - REF_CLK-
     - NC
     - NC
   * - 12
     - UIM_CLK
     - UIM_CLK
     - UIM_CLK
     - SWCLK
     - NC
   * - 13
     - REFCLK+
     - RPI_PCIE_CLK_P
     - REF_CLK+
     - NC
     - NC
   * - 14
     - UIM_RESET
     - UIM_RESET
     - UIM_RESET
     - NC
     - NC
   * - 15
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 16
     - UIM_VPP
     - UIM_VPP
     - UIM_VPP
     - BOOT0
     - POWER_EN(NC)
   * - 17
     - Reserved
     - PCIE_UIM8
     - TDD_GPIO3_N
     - NC
     - HOST_SCK (NC)
   * - 18
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 19
     - Reserved
     - PCIE_UIMC4
     - MHZ_IN
     - NC
     - HOST_MISO(NC)
   * - 20
     - W_DISABLE#
     - NC
     - TDD_GPIO3_P
     - nDISABLE
     - NC
   * - 21
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 22
     - PERST#
     - RPI_PCIE_nRST
     - PERST#
     - nRESET
     - SX1302_RESET_HOST (NC)
   * - 23
     - PERn0
     - RPI_PCIE_RX_N
     - PERn0
     - NC
     - HOST_MOSI(NC)
   * - 24
     - 3.3Vaux
     - VCC3P3
     - +3.3Vaux
     - VCC
     - SX1261_BUSY (NC)
   * - 25
     - PERp0
     - RPI_PCIE_RX_P
     - PERp0
     - NC
     - HOST_CSN (NC)
   * - 26
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 27
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 28
     - 1.5Volt
     - VCC1P5
     - +1.5V
     - NC
     - SX1302_GPIO_8 (NC)
   * - 29
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 30
     - SMB CLK
     - PCIE_SMB_CLK
     - MHZ_OUT
     - NC
     - I2C_SCL (NC)
   * - 31
     - PETn0
     - PCIE_PET0_N
     - PETn0
     - NC
     - PPS
   * - 32
     - SMB Data
     - PCIE_SMB_DATA
     - GPIO8
     - NC
     - I2C_SDA (NC)
   * - 33
     - PETp0
     - PCIE_PET0_P
     - PETp0
     - NC
     - NC
   * - 34
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 35
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 36
     - USB_D-
     - PCIE_USB_N
     - USB_DN
     - USB_D- / Tx
     - USB_DM
   * - 37
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 38
     - USB_D+
     - PCIE_USB_P
     - USB_DP
     - USB_D+ / Rx
     - USB_DP
   * - 39
     - 3.3Vaux
     - VCC3P3
     - PERp1
     - VCC
     - VCC3V3_IN
   * - 40
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 41
     - 3.3Vaux
     - VCC3P3
     - PERp1
     - VCC
     - VCC3V3_IN
   * - 42
     - LED_WWAN#
     - PCIE_LED_WWAN
     - LED_WWAN#_GPIO5
     - nTX
     - NC
   * - 43
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 44
     - LED_WLAN#
     - PCIE_LED_WLAN
     - LED_WLAN#_GPIO6
     - nRX
     - SX1261_NSS (NC)
   * - 45
     - Reserved
     - NC
     - GND
     - NC
     - JTCK-SWCLK (NC)
   * - 46
     - LED_WPAN#
     - PCIE_LED_WPAN
     - LED_WPAN#_GPIO7
     - NC
     - SX1261_DIO1 (NC)
   * - 47
     - Reserved
     - NC
     - PETn1
     - NC
     - JTMS-SWDIO (NC)
   * - 48
     - 1.5Volt
     - VCC1P5
     - +1.5V
     - NC
     - SX1261_NRESET(NC)
   * - 49
     - Reserved
     - NC
     - PETp1
     - NC
     - MCU_NRESET (NC)
   * - 50
     - GND
     - GND
     - GND
     - GND
     - GND
   * - 51
     - Reserved
     - NC
     - GND
     - NC
     - MCU_BOOT0 (NC)
   * - 52
     - 3.3Vaux
     - VCC3P3
     - +3.3V
     - VCC
     - VCC3V3_IN