#Author Jurijus Pacalovas
import paq
import os

# Function to compress data using "paq"
def compress_data(input_data):
    return paq.compress(input_data)

# Function to extract data using "paq"
def extract_data(compressed_data):
    return paq.decompress(compressed_data)

# Initialize variables
X1 = 0
X2 = 0
X3 = 0
X1_limit = 2**24
compressed_data = None

# Define the hidden folder name
hidden_folder = ".bin"

# Define the hidden file name in the hidden folder
hidden_compressed_file = f"{hidden_folder}/.my_hidden_data.paq"

# Check if the hidden folder exists, and create it if not
if not os.path.exists(hidden_folder):
    os.mkdir(hidden_folder)

# Automatically extract data when the program starts
if compressed_data is not None:
    extracted_data = extract_data(compressed_data)
    extracted_file_name = "extracted_data.bin"
    # Check if the file exists, and choose a different name if it does
    file_counter = 1
    while os.path.exists(extracted_file_name):
        extracted_file_name = f"extracted_data_{file_counter}.bin"
        file_counter += 1
    with open(extracted_file_name, "wb") as extracted_file:
        extracted_file.write(extracted_data)
    print(f"Data has been automatically extracted using 'paq' and saved to {extracted_file_name}")

while True:
    # Ask the user for their choice
    choice = input("Enter 1 for compression, 2 for manual extraction, or any other key to exit: ").strip()
    
    if choice == "1":
        input_file_name = input("Enter the name of the input file: ")
        with open(input_file_name, "rb") as input_file:
            input_data = input_file.read()
        compressed_data = compress_data(input_data)

        if X2 == X1:
            with open("x2_x3_save.bin", "w") as save_file:
                save_file.write(f"X2={X2}\nX3={X3}")

        X1 += 1
        if X1 == X1_limit:
            X1 = 0
            X3 += 1

    elif choice == "2":
        if compressed_data is not None:
            extracted_data = extract_data(compressed_data)
            extracted_file_name = input("Enter the name for manual extraction: ")
            # Check if the file exists, and choose a different name if it does
            file_counter = 1
            while os.path.exists(extracted_file_name):
                extracted_file_name = f"{extracted_file_name}_{file_counter}"
                file_counter += 1
            with open(extracted_file_name, "wb") as extracted_file:
                extracted_file.write(extracted_data)
            print(f"Data has been manually extracted using 'paq' and saved to {extracted_file_name}")

    else:
        # Save the compressed data to a hidden file in the hidden folder before exiting
        if compressed_data:
            with open(hidden_compressed_file, "wb") as saved_data_file:
                saved_data_file.write(compressed_data)
        print("Exiting.")
        break