#define Glass 8
#define Plastic 9
#define PC 10
#define IA 11
#define GG 12
#define Battery 13



String str;
 
void setup() {
  pinMode(Glass, OUTPUT);
  pinMode(Plastic, OUTPUT);
  pinMode(PC, OUTPUT);
  pinMode(IA, OUTPUT);
  pinMode(GG, OUTPUT);
  pinMode(Battery, OUTPUT);
  Serial.begin(9600);
}
 
void loop() {
  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
 
    if (str == "Glass") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(Glass, HIGH);     // 開燈
        delay(5000);
        digitalWrite(Glass, LOW);
    } else if (str == "Plastic") {
        digitalWrite(Plastic, HIGH);
        delay(5000);
        digitalWrite(Plastic, LOW);
    } else if (str == "PC") {
        digitalWrite(PC, HIGH);
        delay(5000);
        digitalWrite(PC, LOW);
    } else if (str == "IA") {
        digitalWrite(IA, HIGH);
        delay(5000);
        digitalWrite(IA, LOW);
    } else if (str == "GG") {
        digitalWrite(GG, HIGH);
        delay(5000);
        digitalWrite(GG, LOW);
    } else if (str == "Battery") {
        digitalWrite(Battery, HIGH);
        delay(5000);
        digitalWrite(Battery, LOW);
    }
  }
}
