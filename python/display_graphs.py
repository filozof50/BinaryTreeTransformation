import sys
import pydot;
from Tkinter import *;
from PIL import Image, ImageTk;

def createButton(root, canvas, text, drawer, location):
	if text == "Previous":
		button = Button(root, text = text, command = drawer.draw_previous, anchor = W)
	elif text == "Next":
		button = Button(root, text = text, command = drawer.draw_new, anchor = W)
	elif text == "Loop":
		button = Button(root, text = text, command = drawer.draw_new_timer, anchor = W)
	else:
		button = Button(root, text = text, command = root.quit, anchor = W)
	button.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
	button_window = canvas.create_window(location, root.winfo_height(), anchor=SW, window=button)

def setImageSize(percent, windowWidth, windowHeight, imageWidth, imageHeight):
	baseheight = (percent * windowHeight)/12;
	hpercent = (baseheight/float(imageHeight));
	wsize = int((float(imageWidth)*float(hpercent)));
	if wsize > 3*windowWidth/5:
		return setImageSize(percent - 1, windowWidth, windowHeight, imageWidth, imageHeight);
	else:
		return baseheight, wsize;


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
	    self.image = self.images[self.counter];
            self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
	    print "drew image at i = " , self.counter
            
        def draw_new(self):
	    if (self.counter + 1 <= len(self.images) - 1):
	    	self.counter += 1
            if self.counter < len(self.images):
		self.image = self.images[self.counter];
                self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                print "drew image at i = " , self.counter

        def draw_previous(self):
	    if (self.counter - 1 >= 0):
	    	self.counter -= 1
	    if self.counter >= 0:
		self.image = self.images[self.counter];
                self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                print "drew image at i = " , self.counter

        def draw_new_timer(self):
	    if (self.counter + 1 <= len(self.images) - 1):
	    	self.counter += 1
	    if self.counter < len(self.images):
                self.image = self.images[self.counter];
		self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                print "drew image at i = " , self.counter
                self.canvas.after(5000, self.draw_new_timer);

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
	
	initialPercent = 11
	baseheight, wsize = setImageSize(initialPercent, root.winfo_width(), root.winfo_height(), image.size[0], image.size[1]);
	
	image = image.resize((wsize, baseheight), Image.ANTIALIAS);
	image = ImageTk.PhotoImage(image);
	
	if i != 2:
		images.append(image);

canvas.create_image((0, 0), image = firstLastImage[0], anchor='nw');
canvas.create_image((root.winfo_width(), 0), image = firstLastImage[1], anchor='ne');

drawer = DrawImage(canvas, images, root.winfo_width()/2, root.winfo_height()/2);

createButton(root, canvas, "Previous", drawer, 0);
createButton(root, canvas, "Next", drawer, 120);
createButton(root, canvas, "Loop", drawer, 240);
createButton(root, canvas, "Exit", drawer, 360);

root.mainloop();
