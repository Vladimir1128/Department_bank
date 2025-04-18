def get_mask_card_number(number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    number_str = str(number)
    mask_number = number_str[:4] + " " + number_str[4:6] + ("*" * 2 + " " + "*" * 4) + " " + number_str[12:]
    return mask_number


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. """
    account_str = str(account)
    mask_account = ("*" * 2) + account_str[-4:]
    return mask_account


if __name__ == "__main__":
    number = int(input("Введите номер карты: "))
    print(get_mask_card_number(number))
    account = int(input("Введите номер счета: "))
    print(get_mask_account(account))
