import wiringpi as wiringpi
import datetime
import time

ic1_pin_base = 65
ic1_i2c_addr = 0x24

ic2_pin_base = 81
ic2_i2c_addr = 0x20

wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)
wiringpi.mcp23017Setup(ic2_pin_base,ic2_i2c_addr)

# setup pins
Segment1_1 = 88
Segment1_2 = 87
Segment1_3 = 86
Segment1_4 = 85
Segment1_5 = 84
Segment1_6 = 83
Segment1_7 = 82

Segment2_1 = 96
Segment2_2 = 95
Segment2_3 = 94
Segment2_4 = 93
Segment2_5 = 92
Segment2_6 = 91
Segment2_7 = 90

Segment3_1 = 73
Segment3_2 = 74
Segment3_3 = 75
Segment3_4 = 76
Segment3_5 = 77
Segment3_6 = 78
Segment3_7 = 79

Segment4_1 = 65
Segment4_2 = 66
Segment4_3 = 67
Segment4_4 = 68
Segment4_5 = 69
Segment4_6 = 70
Segment4_7 = 71

Colon = 80

# set pin mode
wiringpi.pinMode(Segment1_1,1)
wiringpi.pinMode(Segment1_2,1)
wiringpi.pinMode(Segment1_3,1)
wiringpi.pinMode(Segment1_4,1)
wiringpi.pinMode(Segment1_5,1)
wiringpi.pinMode(Segment1_6,1)
wiringpi.pinMode(Segment1_7,1)

wiringpi.pinMode(Segment2_1,1)
wiringpi.pinMode(Segment2_2,1)
wiringpi.pinMode(Segment2_3,1)
wiringpi.pinMode(Segment2_4,1)
wiringpi.pinMode(Segment2_5,1)
wiringpi.pinMode(Segment2_6,1)
wiringpi.pinMode(Segment2_7,1)

wiringpi.pinMode(Segment3_1,1)
wiringpi.pinMode(Segment3_2,1)
wiringpi.pinMode(Segment3_3,1)
wiringpi.pinMode(Segment3_4,1)
wiringpi.pinMode(Segment3_5,1)
wiringpi.pinMode(Segment3_6,1)
wiringpi.pinMode(Segment3_7,1)

wiringpi.pinMode(Segment4_1,1)
wiringpi.pinMode(Segment4_2,1)
wiringpi.pinMode(Segment4_3,1)
wiringpi.pinMode(Segment4_4,1)
wiringpi.pinMode(Segment4_5,1)
wiringpi.pinMode(Segment4_6,1)
wiringpi.pinMode(Segment4_7,1)

wiringpi.pinMode(Colon,1)

# set all to 0
wiringpi.digitalWrite(Segment1_1,0)
wiringpi.digitalWrite(Segment1_2,0)
wiringpi.digitalWrite(Segment1_3,0)
wiringpi.digitalWrite(Segment1_4,0)
wiringpi.digitalWrite(Segment1_5,0)
wiringpi.digitalWrite(Segment1_6,0)
wiringpi.digitalWrite(Segment1_7,0)

wiringpi.digitalWrite(Segment2_1,0)
wiringpi.digitalWrite(Segment2_2,0)
wiringpi.digitalWrite(Segment2_3,0)
wiringpi.digitalWrite(Segment2_4,0)
wiringpi.digitalWrite(Segment2_5,0)
wiringpi.digitalWrite(Segment2_6,0)
wiringpi.digitalWrite(Segment2_7,0)

wiringpi.digitalWrite(Segment3_1,0)
wiringpi.digitalWrite(Segment3_2,0)
wiringpi.digitalWrite(Segment3_3,0)
wiringpi.digitalWrite(Segment3_4,0)
wiringpi.digitalWrite(Segment3_5,0)
wiringpi.digitalWrite(Segment3_6,0)
wiringpi.digitalWrite(Segment3_7,0)

wiringpi.digitalWrite(Segment4_1,0)
wiringpi.digitalWrite(Segment4_2,0)
wiringpi.digitalWrite(Segment4_3,0)
wiringpi.digitalWrite(Segment4_4,0)
wiringpi.digitalWrite(Segment4_5,0)
wiringpi.digitalWrite(Segment4_6,0)
wiringpi.digitalWrite(Segment4_7,0)

wiringpi.digitalWrite(Colon,0)

try:

    while True:

        # current time
        now = datetime.datetime.now()
        # split current time into single digits
        clockDigits = [now.hour // 10, now.hour % 10, now.minute // 10, now.minute % 10]

        # sleep timer
        if now.hour == 22:
            wiringpi.digitalWrite(Segment1_1,0)
            wiringpi.digitalWrite(Segment1_2,0)
            wiringpi.digitalWrite(Segment1_3,0)
            wiringpi.digitalWrite(Segment1_4,0)
            wiringpi.digitalWrite(Segment1_5,0)
            wiringpi.digitalWrite(Segment1_6,0)
            wiringpi.digitalWrite(Segment1_7,0)

            wiringpi.digitalWrite(Segment2_1,0)
            wiringpi.digitalWrite(Segment2_2,0)
            wiringpi.digitalWrite(Segment2_3,0)
            wiringpi.digitalWrite(Segment2_4,0)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,0)

            wiringpi.digitalWrite(Segment3_1,0)
            wiringpi.digitalWrite(Segment3_2,0)
            wiringpi.digitalWrite(Segment3_3,0)
            wiringpi.digitalWrite(Segment3_4,0)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,0)
            wiringpi.digitalWrite(Segment3_7,0)

            wiringpi.digitalWrite(Segment4_1,0)
            wiringpi.digitalWrite(Segment4_2,0)
            wiringpi.digitalWrite(Segment4_3,0)
            wiringpi.digitalWrite(Segment4_4,0)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,0)

            wiringpi.digitalWrite(Colon,0)
            
            time.sleep(9*60*60)
            
        # leading hour
        if now.hour // 10 == 0:
            wiringpi.digitalWrite(Segment1_1,0)
            wiringpi.digitalWrite(Segment1_2,0)
            wiringpi.digitalWrite(Segment1_3,0)
            wiringpi.digitalWrite(Segment1_4,0)
            wiringpi.digitalWrite(Segment1_5,0)
            wiringpi.digitalWrite(Segment1_6,0)
            wiringpi.digitalWrite(Segment1_7,0)

        elif now.hour // 10 == 1:
            wiringpi.digitalWrite(Segment1_1,0)
            wiringpi.digitalWrite(Segment1_2,1)
            wiringpi.digitalWrite(Segment1_3,1)
            wiringpi.digitalWrite(Segment1_4,0)
            wiringpi.digitalWrite(Segment1_5,0)
            wiringpi.digitalWrite(Segment1_6,0)
            wiringpi.digitalWrite(Segment1_7,0)

        elif now.hour // 10 == 2:
            wiringpi.digitalWrite(Segment1_1,1)
            wiringpi.digitalWrite(Segment1_2,1)
            wiringpi.digitalWrite(Segment1_3,0)
            wiringpi.digitalWrite(Segment1_4,1)
            wiringpi.digitalWrite(Segment1_5,1)
            wiringpi.digitalWrite(Segment1_6,0)
            wiringpi.digitalWrite(Segment1_7,1)

        else:
            wiringpi.digitalWrite(Segment1_1,0)
            wiringpi.digitalWrite(Segment1_2,0)
            wiringpi.digitalWrite(Segment1_3,0)
            wiringpi.digitalWrite(Segment1_4,0)
            wiringpi.digitalWrite(Segment1_5,0)
            wiringpi.digitalWrite(Segment1_6,0)
            wiringpi.digitalWrite(Segment1_7,0)

        # trailing hour
        if now.hour % 10 == 0:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,1)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,0)

        elif now.hour % 10 == 1:
            wiringpi.digitalWrite(Segment2_1,0)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,0)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,0)

        elif now.hour % 10 == 2:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,0)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,1)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 3:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 4:
            wiringpi.digitalWrite(Segment2_1,0)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,0)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 5:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,0)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 6:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,0)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,1)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 7:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,0)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,0)

        elif now.hour % 10 == 8:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,1)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,1)

        elif now.hour % 10 == 9:
            wiringpi.digitalWrite(Segment2_1,1)
            wiringpi.digitalWrite(Segment2_2,1)
            wiringpi.digitalWrite(Segment2_3,1)
            wiringpi.digitalWrite(Segment2_4,1)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,1)
            wiringpi.digitalWrite(Segment2_7,1)

        else:
            wiringpi.digitalWrite(Segment2_1,0)
            wiringpi.digitalWrite(Segment2_2,0)
            wiringpi.digitalWrite(Segment2_3,0)
            wiringpi.digitalWrite(Segment2_4,0)
            wiringpi.digitalWrite(Segment2_5,0)
            wiringpi.digitalWrite(Segment2_6,0)
            wiringpi.digitalWrite(Segment2_7,0)

        # leading minute
        if now.minute // 10 == 0:
            wiringpi.digitalWrite(Segment3_1,1)
            wiringpi.digitalWrite(Segment3_2,1)
            wiringpi.digitalWrite(Segment3_3,1)
            wiringpi.digitalWrite(Segment3_4,1)
            wiringpi.digitalWrite(Segment3_5,1)
            wiringpi.digitalWrite(Segment3_6,1)
            wiringpi.digitalWrite(Segment3_7,0)

        elif now.minute // 10 == 1:
            wiringpi.digitalWrite(Segment3_1,0)
            wiringpi.digitalWrite(Segment3_2,1)
            wiringpi.digitalWrite(Segment3_3,1)
            wiringpi.digitalWrite(Segment3_4,0)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,0)
            wiringpi.digitalWrite(Segment3_7,0)

        elif now.minute // 10 == 2:
            wiringpi.digitalWrite(Segment3_1,1)
            wiringpi.digitalWrite(Segment3_2,1)
            wiringpi.digitalWrite(Segment3_3,0)
            wiringpi.digitalWrite(Segment3_4,1)
            wiringpi.digitalWrite(Segment3_5,1)
            wiringpi.digitalWrite(Segment3_6,0)
            wiringpi.digitalWrite(Segment3_7,1)

        elif now.minute // 10 == 3:
            wiringpi.digitalWrite(Segment3_1,1)
            wiringpi.digitalWrite(Segment3_2,1)
            wiringpi.digitalWrite(Segment3_3,1)
            wiringpi.digitalWrite(Segment3_4,1)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,0)
            wiringpi.digitalWrite(Segment3_7,1)

        elif now.minute // 10 == 4:
            wiringpi.digitalWrite(Segment3_1,0)
            wiringpi.digitalWrite(Segment3_2,1)
            wiringpi.digitalWrite(Segment3_3,1)
            wiringpi.digitalWrite(Segment3_4,0)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,1)
            wiringpi.digitalWrite(Segment3_7,1)

        elif now.minute // 10 == 5:
            wiringpi.digitalWrite(Segment3_1,1)
            wiringpi.digitalWrite(Segment3_2,0)
            wiringpi.digitalWrite(Segment3_3,1)
            wiringpi.digitalWrite(Segment3_4,1)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,1)
            wiringpi.digitalWrite(Segment3_7,1)

        else:
            wiringpi.digitalWrite(Segment3_1,0)
            wiringpi.digitalWrite(Segment3_2,0)
            wiringpi.digitalWrite(Segment3_3,0)
            wiringpi.digitalWrite(Segment3_4,0)
            wiringpi.digitalWrite(Segment3_5,0)
            wiringpi.digitalWrite(Segment3_6,0)
            wiringpi.digitalWrite(Segment3_7,0)

        # trailing minute
        if now.minute % 10 == 0:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,1)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,0)

        elif now.minute % 10 == 1:
            wiringpi.digitalWrite(Segment4_1,0)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,0)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,0)

        elif now.minute % 10 == 2:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,0)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,1)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 3:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 4:
            wiringpi.digitalWrite(Segment4_1,0)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,0)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 5:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,0)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 6:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,0)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,1)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 7:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,0)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,0)

        elif now.minute % 10 == 8:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,1)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,1)

        elif now.minute % 10 == 9:
            wiringpi.digitalWrite(Segment4_1,1)
            wiringpi.digitalWrite(Segment4_2,1)
            wiringpi.digitalWrite(Segment4_3,1)
            wiringpi.digitalWrite(Segment4_4,1)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,1)
            wiringpi.digitalWrite(Segment4_7,1)

        else:
            wiringpi.digitalWrite(Segment4_1,0)
            wiringpi.digitalWrite(Segment4_2,0)
            wiringpi.digitalWrite(Segment4_3,0)
            wiringpi.digitalWrite(Segment4_4,0)
            wiringpi.digitalWrite(Segment4_5,0)
            wiringpi.digitalWrite(Segment4_6,0)
            wiringpi.digitalWrite(Segment4_7,0)

        wiringpi.digitalWrite(Colon,1)
        
        time.sleep(1)
        
except KeyboardInterrupt:

    print "Clock stopped"

finally:

    # turn off all pins
    wiringpi.digitalWrite(Segment1_1,0)
    wiringpi.digitalWrite(Segment1_2,0)
    wiringpi.digitalWrite(Segment1_3,0)
    wiringpi.digitalWrite(Segment1_4,0)
    wiringpi.digitalWrite(Segment1_5,0)
    wiringpi.digitalWrite(Segment1_6,0)
    wiringpi.digitalWrite(Segment1_7,0)

    wiringpi.digitalWrite(Segment2_1,0)
    wiringpi.digitalWrite(Segment2_2,0)
    wiringpi.digitalWrite(Segment2_3,0)
    wiringpi.digitalWrite(Segment2_4,0)
    wiringpi.digitalWrite(Segment2_5,0)
    wiringpi.digitalWrite(Segment2_6,0)
    wiringpi.digitalWrite(Segment2_7,0)

    wiringpi.digitalWrite(Segment3_1,0)
    wiringpi.digitalWrite(Segment3_2,0)
    wiringpi.digitalWrite(Segment3_3,0)
    wiringpi.digitalWrite(Segment3_4,0)
    wiringpi.digitalWrite(Segment3_5,0)
    wiringpi.digitalWrite(Segment3_6,0)
    wiringpi.digitalWrite(Segment3_7,0)

    wiringpi.digitalWrite(Segment4_1,0)
    wiringpi.digitalWrite(Segment4_2,0)
    wiringpi.digitalWrite(Segment4_3,0)
    wiringpi.digitalWrite(Segment4_4,0)
    wiringpi.digitalWrite(Segment4_5,0)
    wiringpi.digitalWrite(Segment4_6,0)
    wiringpi.digitalWrite(Segment4_7,0)
    
    wiringpi.digitalWrite(Colon,0)

    # change all pins to input
    wiringpi.pinMode(Segment1_1,0)
    wiringpi.pinMode(Segment1_2,0)
    wiringpi.pinMode(Segment1_3,0)
    wiringpi.pinMode(Segment1_4,0)
    wiringpi.pinMode(Segment1_5,0)
    wiringpi.pinMode(Segment1_6,0)
    wiringpi.pinMode(Segment1_7,0)

    wiringpi.pinMode(Segment2_1,0)
    wiringpi.pinMode(Segment2_2,0)
    wiringpi.pinMode(Segment2_3,0)
    wiringpi.pinMode(Segment2_4,0)
    wiringpi.pinMode(Segment2_5,0)
    wiringpi.pinMode(Segment2_6,0)
    wiringpi.pinMode(Segment2_7,0)

    wiringpi.pinMode(Segment3_1,0)
    wiringpi.pinMode(Segment3_2,0)
    wiringpi.pinMode(Segment3_3,0)
    wiringpi.pinMode(Segment3_4,0)
    wiringpi.pinMode(Segment3_5,0)
    wiringpi.pinMode(Segment3_6,0)
    wiringpi.pinMode(Segment3_7,0)

    wiringpi.pinMode(Segment4_1,0)
    wiringpi.pinMode(Segment4_2,0)
    wiringpi.pinMode(Segment4_3,0)
    wiringpi.pinMode(Segment4_4,0)
    wiringpi.pinMode(Segment4_5,0)
    wiringpi.pinMode(Segment4_6,0)
    wiringpi.pinMode(Segment4_7,0)
    
    wiringpi.pinMode(Colon,0)
