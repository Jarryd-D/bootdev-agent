from functions.get_file_content import get_file_content
print("testing")

test_1 = get_file_content("calculator", "lorem.txt")
test_2 = get_file_content("calculator", "main.py")
test_3 = get_file_content("calculator", "pkg/calculator.py")
test_4 = get_file_content("calculator", "/bin/cat") #(this should return an error string)
test_5 = get_file_content("calculator", "pkg/does_not_exist.py") #(this should return an error string)

print(f"lorem.txt length: {len(test_1)}")
print(f"lorem.txt truncated: {'truncated' in test_1}")
print(f"{test_2}\n{test_3}\n{test_4}\n{test_5}")
