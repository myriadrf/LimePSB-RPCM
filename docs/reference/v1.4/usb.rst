USB Subsystem
#############

LimePSB RPCM contains USB 2.0 hub, over current protection, type-C, double type-A sockets and headers. The USB subsystem diagram is as shown in Figure 8.

.. figure:: /images/LimePSB-RPCM_v1.4_diagrams_r3_USB.png
  :width: 600

  Figure 8: LimePSB RPCM v1.4 USB subsystem diagram
  
Main LimePSB RPCM board USB subsystem components:

*	USB type-C socket (J29) is primarily used as one of power supply sources (for more information check section 2.15 Power Distribution). Also it is used to boot CM4/5. To enable RPi USB boot change configuration dip switch (DSW1) bits 1 and 2 to on positions.
*	USB type-A dual socket (J33) may be used to connect USB peripherals to the Raspberry Pi CM4/5. Top socket is USB 3.0 if CM5 is used.
* USB type-A dual socket (J33) and header (J31) have over current protection. Current limit is set to 600 mA. Both sockets share same protection circuitry so if one of them tries to draw more current both sockets will be disabled. Header has it is own separate over current protection.
*	USB2.0 hub USB2517 (IC20) USB 2.0 hub expands Raspberry Pi CM4/5 USB port to dual USB socket (J33), header (J31) and mPCIe (J3). For more information check Table 15.

.. list-table:: Table 15. USB2.0 (IC20) Hub signals
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Pin name
     - Function
     - Schematic signal name
     - Comment
   * - 59/58
     - USBUP_DP / USBUP_DM
     - Root port
     - USB_HUB_D0_P / USB_HUB_D0_N
     - Connected to CM4/5 USB via USB switch
   * - 2/1
     - USBDN1_DP / USBDN1_DM
     - Downstream port
     - USB_HUB_D1_P / USB_HUB_D1_N
     - J3 (mPCIe)
   * - 4/3
     - USBDN2_DP / USBDN2_DM
     - Downstream port
     - USB_HUB_D2_P / USB_HUB_D2_N
     - J33 (USB type-A top socket)
   * - 7/6
     - USBDN3_DP / USBDN3_DM
     - Downstream port
     - USB_HUB_D3_P / USB_HUB_D3_N
     - J31 (USB header pins 3/5)
   * - 9/8
     - USBDN4_DP / USBDN4_DM
     - Downstream port
     - USB_HUB_D4_P / USB_HUB_D4_N
     - J33 (USB type-A bottom socket)
   * - 12/11
     - USBDN5_DP / USBDN5_DM
     - Downstream port
     - USB_HUB_D5_P / USB_HUB_D5_N
     - J31 (USB header pins 2/4)
   * - 54/53
     - USBDN6_DP / USBDN6_DM
     - Downstream port
     - USB_HUB_D6_P / USB_HUB_D5_N
     - IC48 (GNSS)
   * - 56/55
     - USBDN7_DP / USBDN7_DM
     - Downstream port
     - NC
     - NC
