package_weight_response = input("Enter package weight: ")
delivery_distance_response = input("Enter the delivery distance(miles): ")
try:
    package_weight = float(package_weight_response.strip())
    delivery_distance = int(delivery_distance_response.strip())
    
    if package_weight <= 0:
        print("Weight must be greater than 0.")

    elif delivery_distance <= 0:
        print("Distance must be greater than 0.")
        
    else: 
        delivery_cost = package_weight * 0.75 + delivery_distance * 0.25
        
        if package_weight > 50:
            heavy_package = 15.00
            print(f"Delivery cost: ${delivery_cost:.2f} + Heavy package fee: ${heavy_package:.2f}")
            print(f"Total cost: ${(delivery_cost + heavy_package):.2f}")
        else:
            print(f"Delivery cost: ${delivery_cost}")
except ValueError:
    print("Please enter a valid number.")
    


