import json
import logging
from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import find_min, find_max, calculate_average


def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")

def main():

    folder = Path(__file__).parent
    logs_folder = folder / "logs"
    logs_folder.mkdir(exist_ok=True)

    try:
        with open(folder / "config.json", encoding="utf-8") as file:
            config = json.load(file)

        logging.basicConfig(
            filename=folder / config["log_file"],
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            encoding="utf-8"
        )

        logging.info("Программа запущена")

        file_path = folder / config["input_file"]

        print("Рабочая папка:", Path.cwd())
        print("Файл существует:", file_path.exists())

        numbers = read_numbers(file_path)

        validate_numbers(numbers)

        logging.info("Прочитано значений: %s", len(numbers))

        print("\nРезультаты измерений:")
        print("Количество:", len(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
        print("Среднее:", calculate_average(numbers))

        logging.info("Обработка завершена успешно")

    except FileNotFoundError:
        print("Ошибка: файл не найден")
        logging.error("Файл не найден")

    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print("Ошибка:", error)
        logging.error("Ошибка: %s", error)

    finally:
        print("Работа программы завершена")
S
if __name__ == "__main__":
    main()