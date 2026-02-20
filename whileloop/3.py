import logging

logging.basicConfig(
    filename="DigitSumuptosingledigit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

k = int(input("Enter a number: "))
logging.info(f"User entered number: {k}")

s = 0

def total(digit: int) -> int:
    logging.info(f"Calculating digit sum of {digit}")
    digit_sum = 0

    while digit > 0:
        digit_sum += digit % 10
        digit //= 10

    logging.info(f"Digit sum calculated: {digit_sum}")
    return digit_sum


def count(digit: int) -> int:
    logging.info(f"Counting digits of {digit}")
    c = 0

    while digit > 0:
        c += 1
        digit //= 10

    logging.info(f"Number of digits: {c}")
    return c


logging.info("Starting loop to reduce number to single digit")

while count(k) != 1:
    s = total(k)
    logging.info(f"Intermediate result after sum: {s}")
    k = s

logging.info(f"Final single digit result: {s}")

print(s)

logging.info("Program ended")