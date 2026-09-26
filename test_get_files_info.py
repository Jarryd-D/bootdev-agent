from functions.get_files_info import get_files_info
print("Testing")
test_1 = get_files_info("calculator", ".")
test_2 = get_files_info("calculator", "pkg")
test_3 = get_files_info("calculator", "/bin")
test_4 = get_files_info("calculator", "../")
print(f"{test_1}\n{test_2}\n{test_3}\n{test_4}")
print("Test complete")