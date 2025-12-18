import runner
import random
import string

inputs = []

def generate_input():
    length = random.randint(10, 100)
    return "".join(random.choices(string.printable, k=length))

for _ in range(100):
    inputs.append(generate_input())


runner.run_fuzzer("../testCases/whats-your-name", inputs)