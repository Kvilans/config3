import unittest
from parser import TomlToCustomLanguage


class TestTomlToCustomLanguage(unittest.TestCase):
    def setUp(self):
        self.parser = TomlToCustomLanguage()

    def test_simple(self):
        toml_input = 'name = "test"'
        result = self.parser.parse(toml_input)
        self.assertEqual(result, '(define name "test");')

    def test_numbers(self):
        toml_input = 'number = 42'
        result = self.parser.parse(toml_input)
        self.assertEqual(result, "(define number 42);")

    def test_array(self):
        toml_input = 'values = [1, 2, 3]'
        result = self.parser.parse(toml_input)
        self.assertEqual(result, "(define values '( 1 2 3 ));")

    def test_nested(self):
        toml_input = """
        [section]
        key1 = "value1"
        key2 = 42
        """
        result = self.parser.parse(toml_input)
        expected = '(define section { key1 = "value1"; key2 = 42 });'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
