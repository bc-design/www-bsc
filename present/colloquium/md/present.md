# Realtime automation and control of atmospheric plasma devices

Brandon Curtis

2016-11-09

![plasma photos]()

------
<!-- .slide: style="text-align: left;" -->

## Motivations

+ potential for plasma in medicine
+ device development - technology ahead of science
+ lack of prior control work

------
<!-- .slide: style="text-align: left;"> -->

## Project Goals and Overview

1. Metrology and actuation
2. System characterization
   + system modeling
3. Control implementation
   + algorithm selection
   + operating range selection
   + controller implementation
4. Performance demonstration

------
<!-- .slide: style="text-align: left;"> -->

## Fundamental Challenges

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
<!-- .slide: style="text-align: left;"> -->

## Device Design / Construction

Geometry selection:

+ surface microdischarge, corona discharge, rare gas jet

Operating regime:

+ frequency (kHz vs MHz vs GHz)
+ interaction with substrate (direct/indirect)
+ gas mixture
+ dielectric geometry, grounding configuration

This work:

+ rare-gas jet (He), kHz, direct dielectric barrier discharge
  + rare-gas: lower breakdown voltages
  + direct discharge: charged particles interact with surface
  + dielectric barrier: reduced risk of arcing

------
<!-- .slide: style="text-align: left;"> -->

## Metrology and Sensing - Electrical

Oscilloscope: time-resolved V and I

+ V across device
+ I through devices
+ P is not simply I*V due to power spectral frequency
  + can be estimated by other (electrical) methods

------
<!-- .slide: style="text-align: left;"> -->

## Metrology and Sensing - Temperature

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
<!-- .slide: style="text-align: left;"> -->

## Metrology and Sensing - Chemistry

+ optical emission spectroscopy (OES)
+ total optical intensity
+ absorption spectroscopy (UV-Vis)
+ FT-IR spectroscopy
+ indirect chemical asssays (pH, ionic strength)
+ direct chemical assays (NMR, MS, GC)
+ thin-film etching
+ biological response

------
<!-- .slide: style="text-align: left;"> -->

## Characterization - Surface Temperature

+ Get system dynamics from open loop operation
+ Generate a model that describes relationship between measurable states, input sequence

Show random-input automated open loop results

Show automated pipeline for input-output mapping

![surface temperature vs voltage]()

![surface temperature vs frequency]()

![surface temperature vs flowrate]()

------
<!-- .slide: style="text-align: left;"> -->

## Characterization - Power

![power vs voltage]()

![power vs frequency]()

![power vs flowrate]()

Discuss operating range selection

------
<!-- .slide: style="text-align: left;"> -->

## Characterization - Optical Intensity

![optical intensity vs voltage]()

![optical intensity vs frequency]()

![optical intensity vs flowrate]()

Building system model (nonlinear vs. linear w/linear range)

------
<!-- .slide: style="text-align: left;"> -->

## Actuation and Control - Implementation Overview

![Diagram of measurement and control system connections]()

Desirable system features

+ real-time acquisition, analysis, actuation
+ high slew rate (fast response)
+ wide operating range
+ linearity (ideally)

------
<!-- .slide: style="text-align: left;"> -->

## Actuation and Control - Electrical Subsystem

+ applied voltage across device
+ applied frequency

![Diagram of function generator controller and amplifier]()

------
<!-- .slide: style="text-align: left;"> -->

## Actuation and Control - Gas Handling

+ gas flowrate
+ gas composition
  + control reactive species
+ gas preheating

------
<!-- .slide: style="text-align: left;"> -->

## Control Algorithms

Desirable algorithm features

+ rapid optimization
+ support for constraints
+ multivariable objective functions
+ setpoint tracking / disturbance rejection
+ support for nonlinear models

PID lacks most of these features, but it's a place to start

------
<!-- .slide: style="text-align: left;"> -->

## Control Algorithms - PID Implementation

+ Generate tunings, operating range from system model
+ Closed-loop dynamics

------
<!-- .slide: style="text-align: left;"> -->

## Ongoing Work

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
<!-- .slide: style="text-align: left; position: absolute; top: 0; left: 0;" -->

## Acknowledgements

People

+ Professors Graves, Clark, Mesbah
+ Professor Zdenko
+ Carly, Don
+ Undergrads: Connor (2013), Sunil (2014), Nico (2015)
+ Carlet Altamirano

![graveslab photo](img/graveslab-2016.jpg)

![clarklab photo](img/clarklab.jpg)

![nsf logo](img/nsf.png)

![doe logo](img/doe.png)

![lam logo](img/lam.png)

![BIDS](img/bids.png)

Open Source Projects

+ Linux
+ Python
+ Arduino


------
<!-- .slide: style="text-align: left;"> -->

## Fun Photos

Lots of pictures

Note: here is a hidden note
