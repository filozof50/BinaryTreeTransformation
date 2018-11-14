import pydot;
import Tkinter as tk;
import sys;
import os;
from PIL import Image, ImageTk;
from graphviz import Source

if len(sys.argv) != 2:
	print "fali parametar!";
	exit();

numberOfTxtFiles = sys.argv[1];

counter = 1;
previousTree = {};
for i in range(1, int(numberOfTxtFiles)):
	j = 0;
	graph = pydot.Dot(graph_type='graph');

	with open("../files/txt_files/graph" + str(i) + ".txt") as f:
	    content = f.readlines();
	
	children = [];
	tree = {};
	shouldDraw = True;

	for line in content:
	    children = [int(x) for x in line.split()];
	    node = children.pop(0); 
	    tree[node] = children;
	    children = [];  
        
        if tree == previousTree:
		print "hi, im on i = " + str(i)
		shouldDraw = False;
    	
	previousTree = tree;

	if shouldDraw:
		file = open("../files/dot_files/graph" + str(counter) + ".dot", "w");
		file.write("graph G{\n");

		for key, value in tree.iteritems():
			if len(value) == 2:
				file.write(str(key) + " -- " + str(value[0]) + "\n")
				file.write("center" + str(j) + ' [style=invis, width=0, label=""]\n')
				file.write(str(key) + " -- " + "center" + str(j) + " [style=invis]\n")
				file.write(str(key) + " -- " + str(value[1]) + "\n")
				file.write("{rank=same " + str(value[0]) + " -- " + "center" + str(j) + " -- " + str(value[1]) + " [style=invis] }\n")
				j = j + 1
			elif len(value) == 1:
				if value[0] > key:
					leftNode = "center" + str(j);
					j = j + 1
					file.write(leftNode + " [style = invis]\n")
					file.write(str(key) + " -- " + leftNode + " [style=invis]\n")		
					file.write("center" + str(j) + ' [style=invis, width=0, label=""]\n')
					file.write(str(key) + " -- " + "center" + str(j) + "[style=invis]\n")			
					file.write(str(key) + " -- " + str(value[0]) + "\n")
					file.write("{rank=same " + leftNode + " -- " + "center" + str(j) + " -- " + str(value[0]) + " [style=invis] }\n")
					j = j + 1
				else:
					rightNode = "center" + str(j);
					j = j + 1
					file.write(str(key) + " -- " + str(value[0]) + "\n")
					file.write("center" + str(j) + ' [style=invis, width=0, label=""]\n')
					file.write(str(key) + " -- " + "center" + str(j) + "[style=invis]\n")	
					file.write(rightNode + " [style = invis]\n")	
					file.write(str(key) + " -- " + rightNode + " [style=invis]\n")		
					file.write("{rank=same " + str(value[0]) + " -- " + "center" + str(j) + " -- " + str(rightNode) + " [style=invis] }\n")
					j = j + 1

		file.write("}")
		file.close();
		s = Source.from_file(filename="../files/dot_files/graph" + str(counter) + ".dot", format="png")
		#s.view()
		s.render("../files/png_files/graph" + str(counter))
		counter = counter + 1 

os.system("python ../python/display_graphs.py " + str(counter));

