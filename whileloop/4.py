import logging

logging.basicConfig(
    filename="EvenOddDigitCount.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

k = int(input("Enter a number:  "))
logging.info(f"User entered number: {k}")

evencount = 0
oddcount = 0

while k > 0:
    digit = k % 10
    logging.info(f"Processing digit: {digit}")

    if digit % 2 == 0:
        evencount += 1
        logging.info(f"Digit {digit} is EVEN → Even count = {evencount}")
    else:
        oddcount += 1
        logging.info(f"Digit {digit} is ODD → Odd count = {oddcount}")

    k //= 10
    logging.info(f"Remaining number after removing digit: {k}")

logging.info(f"Final Even Count: {evencount}, Final Odd Count: {oddcount}")

print("Even digits:", evencount)
print("Odd digits:", oddcount)

logging.info("Program ended")