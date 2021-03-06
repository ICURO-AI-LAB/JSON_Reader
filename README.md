# JSON_Reader
Read bounding box data from json created by [VIA](http://www.robots.ox.ac.uk/~vgg/software/via/) annotation tool and convert it to [Darknet YOLO](https://pjreddie.com/darknet/yolo/) format

## Usage

* Run as python script:
```bash
python read_json_annotation.py <json file> <image directory> <save directory>
```
**OR**
<br/>
* Create executable using:
```bash
chmod +x read_json_annotation.py
```
and run executable:
```bash
./read_json_annotation.py <json file> <image directory> <save directory>
```

### Arguments
* **json file**       : .json file with bounding box annotation data
* **image directory** : directory containing all images referenced in the .json file
* **save directory**  : directory in which renamed images and YOLO annotation files in '.txt' format will be saved
