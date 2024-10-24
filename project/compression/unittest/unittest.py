import unittest
from compression.rle_compressor import rle_compressor

class test_rle_compressor(unittest.TestCase): # unittest.TestCase означає що це тестовий випадок тому у терміналі буде писати спочатку test_ а потім вже назву перевірки
    # перевірка алгоритму RLE стиснення та розпакування

    def setUp(self): # self використовується всередині класів для позначення поточного екземпляра класа
        self.compressor = rle_compressor() # цей метод setUp використовується перед кожним тестом і створений для налаштування обєктів

    def test_compress(self): # self використовується всередині класів для позначення поточного екземпляра класа
        # перевіркка функції стиснення
        self.assertEqual(self.compressor.compress("abb"), "ab2") # перевірка чи правильно стиснувся рядок

    def test_decompress(self): # self використовується всередині класів для позначення поточного екземпляра класа
        # перевіркка функції розпаковки
        self.assertEqual(self.compressor.decompress("ab2"), "abb") # перевірка чи правильно розпакувався рядок

    def test_full_cycle(self): # self використовується всередині класів для позначення поточного екземпляра класа
        data = "abb" # так сказать вхідний рідок
        compressed = self.compressor.compress(data) # ситснення
        decompressed = self.compressor.decompress(compressed) # розпакування
        self.assertEqual(decompressed, data) # це перевірка чи відповідає оригінальний рядок, рядку після розпакування

if __name__ == "__main__":
    unittest.main() # запуск тестів