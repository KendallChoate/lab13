#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
enemy1 = drawpad.create_oval(290,480,310,500, fill="blue")
enemy2 = drawpad.create_oval(490,280,510,300, fill="blue")
enemy3 = drawpad.create_oval(190,80,210,100, fill="blue")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    # Up button
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
       	    # Left button
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="Left", background= "yellow")
       	    self.left.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
       	    # Right button
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="Right", background= "Red")
       	    self.right.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
       	    # Down button
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "Cyan")
       	    self.down.grid(row=0,column=3)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    global enemy1
	    #drawpad.move(enemy1, -10, 0)
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
	
	# Animation for up, left, right, and down button	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)	
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)

app = MyApp(root)
root.mainloop()