import os
from subprocess import run, Popen, PIPE
from colorama import Fore, init

init(autoreset=True)


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


def compile_and_run_java(java_file):
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
    inputs = "John Doe\nIce Cream\nBlue\nNew York\nDog\nButterflies\nElder Holland"


    try:
        stdout, stderr = process.communicate(inputs)
        stderr = stderr.strip() if stderr is not None else ""
        
    except Exception as e:
        print("Exception:", str(e))
        stdout = ""
        stderr = ""

    # # Print the output and error messages

    expected_output = """Please enter your name:
Hello John Doe!
What is your favorite dessert? 
I hope you like coding Java as much as you like to eat Ice Cream.
What is your favorite color? 
So, you like the color Blue. My favorite color is 0000ff.
Where were you born?
I was born in Silicon Valley. If I had been born in New York, perhaps we would have been friends.
What is your favorite kind of pet? 
I'm sure a Dog is safer than my pet. I have a pet mouse.... but it always BYTES! HaHaHa!
What is your favorite insect? 
Wow! You like Butterflies!?! I like spiders. They make great WEB sites but sometimes they BUG me!
Who was your favorite speaker at the last General Conference? 
I agree. Elder Holland was great! I'm just glad they didn't make Java against the Word of Wisdom!!!
"""
    
    stdout_lines = stdout.splitlines()
    expected_output_lines = expected_output.splitlines()
    delete_space_elements(stdout_lines)
    delete_space_elements(expected_output_lines)

    testArray = []

    if(delete_space_elements(stdout_lines) == delete_space_elements(expected_output_lines)):
        print("Well done!")
        remove_main("Main.class")
    else:
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
compile_and_run_java(java_file_path)