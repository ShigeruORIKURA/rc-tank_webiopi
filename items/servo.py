import sys
import time
import Adafruit_PCA9685

PWM_FREQUENCY = 60
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(PWM_FREQUENCY)

R_SERVO_CH = 4
L_SERVO_CH = 11

MIN_SERVO_PULSE_WIDH = 150
MAX_SERVO_PULSE_WIDH = 450
r_servo_val = MIN_SERVO_PULSE_WIDH
l_servo_val = MIN_SERVO_PULSE_WIDH

def main():

    if len(sys.argv) < 2:
        return 0

    servo_state = int(sys.argv[2])

    while True:
        sleep(0.1)

        if 'right' == sys.argv[0]:
            global r_servo_val
            r_servo_val = r_servo_val + servo_state
            if r_servo_val < MIN_SERVO_PULSE_WIDH or r_servo_val > MAX_SERVO_PULSE_WIDH:
                r_servo_val = r_servo_val - servo_state
            else:
                pwm.set_pwm(R_SERVO_CH, 0, r_servo_val)

        if 'left' == sys.argv[0]:
            global l_servo_val
            l_servo_val = l_servo_val + servo_state
            if l_servo_val < MIN_SERVO_PULSE_WIDH or l_servo_val > MAX_SERVO_PULSE_WIDH:
                l_servo_val = l_servo_val - servo_state
            else:
                pwm.set_pwm(L_SERVO_CH, 0, l_servo_val)