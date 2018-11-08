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
            self.image = self.images.pop(0);
            self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
            self.canvas.after(3000, self.draw_new);

        def draw_new(self):
            if len(self.images) > 0:
                self.image = self.images.pop(0);
                self.canvas.delete("deleteMe");
                self.canvas.create_image((self.x, self.y), tags = "deleteMe", image = self.image, anchor='center');
                self.canvas.after(3000, self.draw_new);

root = Tk();
root.title("Balls");
root.geometry("{0}x{1}+0+0".format(7*root.winfo_screenwidth()/8, 4*root.winfo_screenheight()/5));
root.update();
root.resizable(False, False);
canvas = Canvas(root, width = root.winfo_width(), height = root.winfo_height());
canvas.pack();
canvas.config(background = "white");


images = [];

for i in range(1, int(numberOfTxtFiles) + 1):
	image = Image.open("graph" + str(i) + ".png");
	if i == 1 or i == 2:
		basewidth = root.winfo_width()/5;
		wpercent = (basewidth/float(image.size[0]));
		hsize = int((float(image.size[1])*float(wpercent)));
		image = image.resize((basewidth, hsize), Image.ANTIALIAS);
	else:
		baseheight = 11*root.winfo_height()/12;
		hpercent = (baseheight/float(image.size[1]));
		wsize = int((float(image.size[0])*float(hpercent)));
		image = image.resize((wsize, baseheight), Image.ANTIALIAS);

	image = ImageTk.PhotoImage(image);
	
	if i != 2:
		images.append(image);
	else:
		lastImage = image;

firstImage = images[0];
canvas.create_image((0, 0), image = firstImage, anchor='nw');
canvas.create_image((root.winfo_width(), 0), image = lastImage, anchor='ne');

drawer = DrawImage(canvas, images, root.winfo_width()/2, root.winfo_height()/2);

root.mainloop();
