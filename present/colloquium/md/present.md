# Motivations

+ potential for plasma in medicine
+ device development - technology ahead of science
+ lack of prior control work

------

# Project Goals and Overview

1. Metrology and actuation
2. System characterization
   + system modeling
3. Control implementation
   + algorithm selection
   + operating range selection
   + controller implementation
4. Performance demonstration

------

# Fundamental Challenges

+ Dosage = multivariable (integral) measurements
+ Multiple timescales
  + electronic excitation (kHz-MHz) (µs-ms)
  + gas temperature (degrees per ms)
  + surface temperature (seconds)
  + chemical flux (minutes)
  + biological response (minutes-hours)
+ realtime control with constrains
+ nonlinear input-output relationships (positive feedback)
+ nonlinear dosage response

------

# Device Design / Construction

Selection of geometry:

+ surface microdischarge
+ corona discharge
+ rare gas jet

Operating regume:

+ frequency (kHz vs MHz vs GHz)
+ electrical interaction with substrate (direct/indirect)
+ gas mixture
+ dielectric geometry
+ electrical grounding configuration

This work:

+ rare-gas jet (He), kHz, direct dielectric barrier discharge
  + rare-gas: lower breakdown voltages
  + direct discharge: charged particles interact with surface
  + dielectric barrier: reduced risk of arcing

------

# Metrology and Sensing - Electrical

Oscilloscope: time-resolved V and I

+ V across device
+ I through devices
+ P is not simply I*V due to power spectral frequency
  + can be estimated by other (electrical) methods

------

# Metrology and Sensing - Temperature

Gas temperature

+ can be measured spectroscopically
  + inaccessible at benchtop resolutions
  + glass filament in flowstream

Surface temperature

+ current flow at surface... can't use thermocouple
+ non-contact thermal methods
  + IR spectrometric thermometry
+ can measure substrate and device temperatures

------

# Metrology and Sensing - Chemistry

+ optical emission spectroscopy (OES)
+ total optical intensity
+ absorption spectroscopy (UV-Vis)
+ FT-IR spectroscopy
+ indirect chemical asssays (pH, ionic strength)
+ direct chemical assays (NMR, MS, GC)
+ thin-film etching
+ biological response

------

# Characterization - Surface Temperature

+ Get system dynamics from open loop operation
+ Generate a model that describes relationship between measurable states, input sequence

Show random-input automated open loop results

Show automated pipeline for input-output mapping

![surface temperature vs voltage]()

![surface temperature vs frequency]()

![surface temperature vs flowrate]()

------

# Characterization - Power

![power vs voltage]()

![power vs frequency]()

![power vs flowrate]()

say some stuff about operating range selection

------

# Characterization - Optical Intensity

![optical intensity vs voltage]()

![optical intensity vs frequency]()

![optical intensity vs flowrate]()

Building system model (nonlinear vs. limited range linear)

------

# Actuation and Control - Implementation Overview

Diagram of measurement and control system connections

Desirable system features

+ real-time acquisition, analysis, actuation
+ high slew rate (fast response)
+ wide operating range
+ linearity (ideally)

------

# Actuation and Control - Electrical Subsystem

+ applied voltage across device
+ applied frequency

------

# Actuation and Control - Gas Handling

+ gas flowrate
+ gas composition
  + control reactive species
+ gas preheating

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
+ evaluation of inherent controllability
  + robust device design
+ expand repertoire of measurement techniques
+ demonstration of improved performance with control
  + process goal: control chemistry, etch rate
  + biological response

------

# Acknowledgements

+ Labs
+ Collaborators
+ Admins
+ Funding
+ Organizations that actually helped me

------

# Advice

------

# Fun Photos

Note: here is a hidden note
