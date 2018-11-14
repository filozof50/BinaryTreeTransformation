import sys
import pydot;
from Tkinter import *;
from PIL import Image, ImageTk;

if len(sys.argv) != 2:
	print "fali parametar!";
	exit();

numberOfTxtFiles = sys.argv[1];

class DrawImage:
        def __init__(self, canvas, images, x, y):
	    self.x = x;
	    self.y = y;
            self.images = images;
            self.canvas = canvas;
	    self.counter = 0;
            #self.image = self.images.pop(0);
	    self.image = self.images[self.counter];
            self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
            
        def draw_new(self):
	    if (self.counter + 1 <= len(self.images) - 1):
	    	self.counter += 1
            if self.counter < len(self.images):
                #self.image = self.images.pop(0);
		self.image = self.images[self.counter];
                self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');

        def draw_previous(self):
	    if (self.counter - 1 >= 0):
	    	self.counter -= 1
	    if self.counter >= 0:
		self.image = self.images[self.counter];
                self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                
        def draw_new_timer(self):
	    if (self.counter + 1 <= len(self.images) - 1):
	    	self.counter += 1
	    if self.counter < len(self.images):
                self.image = self.images[self.counter];
		self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                self.canvas.after(5000, self.draw_new);

root = Tk();
root.title("Balls");
root.geometry("{0}x{1}+0+0".format(7*root.winfo_screenwidth()/8, 4*root.winfo_screenheight()/5));
root.update();
root.resizable(False, False);
canvas = Canvas(root, width = root.winfo_width(), height = root.winfo_height());
canvas.pack();
canvas.config(background = "white");


images = [];
firstLastImage = [];

for i in range(1, int(numberOfTxtFiles)):
	image = Image.open("../files/png_files/graph" + str(i) + ".png");
	if i == 1 or i == 2:
		basewidth = root.winfo_width()/5;
		wpercent = (basewidth/float(image.size[0]));
		hsize = int((float(image.size[1])*float(wpercent)));
		img = image.resize((basewidth, hsize), Image.ANTIALIAS);
		img = ImageTk.PhotoImage(img);
		firstLastImage.append(img);
	
	baseheight = 11*root.winfo_height()/12;
	hpercent = (baseheight/float(image.size[1]));
	wsize = int((float(image.size[0])*float(hpercent)));
	image = image.resize((wsize, baseheight), Image.ANTIALIAS);

	image = ImageTk.PhotoImage(image);
	
	if i != 2:
		images.append(image);

canvas.create_image((0, 0), image = firstLastImage[0], anchor='nw');
canvas.create_image((root.winfo_width(), 0), image = firstLastImage[1], anchor='ne');

drawer = DrawImage(canvas, images, root.winfo_width()/2, root.winfo_height()/2);

button0 = Button(root, text = "Previous", command = drawer.draw_previous, anchor = W)
button0.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
button0_window = canvas.create_window(0, root.winfo_height(), anchor=SW, window=button0)

button1 = Button(root, text = "Next", command = drawer.draw_new, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
button1_window = canvas.create_window(120, root.winfo_height(), anchor=SW, window=button1)

button2 = Button(root, text = "Loop", command = drawer.draw_new_timer, anchor = W)
button2.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
button2_window = canvas.create_window(240, root.winfo_height(), anchor=SW, window=button2)

button3 = Button(root, text = "Exit", command = root.quit, anchor = W)
button3.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
button3_window = canvas.create_window(360, root.winfo_height(), anchor=SW, window=button3)

root.mainloop();
