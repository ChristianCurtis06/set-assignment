# Task 1: Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Remove duplicates and display the unique customer IDs
unique_ids = set(customer_ids)

print("Unique Customer IDs:")
for id in unique_ids:
    print(f" - {id}")