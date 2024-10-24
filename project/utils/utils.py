# логування треба для того щоб перевірити правильності розширення файлу і якщо все буде ок то воно пропустить якщо ні то видасть помилку

import logging

def setup_logging():
    # цей весь код на 10 строці буде показувати 
    # logging.basicConfig це база для конфігурації логування
    # level = logging.INFO,  встановлення рівня повідомлення для логування на INFO тобто інформацію
    # format = '%(asctime)s - %(levelname)s - %(message)s' формат логування повідомлення час у форматі рік-місяць-день далі години:хвилини:секунди, мілісекунди - INFO - і вже потім повідомлення
    logging.basicConfig( level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

# помилка у логуванні
def log_error(message: str):
    logging.error(message)

# логування для повідомлення з інформацією
def log_info(message: str):
    logging.info(message)

# попередження логування
def log_warning(message: str):
    logging.warning(message)

# перевірка наявності потрібного розширення для файлу
def validate_file_extension(file_path: str, extension: str) -> bool:
    return file_path.endswith(extension)