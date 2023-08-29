/*
Author: Jacob Davies

see readme for more information
*/

int incomingByte;

void setup()
{
    Serial.begin(9600);
    pinMode(3, OUTPUT);
}

void loop()
{
    if (Serial.available() > 0)
    {
        incomingByte = Serial.read();
        if (incomingByte == 'open')
        {
            servo(3, 180);
        }
        if (incomingByte == 'close')
        {
            servo(3, 0);
        }
    }
}

void servo(int pin, float angle)
{
    analogWrite(11, (angle / 180) * 255);
}