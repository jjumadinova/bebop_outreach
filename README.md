# Bebop Drone Demo

This program uses Bebop 2 drones and a Python interface to program the drones.

### Drone Safety

Drones can be dangerous and cause injury! Additionally, Bebop drones are notoriously hard to catch. You must obey the following safety rules:

- No flying inside the buildings unless it is in the gym.
- No flying over or near anyone.
- Must fly in the flying zone.
- Use hull protection for Bebop 1 or 3D print propeller guards for Bebop 2 (the 3D printing files are provided in the lab repository).
- Use safety glasses if you are operating in the close proximity of the flying drone, especially if flying it without hull or propeller protection.
- If you are not wearing glasses, do NOT put your eyes near the propellers.
- If you decide to test your drone outside, make sure to do so outside of campus, remember flying drones on Allegheny campus is not allowed! Also, be sure to obey the [FAA flying restrictions](https://www.faa.gov/uas/recreational_fliers/where_can_i_fly/).
- Do NOT connect to drone's wifi of another team -- this is dangerous.

## Learning

To learn about `pyparrot` interface please read the [`pyparrot` documentation](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). To learn more about autonomous drones please read the article titled [The Future of Flight: AI in the Cockpit](https://www.wsj.com/articles/the-future-of-flight-ai-in-the-cockpit-1542018600).

## Instructions

### 1\. Set Up

- Review the [Tutorial 1 (Set Up)](https://www.parrot.com/us/support/products/parrot-bebop-2/preparing-your-drone). Download the app called "FreeFlight Pro", upgrade the firmware if needed and perform the calibrations (roll, pitch, yaw). Now, without flying it, ensure that you are able to connect your drone (wifi works) and that you can see the camera's input on the app.

Also, please remember that you can't control your drone from the Allegheny's wifi. You MUST be connected to YOUR drone's wifi.

### `pyparrot` Notes

To get started with `pyparrot`, you should first try to run `demo.py` program first, uncommenting each movement one by one.

Also, when starting your program in Python3 using `pyparrot`, please remember to specify the correct Bebop type. If you are using smaller (blue or red) Bebop drones (these are Bebop 1s), then you have to specify that when creating a Bebop object as `bebop = Bebop(drone_type="Bebop")` since the default Bebop type is Bebop 2 (white Bebop drones). Also, if you are using hull protectors in Bebop 1 you should use the `set_hull_protection` method, where the hull protector parameters is set to 1 for a hull protection being in place on Bebop 1\. You are free to use and extend any of the programs in the `examples/` directory of the `pyparrot` repository.

Also, if you have trouble connecting the drone to wifi, you may need to revert to an earlier `zeroconf` version, for example by running `pip3 install zeroconf==0.20.0`.

You can use `move_relative` method to fly the drone a relative number of meters as specified in [`bebop` commands doc](https://pyparrot.readthedocs.io/en/latest/bebopcommands.html). If you would like to estimate the distance and use `fly_direct` method, you can use the distance formula.
