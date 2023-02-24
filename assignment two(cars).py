# Emmanuel Asiedu
# 6930221
#list of available cars and their prices
cars={
"bugatti Chiron": 3000000,
"Honda Civc": 150000,
"Rolls Royce Sweptail": 4500000,
"Mercedes Benz Maybach Exelero": 1000000,
"Lamborghini Veneno": 2500000,
"Bugatti Veyron": 1100000,
"Ferrari Sergio": 1000500,
"Honda Accord": 400000,
"Toyota RAV4": 220000,
"Chevrolet Camaro": 500000,
"Toyota Corolla": 250000,
"Ferrari FF": 2000000,
"Hyundai Sonata": 450000,
"Toyota Camry": 170000,
"Ford Focus": 500000,
"BMW X5": 600000,
"Fiat 124 Spider": 900000,
"Honda CR-V": 240000,
"Jaguar I-Pace": 800000,
"lexus IS Sedan": 600000,
"Maserati Levante SUV": 950000,
"Nisan Titan": 440000,
"Porsche 911": 780000,
"Toyota 4Runner": 860000,
"Volkswagen GTI": 820000,
"Audi Q8": 1200000,
"Acura TLX": 4000000,
"Jeep Patriot": 590000,
"Ford Torino": 2000000,
"Toyota Highlander": 470000,
"Toyota Fortuner": 600000,
"Dodge Viper": 5000000,
}
#get use input for car name
CarName = input("Enter a carName:")
#check if Car name is in the list of available cars
if CarName in cars:
    print("Yes")
#if car name is present, get its price
    CarPrice= cars[CarName]
    print(f"The price of {CarName} is £{CarPrice}.")
else:
    #if car name is not present, inform the user
    print(f"Sorry, {CarName} is not available.")