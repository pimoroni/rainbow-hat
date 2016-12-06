import rainbowhat
import time

rgb = [100,0,0]

#c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
b = 493
c = 523

states = [
    [100,0,0, "Reed", a],
    [0,100,0, "Gren", b],
    [0,0,100, "Blue", c]
]

#for note in [a,a,g,g,a,a,g,None,f,f,e,e,d,d,c,None,g,g,f,f,e,e,d,None,c,c,g,g,a,a,g,None,f,f,e,e,d,d,c,None]:
#    rainbowhat.buzzer.note(note,0.3,0.9)

@rainbowhat.touch.press()
def test(index):
    print("Touch:", index)
    r, g, b, text, note = states[index]
    rainbowhat.lights.rgb(r, g, b)
    rainbowhat.rainbow.set_all(r, g, b)
    rainbowhat.rainbow.show()
    rainbowhat.display.print_str(text)
    rainbowhat.display.show()
    rainbowhat.buzzer.note(note,0.30,0.8)

@rainbowhat.touch.release()
def test(index):
    print("Release:", index)

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
