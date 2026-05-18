MIPI DSI Display and CSI Camera Connectors
##########################################

LimePSB RPCM has two 15-pin FPC connectors for MIPI DSI display and MIPI CSI camera. MIPI DSI interface is used for connecting serial display. Detailed display 1 connector J15 pinout is as shown in table 13.

.. list-table:: Table 13. MIPI DSI display 1 connector (J15) pinout
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - GND
     - Ground (0V)
   * - 2
     - DSI1_D1_N
     - Output Display1 D1 negative
   * - 3
     - DSI1_D1_P
     - Output Display1 D1 positive
   * - 4
     - GND
     - Ground (0V)
   * - 5
     - DSI1_CLK_N
     - Output Display1 clock negative
   * - 6
     - DSI1_CLK_P
     - Output Display1 clock positive
   * - 7
     - GND
     - Ground (0V)
   * - 8
     - DSI1_D0_N
     - Output Display1 D2 negative
   * - 9
     - DSI1_D0_P
     - Output Display1 D2 positive
   * - 10
     - GND
     - Ground (0V)
   * - 11
     - RPI_I2C0_SCL
     - I2C clock
   * - 12
     - RPI_I2C0_SDA
     - I2C data
   * - 13
     - GND
     - Ground (0V)
   * - 14
     - VCC3P3
     - 3.3V power rail
   * - 15
     - VCC3P3
     - 3.3V power rail

MIPI CSI interface is used for serial camera. Detail camera 1 connector J16 pinout is as shown in table 14.

.. list-table:: Table 14. MIPI CSI camera 1 connector (J16) pinout
   :header-rows: 1
   :stub-columns: 1

   * - Pin
     - Schematic signal name
     - Description
   * - 1
     - GND
     - Ground (0V)
   * - 2
     - CAM1_D0_N
     - Input Camera1 D0 negative
   * - 3
     - CAM1_D0_P
     - Input Camera1 D0 positive
   * - 4
     - GND
     - Ground (0V)
   * - 5
     - CAM1_D1_N
     - Input Camera1 D1 negative
   * - 6
     - CAM1_D1_P
     - Input Camera1 D1 positive
   * - 7
     - GND
     - Ground (0V)
   * - 8
     - CAM1_CLK_N
     - Input Camera1 clock negative
   * - 9
     - CAM1_CLK_P
     - Input Camera1 clock positive
   * - 10
     - GND
     - Ground (0V)
   * - 11
     - CAM1_GPIO0
     - Typically used to shut down the camera
   * - 12
     - CAM1_GPIO1
     - NC
   * - 13
     - RPI_I2C0_SCL
     - I2C clock
   * - 14
     - RPI_I2C0_SDA
     - I2C data
   * - 15
     - VCC3P3
     - 3.3V power rail