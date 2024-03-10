import logging

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt as e:
        print("\nexiting")
        logging.exception()
    finally:
        logging.exception()