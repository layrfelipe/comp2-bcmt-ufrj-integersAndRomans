from tkinter import *
from DigitalClock import *
from myThread import *

# Toplevel widget of application
root = Tk()

# Clock label widget
aLabel = Label(root, font=('times 28', 20, 'bold'), bg='green')
aLabel.pack(fill="both", side="top", expand=1)

# Timer constructor being called
d = digitalClock(clock=aLabel)

# Separated threads to run both services on the same application (Clock and count down timer)
#
# Digital Clock 
t = makeThread(d.tick)
t.start()
# Count down timer
t2 = makeThread(d.tickDown)
t2.start()

mainloop()