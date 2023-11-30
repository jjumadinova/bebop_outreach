# Bebop Drone Demo

This program uses Bebop 2 drones and a Python interface to program the drones.

### Drone Safety

Drones can be dangerous and cause injury! Additionally, Bebop drones are notoriously hard to catch. You must obey the following safety rules:

- No flying inside the buildings unless it is in the gym.
- No flying over or near anyone.
- Must fly in the flying zone.
- Use safety glasses if you are operating in the close proximity of the flying drone, especially if flying it without hull or propeller protection.
- If you are not wearing glasses, do NOT put your eyes near the propellers.
- Do NOT connect to drone's wifi of another team -- this is dangerous.

## Learning

To learn about `pyparrot` interface please read the [`pyparrot` documentation](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). 

## Instructions

### 1\. Connect

- Push the button on the drone's battery to turn it on.
- Connect to your drone's WiFi. The number is written on the drone.

### 2. Fly

To get started, you should first try to run `demo.py` program first. The initial program has the drone take off, hover for a bit, and then land. You can uncomment other movements (flips) one by one and try it out.

Also, when starting your program in Python3 using `pyparrot`, please remember to specify the correct Bebop type. If you are using smaller (blue or red) Bebop drones (these are Bebop 1s), then you have to specify that when creating a Bebop object as `bebop = Bebop(drone_type="Bebop")` since the default Bebop type is Bebop 2 (white Bebop drones). 

You can use `move_relative` method to fly the drone a relative number of meters as specified in [`bebop` commands doc](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). If you would like to estimate the distance and use `fly_direct` method, you can use the distance formula.

### Calibration

If drone's movements are off, you may need to calibrate it. Download the app called "FreeFlight Pro" and perform the calibrations (roll, pitch, yaw). Now, without flying it, ensure that you are able to connect your drone (wifi works) and that you can see the camera's input on the app.



