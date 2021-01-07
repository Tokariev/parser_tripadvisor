# Tripadvisor parser to get information about german restaurants

### 1. Get cities list
Get all cities from Germany https://www.deutsche-staedte.de.  
Result:  
![](/images/city.png)

### 2. Get Tripadvisor URLs by city name
For this step will be check if the same city exists on Tripadvisor.  
Some cities are too small and doesn't exists on Tripadvisor.  
For some cities will be many proposal found.  
![](/images/search_dropdown.png)  
If proposal matched with city name, city URL will be saved.  
Also will be checked if the city is german city.   
![](/images/search_aachen.png)  
Result:  
![](/images/city_url_paar.png)

### 3. Read restaurants content by city URL
...and remove ads restaurants from list(optional)  
![](/images/premium.png) 

### 4. Get last number on the page  
![](/images/pagination.png) 


### 5. Go through paginaton list
![](/images/pagination_next.png) 
