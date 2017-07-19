import time
class Lightpole:
    green_pin = 2
    yellow_pin = 3
    red_pin = 4
    buzzer_pin = 5

    def __init__(self, ip):
        Lightpole.ip = ip

    def on(self, pin):
        print(str(pin) + " on")

    def off(self, pin):
        print(str(pin) + " off")

    def alternate(self, pin):
        while True:
            self.on(pin)
            time.sleep(0.3)
            self.off(pin)
            time.sleep(0.3)

    def buzzer_and_color(self, color_pin):
        self.on(self.buzzer_pin)
        self.on(color_pin)
        time.sleep(2)
        self.off(self.buzzer_pin)


    def print_ip(self):
        print(Lightpole.ip)


lightpole = Lightpole('192.168.1.1')
lightpole.buzzer_and_color(lightpole.red_pin)