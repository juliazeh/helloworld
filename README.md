# helloworld
This is the helloworld package for assignment 2.3

##Installation
Clone the repo and use pip to install it.
```
git clone https://github.com/juliazeh/helloworld.git
cd helloworld/
pip install .
```

##CLI Usage
To use the executable helloworld command line program:
```
$ helloworld -h
usage: helloworld [-h] [-m MILITARYTIME] [--age AGE]

optional arguments:
  -h, --help            show this help message and exit
  -m MILITARYTIME, --militarytime MILITARYTIME
                        optional time to determine greeting
  --age AGE             convert and return inputted age to age in dog years
```

##API Usage
To use the hellowrold Python API:
```
import helloworld
helloworld.helloworld(militarytime=14,age=21)
```
```
good afternoon
you are 147 dog years old
```