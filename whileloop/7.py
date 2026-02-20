import logging

logging.basicConfig(
    filename="SumUntil100.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

total = 0

while total <= 100:
    num = int(input("Enter the number:  "))
    logging.info(f"User entered number: {num}")

    total += num
    logging.info(f"Updated total: {total}")

logging.info(f"Loop ended as total exceeded 100 → Final total: {total}")

print(total)

logging.info("Program ended")