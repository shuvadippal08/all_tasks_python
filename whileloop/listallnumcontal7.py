import logging

logging.basicConfig(
    filename="listallnumcontaining7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - %(name)s",
    filemode="a",
    force=True,
)

logging.info("This is the program to calculate number of digit within range containing 7")
i=0
l = []
while i < 101:
    k = (str)(i)
    if '7' in k:
        l.append((int)(k))
    i+=1

l.sort()
logging.info(f"The list is {l}")
print(l)