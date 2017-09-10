"""
This script creates an empty file
"""

filename="sample.txt"

# Create empty file
def create_file():
    """
    This function creates empty file
    """
    with open(filename,"w") as file:
        file.write("") # Writing empty string
