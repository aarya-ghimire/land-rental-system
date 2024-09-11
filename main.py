from operation import rent_land, return_land, generate_invoice, generate_return_invoice, display_available_lands_to_rent, display_available_land_to_return
from write import land_info_writing
from read import land_info_reading
from datetime import datetime

# Main function
def main():
    while True:
        try:
            decision = int(input('Enter "1" to "rent" a land, "2" to "return" a rented land and "3" to "exit": '))
            if decision == 1:
                land_data = land_info_reading()
                display_available_lands_to_rent(land_data)
                
                # Generating a list of available kitta numbers
                available_kitta_numbers = []
                for land in land_data:
                    if land[-1] == "Available":
                        available_kitta_numbers.append(land[0])
                        
                kitta_number = input("Enter the Kitta Number of land you want to rent: ")
                if kitta_number not in available_kitta_numbers:
                    print("The land with this kitta number is not available for rent.")
                    continue
                
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                full_name = f"{first_name} {last_name}"
                rent_duration = int(input("How many months would you like to rent the land for? "))
                
                message = rent_land(land_data, kitta_number, full_name, rent_duration)
                
                if message == "Land rented successfully.":
                    # Generate the invoice
                    generate_message = generate_invoice(land_data, kitta_number, full_name, rent_duration)
                    if generate_message == "Invoice generated successfully.":
                        print("The rent invoice has been generated successfully.")

                        invoice_file_name = f"Invoice_{full_name.replace(' ', '_')}.txt"
                        try:
                            # Append invoice data to the existing file
                            with open(invoice_file_name, 'a') as file:
                                file.write("\n" + generate_message)  
                        except FileNotFoundError:
                            with open(invoice_file_name, 'w') as file:
                                file.write(generate_message)  # Create a new file if it doesn't exist
                        # Update land status in text file
                        land_info_writing(land_data)
                    else:
                        print(generate_message)
                    
                else:
                    print(message)
                    
            elif decision == 2:
                land_data = land_info_reading()
                available_lands_to_return = [land for land in land_data if land[-1] == "Not Available"]
                if not available_lands_to_return:
                    print("No lands available for return.")
                    continue
                
                display_available_land_to_return(available_lands_to_return)  
                
                # Generating a list of available kitta numbers for return
                available_return_kitta_numbers = [land[0] for land in available_lands_to_return]

                kitta_number = input("Enter the Kitta Number of land you want to return: ")
                if kitta_number not in available_return_kitta_numbers:
                    print("The land with this kitta number is not available for return.")
                    continue
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                full_name = f"{first_name} {last_name}"
                
                # Prompt the user for the return duration
                return_duration = int(input("Enter the duration of return (in months): "))
        
                message = return_land(land_data, kitta_number, full_name)
                if message == "Land returned successfully.":
                    return_invoice = generate_return_invoice(land_data, kitta_number, full_name, return_duration)
                    if return_invoice == "Return invoice generated successfully.":
                        print("The return invoice has been generated successfully.")
       
                        return_invoice_file_name = f"Return_Invoice_{full_name.replace(' ', '_')}.txt"
                        try:
                            with open(return_invoice_file_name, 'a') as file:
                                file.write("\n" + return_invoice)
                        except FileNotFoundError:
                            with open(return_invoice_file_name, 'w') as file:
                                file.write(return_invoice)  
                        # Update land status in text file
                        land_info_writing(land_data)
                    else:
                        print(return_invoice)
                else:
                    print(message)
                
            elif decision == 3:
                print("Thank you for choosing us. Have a good day!")
                break
            else:
                print("You have entered an invalid number. Please enter 1, 2, or 3.")
        except ValueError:
            print("Your input is invalid. Make sure to enter a numeric value.")

main()