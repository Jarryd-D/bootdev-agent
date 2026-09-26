from functions.run_python_file import run_python_file

test_1 = run_python_file("calculator", "main.py") #(should print the calculator's usage instructions)
test_2 = run_python_file("calculator", "main.py", ["3 + 5"]) #(should run the calculator... which gives a kinda nasty rendered result)
test_3 = run_python_file("calculator", "tests.py") #(should run the calculator's tests successfully)
test_4 = run_python_file("calculator", "../main.py") #(this should return an error)
test_5 = run_python_file("calculator", "nonexistent.py") #(this should return an error)
test_6 = run_python_file("calculator", "lorem.txt") #(this should return an error)

print(test_1, test_2, test_3, test_4, test_5, test_6)