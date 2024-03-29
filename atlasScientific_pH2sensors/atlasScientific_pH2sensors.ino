// MC Lusardi - May 2021
// This code has been adapted from the Arduino Sample code available on Atlas Scientific's website:
// https://atlas-scientific.com/files/Arduino-Mega-pH-Sample-Code.pdf
// This code is intened to read values from two Atlas Scientific pH micro sensor via Serial communication
// To work, connect the sensors to serial port 3 (pins 14 and 15 on Arduino Mega) and serial port 2 (pins 16 and 17)
// To send commands to the sensor, follow the UART documentation here:
// https://atlas-scientific.com/files/pH_EZO_Datasheet.pdf
// Each command must be preceded by what sensor it is intended for:
// if the command is preceded by "s3:" the command is sent to the sensor connected to serial port 3
// if the command is preceded by "s2:" the command is sent to the sensor connected to serial port 2
// if the command is preceded by "AS:" the command is sent to both sensors. 


String inputstring = "";                              //a string to hold incoming data from the PC
boolean input_string_complete = false;                //have we received all the data from the PC
String sensorType = "";
String command = "";

String pHsensorstring3 = "";                          //a string to hold the data from pH sensor 3
boolean pHinput_string_complete3 = false;             //have we received all the data from pH3
boolean pHsensor_string_complete3 = false;            //have we received all the data from pH3
float pH1;                                            //used to hold a floating point number that is pH3

String pHsensorstring2 = "";                          //a string to hold the data from pH sensor 2
boolean pHinput_string_complete2 = false;             //have we received all the data from pH2
boolean pHsensor_string_complete2 = false;            //have we received all the data from pH2
float pH2;                                            //used to hold a floating point number that is pH2

void setup() {                                        //set up the hardware
  Serial.begin(9600);                                 //set baud rate for the hardware serial port_0 to 9600
  Serial3.begin(9600);                                //set baud rate for software serial port_3 to 9600
  Serial2.begin(9600);                                //baur rate for port_2
  
  inputstring.reserve(10);                            //set aside some bytes for receiving data from the PC
  pHsensorstring3.reserve(30);                          //set aside some bytes for receiving data from pH3
  pHsensorstring2.reserve(30);                          //set aside bytes for data from pH2        
}

void serialEvent() {                                  //if the hardware serial port_0 receives a char
  inputstring = Serial.readStringUntil(13);           //read the string until we see a <CR>
  input_string_complete = true;                       //set the flag used to tell if we have received a completed string from the PC
}


void serialEvent3() {                                 //if the hardware serial port_3 receives a char
  pHsensorstring3 = Serial3.readStringUntil(13);        //read the string until we see a <CR>
  pHsensor_string_complete3 = true;                   //set the flag used to tell if we have received a completed string from the PC
}

void serialEvent2() {                                 //ditto for serial port_2
  pHsensorstring2 = Serial2.readStringUntil(13);         
  pHsensor_string_complete2 = true;                 
}

void loop() {                                         //here we go...


  if (input_string_complete == true) {                //if a string from the PC has been received in its entirety
    sensorType = parseSensorTypeInput(inputstring);
    command = parseCommandInput(inputstring);

    if(sensorType.compareTo("s3:") == 0){        //if the sensor indicated is s3 (serial port_3)
      //Serial.print("Sending command to PH: ");
      //Serial.println(command);
      
      Serial3.print(command);                         //send that command to that sensor
      Serial3.print('\r');                            //add a <CR> to the end of the string
    }
    else if(sensorType.compareTo("s2:") == 0){        //if the sensor indicated is s2 (serial port_2)
      //Serial.print("Sending command to PH: ");
      //Serial.println(command);
      
      Serial2.print(command);                         //send that command to that sensor
      Serial2.print('\r');                            //add a <CR> to the end of the string
    }
    else if(sensorType.compareTo("AS:") == 0){        //if all sensors are indicated
      //Serial.print("Sending command to AS: ");
      //Serial.println(command);
      
      Serial2.print(command);                         //send that string to s2
      Serial2.print('\r');                            //add a <CR> to the end of the string
      
      Serial3.print(command);                         //send that string to s3
      Serial3.print('\r');                            //add a <CR> to the end of the string
    }
    else {
      Serial.println("incorrect format for command");
    }
    inputstring = "";                                 //clear the string
    sensorType = "";
    command = "";
    input_string_complete = false;  
  }

// the commented out functions below would print data from just s3 or just s2
  /*if (pHsensor_string_complete3 == true) {            //if a string from the Atlas Scientific product has been received in its entirety
    Serial.print("s2,");
    Serial.println(pHsensorstring3);                    //send that string to the PC's serial monitor
    pHsensorstring3 = "";                               //clear the string:
    pHsensor_string_complete3 = false;                //reset the flag used to tell if we have received a completed string from the Atlas Scientific product
  }

  if (pHsensor_string_complete2 == true) {            //if a string from the Atlas Scientific product has been received in its entirety
    Serial.print("s1,");
    Serial.println(pHsensorstring2);                    //send that string to the PC's serial monitor
    pHsensorstring2 = "";                               //clear the string:
    pHsensor_string_complete2 = false;                //reset the flag used to tell if we have received a completed string from the Atlas Scientific product
  }*/

// if both s3 and s2 have sent data, this funciton will print each value in the order "s3, s2"
  if (pHsensor_string_complete3 == true && pHsensor_string_complete2 == true) {
    //Serial.print("Testing printing, ");
    Serial.print(pHsensorstring3);
    Serial.print(',');
    Serial.println(pHsensorstring2);
    pHsensorstring3 = "";
    pHsensor_string_complete3 = false;
    pHsensorstring2 = "";
    pHsensor_string_complete2 = false;
  }
}

//this function will return a string of the first three characters of the input, which will indicates the sensor it's intended for
String parseSensorTypeInput(String input){
  String result = input.substring(0,3);
  //Serial.print("First three char are: ");
  //Serial.println(result);
  return result;
}

//this function will return a string of the characters after the first three in the input, which indicates the command
String parseCommandInput(String input) {
  String result = input.substring(3);
  //Serial.print("Last char are: ");
  //Serial.println(result);
  return result;
}
