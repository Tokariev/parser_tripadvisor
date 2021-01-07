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
