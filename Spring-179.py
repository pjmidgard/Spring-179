import paq
import os

# Function to compress data
def compress_data(input_data):
    return paq.compress(input_data)

# Function to extract data
def extract_data(compressed_data):
    return paq.decompress(compressed_data)

# Initialize variables
X1 = 0
X2 = 0
X3 = 0
X1_limit = 2**24
compressed_data = None

# Check if a saved compressed data file exists and load it
if os.path.exists("compressed_data.gz"):
    with open("compressed_data.gz", "rb") as saved_data_file:
        compressed_data = saved_data_file.read()

# Automatically extract data when the program starts
if compressed_data is not None:
    extracted_data = extract_data(compressed_data)
    with open("extracted_data.bin", "wb") as extracted_file:
        extracted_file.write(extracted_data)
    print("Data has been automatically extracted.")

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
            extracted_file_name = input("Enter the name for extracted file: ")
            with open(extracted_file_name, "wb") as extracted_file:
                extracted_file.write(extracted_data)
            print(f"Data has been manually extracted and saved to {extracted_file_name}")

    else:
        # Save the compressed data to a file before exiting
        if compressed_data:
            with open("compressed_data.paq", "wb") as saved_data_file:
                saved_data_file.write(compressed_data)
        print("Exiting.")
        break