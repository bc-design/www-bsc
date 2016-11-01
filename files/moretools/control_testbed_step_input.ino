/*
  Control Testbed v4
  
  Implements a PID controller on the (temperature, current, input voltage)
  of an NPN transistor by varying the (duty cycle of a 0-5V 440Hz PWM
  that provides the base voltage, across a 1kohm resistor, to the transistor)
  
  Can choose between
   - MODE_CONTROL (PID control mode)
   - MODE_OPENLOOP (input-setting mode)
   
  Can choose between different controller inputs:
   - outTemp, the temperature measured on the transistor
   - outI, the current measured at the transistor emitter
   - inV, the low-pass filtered transistor base voltage
  
*/
 
#include <PID_v1.h>

// PREPROCESSOR DIRECTIVES
#define MODE_RANDOM false
#define MODE_CONTROL false
#define MODE_OPENLOOP true
// choose between the measured variables listed below
#define CTRL_VAR processTemp

// EXPERIMENT STUFF
//mySet[] = {500,525,550,575,600,625,650,675,700};
long stepDuration = 1200000; //milliseconds; 180000 = 3min; 600000 = 10min
long lastStep = 0;
long printDuration = 1000;  // milliseconds between prints
long lastPrint = 0;
long now = 0;

// PID STUFF
// Define Variables we'll be connecting to
double ctrlSetpoint, ctrlInput, ctrlOutput;
double Kp = 0.5;                   // gain for proportional control
double Ki = 0.1;                   // gain for integral control
double Kd = 0.00;                  // gain for derivative control

// Specify the links and initial tuning parameters
PID myPID(&ctrlInput, &ctrlOutput, &ctrlSetpoint, Kp, Ki, Kd, DIRECT); // DIRECT or REVERSE linkage

// These constants won't change.  They're used to give names
// to the pins used:
const int pinOutTemp = A1;    // Analog input pin attached to -- thermistor voltage divider
const int pinOutTempAmb = A0; // Analog input pin attached to -- thermistor voltage divider
const int pinInV = A3;        // Analog input pin attached to -- V_{B} with series resistor
const int pinOutI = A2;       // Analog input pin attached to -- current resistor
const int pinCtrlV = 3;       // Analog output pin attached to -- PWM output

/// variables to store the measured and calculated values
int ad_ambtemp;
int ad_outtemp;
int ad_outi;
int ad_inv;
int ctrlV;

float ambTemp;
float processTemp;
float processV;
float processI;

int userInput;

// variables to set and constrain the PID outputs
// TODO define these based on the selected CTRL_VAR
// TODO const int, versus preprocessor directives?
const int ctrlSetpoint0 = 50;
const int ctrlSetpointMin = 30;
const int ctrlSetpointMax = 50;
const int ctrlSetpointMid = (ctrlSetpointMin + ctrlSetpointMax) / 2;

const int ctrlOutput0 = 20;
const int ctrlOutputMin = 0;
const int ctrlOutputMax = 20;
const int ctrlOutputMid = (ctrlOutputMin + ctrlOutputMax) / 2;

////////////////
/// FUNCTIONS
////////////////

void stepTimeout() {
  lastStep += stepDuration;
  
  if (MODE_CONTROL) {
    ctrlSetpoint = random(ctrlSetpointMin, ctrlSetpointMax); // randomly vary the setpoint
  }
  
  if (MODE_OPENLOOP) {
    
    if (ctrlOutput == ctrlOutputMid) {
      ctrlOutput = random(ctrlOutputMin,ctrlOutputMax); // randomly vary the system input
    }
    
    else {
      ctrlOutput = ctrlOutputMid;     // return to the control midpoint input
    }
    
    analogWrite(pinCtrlV, ctrlOutput );
  }
}

void printTimeout() {
  lastPrint += printDuration;
  
  // print the results to the serial monitor:
  //Serial.print(lastStep)  ;  // time of last setpoint change
  //Serial.print(',');
  Serial.print(now);      // time now
  Serial.print(',');
  Serial.print(ambTemp);    // measured ambient temperature
  Serial.print(',');
  Serial.print(lastPrint)  ;  // time of last setpoint change
  //Serial.print(',');
  //Serial.print(ctrlSetpoint); // target temperature
  //Serial.print(',');
  //Serial.print(ctrlInput);    // measured temperature
  //Serial.print(',');
  //Serial.print("\t input ");      
  //Serial.print(ctrlOutput);   // signal to base voltage actuator (PWM)
  //Serial.print(',');
  //Serial.print(processVolt);      // measured voltage applied to base
  //Serial.print(',');
  //Serial.print("\t output ");      
  //Serial.print(processI);     // measured current flow
  //Serial.print(',');
  Serial.println();
}

int getSerial() {
  String inputString = "";         // a string to hold incoming data
  boolean stringComplete = false;  // whether the string is complete
  
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    
    if (isDigit(inChar)) {
      // add it to the inputString:
    inputString += inChar;
    }
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
      stringComplete = true;
  }
  
  //Serial.println(inputString);
  //inputString = "";
  //stringComplete = false;
  Serial.println(inputString);
  Serial.println(inputString.toInt());
  
  return inputString.toInt();
}

////////////////////////////
/// FUNCTION - MAIN SETUP
////////////////////////////

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(57600);
  analogReference(INTERNAL1V1);
  
  // initial output is zero
  ctrlOutput = ctrlOutput0;
  analogWrite(pinCtrlV, ctrlOutput);
  
  // PID STUFF
  ctrlSetpoint = ctrlSetpoint0;
  //turn the PID on
  // myPID.SetTunings(Kp,Ki,Kd) // set the tuning parameters
  // myPID.SetControllerDirection(DIRECT); // DIRECT or REVERSE
  myPID.SetOutputLimits(0,255);         // potentiometer range is 0-100%
  myPID.SetSampleTime(50);              // in milliseconds
  if (MODE_CONTROL) {
     myPID.SetMode(AUTOMATIC);          // AUTOMATIC = on; MANUAL = off
  }
  else {
     myPID.SetMode(MANUAL);             // AUTOMATIC = on; MANUAL = off
  }
}

///////////////////////////
/// FUNCTION - MAIN LOOP
///////////////////////////

void loop() {
  
  now = millis();
  
  // read the analog in value:
  ad_ambtemp = analogRead(pinOutTempAmb);
  ad_outtemp = analogRead(pinOutTemp);
  ad_outi = analogRead(pinOutI);
  ad_inv = analogRead(pinInV);

  ambTemp = ad_ambtemp / 9.31;
  processTemp = ad_outtemp / 9.31;
  processV = ad_inv*5./1024.;
  processI = ad_outi*5.*1000./1024./4.7;
  ctrlInput = CTRL_VAR;

  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  //outputValue = 128;
  
  if ( myPID.Compute() ) {
    //Serial.print("PID!\n");  
    // change the analog out value:
    analogWrite(pinCtrlV, ctrlOutput);  // int value (0-255); PID is adjusting this!
  }  

  if (now - lastPrint > printDuration) {
    printTimeout();
  }

#if MODE_RANDOM
  if (now - lastStep > stepDuration) {
    stepTimeout();
  }
#endif

  if (Serial.available()) {
    
    userInput = getSerial();
    
#if MODE_CONTROL
    // avoid using other functions inside min()
    ctrlSetpoint = min(userInput,ctrlSetpointMax); // get incoming data over the serial port
#endif
    
#if MODE_OPENLOOP
    // avoid using other functions inside min()
    ctrlOutput = min(userInput,ctrlOutputMax); // get incoming data over the serial port
    analogWrite(pinCtrlV, ctrlOutput);
#endif
  }

  // wait 10 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(10);
}
