import re

def check_print_statements(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    # Regular expression to find all print statements
    print_pattern = re.compile(r'print\((.*?)\)', re.DOTALL)

    for line_number, line in enumerate(content, start=1):
        matches = print_pattern.findall(line)
        for match in matches:
            # Remove leading and trailing whitespace and split by newline
            lines = match.strip().split('\\n')
            for sub_line in lines:
                # Remove leading and trailing whitespace from each line
                sub_line = sub_line.strip()
                if len(sub_line) > 21:
                    print(f"Line {line_number}: {sub_line}")

# Path to the file
file_path = 'KRCKalkulator.py'
check_print_statements(file_path)