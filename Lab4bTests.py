import os
from subprocess import run, Popen, PIPE
from colorama import Fore, init

init(autoreset=True)


def switch_case(case):
    if case == "I do!\nSi\nY\n":
        return """Do you like to code in Java?:
Error: Please answer with a 'Y' or 'N'.
Do you like to code in Java?:
Error: Please answer with a 'Y' or 'N'.
Do you like to code in Java?:
That's great! I do too!
"""
    elif case == "nope, I don't\nN\n":
        return """Do you like to code in Java?:
Error: Please answer with a 'Y' or 'N'.
Do you like to code in Java?:
That's ok. There are many other wonderful things in life to learn."""
    


def remove_whitespace(strings):
    cleaned_strings = [string.strip() for string in strings]
    return cleaned_strings

def delete_space_elements(arr):
    return [element for element in arr if element != '']

def remove_duplicates_preserve_order(arr):
    result = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

def merge_corrected_strings(strings):
    merged_strings = []

    for string in strings:
        start_index = string.find("Got '") + len("Got '")
        end_index = string.find("'", start_index)
        original_part = string[start_index:end_index]

        start_index = string.find("Expected '") + len("Expected '")
        end_index = string.find("'", start_index)
        corrected_part = string[start_index:end_index]

        # merged_strings.append(f"Got '{Fore.YELLOW + original_part}', Expected '{ Fore.BLUE + corrected_part}'")
        merged_string = (
            f"\033[91mGot '{original_part}'\033[0m, "
            f"\033[92mExpected '{corrected_part}'\033[0m"
        )
        
        merged_strings.append(merged_string)

    return merged_strings


def remove_main(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file: {e.filename} - {e.strerror}")


def compile_and_run_java(java_file, values):
    # Compile the Java file

    run(['javac', java_file])

    # Get the class name by removing the file extension
    class_name = java_file.rsplit('.', 1)[0]

    # Run the Java program and pass input
    process = Popen(
        ['java', class_name], 
        stdin=PIPE, 
        stdout=PIPE, 
        stderr=PIPE, 
        text=True)
    inputs = values


    try:
        stdout, stderr = process.communicate(inputs)
        stderr = stderr.strip() if stderr is not None else ""
        
    except Exception as e:
        print("Exception:", str(e))
        stdout = ""
        stderr = ""

    expected_output = switch_case(inputs)
    
    stdout_lines = stdout.splitlines()
    stdout_lines = delete_space_elements(stdout_lines)
    stdout_lines = remove_whitespace(stdout_lines)

    expected_output_lines = expected_output.splitlines()
    expected_output_lines = delete_space_elements(expected_output_lines)
    expected_output_lines = remove_whitespace(expected_output_lines)

    testArray = []

    if(stdout_lines == expected_output_lines):
        print("Well done!")
        remove_main("Main.class")
    else:
        print()
        print("Actual")
        print()
        print(stdout)
        print()
        print("Expected")
        print()
        print(expected_output)
        print()
        print("There might be some mistakes in the typo. Check your actual output and the expected output")
        print()

        for index, (stdout_lines, expected_output_lines) in enumerate(zip(stdout_lines, expected_output_lines)):
            if stdout_lines != expected_output_lines:
                result = f"Got '{stdout_lines}', Expected '{expected_output_lines}'"
                testArray.append(result)

        result_best = remove_duplicates_preserve_order(testArray)

        

        merged_output = merge_corrected_strings(result_best)
        for string in merged_output:
            print(string)
        print()
        remove_main("Main.class")


    if stderr:
        print("Error:")
        print(Fore.RED + stderr)
        remove_main("Main.class")

# Specify the path to your Java file
java_file_path = "Main.java"


# Call the function to compile and run the Java file
compile_and_run_java(java_file_path,"I do!\nSi\nY\n")

compile_and_run_java(java_file_path,"nope, I don't\nN\n")
