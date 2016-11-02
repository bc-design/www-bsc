# Motivations

------

# Project Goals and Overview

------

# Fundamental Challenges

------

# Device Design / Construction

------

# Metrology and Sensing - Electrical

------

# Metrology and Sensing - Temperature

------

# Metrology and Sensing - Chemistry

------

# Characterization - Surface Temperature

+ Get system dynamics from open loop operation
+ Generate a model that describes relationship between measurable states, input sequence

------

# Characterization - Power

------

# Characterization - Optical Intensity

------

# Actuation and Control - Implementation Overview

Desirable system features

+ real-time acquisition, analysis, actuation
+ high slew rate (fast response)
+ wide operating range
+ linearity (ideally)

------

# Actuation and Control - Electrical Subsystem

------

# Actuation and Control - Gas Handling

------

# Control Algorithms

Desirable algorithm features

+ rapid optimization
+ support for constraints
+ multivariable objective functions
+ setpoint tracking / disturbance rejection
+ support for nonlinear models

PID lacks these features, but it's a place to start

------

# Control Algorithms - PID Implementation

+ Generate tunings, operating range from system model
+ Closed-loop dynamics

------

# Ongoing Work

+ implementation of advanced control algorithms
  + QDMC
  + Nonlinear MPC
+ demonstration of improved performance with control
+ robust device design
+ expand repertoire of measurement techniques
+
