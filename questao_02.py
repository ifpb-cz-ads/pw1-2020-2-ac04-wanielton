# Questão 02:

import time 

temp = 10 

while temp: 
    minuto, segundo = divmod(temp, 60) 
    print(temp) 
    time.sleep(1) 
    temp -= 1
    
print('Fogo!!') 
  

  
