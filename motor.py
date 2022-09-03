import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

dc = MotorKit(address=0x61)
st = MotorKit()
one_eighth = int(2048 / 8)


def all_motors_off():
    st.stepper1.release()
    st.stepper2.release()

    dc.motor1.throttle = None
    dc.motor2.throttle = None
    dc.motor3.throttle = None


def one_coin_stepper2():
    for i in range(one_eighth + 50):
        st.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.008)
    time.sleep(0.2)
    for i in range(50):
        st.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.008)
    st.stepper1.release()


def one_coin_stepper1():
    for i in range(one_eighth + 50):
        st.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.008)
    time.sleep(0.2)
    for i in range(50):
        st.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.008)
    st.stepper2.release()


def rotate_m1():
    dc.motor1.throttle = -0.3


def rotate_m2():
    dc.motor2.throttle = -0.3


def rotate_m3():
    dc.motor3.throttle = -0.3


def stop_m1():
    dc.motor1.throttle = 0


def stop_m2():
    dc.motor2.throttle = 0


def stop_m3():
    dc.motor3.throttle = 0
