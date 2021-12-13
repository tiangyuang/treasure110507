#define pin 13



String str;
 
void setup() {
  pinMode(pin , OUTPUT);
  Serial.begin(9600);
}
 
void loop() {
  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
 
    if (str == "Glass") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(pin , HIGH);     // 馬達轉動
        delay(1000);
        digitalWrite(pin , LOW);
    } else if (str == "Plastic") {
        digitalWrite(pin , HIGH);
        delay(2000);
        digitalWrite(pin , LOW);
    } else if (str == "PC") {
        digitalWrite(pin , HIGH);
        delay(3000);
        digitalWrite(pin , LOW);
    } else if (str == "IA") {
        digitalWrite(pin , HIGH);
        delay(4000);
        digitalWrite(pin , LOW);
    } else if (str == "GG") {
        digitalWrite(pin , HIGH);
        delay(5000);
        digitalWrite(pin , LOW);
    } else if (str == "Battery") {
        digitalWrite(pin , HIGH);
        delay(6000);
        digitalWrite(pin , LOW);
    }
  }
}
