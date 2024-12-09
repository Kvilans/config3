import argparse
import sys
from parser import TomlToCustomLanguage


def main():
    parser = argparse.ArgumentParser(description="CLI для преобразования TOML в учебный конфигурационный язык.")
    args = parser.parse_args()

    try:
        input_data = sys.stdin.read()
        converter = TomlToCustomLanguage()
        result = converter.parse(input_data)
        print("Результат:")
        print(result)
    except ValueError as ve:
        print(f"Ошибка синтаксиса: {ve}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
