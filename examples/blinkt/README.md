# Examples from Blinkt!

The examples in this folder have been ported from Blinkt! repository:

* Blinkt! has 8 rather than 7 APA102 LEDs, so the code was quickly adapted.
* Blinkt! and Rainbow have different module name but same API... a trick
has been used to port with minimal modification the existing example:

	import rainbowhat
	
	set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit  
	set_pixel=rainbowhat.rainbow.set_pixel  
	show=rainbowhat.rainbow.show  
	set_brightness=rainbowhat.rainbow.set_brightness  
	# Add any required alias function from blinkt  
