from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.fly_left(100)
tello.turn_right(90)
tello.fly_forward(100)

tello.land()
