# Shaik Fahad
# 07 Nov, 2024

# Problem 2, This program user may choose a beginning range and it will then check if a given number falls within that range of 10. 

def lets_see(number, lower_bound = 10):
    upper_bound = lower_bound + 10

    if lower_bound <= number <= upper_bound:
        print(f"The number {number} is in the range {lower_bound} to {upper_bound}.")
        return True
    else: 
        print(f"The number {number} is in the range {lower_bound} to {upper_bound}.")
        return False

results = lets_see(20)

print(results)


# Shaik Fahad
# 07 Nov, 2024
# Problem 5, This program prints a message every time it is run or imported

def main():
    print("This only runs when I run the file directly.")
print("I will always get printed.")
if __name__ == "__main__":
    main()

