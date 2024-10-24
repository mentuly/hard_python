# цей код буде використовуватися тільки у rle_compressor.py бо у тому коді як раз і створюється клас який буде стискати та розпаковувати pylin.txt

from abc import ABC, abstractmethod

class compressor(ABC): # абстрактний клас, що визначає інтерфейс для стиснення та розпакування

    @abstractmethod
    def compress(self, data: str) -> str: # метод що стискає данні
        pass

    @abstractmethod
    def decompress(self, data: str) -> str: # метод що розпаковує данні
        pass