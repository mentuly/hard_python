import sys
import unittest
# імпорт класів
from compression.checksum import checksum_handler
from compression.file_handler import file_handler
from compression.rle_compressor import rle_compressor
from compression.unittest.unittest import test_rle_compressor
# імпорт логування
from utils.utils import setup_logging, log_info, log_error, validate_file_extension 

def test():
    # функція для запуску юніттесту
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test_rle_compressor)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)

def main(file_path: str):
    # основна функція для стиснення файлів
    # логування
    setup_logging() # ініціалізація логування

    # перевірка щоб убідитись чи є цей файл взагалі
    if not validate_file_extension(file_path, ".txt"): # validate_file_extension - перевіряє наявність фалу і ця функція
        log_error("Invalid file extension. Please provide a .txt file.")
        sys.exit(1)
    log_info(f"Reading file: {file_path}")

    # зчитування pylint.txt
    file_content = file_handler.read_file(file_path)

    # стиснення
    compressor = rle_compressor()
    compressed_data = compressor.compress(file_content)
    compressed_file_path = file_path + ".rle"  # зміна розширення на .txt.rle
    file_handler.write_file(compressed_file_path, compressed_data)
    log_info(f"File compressed and saved to: {compressed_file_path}") # вивід у термінал що файл створений і записаний як (у нашому випадку буде) pylint.txt.rle

    # вивід контрольної оцінки
    original_checksum = checksum_handler.calculate_checksum(file_content)
    compressed_checksum = checksum_handler.calculate_checksum(compressed_data)
    log_info(f"Original checksum: {original_checksum}") # вивидення оцінки оригінального файлу
    log_info(f"Compressed checksum: {compressed_checksum}") # вивидення оцінки зжатого файлу

    # тут вивід скільки байтів є і у якого файлу
    original_size = len(file_content)
    compressed_size = len(compressed_data)
    log_info(f"Original file size: {original_size} bytes") # вага оригінального файлу
    log_info(f"Compressed file size: {compressed_size} bytes") # вага стисненного файлу

if __name__ == "__main__":
    # запускаємо тест на початку для перевірки а вже потім сам файл
    test()

    # якщо передано аргумент з файлом то запускаємо основну функцію якщо ж ні то повідомляємо про помилку
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]
        main(input_file_path)
    else:
        print("Usage: python main.py <path_to_text_file>")
        sys.exit(1)