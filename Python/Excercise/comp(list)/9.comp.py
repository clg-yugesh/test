# Generate palindrome numbers from 1 to 100
palindromes = [n for n in range(1, 101) if str(n) == str(n)[::-1]]

# Print the list of palindromes
print(palindromes)