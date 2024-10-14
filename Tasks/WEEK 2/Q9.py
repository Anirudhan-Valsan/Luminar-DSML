'''
Q9. Accept any city from the user and display monument of that city.

City        Monument

Delhi       Red Fort
Agra        Taj Mahal
Jaipur      Jal Mahal
'''

def  monument(city):

    monuments = {
                    'delhi':'Red Fort',
                    'agra' :'Taj Mahal',
                    'jaipur':'Jal Mahal'
                 }
    
    return monuments[city.lower()]



city = input("Enter the city name (Delhi,Agra or Jaipur):\t")

print(f"The monument in the city of {city} is {monument(city)}")

