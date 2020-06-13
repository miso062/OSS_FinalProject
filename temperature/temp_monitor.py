from flask import Flask, render_template, request
from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()
app = Flask(__name__)

@app.route('/')
def index():
    temp = cpu.temperature
    result = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp))
    return render_template('index.html', result = result);

if __name__ == '__main__':
    app.run(host='192.168.137.64', port=5550)

with open("/home/pi/temprature/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))
        sleep(600)
