# Examples from Blinkt!

The examples in this folder have been ported from Blinkt! repository.

Here is why it is easy to port those example:
* Blinkt! has 8 rather than 7 APA102 LEDs but Blinkt! but most example use blinkt.NUM_PIXELS.
* Blinkt! and Rainbow have different module name but same API so one can fake to use one as the other.

This is the trick used in the code:
```python
#import blinkt
from rainbowhat import rainbow as blinkt
```

Some example have not been ported and could benefit from the same treatment:
* 1d_tetris.py
* binary_clock_meld.py
* binary_clock.py
* blinkt_thermo.py
* cheerlights.py
* cpu_temp.py
* extra_examples
* mem_load.py
* mqtt.py
* resistor_clock.py
* twitter_monitor.py

If you encounter example that do not use the simple "import blinkt" but the more complex "from blinkt import xxx" then you can use an alias trick for the function you want to use, like this:

```python
#from blinkt import set_clear_on_exit, set_pixel, show, set_brightness
import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit  
set_pixel=rainbowhat.rainbow.set_pixel  
show=rainbowhat.rainbow.show  
set_brightness=rainbowhat.rainbow.set_brightness  
# Add any required alias function from blinkt  
```
