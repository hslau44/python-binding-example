# Text Math Solve (Python_binding_example)

An example project using pybind11 and CMake
This program calculate math by inputing the question in literal

# Instruction


1. install pybind11, submodule is advised, which can be download by the following command: 
```
git submodule add -b stable ../../pybind/pybind11 extern/pybind11
``` 
2. build the C++ part of the project by the following command:
```
mkdir build
cd build/
cmake ..
make
```
3. Install python requirements by the command `pip install -r requirements.txt`


# Run
Run the following command:
```
python textmathsolve TEXT
```
where: 
`TEXT` is the question to be solved. 

Currently, it only support one operation, such as `1.6/0.8` and no negative value is supported. See test case in `test.py`