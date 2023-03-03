# The Vision System for FRC2023
## The most basic information for the vision system this year
For the vision system this year, we chosed to use python and opencv. We are running all the code in **Raspberry Pi 4B** and connect it to Robrio by Eternet.
```python
import cv2
import numpy
#These are the two most important package we are using in the code
```
## The Mirror we are using (For Raspberry Pi)
We are using the mirror from Thsinghau university

<https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/> 

(sorry they are in Chinese)
```
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
``` 

3/2/2023
Fix the bugs on Raspberry Pi
