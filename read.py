def land_info_reading():
    """This function reads land data from a file."""
    # Initialize an empty list to store land data
    land_info_list = []
    # Open the land_data.txt file in read mode and closes automatically because of with
    with open("land_data.txt", 'r') as file:
        for data in file:
            # This removes space from the data and then split it by ',' and stores in a variable 
            land_info = data.strip().split(',')
            # Append the land information to the land_data list
            land_info_list.append(land_info)                    
    # Return the list containing land data
    return land_info_list