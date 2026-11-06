def read_numbers(file_path):
    numbers = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip():
                try:
                    numbers.append(float(line))
                except ValueError:
                    raise ValueError(f"Ошибка в строке {line_number}")

    return numbers
