int incomingAudio;//storage for A0 data
int t =0;
int max_amp = 0;
int tot_amp = 0;
int avg_amp = 0;
int count = 0;
int msgCount = 1 ;
void setup(){

  Serial.begin(115200);
  pinMode(A0, INPUT);
  ADCSRA = 0;
  ADCSRB = 0;

  ADMUX |= (1 << REFS0); 
  ADMUX |= (1 << ADLAR); 

  ADCSRA |= (1 << ADPS2) | (1 << ADPS0);
  ADCSRA |= (1 << ADATE); 
  ADCSRA |= (1 << ADEN); 
  ADCSRA |= (1 << ADSC); 

}

void loop(){
  incomingAudio = ADCH;
  t++;
 // Serial.println(incomingAudio);
  int val = incomingAudio;
   int prev_val;
  if ( t < 100){
  if(val > max_amp)
  {
    max_amp = val;
  }
   prev_val =  val;
   //Serial.println(val);
   if(val >= 70){
    count++;
   }
   tot_amp += val; 
   avg_amp = tot_amp/ t;
  }
  if (t == 100){
  Serial.print("id: ");
  Serial.println(msgCount);
  Serial.print("Total Amplitude:");
  Serial.println(tot_amp);
  Serial.print("Avarage Amplitude:");
  Serial.println(avg_amp);
  Serial.print("Maximum Amplitude:");
  Serial.println(max_amp);
  Serial.print("No of Cars:");
  Serial.println(count);
  Serial.println(",");

  msgCount++;
  max_amp = 0;
  tot_amp = 0;
  avg_amp = 0;
  prev_val = 0;
  count = 0;
  val = 0;
  t = 0;
  } 
  delay(100);

}
