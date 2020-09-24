
import requests	 
from output_m import output
from internet import check_connection

def get_news(): 

    if check_connection():
	
	
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e39b0326688446889cbbac7d76d7031f"

        
        open_bbc_page = requests.get(main_url).json() 

        
        article = open_bbc_page["articles"] 

        
        results = [] 
        
        for ar in article: 
            results.append(ar["title"]) 
            
        for i in range(len(results)): 
            
            
            output(str(i + 1)+" " +results[i])
        return "Here are your top news from today."    

    else:

        return "Please connect to the internet to use this feature."
         


