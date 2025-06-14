def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    print("--------------------")
    
    while True:
        try:
            temp = float(input("Enter temperature value: "))
            
            unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()
            
            if unit == 'C':
                converted = celsius_to_fahrenheit(temp)
                print(f"{temp}°C is {converted:.2f}°F")
            elif unit == 'F':
                converted = fahrenheit_to_celsius(temp)
                print(f"{temp}°F is {converted:.2f}°C")
            else:
                print("Invalid unit. Please enter 'C' or 'F'.")
                continue
                
            another = input("Convert another? (Y/N): ").upper()
            if another != 'Y':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a numeric temperature value.")

temperature_converter()