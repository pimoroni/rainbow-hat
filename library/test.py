import rainbowhat
import time

rgb = [100,0,0]

states = {
    rainbowhat.touch.A: [100,0,0, "Reed"],
    rainbowhat.touch.B: [0,100,0, "Gren"],
    rainbowhat.touch.C: [0,0,100, "Blue"]
}

c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
b = 493

for note in [a,a,g,g,a,a,g,None,f,f,e,e,d,d,c,None,g,g,f,f,e,e,d,None,c,c,g,g,a,a,g,None,f,f,e,e,d,d,c,None]:
    rainbowhat.buzzer.note(note,0.3,0.9)

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
