import funcitons_for_selection as ffs
import work_with_json
import text_colors


def main() -> None:
    data = work_with_json.read_json_file("./requisites/data_for_selection_card.json")
    target_hash = data["hash"]
    last_numbers = data["last_numbers"]
    bin_numbers = data["BIN gazprombank mastercard debit"]

    number_card = ffs.Check_cumber_of_card(target_hash, last_numbers, bin_numbers, 16)
    find_card = number_card.find_number_of_card()
    if find_card:
        print(f"Номер подобранной карты: {text_colors.COLOR_GREEN}{find_card}{text_colors.COLOR_RESET}")
    else:
        print(f"{text_colors.COLOR_RED}Номер карты не получилось подобрать{text_colors.COLOR_RESET}")


if __name__ == "__main__":
    main()
