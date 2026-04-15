Power Distribution
##################


LimePSB RPCM board power delivery network consists of different power rails with different regulators, voltages and filters. LimePSB RPCM board power distribution block diagram is presented in Figure 10.

.. figure:: /images/LimePSB-RPCM_v1.4_diagrams_r3_power.png
  :width: 600
  
  Figure 10: LimePSB RPCM v1.4 board power distribution block diagram
  
LimePSB RPCM board may be supplied from USB Type-C port (USB Power delivery), Ethernet RJ45 port (PoE) or barrel DC connector (9-14V):

* USB Type-C socket (9-12V 2.5 A or 1.5 A) may be used to supply LimePSB RPCM board. In this case make sure that USB Power Delivery 18W or more power adapter is used. Depending on application board requested current from source may be lowered from 2.5A to 1.5A by changing configuration dip switch (DSW1) bit 3 to ON position.
* RJ45 socket is an alternative way to supply the LimePSB RPCM board. Make sure PoE+ (802.3at) class 4 compliant power source is used.
* Barrel connector (9-14V 2A) also may be used to power LimePSB RPCM board.

To keep on board RTC running and enable GNSS hardware backup mode when board power is disconnected lithium coin cell 3V CR1220 battery must be inserted into BATT1 battery holder.
