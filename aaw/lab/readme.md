# AAW LAB
1. Use the example which converts Temperature in fahrenheit. Add one output: calculate speed of an oxygen molecule at that temperature in m/s. 
2. Build the docker image and create model, deploy it in AAW.

Answer should take temperature in fahrenheit as input and generate 4 outputs:
```
Temperature in K
Temperature in C
State of water 
Speed of oxygen molecule at temperature given
```
You can use this formula:
```
rms speed= squareroot(3*8.31*K/0.032)
```
K is temperature in kelvin, 0.032 is the oxygen molecule mass in kg/mol.