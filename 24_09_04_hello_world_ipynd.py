# -*- coding: utf-8 -*-
"""24-09-04-hello-world.ipynd

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14dMhIEtOvVLAElKYoMFLPyFfuIScnUYQ
"""

print("Hello World!!")

print("Hello Python")

print("안녕")

"""1 import pylab as py
2
3 x_deg= py.arange(-180, 180+1)
4 x_rad=py.deg2rad(x_deg)
5 y=py.sin(x_rad)
6
7 py.plot(x_deg, y)
8
9 py.xlabel('x(deg)')
10 py.ylabel('sin(x)')
11 py.grid(True)
12
"""

import pylab as py
x_deg= py.arange(-180, 180+1,)
x_rad=py.deg2rad(x_deg)
y=py.sin(x_rad)
py.plot(x_deg, y)
py.xlabel('x(deg)')
py.ylabel('sin(x)')
py.grid(True)

