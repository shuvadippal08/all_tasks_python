import logging

logging.basicConfig(
    filename="DigitOccurrence.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

k = int(input("Enter the digit:  "))
logging.info(f"Number entered: {k}")
print(k)

d = int(input("Enter the specific digit:  "))
logging.info(f"Digit to search: {d}")

cnt = 0

while k > 0:
    digit = k % 10
    logging.info(f"Checking digit: {digit}")

    if digit == d:
        cnt += 1
        logging.info(f"Match found for {d} → Count = {cnt}")

    k //= 10
    logging.info(f"Remaining number: {k}")

logging.info(f"Final count of digit {d}: {cnt}")

print(d)
print(cnt)

logging.info("Program ended")