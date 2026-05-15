Configuration Switch
####################

Boot source, USB 2.0 mux, USB PD configuration and CM4/5 compatibility can be done by switching SW1 DIP switch bits. Detailed switch bit descriptions is given in Table 6.

.. table:: Table 6. DIP switch configuration bits

  +---------+---------------------------+-----------------------------------------------------------------------------------------------------+
  | **Bit** | **Schematic signal name** | **Description**                                                                                     |
  +=========+===========================+=====================================================================================================+
  | 1       | RPI_nRPIBOOT              | RPi boot source:                                                                                    |
  |         |                           |                                                                                                     |
  |         |                           | OFF: RPI boots from eMMC/uSD (default).                                                             |
  |         |                           |                                                                                                     |
  |         |                           | ON: Booting from eMMC will be stopped and booting will be transferred to RPi boot which is via USB. |
  +---------+---------------------------+-----------------------------------------------------------------------------------------------------+
  | 2       | USB_C_RPI1                | RPi USB 2.0 port mux control:                                                                       |
  |         |                           |                                                                                                     |
  |         |                           | OFF: RPi USB is connected to USB hub (default).                                                     |
  |         |                           |                                                                                                     |
  |         |                           | ON: RPi USB is connected to USB C connector.                                                        |
  +---------+---------------------------+-----------------------------------------------------------------------------------------------------+
  | 3       | USB_PD_I                  | USB C PD current configuration:                                                                     |
  |         |                           |                                                                                                     |
  |         |                           | OFF: I=2.5A (default).                                                                              |
  |         |                           |                                                                                                     |
  |         |                           | ON: I=1.5A.                                                                                         |
  +---------+---------------------------+-----------------------------------------------------------------------------------------------------+
  | 4       | EN_CM5_USB3               | Dual USB socket source:                                                                             |
  |         |                           |                                                                                                     |
  |         |                           | OFF: connected to USB 2.0 hub (for CM4).                                                            |
  |         |                           |                                                                                                     |
  |         |                           | ON: connected to CM5 USB3.0 lines (for CM5).                                                        |
  +---------+---------------------------+-----------------------------------------------------------------------------------------------------+