print("Setting up GPIO environment")
print(". . . . . . ")

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) #Connected to PWMA
GPIO.setup(11, GPIO.OUT) #Connected to AIN2
GPIO.setup(12, GPIO.OUT) #Connected to AIN1
GPIO.setup(13, GPIO.OUT) #Connected to STBY
GPIO.setup(15, GPIO.OUT) #Connected to BIN1
GPIO.setup(16, GPIO.OUT) #Connected to BIN2
GPIO.setup(18, GPIO.OUT) #Connected to PWMB
GPIO.setup(21, GPIO.OUT)

print("GPIO environment set-up complete")

pwmA = GPIO.PWM(7,50)
pwmB = GPIO.PWM(18,50)
pwmA.start(100)
pwmB.start(100)

GPIO.output(13, GPIO.LOW)
p = GPIO.PWM(21,50)
p.start(75)
while True:
    try:

        time.sleep(.25)

        inputStr = input('Enter next diection:')

        try:
            char = ord(inputStr[0][0])
            print('Detected char:', char)
        except IndexError:
            char = 53
            print('Wrong key entered. Stopping car.')


        if char == 50:   #straight
            print('Reverse Straight')
            p.ChangeDutyCycle(7.5)
            time.sleep(1)

 #Set the direction of Motor A
            GPIO.output(12, GPIO.LOW) #Set AIN1
            GPIO.output(11, GPIO.HIGH) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)

            #Set the direction of Motor B
            #GPIO.output(16, GPIO.LOW) #Set BIN1
            #GPIO.output(15, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)

        elif char == 53:
            print('Stop')
            pwmA.ChangeDutyCycle(0)
            #pwmB.ChangeDutyCycle(0)

        elif char ==56:

            print('Front Straight')
            p.ChangeDutyCycle(7.5)
            time.sleep(1)

                                                              70,0-1        28%
  GPIO.output(11, GPIO.LOW) #Set AIN1
            GPIO.output(12, GPIO.HIGH) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)


            #Set the direction of Motor B
            #GPIO.output(15, GPIO.LOW) #Set BIN1
            #GPIO.output(16, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)

        elif char == 57:

            print('Front Right')
            p.changeDutyCycle(2.5)
            time.sleep(1)

            #Set the direction of Motor A
            GPIO.output(11, GPIO.LOW) #Set AIN1
            GPIO.output(12, GPIO.HIGH) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(20)
                                                              94,1          42%
 #Set the direction of Motor B
            #GPIO.output(15, GPIO.LOW) #Set BIN1
            #GPIO.output(16, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)

        elif char == 55:

            print('Front Left')
            p.changeDutyCycle(12.5)
            time.sleep(1)

            #Set the direction of Motor A
            GPIO.output(11, GPIO.LOW) #Set AIN1
            GPIO.output(12, GPIO.HIGH) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)


            #Set the direction of Motor B
                                                              94,1          56%
 #Set the direction of Motor B
            #GPIO.output(15, GPIO.LOW) #Set BIN1
            #GPIO.output(16, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)

        elif char == 55:

            print('Front Left')
            p.changeDutyCycle(12.5)
            time.sleep(1)

            #Set the direction of Motor A
            GPIO.output(11, GPIO.LOW) #Set AIN1
            GPIO.output(12, GPIO.HIGH) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)


            #Set the direction of Motor B
                                                              94,1          56%
 #GPIO.output(15, GPIO.LOW) #Set BIN1
            #GPIO.output(16, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(20)

        elif char == 54:

            print('Point Right')
            #Set servo to 0
            p.ChangeDutyCycle(2.5)
            time.sleep(1)

            #Set the direction of Motor A
            GPIO.output(11, GPIO.HIGH) #Set AIN1
            GPIO.output(12, GPIO.LOW) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)


            #Set the direction of Motor B
                                                              136,1         68%
          #GPIO.output(15, GPIO.LOW) #Set BIN1
            #GPIO.output(16, GPIO.HIGH) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)

        elif char == 52:

            print('Point Left')
            #Set servo to 180
            p.ChangeDutyCycle(12.5)
            time.sleep(1)

            #Set the direction of Motor A
            GPIO.output(11, GPIO.HIGH) #Set AIN1
            GPIO.output(12, GPIO.LOW) #Set AIN2
            #Set the Speed / PWM for A
            pwmA.ChangeDutyCycle(100)


            #Set the direction of Motor B
            #GPIO.output(15, GPIO.HIGH) #Set BIN1
            #GPIO.output(16, GPIO.LOW) #Set BIN2
            #Set the Speed / PWM for B
            #pwmB.ChangeDutyCycle(100)
        elif char == 115:

            print('Stopping program')
            break

        else:
            print('Unrecognized Input')
            pwmA.ChangeDutyCycle(0)
            pwmB.ChangeDutyCycle(0)

        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(13, GPIO.LOW)
        print('. . . . . .')
    except KeyboardInterrupt:
        pass

print('Cleaning GPIO state')
print('. . . . . .')
GPIO.output(13, GPIO.LOW)
pwmA.stop()
pwmB.stop()
                                                                                                                                137,1         95%

