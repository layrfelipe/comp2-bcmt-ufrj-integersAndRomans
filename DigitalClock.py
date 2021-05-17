from tkinter import *
from time import *

class digitalClock:

    # 
    # Constructor.
    #
    # @param clock a label to display the time.
    # @param secs number of seconds for time regressive counting.
    # @param time string for initializing the time. Just leave the default.
    #
    # 
    def __init__ ( self, clock, secs = 0, time='' ):
        self.clock = clock
        self.secs = secs
        self.time = time
        self.running = True

    # 
    # Updates the clock display.
    #
    def tick(self):
        self.clock.config(text=strftime('%H:%M:%S'))
        self.clock.after(1000, self.tick)

    # 
    # Starts a count down from the number of seconds set to zero.
    #
    def tickDown(self):
        #
        # The callback functions are called when buttons in application are triggered

        #
        # Callback function
        #
        # Sets timer to 30 seconds
        def setThirty():
            self.aEntry.delete(0, "end")
            self.aEntry.insert(0, "30")

        #
        # Callback function
        #
        # Increases 30 seconds on the timer
        def handle30sec():
            try:
                time = self.aEntry.get()
                if time == "Time is over":
                    self.aEntry.after(200, setThirty)
                else:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, str(int(time)+30))
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")

        #
        # Callback function
        #
        # Starts the count down in timer to 0
        def handleStart():
            try:
                current = int(self.aEntry.get())
                if current > 0 and self.running == True:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, str(current - 1))
                    self.aEntry.after(1000, handleStart)
                elif current == 0 and self.running == True:
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, "Time is over")
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")
        
        #
        # Callback function
        #
        # Pauses the count down timer
        def handlePause():
            try:
                if self.running == True:
                    self.running = False
                    current = int(self.aEntry.get())
                    self.aEntry.delete(0, "end")
                    self.aEntry.insert(0, current)
                else:
                    self.running = True
                    handleStart()
            except:
                self.aEntry.delete(0, "end")
                self.aEntry.insert(0, "0")

        # Receives TCL variable which Tkinter uses to insert in the timer
        e1Var = StringVar(self.clock.master)
        e1Var.set(str(self.secs))

        # Creating visual elements using Tkinter widgets
        # Input fields (named as Entries) and Buttons
        self.aEntry = Entry(self.clock.master, font=('times 28', 20, 'bold'), bg="red", textvar=e1Var)
        self.aEntry.pack(fill="both", side="top", expand=1)

        self.bottomFrame = Frame(self.clock.master, bg="white")

        self.startButton = Button(self.bottomFrame, text="Start", command=handleStart)
        self.startButton.pack(fill="both", side="left", expand=1)

        self.plus30Button = Button(self.bottomFrame, text="+30s", command=handle30sec)
        self.plus30Button.pack(fill="both", side="left", expand=1)

        self.pauseButton = Button(self.bottomFrame, text="Pause", command=handlePause)
        self.pauseButton.pack(fill="both", side="left", expand=1)

        self.bottomFrame.pack(fill="both", side="top", expand=1)