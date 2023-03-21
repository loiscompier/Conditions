# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# create funtion " farm_action"
def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status):
# take cows to cowshed - The cows are on the pasture at night
    if  (weather == "rainy" and time_of_day=="night" and location_of_the_cows == "pasture"):
        return print("take cows to cowshed")
    # milk cows - The cows are in the cowshed
    elif (location_of_the_cows == "cowshed" and cow_milking_status == "True"):
        return "milk cows"
    # take cows to cowshed  - The cows are standing in the rain
    elif (weather == "rainy"):
        return "take cows to cowshed"
    # fertilize pasture - The cows are in the cowshed
    elif (slurry_tank == True and location_of_the_cows == "cowshed"):
        return "fertilize pasture"
    # fertilize pasture - The weather is not sunny or windy
    elif (slurry_tank == True and  (weather == "rainy" or  weather == "neutral")):
        return "fertilize pasture"
    # mow grass 
    elif (location_of_the_cows == "cowshed" and season == "spring" and grass_status == True):
        return "mow grass"
    else: 
        return "wait"
    
print (farm_action("rainy", "night", False, "cowshed", "winter", True, True))
print (farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))



#print (test_1) 

#test_2 = farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
#print (test_2)
  
""""  farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
'fertilize pasture'

>>> farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
'wait'

Print (farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
'milk cows'

>>> farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
take cows to cowshed
milk cows
take cows back to pasture"""