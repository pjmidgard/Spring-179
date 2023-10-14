#Author Jurijus Pacalovas 
import gzip

# Function to compress data
def compress_data(input_data):
    return gzip.compress(input_data)

# Function to extract data
def extract_data(compressed_data):
    return gzip.decompress(compressed_data)

# Initialize variables
X1 = 0
X2 = 0
X3 = 0
X1_limit = 2**24

# Initialize compressed data variable
compressed_data = None

while True:
    # Ask the user for their choice
    choice = input("Enter 1 for compression, 2 for extraction, or any other key to exit: ").strip()
    
    if choice == "1":
        # Perform compression
        input_file_name = input("Enter the name of the input file: ")
        with open(input_file_name, "rb") as input_file:
            input_data = input_file.read()
        compressed_data = compress_data(input_data)

        # Check if X2 equals X1
        if X2 == X1:
            # Save X2 and X3
            with open("x2_x3_save.bin", "w") as save_file:
                save_file.write(f"X2={X2}\nX3={X3}")

        # Increment X1 and check if it reaches the limit
        X1 += 1
        if X1 == X1_limit:
            X1 = 0
            X3 += 1

    elif choice == "2":
        if compressed_data is not None:
            # Extraction
            extracted_data = extract_data(compressed_data)
            extracted_file_name = input("Enter the name for the extracted file: ")
            with open(extracted_file_name, "wb") as extracted_file:
                extracted_file.write(extracted_data)
            print(f"Data has been extracted and saved to {extracted_file_name}")

    else:
        print("Exiting.")
        break
