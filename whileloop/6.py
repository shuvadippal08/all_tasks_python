import logging

logging.basicConfig(
    filename="LoginAttempts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True,
)

logging.info("Program started")

username = 'shuvadip'
password = '1324'

uname = input("Enter the username:  ")
logging.info(f"Entered username: {uname}")

if uname == username:
    logging.info("Username matched")

    passwd = ""
    i = 1

    while i <= 3:
        passwd = input("Enter the password:  ")
        logging.info(f"Password attempt {i}")

        if passwd == password:
            logging.info("Login successful")
            print("You have successfully logged in")
            break
        else:
            logging.warning(f"Wrong password on attempt {i}")

            if i == 3:
                logging.error("Too many failed attempts")
                print("Too many attempts")
                break

        i += 1

else:
    logging.warning("Wrong username entered")
    print("Wrong username")

logging.info("Program ended")