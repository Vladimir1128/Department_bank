import logging

mask_card_number_logger = logging.getLogger("app.mask_number")
mask_account_logger = logging.getLogger("app.mask_account")
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
mask_card_number_logger.addHandler(file_handler)
mask_card_number_logger.setLevel(logging.DEBUG)
mask_account_logger.addHandler(file_handler)
mask_account_logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: int | str | None) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    mask_card_number_logger.info("Starts work!")
    try:
        number_str = str(number)
        if len(number_str) == 16 and len(number_str) > 0 and number_str.isdigit():
            mask_number = number_str[:4] + " " + number_str[4:6] + ("*" * 2 + " " + "*" * 4) + " " + number_str[12:]
            mask_card_number_logger.info("Program works correctly!")
            return mask_number
        else:
            mask_card_number_logger.warning("Unsuccessful  program termination!")
    except Exception as e:
        mask_card_number_logger.error(f"An error occurred!: {e}", exc_info=True)
    finally:
        mask_card_number_logger.info("Completion of work!")


def get_mask_account(account: int | str | None) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску."""
    mask_account_logger.info("Starts work!")
    try:
        account_str = str(account)
        if len(account_str) == 20 and len(account_str) > 0 and account_str.isdigit():
            mask_account = ("*" * 2) + account_str[-4:]
            mask_account_logger.info("Program works correctly!")
            return mask_account
        else:
            mask_account_logger.warning("Unsuccessful  program termination!")
    except Exception as e:
        mask_account_logger.error(f"An error occurred!: {e}", exc_info=True)
    finally:
        mask_account_logger.info("Completion of work!")


if __name__ == "__main__":
    number = input("Введите номер карты: ")
    print(get_mask_card_number(number))
    account = input("Введите номер счета: ")
    print(get_mask_account(account))
