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
            solinoid(3, 1);
        }
        if (incomingByte == 'close')
        {
            solinoid(3, 0);
        }
    }
}

void solinoid(int pin, int state)
{
    if (state == 1)
    {
        digitalWrite(pin, HIGH);
    }
    else
    {
        digitalWrite(pin, LOW);
    }
}