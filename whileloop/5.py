import logging

logging.basicConfig(
    filename="PalindromeCheck.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

num = int(input("Enter a number: "))
logging.info(f"User entered number: {num}")

rev = 0
original = num

logging.info("Starting number reversal process")

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

    logging.info(f"Extracted digit: {digit}, Reversed so far: {rev}, Remaining number: {num}")

logging.info(f"Final reversed number: {rev}")

if rev == original:
    logging.info(f"{original} is a palindrome")
    print("palindrome")
else:
    logging.info(f"{original} is NOT a palindrome")
    print("not a palindrome")

logging.info("Program ended")