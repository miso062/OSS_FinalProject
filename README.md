Open Source Software Final Project
===============================
- Raspberry Pi
- real time temperature checking server

### 21600062 Kim Miso

## 개요
1. 라즈베리 파이의 온도에 대한 정보를 실시간으로 서버에 전송한다.
2. 서버가 중단되어 있는 경우 라즈베리 파이의 온도를 10분에 한번씩 기록하여 .csv 파일로 남긴다.

## 1. git clone
``` c
$ cd ~ 또는 cd
$ git clone https://github.com/miso062/OSS_FinalProject.git
```

## 2. shell script 파일을 실행하여 작업에 필요한 package 설치
``` c
$ ./setting.sh
```

## 3. temp_monitor.py 수정
``` 
if __name__ == '__main__':
    app.run(host='000.000.000.00', port=5550)
```
* 해당 서버의 IP로 host 를 바꾸어 준다.

``` 
with open("/home/pi/temprature/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))
        sleep(600)
```
* with open 안에 있는 파일 경로를 원하는 경로로 수정한다.
* 온도가 기록된 .csv 파일이 해당 경로에 저장된다.



## 4. python temp_monitor.py
``` 
$ python temp_monitor.py
```
실행 후 
입력한 ip:port를 입력하면 라즈베리 파이의 온도를 실시간으로 확인할 수 있다.

![page.PNG](https://github.com/miso062/OSS_FinalProject/blob/master/img/page.PNG)

* ctrl + c를 누르면 서버가 종료되며, .csv 파일로 온도 기록이 시작된다.
  - 원한다면 temp_monitor.py 내의 sleep(time)값-second가 기준임-을 바꾸어 기록되는 시간을 변경할 수 있다.
* ctrl + c를 한번 더 누르면 .csv 파일로의 기록이 종료된다.

![csvfile.PNG](https://github.com/miso062/OSS_FinalProject/blob/master/img/csvfile.PNG)
