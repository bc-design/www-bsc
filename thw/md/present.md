# The Hacker Within

## Physical Computing

##### or: how to fool people into learning more than they intended

Brandon Curtis - [Follow Along](https://www.brandoncurtis.com/thw)

[Presentation source and random files](https://www.github.com/brandoncurtis/thw-physicalcomputing)

------

## or: mostly a collection of asides

WARNING: not a computer scientist.

![lots of salt](img/salt.jpg "Season To Taste")

---

## Who Am I?

Brandon Curtis

+ a very sleep-deprived chemical engineering grad student
+ supposed to be 'finished up in the lab' in December
+ passionate about open source software
+ interested in exploring low-cost open hardware/software in education

---

### Destined for depravity

![hs](img/bc-hs.png)

---

### Allergic to adult supervision

![rockets](img/bc-rocket.png)

---

### Recovering Biologist

![rhodo](img/bc-rhodo.png)

---

### Recovering SYNTHETIC Biologist

![zfp](img/bc-zfp.png)

---

### Advanced Control for Plasma Processing

<iframe width="560" height="315" src="https://www.youtube.com/embed/7F2OqmqJBCw" frameborder="0" allowfullscreen></iframe>

---

### ...

<iframe width="560" height="315" src="https://www.youtube.com/embed/rHfVr7ohois" frameborder="0" allowfullscreen></iframe>

------

## Brought to you by...

This presentation is written in `reveal.js`

Assembled and tested in [Atom](https://atom.io/)

![atom text editor](img/atom.png)

------

## Challenge #1 - Get Code In

+ Install [Arduino IDE](https://www.arduino.cc/en/Main/Software) <!-- .element: class="fragment" data-fragment-index="1" -->
+ OR... install a command-line compile-and-upload tool <!-- .element: class="fragment" data-fragment-index="2" -->
+ Atom users: [arduino-upload package](https://atom.io/packages/arduino-upload) <!-- .element: class="fragment" data-fragment-index="3" -->

---

## What Code?

+ The Arduino IDE comes with lots of example code
+ I've provided two kinds of analog sensors
  + [LM35DZ temperature sensor](http://www.ti.com/lit/ds/symlink/lm35.pdf)
  + [Photoresistor](https://en.wikipedia.org/wiki/Photoresistor)

------

## Challenge #2 - Get Data Out

+ Must print the data over the USB-serial connection to a computer
+ Arduino IDE has a built-in 'serial monitor'
+ Unix-y folks: `cat /dev/ttyACM0`
+ Can set [udev rules](https://www.brandoncurtis.com/files/arduino/50-arduino.rules) to e.g. always use /dev/arduino

------
