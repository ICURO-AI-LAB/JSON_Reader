#!/usr/bin/env python2.7

import sys
import json
from PIL import Image
import time

def via_to_yolo(json_file, img_dir, save_dir):
	with open(str(json_file)) as annotation:
		# Load items in json
		data = json.load(annotation)
		for item in data:
			filename = str(data[item]["filename"])
			filepath = str(img_dir) + "/" + filename
			# Open image file correspoding to this annotation
			im = Image.open(filepath)
			# Get width and height of image
			width, height = im.size
			# Convert to float for yolo
			im_width = float(width)
			im_height = float(height)

			# Unique names for files
			save_name = str(int(time.time() * 1000000))
			img_name  = save_name + ".jpg"
			txt_name  = save_name + ".txt"

			# Create txt file with same name as image
			# txt_file = str(filename[:-4]) + ".txt"

			txt_file = str(save_dir) + "/" + txt_name 
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
				for cat in region["region_attributes"]:
					item_cat   = region["region_attributes"][str(cat)]
				yolo_x = (top_left_x + (bb_width/2) )/im_width
				yolo_y = (top_left_y + (bb_height/2))/im_height
				yolo_w = bb_width/im_width
				yolo_h = bb_height/im_height

				# Write line to file
				writeline = str(item_cat) + " " + str(yolo_x) + " " + str(yolo_y) + " " + str(yolo_w) + " " + str(yolo_h) + "\n"
				f.write(writeline)
			f.close()

			# Save image in the same path as txt
			img_path = str(save_dir) + "/" + img_name
			im.save(img_path)
			time.sleep(0.00001) 

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print "Usage : ./read_json_annotation.py <json file> <image directory> <save directory>"
	else:
		print "Converting json file....."
		via_to_yolo(sys.argv[1], sys.argv[2], sys.argv[3])
		print "Done!"
