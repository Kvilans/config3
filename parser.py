import toml


class TomlToCustomLanguage:
    def __init__(self):
        self.constants = {}

    def parse(self, toml_input):
        try:
            data = toml.loads(toml_input)
            return self._to_custom_language(data)
        except toml.TomlDecodeError as e:
            raise ValueError(f"Ошибка парсинга TOML: {e}")

    def _to_custom_language(self, data):
        result = []
        for key, value in data.items():
            result.append(self._process_key_value(key, value))
        return "\n".join(result)

    def _process_key_value(self, key, value):
        if isinstance(value, dict):
            return f"(define {key} {{ {self._process_dict(value)} }});"
        elif isinstance(value, list):
            return f"(define {key} '( {self._process_array(value)} ));"
        elif isinstance(value, str):
            return f'(define {key} "{value}");'
        elif isinstance(value, (int, float, bool)):
            return f"(define {key} {str(value).lower()});"
        else:
            raise ValueError(f"Неподдерживаемое значение: {value}")

    def _process_array(self, array):
        return " ".join([self._format_value(item) for item in array])

    def _process_dict(self, dictionary):
        return "; ".join([f"{key} = {self._format_value(value)}" for key, value in dictionary.items()])

    def _format_value(self, value):
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, (int, float, bool)):
            return str(value).lower()
        elif isinstance(value, list):
            return f"'( {self._process_array(value)} )"
        elif isinstance(value, dict):
            return f"{{ {self._process_dict(value)} }}"
        else:
            raise ValueError(f"Неподдерживаемое значение: {value}")
