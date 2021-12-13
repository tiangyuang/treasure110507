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
        digitalWrite(Glass, HIGH);     // 馬達轉動
        delay(1000);
    } else if (str == "Plastic") {
        digitalWrite(Plastic, HIGH);
        delay(2000);
    } else if (str == "PC") {
        digitalWrite(PC, HIGH);
        delay(3000);
    } else if (str == "IA") {
        digitalWrite(IA, HIGH);
        delay(4000);
    } else if (str == "GG") {
        digitalWrite(GG, HIGH);
        delay(5000);
    } else if (str == "Battery") {
        digitalWrite(Battery, HIGH);
        delay(6000);
    }
  }
}
