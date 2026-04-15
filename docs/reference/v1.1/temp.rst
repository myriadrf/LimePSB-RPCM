Board Temperature Control
#########################

LimePSB RPCM board has two dedicated 0.1” pitch headers J25 and J26 for fans. Header J25 is standard 4-pin fan header while J25 is 2-pin header. Fan control voltage is 5V by default, but it may be changed to 3.3V or supply voltage VCC_INT by resistors. Fan power may be controlled from shift register IC16 output Q7 (FAN_CTRL, default) or directly from temperature sensor IC9 pin 3 (LM75_OS).
