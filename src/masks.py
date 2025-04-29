def get_mask_card_number(number: int = None) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    number_str = str(number)
    if len(number_str) == 16 and len(number_str) > 0 and number_str.isdigit():
        mask_number = number_str[:4] + " " + number_str[4:6] + ("*" * 2 + " " + "*" * 4) + " " + number_str[12:]
        return mask_number


def get_mask_account(account: int = None) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску. """
    account_str = str(account)
    if len(account_str) == 20 and len(account_str) > 0 and account.isdigit():
        mask_account = ("*" * 2) + account_str[-4:]
        return mask_account


if __name__ == "__main__":
    number = input("Введите номер карты: ")
    print(get_mask_card_number(number))
    account = input("Введите номер счета: ")
    print(get_mask_account(account))
