# Tripadvisor parser to get information about german restaurants

### 1. Get cities list
Get all cities from Germany https://www.deutsche-staedte.de.  
All cities will be save localy into TXT file.
If you need a fresh cities list, just remove the file from your directory.

### 2. Get Tripadvisor URLs by city name
For this step will be check if the same city exists on Tripadvisor.  
Some cities are too small and doesn't exists on Tripadvisor.  
For some cities will be many proposal found.  
![](/images/search_dropdown.png)  
If proposal matched with city name, city URL will be saved.  
Also will be checked if the city is german city.   
![](/images/search_aachen.png)  


### 3. Read restaurants content by city URL
...and remove ads restaurants from list(optional)  
![](/images/premium.png) 

### 4. Get last number on the page  
![](/images/pagination.png) 


### 5. Go through paginaton list
![](/images/pagination_next.png) 
