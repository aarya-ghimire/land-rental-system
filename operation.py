from datetime import datetime
from write import land_info_writing

def rent_land(land_info_list, kitta_number, customer_name, rent_duration):
    """ Rent a land to a customer. """

    for land_info in land_info_list:

        if land_info[0] == kitta_number:
            if land_info[-1] == "Available":
                # Set the land status to "Not Available"
                land_info[-1] = "Not Available"
                land_info_writing(land_info_list)
                return "Land rented successfully."
            else:
                return "This land is already rented."
    return "Land not found."

def generate_invoice(land_info_list, kitta_number, customer_name, rent_duration):
    """ Generate an invoice for renting a land and print it in terminal. """
    
    # Check if an the customer with same name already exist or not
    invoice_file_name = "Invoice_" + customer_name.replace(' ', '_') + ".txt"
    
    # Iterate through each land in the land_info list
    for land_info in land_info_list:
        if land_info[0] == kitta_number:
            # Calculate the total rent amount
            total_amount = int(land_info[4]) * rent_duration
            
            # Construct invoice data
            invoice_data = [
                "==================== Invoice for Rented Land ====================",
                f"Customer Name: {customer_name}",
                '-' * 65,
                f"Kitta Number: {kitta_number}",
                '-' * 65,
                f"City/District: {land_info[1]}",
                '-' * 65,
                f"Land Faced: {land_info[2]}",
                '-' * 65,
                f"Area of Land: {land_info[3]} anna",
                '-' * 65,
                f"Date and Time of Rent: {datetime.now()}",
                '-' * 65,
                f"Duration of Rent: {rent_duration} months",
                '-' * 65,
                f"Total Amount: {total_amount} Nepali Rupees",
                "=================================================================",
            ]
            
            try:
                with open(invoice_file_name, 'a') as file:  # Open file in append mode
                    for line in invoice_data:
                        file.write(line + '\n')
                    file.write('\n')
            except FileNotFoundError:
                with open(invoice_file_name, 'w') as file:
                    for line in invoice_data:
                        file.write(line + '\n')
                    file.write('\n')
            
            max_len = max(len(line) for line in invoice_data)
            print("*" * (max_len + 1))
            for line in invoice_data:
                print(f"* {line.ljust(max_len)} *")
            print("*" * (max_len + 1))
            
            print("Invoice generated successfully.")

            return
    
    print("Land not found.") 

def return_land(land_info_list, kitta_number, customer_name):
    """ Return a rented land. """
    
    for index, land_info in enumerate(land_info_list):
        # Check if the kitta number matches the desired land and it is not available
        if land_info[0] == kitta_number:
            if land_info[-1] == "Not Available":
                late_period = int(input("Enter how many months late you are returning the land: "))
                # Calculate fine if the return is late
                if late_period > 0:
                    fine = late_period * 100  # Fine is Rs. 100 per month so mulitplying months by 100
                    print(f"You are returning the land {late_period} months late.")
                    print(f"Your fine amount is: {fine} Nepali Rupees.")
                else:
                    print("You returned the land on time. No fine is applicable.")
                # Set the land status to "Available"
                land_info[-1] = "Available"
                land_info_list[index] = land_info 
                return "Land returned successfully."
            else:
                return "This land is not currently rented."
    return "Land not found."

def generate_return_invoice(land_info_list, kitta_number, customer_name, return_duration):
    """ Generate an invoice for returning a rented land and print it in terminal. """
    
    # Check if an the customer with same name already exist or not
    invoice_file_name = "Return_Invoice_" + customer_name.replace(' ', '_') + ".txt"
    
    for land_info in land_info_list:
        if land_info[0] == kitta_number:
            # Calculate the total rent amount
            total_amount = int(land_info[4]) * return_duration
            
            # Construct return invoice data
            return_invoice_data = [
                "================ Return Invoice for Rented Land ================",
                f"Customer Name: {customer_name}",
                '-' * 65,
                f"Kitta Number: {kitta_number}",
                '-' * 65,
                f"City/District: {land_info[1]}",
                '-' * 65,
                f"Land Faced: {land_info[2]}",
                '-' * 65,
                f"Area of Land: {land_info[3]} anna",
                '-' * 65,
                f"Date and Time of Return: {datetime.now()}",
                '-' * 65,
                f"Duration of Rent: {return_duration} months",
                '-' * 65,
                f"Total Amount: {total_amount} Nepali Rupees",
                "=================================================================",
            ]
            
            # Write the return invoice data to the invoice file
            with open(invoice_file_name, 'w') as file:
                for line in return_invoice_data:
                    file.write(line + '\n')
                file.write('\n')
            
            # Print the return invoice details
            max_len = max(len(line) for line in return_invoice_data)
            print("*" * (max_len + 4))
            for line in return_invoice_data:
                print(f"* {line.ljust(max_len)} *")
            print("*" * (max_len + 4))
            
            return "Return invoice generated successfully."
    
    return "Land not found."


def display_available_lands_to_rent(land_data):
    """Display available lands."""
    print("Currently these lands are available to rent:")
    for land in land_data:
        if land[-1] == "Available":
            print(", ".join(land))

def display_available_land_to_return(land_data):
    """Display available lands for return."""
    available_lands_to_return = [land for land in land_data if land[-1] == "Not Available"]
    if available_lands_to_return:
        print("Currently these lands are available to return:")
        for land in available_lands_to_return:
            print(", ".join(land))
    else:
        print("No lands available for return.")