# csci4220u-project
This is a computer vision system made to detect road signs.

## Running
This project uses ultralytics for the machine learning and related systems. As
long as a recent version of these libraries are on your system it should work
just fine. I used pipenv for dependency management so that will work as well.

after all of the dependencies are installed simply pass the images that the
model should be tested on.

native python (make sure that the dependency's are installed)
```sh
python3 detect.py [imgs]
```
with pipenv
```sh
pipenv run python3 detect.py [imgs]
```
