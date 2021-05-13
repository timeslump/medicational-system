import time
import requests, json 
import RPi.GPIO as GPIO
import threading

def log():
    return '[ '+ time.ctime().split()[3] +' ]'

class SmartBottle(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.isexist = [0, 0]
        self.valid = True
        self.time = [[9, 0], [12, 0], [18, 0]]
        self.id = [1, 2]
        self.push = [8, 10]
        self.buzzer = 10 
        self.pins = {'RED' : 3, 'GREEN' : 5,  'BLUE' : 7}
        self.url = 'XXXXXXXX'
        self.init()

    def init(self):
        print(f'{log()} Initialize GPIO status')
        for push in self.push:
            GPIO.setup(push, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in self.pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
            GPIO.output(pin, True)
        GPIO.setup(self.buzzer, GPIO.OUT)
        self.checkvalid()
        self.ChangeColor("GREEN")
        thread = threading.Thread(target = self.checkTime, args = ())
        thread.start()
        thread.join()
    
    def ChangeColor(self, color):
        for col in self.pins.values():
            GPIO.output(col , True)
        GPIO.output(self.pins[color], False)

    def Ring(self):
        scale = [261, 294, 329, 349, 392, 440 , 493 , 523]
        GPIO.setup(self.buzzer, GPIO.OUT)
        p = GPIO.PWM(button_pin, 600)
        p.start(50)
        for fq in scale:
            p.ChangeFrequency(fq)
            time.sleep(0.5)
        p.stop()

    def checkvalid(self):
        print(f'{log()} Requesting Medicine data Start')
        for i in self.id:
            data = {'getValid' : i}
            #res = requests.post(url, data = data)
            pass
            # self.isexist[i] = 
            # 여기서 불 바꿔주는거 해야댐
        print(f'{log()} Requesting Medicine data End')

    def isPushed(self, idx):
        if GPIO.input(self.push[idx]) == 0:
            return True
        return False
    def Alarm(self, idx)
    def checkTime(self):
        print(f'{log()} Checking Time Thread Start')
        while True:
            cur_time = list(map(int, time.ctime().split()[-2].split(':')[:2]))
            for i, val in enumerate(self.time):
                if cur_time == val:
                    if any(self.isexist) == 1:
                        print(f'{log()} Time to take Medicine')
                        self.Ring(Time)
                        self.ChangeColor('BLUE')
                        #
                        pass
            if cur_time == [0, 0]:
                print(f'{log()} Date changed, Request New data')
                self.checkvalid()
            time.sleep(10)
        print(f'{log()} Checking Time Thread End')
try:
    print(f'{log()} Program Start')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    start = SmartBottle()
    print(f'{log()} Clean GPIO information')
    GPIO.cleanup()
    print(f'{log()} Program End')
except:
    GPIO.cleanup()