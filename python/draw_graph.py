import pydot;
import Tkinter as tk;
#from PIL import Image, ImageTk;
from PIL import Image, ImageTk;

def showPIL(pilImage, window_width, window_height, name):
	root = tk.Tk();  
	root.title(name);  
	screenWidth = root.winfo_screenwidth();
	screenHeight = root.winfo_screenheight();

	x = screenWidth/2 - window_width/2;
	y = screenHeight/2 - window_height/2;

	root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y));

	im=pilImage;
	photo=ImageTk.PhotoImage(im);  
	cv = tk.Canvas();
	cv.pack(side='bottom', fill='both', expand='yes'); 
	cv.create_image(window_width/2, window_height/2, image=photo, anchor='center');  

	root.after(3000, lambda: root.destroy()) 

	root.mainloop();



graph = pydot.Dot(graph_type='graph');
graph2 = pydot.Dot(graph_type='graph');
graph3 = pydot.Dot(graph_type='graph');
graph4 = pydot.Dot(graph_type='graph');

with open("./test_pre.txt") as f:
    content1 = f.readlines();

with open("./test_posle.txt") as f:
    content2 = f.readlines();

with open("./test_final.txt") as f:
    content3 = f.readlines();

with open("./test_pre_drugo.txt") as f:
    content4 = f.readlines();

children = [];
tree_before = {};
tree_after = {};
tree_final = {};
tree_second = {};

for line in content1:
    children = [int(x) for x in line.split()];
    node = children.pop(0); 
    tree_before[node] = children;
    children = [];  

for line in content2:
    children = [int(x) for x in line.split()];	
    node = children.pop(0);	
    tree_after[node] = children;
    children = [];

for line in content3:
    children = [int(x) for x in line.split()];	
    node = children.pop(0);	
    tree_final[node] = children;
    children = [];

for line in content4:
    children = [int(x) for x in line.split()];	
    node = children.pop(0);	
    tree_second[node] = children;
    children = [];

for key, value in tree_before.iteritems():
    for el in value: 
        edge = pydot.Edge(key, el);
        graph.add_edge(edge);
        
graph.write_png("test.png");

im = Image.open("test.png");
basewidth = 500;
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth, hsize), Image.ANTIALIAS);
im.save("test.png");

image = Image.open("test.png");
showPIL(image, basewidth, hsize, "T1");


for key, value in tree_after.iteritems():
    print key, value
    for el in value: 
        edge = pydot.Edge(key, el);
        graph2.add_edge(edge);
        
graph2.write_png("test2.png");

im = Image.open("test2.png");
basewidth = 80;
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth, hsize), Image.ANTIALIAS);
im.save("test2.png");

image = Image.open("test2.png");
showPIL(image, basewidth, hsize, "List");


for key, value in tree_final.iteritems():
    print key, value
    for el in value: 
        edge = pydot.Edge(key, el);
        graph3.add_edge(edge);
        
graph3.write_png("test3.png");

im = Image.open("test3.png");
basewidth = 500;
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth, hsize), Image.ANTIALIAS);
im.save("test3.png");

image = Image.open("test3.png");
showPIL(image, basewidth, hsize, "T2");


for key, value in tree_second.iteritems():
    print key, value
    for el in value: 
        edge = pydot.Edge(key, el);
        graph4.add_edge(edge);
        
graph4.write_png("test4.png");

im = Image.open("test4.png");
basewidth = 500;
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth, hsize), Image.ANTIALIAS);
im.save("test4.png");

image = Image.open("test4.png");
showPIL(image, basewidth, hsize, "Original T2");

