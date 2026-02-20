import logging

logging.basicConfig(
    filename="reversecheck.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)
logging.info("This is the program which reverse the number and checks with previous number and checks greater or not")
k = int(input("Enter a number: "))
num =  k
sum = 0
while k > 0:
    rem = k % 10
    sum = sum * 10 + rem
    k//=10
logging.info("The original number was taken %s",num)
if sum > num:
    logging.info("The reversed number is greater than original number")
    print("The reversed number is greater than original number")
elif sum == num:
    logging.info("number is a palindrome number")
    print("number is a palindrome number")
else:
    logging.info("The reversed number is smaller than the original number")
    print("The reversed number is smaller than the original number")