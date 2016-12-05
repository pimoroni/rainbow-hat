import rainbowhat
import time

rgb = [100,0,0]

states = {
    rainbowhat.touch.A: [100,0,0, "Reed"],
    rainbowhat.touch.B: [0,100,0, "Gren"],
    rainbowhat.touch.C: [0,0,100, "Blue"]
}

@rainbowhat.touch.on_touch()
def test(pin):
    print("Touch:", pin)
    r, g, b, text = states[pin]
    rainbowhat.rainbow.set_all(r, g, b)
    rainbowhat.rainbow.show()
    rainbowhat.lights.rgb(r, g, b)
    rainbowhat.display.print_str(text)
    rainbowhat.display.show()

@rainbowhat.touch.on_release()
def test(pin):
    print("Release:", pin)

while True:
    time.sleep(1)
    continue

    r, g, b = rgb
    print(r, g, b)
    rainbowhat.apa102.set_all(r, g, b)
    rainbowhat.apa102.show()
    rainbowhat.lights.rgb(r, g, b)
    rgb.insert(0,rgb.pop())
    time.sleep(0.5)
