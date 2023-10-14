#Author Jurijus Pacalovas
import paq
import os
import shutil

# Function to compress data using "paq"
def compress_data(input_data):
    return paq.compress(input_data)

# Function to extract data using "paq"
def extract_data(compressed_data):
    return paq.decompress(compressed_data)

# Function to save the values of X1 and X3 to a file
def save_x1_x3_to_file(filename, x1_value, x3_value):
    with open(filename, "w") as file:
        file.write(f"X1={x1_value}\nX3={x3_value}")

# Initialize variables
X1 = 0
X2 = 0
X3 = 0
X1_limit = 2**24
compressed_data = None
Y = 0

# Define the hidden folder name
hidden_folder = ".bin"

# Create the hidden folder if it doesn't exist
if not os.path.exists(hidden_folder):
    os.mkdir(hidden_folder)

# Define the path for "x1_x2_bin"
x1_x2_bin_path = "x1_x2_bin"

while True:
    # Ask the user for their choice
    choice = input("Enter 1 for compression, 2 for manual extraction, or any other key to exit: ").strip()

    if choice == "1":
        # Compress data and save it to "x1_x2_bin" when the program closes
        input_file_name = input("Enter the name of the input file: ")
        with open(input_file_name, "rb") as input_file:
            input_data = input_file.read()
        compressed_data = compress_data(input_data)

        # Save X1 and X3 to a file
        x1_x3_file = "x1_x3_values.txt"
        save_x1_x3_to_file(x1_x3_file, X1, X3)

        X1 += 1
        if X1 == X1_limit:
            X1 = 0
            X3 += 1

    elif choice == "2":
        if compressed_data is not None:
            # Manually extract data
            extracted_data = extract_data(compressed_data)
            extracted_file_name = input("Enter the name to save the extracted data: ")
            with open(extracted_file_name, "wb") as extracted_file:
                extracted_file.write(extracted_data)
            print(f"Data has been manually extracted using 'paq' and saved to {extracted_file_name}")
            
            # Increment and save Y
            Y += 1
            y_file = "y_value.txt"
            with open(y_file, "w") as y_output_file:
                y_output_file.write(str(Y))

    else:
        try:
            if compressed_data is not None:
                # Save the compressed data to "x1_x2_bin" before exiting
                with open(x1_x2_bin_path, "wb") as x1_x2_file:
                    x1_x2_file.write(compressed_data)

                # Use shutil to copy or move the "x1_x2_bin" file as needed
                destination_path = "/path/to/destination/x1_x2_bin"
                shutil.copy(x1_x2_bin_path, destination_path)
            print("Exiting.")
            break
        except Exception as e:
            pass