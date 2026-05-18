Changelog
#########

The first production LimeSDR XTRX was revision v1.1 and so this changelog starts with changes from that point.

.. note::
   Details of internal-only versions which were never released are not included here.

v1.4
****


LimeSDR-PSB RPCM v1.4 implementation is based on LimePSB RPCM v1.3 board with the schematic and PCB Layout changes described in this document. The major changes are:

* Replaced discontinued SKY13286-359LF RF switches with F2972NEGK. Swapped RF switches RF1 and RF2 ports so RF_SW_TDD polarity inverted.
* Added RF couplers and power detectors on both TX channels
* Changed discrete PoE solution (NCP1083) to PoE module (AG5712-LPB)
*	Changed from Type A HDMI sockets to Type D(Micro) HDMI sockets
*	Replaced clock configuration path jumpers with switches
*	Altium variant function used in the project

Board size and main components positions remained the same as in LimePSB RPCM v1.3. New LimePSB RPCM v1.4 block diagram is shown in Figure 1.

.. figure:: /images/LimePSB-RPCM_v1.4_diagrams_r3_block.png
  :width: 600
  
  Figure: 1 LimePSB RPCM v1.4 block diagram

Raspberry Pi Connector
======================

Raspberry Pi CM4/5 connector signal changes are:

* PCIe LEDs (PCIE_LED_WWAN, PCIE_LED_WLAN, PCIE_LED_WPAN) were moved from RPI connector to I2C GPIO expander number 2 (EXP2).
* Newly added RF power detectors (RFPD) were connected to RPI I2C. Their enable signals RFPD1_CONV and RFPD2_CONV were connected to RPI GPIO25 and RPI GPIO26 respectively. 
* RPI_GPIO3 and RPI_GPIO6 connected to GPIO header (J10).
* ADF_MUXOUT moved from RPI_GPIO3 to EXP2 GPB4.

New Raspberry Pi CM4/5 connector changes are shown in Figure 2.

.. figure:: /images/LimePSB-RPCM_v1.4_RPI_changes.png
  :width: 600
  
  Figure: 2 Raspberry Pi CM4/5 connector

mPCIe Connector
===============

Added 0R resistor in series to PCIE_UIM4 for mPCIe modules compatibility porpuses. mPCIe connector changes are shown in Figure 3.

.. figure:: /images/LimePSB-RPCM_v1.4_mPCIE_changes.png
  :width: 600
  
  Figure: 3 mPCIe connector

Replaced PCIE_PPS_OUT selection resistors R3 and R8 with analog mux as shown in Figure 4.

.. figure:: /images/LimePSB-RPCM_v1.4_COEX_changes.png
  :width: 600
  
  Figure: 4 mPCIe PCIE_PPS_OUT


FPGA
====

Added FPGA_CDONE signal to EXP2 for monitoring purposes. Also 0R was added as a option to disconnect FPGA LED from FPGA_CDONE signal when monitoring by RPI is required. In this case FPGA LED can still indicate CDONE by EXP2 GPB2 pin (FPGA_CDONE_LED). FPGA LED changes are shown in Figure 5.

.. figure:: /images/LimePSB-RPCM_v1.4_CDONE_changes.png
  :width: 600
  
  Figure: 5 FPGA CDONE

Removed FPGA configuration flash from default BOM as shown in Figure 6.

.. figure:: /images/LimePSB-RPCM_v1.4_FLASH_changes.png
  :width: 600
  
  Figure: 6 FPGA flash

Increased HW_VER from 0 to 1. And added test point for FPGA I2C0 signals (FPGA_I2C0_SCL, FPGA_I2C0_SDA) as shown in Figure 7.

.. figure:: /images/LimePSB-RPCM_v1.4_HW_changes.png
  :width: 600
  
  Figure: 7 HW_VER and FPGA I2C0

USB
===

Changed USB header (J31) to Amphenol ICC G823J201240BHR. New header is fully compatible with standard USB header connectors.

HDMI
====

Changed Type A HDMI soctes (J34, J35) to Type D (Micro) HDMI.

Clock
=====

Renamed XO_VC signal name to XORF_VC.

Added testpoint for XO DACs outputs as shown in Figure 8.

.. figure:: /images/LimePSB-RPCM_v1.4_DACTP_changes.png
  :width: 600
  
  Figure: 8 XO DAC test point

Renamed phase detectors signals names REF_ADF to ADF_RFIN and also REF_CLK_IN to ADF_REFIN to better reflect signals purpose as shown in Figure 9.

.. figure:: /images/LimePSB-RPCM_v1.4_DACTP_changes.png
  :width: 600
  
  Figure: 9 Phase detector schematics

Added 0R NF on GNSS_RF_IN net in series with U.FL connector and changed J44 to NF. By default GNSS_RF_IN is connected to INT_TO_EXT2 (SMA) as shown in Figure 10.

.. figure:: /images/LimePSB-RPCM_v1.4_GNSS_changes.png
  :width: 600
  
  Figure: 10 GNSS antenna connection schematics

Added pull down resistor for RPI_PIN18 (2.2k) and RPI_PIN16 (2.2k NF). This change fixes Raspberry Pi CM4/5 ethernet connection not working after booting up. 

All clock circuitry selection jumper were changed to analog muxes a shown in Figure 11.

.. figure:: /images/LimePSB-RPCM_v1.4_diagrams_r3_clock.png
  :width: 600
  
  Figure: 11 LimePSB RPCM v1.4 clock diagram

RFFE
====

Replaced discontinued SKY13286-359LF RF switches with F2972NEGK. Swapped RF switches RF1 and RF2 ports so RF_SW_TDD polarity inverted.

Added RF couplers (HHM22152A2) for channel A and B TX PA RF outputs.

Mentioned RFFE schematic changes are highlighted in Figure 12.

.. figure:: /images/LimePSB-RPCM_v1.4_RFFE_changes.png
  :width: 600
  
  Figure: 12 RFFE 

Due to changed RF_SW_TDD polarity a pull-up resistor was added and pull-down resistor was removed from BOM as shown in Figure 28.

.. figure:: /images/LimePSB-RPCM_v1.4_TDD_changes.png
  :width: 600
  
  Figure: 13 TDD control

Added RF power detectors (LTC5587) for channel A and B TX PA RF outputs. RF power detector schematic is shown in Figure 14.

.. figure:: /images/LimePSB-RPCM_v1.4_RFPD_changes.png
  :width: 600
  
  Figure: 14 RF power detectors schematics

Power 
=====

Changed discrete PoE solution (NCP1083) to PoE module (AG5712-LPB). New POE shcmatic is shown in Figure 15.

.. figure:: /images/LimePSB-RPCM_v1.4_POE_changes.png
  :width: 600
  
  Figure: 15 POE module schematics

Removed VCC2P5 circuit from BOM as shown in Figure 16.

.. figure:: /images/LimePSB-RPCM_v1.4_VCC2P5_changes.png
  :width: 600
  
  Figure: 16 VCC2P5 schematics

Changed R135 from 1k to 330R as shown in Figure 17.

.. figure:: /images/LimePSB-RPCM_v1.4_R135_changes.png
  :width: 600
  
  Figure: 17 Voltage reference schematic

Miscellaneous
=============

Raspberry Pi button was changed to a part with a longer cap (from 3.86 mm to 6.85 mm). Also added option to change button function to RPI CM5 power on/off as shown in Figure 18. 

.. figure:: /images/LimePSB-RPCM_v1.4_BUTTON_changes.png
  :width: 600
  
  Figure: 18 RPI button 

Changed GPIO header (J10) GND pins 7 and 6 to RPI_GPIO6 and RPI_GPIO3 as shown in Figure 19.

.. figure:: /images/LimePSB-RPCM_v1.4_GPIO_changes.png
  :width: 600
  
  Figure 19 GPIO header (J10) 

Added test points for Raspberry Pi I2C0 signals (RPI_I2C0_SCL and RPI_I2C0_SDA) as hsown in Figure 20.

.. figure:: /images/LimePSB-RPCM_v1.4_I2C_changes.png
  :width: 600
  
  Figure 20 I2C signal 

Added new additional I2C IO expander (EXP2). All signals connected to EXP2 are shown in Figure 21.

.. figure:: /images/LimePSB-RPCM_v1.4_EXP_changes.png
  :width: 600
  
  Figure 21 New GPIO expander (EXP2)

New GPIO expander was mainly added to control all new muxes added to clock circuitry. But also some already existing signals were added to it:

* FPGA configuration signals (FPGA_CRESET and FPGA_CDONE). FPGA_CRESET signal moved from EXP1 to EXP2. Also added posibility to monitor FPGA_CDONE by adding it to EXP2. 
* PCIE_LED_WLAN, PCIE_LED_WPAN and PCIE_LED_WWAN were disconnected from RPI connector and connected to EXP2.
* ADF_MUXOUT was moved from RPI GPIO3 to EXP2 GPB4. 

Added Internal U.FL to external SMA connector (EXT2) and renamed old internal U.FL to external SMA connectors to EXT1. New EXT2 SMA connector can be directly connected to on board GNSS module (IC48) RF_IN pin (default) as shown in Figure 22.

.. figure:: /images/LimePSB-RPCM_v1.4_EXT_changes.png
  :width: 600
  
  Figure 22 Internal to external connectors

PCB
===

Layout and PCB changes for LimePSB RPCM v1.4 board are as follows:

* Changes made according to schematic.
* Moved 3.5mm A/V socked to the PCB edge and made cutout for socket ring.
*	Changed tactile switch from 1825027-5 (L=3.86mm) to CT1102V6.85F160 (L=6.85mm).
*	Changed LED light pipes from SLP3-200-100-F (center line 0.2" (5.1mm)) to SLP3-150-100-F (center line 0.15" (3.8mm)).
*	Added HDMI and USB3 internal layer trace impedance requirements in specification.
*	Board size and main components positions remained the same.

.. figure:: /images/LimePSB-RPCM_v1.4_3D_top.png
  :width: 600
  
  Figure 24 LimePSB RPCM v1.4 board top view

.. figure:: /images/LimePSB-RPCM_v1.4_3D_bot.png
  :width: 600
  
  Figure 25 LimePSB RPCM v1.4 board bottom view

v1.3
****

LimeSDR-PSB RPCM v1.3 implementation is based on LimeSDR-KEY RPCM v1.2 board with the schematic and PCB Layout changes described in this document. The major changes are added FPGA (Lattice), 10 MHZ OCXO with alternatives and GNSS receiver. This enables disciplined OCXO function from hardware perspective. For these modifications required to add two additional schematic sheets and change project structure

Board size and main components positions remained the same.

Raspberry Pi Connector
======================

Disconnected PCIE_LED_WWAN from RPi GPIO16 and connected RPI_SPI1_SS2 (XO DAC SS).

Disconnected RPI_RF_SW_TDD from RPi GPIO6 and connected PCIE_LED_WWAN.

Changed SPI interfaces: 
 * RPI_SPI0 SS0 changed from XO DA to FPGA CFG
 * RPI_SPI1 SS1 changed from SR to FPGA
 * RPI_SPI1 SS2 connected to XO DAC (GPIO16 to FPGA)

Board SPI interfaces:
 * RPI_SPI0 (3.3V): FPGA CFG (SS0 - GPIO8), ADF (SS1 - GPIO7)
 * RPI_SPI1 (3.3V): ADC (SS0 - GPIO18), FPGA (SS1 - GPIO17), XO DAC (SS2 - GPIO16 to FPGA)

RPI connector schematic changes are shown in Figure 26.

.. figure:: /images/LimePSB-RPCM_v1.3_RPI_changes.png
  :width: 600
  
  Figure 26: Raspberry Pi CM4/5 connector 

Added bypass option for RPI_PIN11 as shown in Figure 27.

.. figure:: /images/LimePSB-RPCM_v1.3_RPIMUX_changes.png
  :width: 600
  
  Figure 27: RPI_PIN11 analog mux

FPGA
====

Added Lattice ICE5LP4K-SG48ITR FPGA. Schematics are designed for two FPGA configuration modes: Slave SPI (default) and master SPI. 
Connected GNSS interface, clocks, XO DAC, RPI_SPI1, RPI_I2C0, RPI_UART0, HW_VER, BOM_VER, FPGA_GPIO, TDD control and other lines to FPGA as shown in Figure 28.

.. figure:: /images/LimePSB-RPCM_v1.3_FPGA_changes.png
  :width: 600
  
  Figure 28: New FPGA schematics

Added hard ware (HW_VER) and Bill of materials (BOM_VER) version indentification to schemtics as shown in Figure 29.

.. figure:: /images/LimePSB-RPCM_v1.3_BOM_changes.png
  :width: 600
  
  Figure 29: New HW_VER and BOM_VER schematics 

Added new power rails (VCC1P2 and VCC2P5) for FPGA. FPGA power schematics are shown in Figure 30.

.. figure:: /images/LimePSB-RPCM_v1.3_FPGAPOW_changes.png
  :width: 600
  
  Figure 30: New FPGA power schematics

Added configuration flash for FPGA as shown in Figure 31.

.. figure:: /images/LimePSB-RPCM_v1.3_FLASH_changes.png
  :width: 600
  
  Figure 31: New FPGA flash schematics

USB 
===

Replaced USB 2.0 header (J27) with USB 3.0 header. Removed one of the USB 2.0 port and added USB 3.0 port. Renamed USB header power rail to VCC5P0_USB3H. New USB header shcemtics are given in Figure 32. 

.. figure:: /images/LimePSB-RPCM_v1.3_USBHDR_changes.png
  :width: 600
  
  Figure 32: USB header

Replaced USB 3.0 port from dual USB top socket (J30) with a USB 2.0 port. Renamed dual USB  as shown in Figure 33. 

.. figure:: /images/LimePSB-RPCM_v1.3_USBSOC_changes.png
  :width: 600
  
  Figure 33: USB socket changes

From now on when CM4 is used all socket ports are USB2.0. When CM5 is used only bottom port is USB3.0.

Renamed dual USB top socket port signals prefixes to USB3H_1, since they are now connected to USB 3.0 header. 

.. figure:: /images/LimePSB-RPCM_v1.3_USBSW_changes.png
  :width: 600
  
  Figure 34: USB switch changes

Connected GNSS USB to USB HUB port 6 via 0R. 
Swapped some ports between USB header and socket. Changed USB2.0 hub OCS and PRTPWR lines connections according to swapped USB ports between USB header and socket. 
New USB hub schamtics are given in Figure 35.

.. figure:: /images/LimePSB-RPCM_v1.3_USBHUB_changes.png
  :width: 600
  
  Figure 35: USB hub changes

Clock
=====

Renamed clock buffer signals:

 * LMK_CLK_OUTn to LMKRF_CLK_OUTn
 * VCC3P3_LMK to VCC3P3_LMKRF
 * VCC3P3_LMK_VDDO to VCC3P3_LMKRF_VDDO  
 
Resulting clock buffer schematics are shown in Figure 36.

.. figure:: /images/LimePSB-RPCM_v1.3_RFREF_changes.png
  :width: 600
  
  Figure 36: Reference clock buffer

Connected XO DAC SPI to FPGA_SPI0. Added TCXO_DAC mux for two groups of XOs as shown in Figure 37.

.. figure:: /images/LimePSB-RPCM_v1.3_DAC_changes.png
  :width: 600
  
  Figure 37: XO DAC and mux

Added 10 MHz OCXO reference with alternatives and clock buffer.

.. figure:: /images/LimePSB-RPCM_v1.3_10MHZ_changes.png
  :width: 600
  
  Figure 38: XO New 10 MHz reference with clock buffer

Changed EXT_SYNC_OUT header (J36) wit a bigger one. Added new 10 MHz clock LMK10_CLK_OUT3 as one of possible EXT_SYNC_OUT sources. 

Added new clock signal SYNC_OUT that can be sourced by RPI_SYNC_OUT or FPGA_SYNC_OUT. Added new header (J42) for RPI_SYNC_OUT/FPGA_SYNC_OUT path selection to SYNC_OUT.

Changed REF_CLK_IN header (J38) input signal RPI_SYNC_OUT to LMK10_CLK_OUT2.

Changed PCIE_PPS_IN header (J39) input signal RPI_SYNC_OUT to SYNC_OUT.

New clock schematics are given in Figure 39:.

.. figure:: /images/LimePSB-RPCM_v1.3_CLKJMP_changes.png
  :width: 600
  
  Figure 39: Clock config jumpers and connectors

Added GNSS receiver ublox NEO-M8Q. Possible to use LynQ N20B (without USB).


Added ESDs for Dual USB 3.0 socket. 

.. figure:: /images/LimePSB-RPCM_v1.3_GNSS_changes.png
  :width: 600
  
  Figure 40: New GNSS receiver

Power 
=====

Added new LDOs for VCC3P3_CLK2, VCC1P2 and VCC2P5

.. figure:: /images/LimePSB-RPCM_v1.3_PWR_changes.png
  :width: 600
  
  Figure 41: New GNSS receiver

Miscellaneous
=============

Connected FPGA_GPIO0 and FPGA_GPIO1 to J10 pins 10 and 12 instead GND pins as shown in figure 42. 

.. figure:: /images/LimePSB-RPCM_v1.3_GPIO_changes.png
  :width: 600
  
  Figure 42: GPIO connector 

Changed shift registers to I2C I/O expander (MCP23017) because there was not enough SS pins on RPi.

Connected FPGA_CRESET and XO_VC_SEL to IO I2C expander

New I2C I/O expander schematic is given in Figure 43.


.. figure:: /images/LimePSB-RPCM_v1.3_EXP_changes.png
  :width: 600
  
  Figure 43: new I2C I/O expander

Disconnected RPI_RF_SW_TDD and PCIE_UIM8 from RF_SW_TDD and connected FPGA_RF_SW_TDD. Resulting RFFE TDD control schematic is shown in Figure 44.

.. figure:: /images/LimePSB-RPCM_v1.3_TDD_changes.png
  :width: 600
  
  Figure 44: RFFE TDD control 

Corrected FAN controller I2C address note.

Added EMC2301 CLK pull up for fan default drive setting decode.

Added EMC2301 PWM pull up.

.. figure:: /images/LimePSB-RPCM_v1.3_FAN_changes.png
  :width: 600
  
  Figure 45: Fan controller change

PCB
===

Layout and PCB changes for LimePSB RPCM v1.3 board are as follows:

*	Changes made according to schematic
*	Board size and main components positions remained the same

.. figure:: /images/LimePSB-RPCM_v1.3_3D_top.png
  :width: 600
  
  Figure 46: LimePSB RPCM v1.3 3D top view 

.. figure:: /images/LimePSB-RPCM_v1.3_3D_bot.png
  :width: 600
  
  Figure 47: LimePSB RPCM v1.3 3D bottom view

v1.2
****

LimeSDR-PSB RPCM v1.2 implementation is based on LimeSDR-KEY RPCM v1.1 board with the schematic and PCB Layout changes described in this document. The major changes were made to make the board compatible with Raspberry Pi CM4 and CM5 compute modules.

Raspberry Pi Connector
======================

Added USB 3.0 (RPI_USB3) signals for RPi CM5 USB3 ports 0, 1 and added RPI_VBAT as shown in figure 48.

.. figure:: /images/LimePSB-RPCM_v1.2_RPI_changes.png
  :width: 600
  
  Figure 48: Raspberry Pi CM4/5 connector changes

Changed CM4/5 connector from DF40C-100DS-0.4V(51) to 10164227-1001A1RLF. New connector supports higher current (old 0.25A, new 0.3A per contact).

Connected analog mux 74LVC1G3157FZ4 between RPI_TVDAC and CVIDEO as shown in figure 49.

.. figure:: /images/LimePSB-RPCM_v1.2_mux_changes.png
  :width: 600
  
  Figure 49: RPI_PIN11 analog mux

mPCIe
=====

Connected RPI_PCIE_DET_nWAKE signal to mPCIe pin 1 via 0R resistor. Also added capacitor for PCIE_CLK signals because CM5 PCIe CLK signals are no longer capacitively coupled as shown in figure 50.

.. figure:: /images/LimePSB-RPCM_v1.2_mPCIe_changes.png
  :width: 600
  
  Figure 50: mPCIe connector

Miscellaneous
=============

Changed RPI_SYNC_OUT voltage converters VCCA from VCC1P8_RPI to VCC3P3. Populated bypass resistors and voltage converters are no longer mounted (NF) in default BOM as shown in figure 51.

.. figure:: /images/LimePSB-RPCM_v1.2_sync_changes.png
  :width: 600
  
  Figure 51: RPI_SYNC_OUT voltage converters

Changed SYS header (J12) pins:

* Pin 11 connected to RPI_PIN11 instead of RPI_TVDAC
* Pin 10 connected to RPI_RUN_PF instead of GND

New system header schematics are given in figure 52.

.. figure:: /images/LimePSB-RPCM_v1.2_sys_changes.png
  :width: 600
  
  Figure 52: SYS header

Added 4 bit DIP switch to configure:

* Bit 1 RPi boot source.
* Bit 2 RPi USB 2.0 port mux control.
* Bit 3 USB C PD current.
* Bit 4 dual USB socket source. 

New configuration DIP switch schematics are shown in figure 53.

.. figure:: /images/LimePSB-RPCM_v1.2_dip_changes.png
  :width: 600
  
  Figure 53: New 4 bit configuration DIP switch

Added possibility to connect RPI_VBAT to coin cell via not mouted (NF) 0R. Also added 0R for RPI_GLOBAL_EN (PMIC_ENABLE) as shown in figure 54.

.. figure:: /images/LimePSB-RPCM_v1.2_vbat_changes.png
  :width: 600
  
  Figure 54: New VBAT and RPI_GLOBAL_EN 0R resistors

Connected PTP_SYNC_SEL to shift register (SR1) pin Q6 as hsown in figure 55.

.. figure:: /images/LimePSB-RPCM_v1.2_shift_changes.png
  :width: 600
  
  Figure 55: Shift register (SR1)

Fan control
===========

Added EMC2301 fan controller as shown in figure 56.

.. figure:: /images/LimePSB-RPCM_v1.2_fan_changes.png
  :width: 600
  
  Figure 56: New fan controller

ESDs
====

Added ESD for INT_TO_EXT SMA  as shown in figure 57.

.. figure:: /images/LimePSB-RPCM_v1.2_rfesd_changes.png
  :width: 600
  
  Figure 57: New INT_TO EXT ESD protection

Added extra ESD for HDMI (CM5) as shown in figure 58.

.. figure:: /images/LimePSB-RPCM_v1.2_hdmiesd_changes.png
  :width: 600
  
  Figure 58: New HDMI ports ESD protection

Added ESDs for Dual USB 3.0 socket as shown in figure 59.

.. figure:: /images/LimePSB-RPCM_v1.2_usbesd_changes.png
  :width: 600
  
  Figure 59: New Dual USB 3.0 ESD protection

Fitted ESDs on RF ports as shown in figure 60.

.. figure:: /images/LimePSB-RPCM_v1.2_rffeesd_changes.png
  :width: 600
  
  Figure 60: New RF ports ESD rotection

USB
===

Changed USB switch FSUSB42UMX to NX3DV42GU,115 due stock absence. RPI boot header is no longer mounted (NF) since RPI boot source can be configured from new configuration DIP switch. New USB switch schematics are shown in figure 61.

.. figure:: /images/LimePSB-RPCM_v1.2_usbsw_changes.png
  :width: 600
  
  Figure 61: USB switch

Added bypass option for USB_HUB_D0 and PCIE_USB port as shown in figure 62.

.. figure:: /images/LimePSB-RPCM_v1.2_usbbypass_changes.png
  :width: 600
  
  Figure 62: New USB_HUB_D0 and PCIE_USB bypass option

Changed USB 2.0 dual socket to USB 3.0 socket as shown in figure 63. CM5 module offers USB 3.0 ports. 

.. figure:: /images/LimePSB-RPCM_v1.2_usbsocket_changes.png
  :width: 600
  
  Figure 63: New dual USB3 socket

Connected RPI_VBUS_EN IC24 as optional EN control source as shown in figure 64.

.. figure:: /images/LimePSB-RPCM_v1.2_vbus_changes.png
  :width: 600
  
  Figure 64: RPI_VBUS_EN connection

Added USB switches for USB3 socket to switch dual USB socket between USB2.0 hub and CM5 USB3.0 lines as shown in figure 65.

.. figure:: /images/LimePSB-RPCM_v1.2_usbsws_changes.png
  :width: 600
  
  Figure 65: USB 2.0 and 3.0 switches

XO DAC and ADC reference source 
===============================

Populated 2.5V voltage reference for XO DAC and DAC as shown in figure 66.

.. figure:: /images/LimePSB-RPCM_v1.2_vref_changes.png
  :width: 600
  
  Figure 66: New 2.5V reference source

Selected VCC2P5_VREF as source for ADC (R48 fit, R45, R49, C34, C35 NF) as shwn in figure 67.

.. figure:: /images/LimePSB-RPCM_v1.2_adcvref_changes.png
  :width: 600
  
  Figure 67: ADC VREF source

Selected VCC2P5_VREF as source for XO DAC (R165 fit, R166, R172, C139, C140 NF) as shown in figure 68. Also possibility to hard enable OE with resistors is left.

.. figure:: /images/LimePSB-RPCM_v1.2_dacref_changes.png
  :width: 600
  
  Figure 68: DAC VREF source

RFFE
====

PA changed from SBB-5089 to TQP3M9018. Also inductor added for low frequency range. New RF PA schematic are shown in figure 69.

.. figure:: /images/LimePSB-RPCM_v1.2_rffe_changes.png
  :width: 600
  
  Figure 69: RFFE

PCB
===

Layout and PCB changes for LimePSB RPCM v1.2 board are as follows:

* Passive components moved from under RPi CM4/5
* Changes made according to schematic

.. figure:: /images/LimePSB-RPCM_v1.2_3D_top.png
  :width: 600
  
  Figure 70. LimePSB RPCM v1.2 board top view

.. figure:: /images/LimePSB-RPCM_v1.2_3D_bot.png
  :width: 600
  
  Figure 71. LimePSB RPCM v1.2 board bottom view

v1.1
****

First production version.