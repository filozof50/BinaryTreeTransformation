import pydot;
import Tkinter as tk;
import sys;
import os;
from PIL import Image, ImageTk;

if len(sys.argv) != 2:
	print "fali parametar!";
	exit();

numberOfTxtFiles = sys.argv[1];

for i in range(1, int(numberOfTxtFiles) + 1):
	graph = pydot.Dot(graph_type='graph');

	with open("./graph" + str(i) + ".txt") as f:
	    content = f.readlines();

	children = [];
	tree = {};

	for line in content:
	    children = [int(x) for x in line.split()];
	    node = children.pop(0); 
	    tree[node] = children;
	    children = [];  

	for key, value in tree.iteritems():
	    for el in value: 
		edge = pydot.Edge(key, el);
		graph.add_edge(edge);
        
	graph.write_png("graph" + str(i) + ".png");

os.system("python display_graphs.py " + str(numberOfTxtFiles));

