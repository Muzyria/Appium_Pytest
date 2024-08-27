import logging
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    log_file = "test_log.log"

    # Очистка файла перед началом тестов
    if os.path.exists(log_file):
        with open(log_file, 'w'):
            pass  # Открываем файл в режиме записи, чтобы очистить его

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  # Настраиваем формат даты и времени
    )

    # Обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Обработчик для вывода в файл
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Логирование настроено")


