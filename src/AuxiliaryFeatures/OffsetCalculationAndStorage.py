def read_and_convert(file_path):
    try:
        with open(file_path) as file:
            text = file.read()
            value = float(text.strip())
            return value
    except ValueError:
        print("Error: unable to convert text to a floating-point number.")
        return None

def write_value(tempOffset, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(str(tempOffset))
        print(f"tempOffset {tempOffset} written to {file_path}")
    except Exception as e:
        print(f"Error writing value: {e}")
