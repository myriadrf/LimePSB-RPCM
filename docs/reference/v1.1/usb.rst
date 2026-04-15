USB Subsystem
#############

LimePSB RPCM contains USB 2.0 hub, over current protection, type-C, double type-A sockets and headers. The USB subsystem diagram is as shown in Figure 8.

.. figure:: /images/LimePSB-RPCM_v1.1_diagrams_r1_USB.png
  :width: 600

  Figure 8: LimePSB RPCM v1.1 USB subsystem diagram
  
Main LimePSB RPCM board USB subsystem components:

  * USB type-C socket (J27) is primarily used as LimeSPB RPCM one of power supply sources (for more information check Power Distribution section). To enable RPi USB boot mount nRPIBOOT jumper on J14 pins 1-2 and mount a jumper on header J28 to switch Raspberry Pi USB from USB hub to USB C (more information check section 2.2 Raspberry Pi CM4 Configuration Headers).
  * USB type-A dual sockets (J29) may be used to connect USB peripherals to the Raspberry Pi CM4.
  * USB2.0 hub USB2517 (IC19) USB 2.0 hub expands Raspberry Pi CM4 USB port to dual USB socket (J29), header (J31) and mPCIe (J3). For more information check Table 13.

.. list-table:: Table 13. USB2.0 (IC19) Hub signals
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Pin name
     - Function
     - Schematic signal name
     - Connector ID
   * - 59/58
     - USBUP_DP/

       USBUP_DM
     - Root port
     - USB_HUB_D0_P/

       USB_HUB_D0_N
     - Connected to CM4 USB via USB switch
   * - 2/1
     - USBDN1_DP/

       USBDN1_DM
     - Downstream port
     - USB_HUB_D1_P/

       USB_HUB_D1_N
     - J3 (mPCIe)
   * - 4/3
     - USBDN2_DP/

       USBDN2_DM
     - Downstream port
     - USB_HUB_D2_P/

       USB_HUB_D2_N
     - J29 (bottom)
   * - 7/6
     - USBDN3_DP/

       USBDN3_DM
     - Downstream port
     - USB_HUB_D3_P/

       USB_HUB_D3_N
     - J29 (top)
   * - 9/8
     - USBDN4_DP/

       USBDN4_DM
     - Downstream port
     - USB_HUB_D4_P/

       USB_HUB_D4_N
     - J31 (pins 5/3)
   * - 12/11
     - USBDN5_DP/

       USBDN5_DM
     - Downstream port
     - USB_HUB_D5_P/

       USB_HUB_D5_N
     - J31 (pins 6/4)
   * - 54/53
     - USBDN6_DP/

       USBDN6_DM
     - Downstream port
     - NC
     - NC
   * - 56/55
     - USBDN7_DP/

       USBDN7_DM
     - Downstream port
     - NC
     - NC

Dual USB 3.0 socket (J29) and header (J27) have over current protection. Current limit is set to 600 mA. Both sockets share same protection circuitry so if one of them tries to draw more current both sockets will be disabled. Header has it is own separate over current protection.
