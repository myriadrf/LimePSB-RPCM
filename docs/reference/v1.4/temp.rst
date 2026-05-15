Board Temperature Control
#########################

LimePSB-RPCM board has two dedicated 0.1” pitch headers J26 and J27 for fans. Header J26 is standard 4-pin fan header while J27 is 2-pin header. Fan control voltage is VCC_IN (12V) by default, but it may be changed to 3.3V or 5V by resistors. Fan power may be controlled from I/O expander (EXP0) output GPB7 (FAN_CTRL), directly from temperature sensor IC7 pin 3 (LM75_OS) or by FAN controller (IC13) (default). 

4 pin FAN connector (J26) is compatible with 3 pin fans. PWM signal from FAN controller (IC13) can be used to control fan speed by switching MOSFET (VT2) if R92 is fitted (default). If 4 pin fan is used remove R92 and fit R83 to route PWM signal to the connectors 4th pin.

