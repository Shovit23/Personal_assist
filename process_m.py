from output_m import output
from time_m import get_time , get_date , show_calender
from database import *
from input_m import inp_m
from internet import check_connection , ipaddress , check_wiki
import assistance_details
from web import *
import pyjokes
from music import *
from news import get_news
from help import help


def pro_m(query):

    if 'play' in query and 'music' not in query:
        
        answer = get_answer('play')
    
    else:

        answer = get_answer(query)


    if answer == "":
        output("Don't know this one . Should i search it on internet ?")
        ans = inp_m()
        if "yes" in ans :

            answer = check_wiki(query)
            if answer != "":
                return answer


    if answer == "byee":

        return ("The Time is "+get_time())

    elif answer == "calender":

        return show_calender()
    
    elif answer == "joke":

        return (pyjokes.get_joke())

    

        
    elif answer == "live":

        return "Right now am under development . once m released you can find me in every system. "
    
    elif answer == "sad":

        return "That's ok . if you want me to tell some joke then just type tell me a joke"

         
    elif answer == "friends":

        return "Yes. you are my true friend"
    
    elif answer == "siri":

        return "Yes. Siri is my friend . she is serving for apple "
    
    elif answer == "check internet connection":

        if check_connection():
            return "Internet is connected"
        
        else:
            return "Not connected to the internet"
    
    elif answer == "news":

        return get_news()

    
    elif answer == "help":
        return help()

    elif answer == "your name":
        
        A = assistance_details.name
        return "Hey! My name is "+A+" How can i assist you sir ?"

    
    
    

    elif answer == "name":
         return "Developer name is Shovit Roy"

    elif answer == "google":

        open_google()
        return "opening Google"

    
    elif answer == "facebook":
    
        open_facebook()
        return "opening Facebook"

    elif answer == "gmail":

        open_gmail() 
        return "opening Gmail"
        
    elif answer == "browser":

        open_bro()
        return "opening Browser"
           
        

    elif answer == "todays date":

        return get_date()

    elif answer == "on speak":

        return turn_on_speech()

    elif answer == "off speak":

        return turn_off_speech()
        
    elif answer == "play song":

        return play_music()
    
    elif answer == "play":

        return specfic_music(query)

    elif answer == "stop":

        return stop_music()
    
    elif answer == "next":

        return next_music()
    
    elif answer == "pause":

        return pause_music()

    elif answer == "change name":
        output("Okay! what do you wanna call me? ")
        temp = inp_m()
        if temp == assistance_details.name:
            return "Opps! Look like you entered my old name"
        
        else:

            update_name(temp)
            assistance_details.name = temp
            return "Huraah! Now you can call me "+ temp

        
    elif answer == "ip":

        if ipaddress():
            return "Is your IP"
        
        else :
            return "You don't have a internet connection"

    


        

    else :
        #for feedind into the data base
        output("I don't know what is this, could you please tell me what it means? ")
        ans = inp_m()
        if "it means" in ans:
            ans = ans.replace("it means","")
            ans = ans.split()

            value = get_answer(ans)
            if value == "":
                return "couldn't understand what you said"
            else:
                insert_qna(query,value)
                return "Thanks , i will remember it from next time"
        else :
            return "can't help with this one"


        
