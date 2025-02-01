import machine
import utime

# Define pins for three traffic lights
traffic_lights = {
    1: {'red': machine.Pin(0, machine.Pin.OUT), 'yellow': machine.Pin(1, machine.Pin.OUT), 'green': machine.Pin(2, machine.Pin.OUT)},
    2: {'red': machine.Pin(3, machine.Pin.OUT), 'yellow': machine.Pin(4, machine.Pin.OUT), 'green': machine.Pin(5, machine.Pin.OUT)},
    3: {'red': machine.Pin(6, machine.Pin.OUT), 'yellow': machine.Pin(7, machine.Pin.OUT), 'green': machine.Pin(8, machine.Pin.OUT)}
}

# Define time delays
red_delay = 10
yellow_delay = 2
green_delay = 10

def set_traffic_light(light_number, red, yellow, green):
    """Set the state of a traffic light."""
    traffic_lights[light_number]['red'].value(red)
    traffic_lights[light_number]['yellow'].value(yellow)
    traffic_lights[light_number]['green'].value(green)

def all_red_except(active_light):
    """Sets all lights to red except the one turning green."""
    for light in traffic_lights:
        set_traffic_light(light, 1, 0, 0)
    set_traffic_light(active_light, 0, 0, 1)

def traffic_sequence():
    """Runs the traffic light sequence in a loop."""
    try:
        while True:
            for light in [1, 2, 3]: 
                all_red_except(light) 
                utime.sleep(green_delay)

                # Switch to yellow before red
                set_traffic_light(light, 0, 1, 0)
                utime.sleep(yellow_delay)

    except KeyboardInterrupt:
        print("Traffic light system interrupted. Turning off all lights.")
        for light in traffic_lights:
            set_traffic_light(light, 0, 0, 0)  # Turn off all lights

# Run the traffic light system
traffic_sequence()
