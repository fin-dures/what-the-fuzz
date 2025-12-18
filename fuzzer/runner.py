import subprocess

def run_fuzzer(target_program, inputs):

    for input in inputs:


        try:
            process = subprocess.Popen([target_program], 
                                       stdin=subprocess.PIPE, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=input.encode())

            if process.returncode != 0:
                print(f"Crash detected with input: {repr(input)}")
                print(f"Error output: {stderr.decode()}")


        except Exception as e:
            print(f"An error occurred while running the fuzzer: {e}")


