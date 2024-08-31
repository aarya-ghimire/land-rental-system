def land_info_writing(land_info_list):
    """This function writes land data to a file."""
    # Open the land_data.txt file in write mode and closes automatically because of with
    with open("land_data.txt", 'w') as file:
        for land_info in land_info_list:
            # Join the land information with ',' separator and write it to the file
            file.write(",".join(land_info) + "\n")