// --- Motor Control Pins (MDD10A Driver) ---
const int M1_PWM = 10; // Motor 1 Speed (Left)
const int M1_DIR = 6;  // Motor 1 Direction

const int M2_PWM = 9;  // Motor 2 Speed (Right)
const int M2_DIR = 5;  // Motor 2 Direction

// --- Encoder Pins (Prepared for your next phase!) ---
const int ENC_RIGHT_A = 3;
const int ENC_RIGHT_B = 2;
const int ENC_LEFT_A = A4;
const int ENC_LEFT_B = A5;

void setup() {
  // Start communication with Raspberry Pi at 115200 baud rate
  Serial.begin(115200); 
  
  // Set motor pins as Outputs
  pinMode(M1_PWM, OUTPUT);
  pinMode(M1_DIR, OUTPUT);
  pinMode(M2_PWM, OUTPUT);
  pinMode(M2_DIR, OUTPUT);

  // Set encoder pins as Inputs (for later when you read wheel speeds)
  pinMode(ENC_RIGHT_A, INPUT_PULLUP);
  pinMode(ENC_RIGHT_B, INPUT_PULLUP);
  pinMode(ENC_LEFT_A, INPUT_PULLUP);
  pinMode(ENC_LEFT_B, INPUT_PULLUP);
}

void loop() {
  // Check if the Raspberry Pi sent a command over USB
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    
    // Find the comma separating the left and right speeds
    int commaIndex = command.indexOf(',');
    if (commaIndex > 0) {
      // Extract the numbers (e.g., "200,-200")
      int leftSpeed = command.substring(0, commaIndex).toInt();
      int rightSpeed = command.substring(commaIndex + 1).toInt();
      
      driveMotors(leftSpeed, rightSpeed);
    }
  }
}

void driveMotors(int left, int right) {
  // --- Left Motor (M1) Control ---
  // Flipped logic: LOW = Forward, HIGH = Backward (to fix "ulta" driving)
  if (left >= 0) {
    digitalWrite(M1_DIR, LOW);  // Drive Forward
  } else {
    digitalWrite(M1_DIR, HIGH); // Drive Backward
    left = -left;               // Convert negative speed to positive for PWM
  }
  analogWrite(M1_PWM, constrain(left, 0, 255));

  // --- Right Motor (M2) Control ---
  // Flipped logic: LOW = Forward, HIGH = Backward (to fix "ulta" driving)
  if (right >= 0) {
    digitalWrite(M2_DIR, LOW);  // Drive Forward
  } else {
    digitalWrite(M2_DIR, HIGH); // Drive Backward
    right = -right;             // Convert negative speed to positive for PWM
  }
  analogWrite(M2_PWM, constrain(right, 0, 255));
}