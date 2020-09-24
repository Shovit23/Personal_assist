import assistance_details 
from speak_m import speak
from database import speak_is_on

def output(o):


   if speak_is_on():
      speak(o)

   print(assistance_details.name+ " : " +o)
   print()