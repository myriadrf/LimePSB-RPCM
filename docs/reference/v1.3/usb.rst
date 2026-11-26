USB Subsystem
#############

LimePSB RPCM contains USB 2.0 hub, over current protection, type-C, double type-A sockets and headers. The USB subsystem diagram is as shown in Figure 8.

.. figure:: /images/LimePSB-RPCM_v1.3_diagrams_USB.png
  :width: 600

  Figure 8: LimePSB RPCM v1.3 USB subsystem diagram
  
Main LimePSB RPCM board USB subsystem components:

* USB type-C socket (J26) is primarily used as one of power supply sources (for more information see :doc:`power`). It is also used to boot CM4/5. To enable RPi USB boot change configuration DIP switch (SW1) bits 1 and 2 to ON positions (see :doc:`dipsw`). Header J27 (not fitted by default) can be used instead of SW1 bit 2.
* USB type-A dual socket (J30) may be used to connect USB peripherals to the Raspberry Pi CM4/5. Top socket is USB 3.0 if CM5 is used.
* USB type-A dual socket (J30) and header (J28) have over current protection. Current limit is set to 600 mA. Both sockets share same protection circuitry so if one of them tries to draw more current both sockets will be disabled. Header has it is own separate over current protection.
* USB2.0 hub USB2517 (IC19) USB 2.0 hub expands Raspberry Pi CM4/5 USB port to dual USB socket (J30), header (J28) and mPCIe (J3). For more information check Table 15.

.. list-table:: Table 15. USB2.0 (IC19) Hub signals
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
     - J30 (USB type-A top socket)
   * - 7/6
     - USBDN3_DP / USBDN3_DM
     - Downstream port
     - USB_HUB_D3_P / USB_HUB_D3_N
     - J28 (USB header pins 3/5)
   * - 9/8
     - USBDN4_DP / USBDN4_DM
     - Downstream port
     - USB_HUB_D4_P / USB_HUB_D4_N
     - J30 (USB type-A bottom socket)
   * - 12/11
     - USBDN5_DP / USBDN5_DM
     - Downstream port
     - USB_HUB_D5_P / USB_HUB_D5_N
     - J28 (USB header pins 2/4)
   * - 54/53
     - USBDN6_DP / USBDN6_DM
     - Downstream port
     - USB_HUB_D6_P / USB_HUB_D6_N
     - IC40 (GNSS)
   * - 56/55
     - USBDN7_DP / USBDN7_DM
     - Downstream port
     - NC
     - NC
