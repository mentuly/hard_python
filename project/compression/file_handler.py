# клас для роботи з фалами
class file_handler: # клас який виконує основні операції з файлами
    @staticmethod # метод що позначає що не треба йому атрибутів, в ньому буде читання файлу
    def read_file(file_path: str) -> str: # шлях до файлу рядком
        with open(file_path, 'r') as file: # відкриття файлу в режимі читання тому написанно 'r'
            return file.read() # читає вміст файлу

    @staticmethod # метод що позначає що не треба йому атрибутів, в ньому буде проходити запис pylint.txt.rle
    def write_file(file_path: str, data: str) -> None: # записання радка даних у файл
        with open(file_path, 'w') as file: # відкриття файлу в режимі писання тому написанно 'w' 
            file.write(data) # пише у файлі