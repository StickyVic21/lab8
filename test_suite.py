import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)
#Following commands control the state of the output
#GPIO.output(pin, GPIO.HIGH)
#GPIO.output(pin, GPIO.LOW)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# get reading from adc 
# mcp.read_adc(adc_channel)


def read_light_sensor():
    # threshold_light = 600
    raw_value = mcp.read_adc(0)  # Read from channel 0 (light sensor)
    if raw_value > 600:
        print(f"Light: {raw_value} (bright)")
    else:
        print(f"Light: {raw_value} (dark)")

def read_sound_sensor():
    raw_value = mcp.read_adc(1)  # Read from channel 1 (sound sensor)
    # threshold_sound = 500
    # print(f"Sound: {raw_value}")
    if raw_value > 700:
        print(f"Threshold achieved: {raw_value}")
        # Turn on the LED for 100ms
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(11, GPIO.LOW)

while True:
    # time.sleep(0.5) 
    #channel 0 = light sensor
    #channel 1 = sound sensor
    # Blink the LED 5 times with on/off intervals of 500ms
    for _ in range(5):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)

    # Read and print light sensor values for about 5 seconds with intervals of 100ms
    start_time = time.time()
    while time.time() - start_time < 5:
        read_light_sensor()
        time.sleep(0.1)

    # Blink the LED 4 times with on/off intervals of 200ms
    for _ in range(4):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)

    # Read and print sound sensor values for about 5 seconds with intervals of 100ms
    start_time = time.time()
    print("reached sound testing")
    while time.time() - start_time < 5:
        read_sound_sensor()
        time.sleep(0.1)
    print("end of sound testing")

