#!/usr/bin/env python2.7

import json
from PIL import Image

with open('via_region_data.json') as annotation:
	# Load items in json
	data = json.load(annotation)
	for item in data:
		filename = data[item]["filename"]
		# Open image file correspoding to this annotation
		im = Image.open(filename)
		# Get width and height of image
		width, height = im.size
		# Convert to float for yolo
		im_width = float(width)
		im_height = float(height)
		# Create txt file with same name as image
		txt_file = str(filename[:-4]) + ".txt"
		f = open(txt_file, "w+")
		# Loop through all regions in the image
		for region in data[item]["regions"]:
			# Check if region is rectangle
			if region["shape_attributes"]["name"] != "rect":
				print "In " + str(filename) + ", region is not rect\n"
				break

			# Read data from json in float
			top_left_x = float(region["shape_attributes"]["x"])
			top_left_y = float(region["shape_attributes"]["y"])
			bb_width   = float(region["shape_attributes"]["width"])
			bb_height  = float(region["shape_attributes"]["height"])
			
			# Convert to yolo format
			item_cat   = region["region_attributes"]["category"]
			yolo_x = (top_left_x + (bb_width/2) )/im_width
			yolo_y = (top_left_y + (bb_height/2))/im_height
			yolo_w = bb_width/im_width
			yolo_h = bb_height/im_height

			# Write line to file
			writeline = str(item_cat) + " " + str(yolo_x) + " " + str(yolo_y) + " " + str(yolo_w) + " " + str(yolo_h) + "\n"
			f.write(writeline)

		f.close()



