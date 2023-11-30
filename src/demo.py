"""
Land
"""

from pyparrot.Bebop import Bebop

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

if (success):
    bebop.safe_takeoff(5)

    bebop.smart_sleep(2)
    
    bebop.safe_land(5)

    # set safe indoor parameters
    bebop.set_max_tilt(5)
    bebop.set_max_vertical_speed(1)

    # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
    #bebop.set_hull_protection(1)

    #print("Flying direct: Slow move for indoors")
    #bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)

    # set safe indoor parameters
    #bebop.set_max_tilt(5)
    #bebop.set_max_vertical_speed(1)

    #print("Flying direct: Slow move for indoors")
    #bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)

    #print("flip left")
    #print("flying state is %s" % bebop.sensors.flying_state)
    #success = bebop.flip(direction="left")
    #print("mambo flip result %s" % success)
    #bebop.smart_sleep(5)

    #print("flip right")
    #print("flying state is %s" % bebop.sensors.flying_state)
    #success = bebop.flip(direction="right")
    #print("right flip result %s" % success)
    #bebop.smart_sleep(5)

    #print("flip front")
    #print("flying state is %s" % bebop.sensors.flying_state)
    #success = bebop.flip(direction="front")
    #print("left flip result %s" % success)
    #bebop.smart_sleep(5)

    #print("flip back")
    #print("flying state is %s" % bebop.sensors.flying_state)
    #success = bebop.flip(direction="back")
    #print("back flip result %s" % success)
    #bebop.smart_sleep(5)

    print("DONE - disconnecting")
    bebop.disconnect()
