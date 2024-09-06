import logging
import pytest

# @pytest.fixture(scope='session', autouse=True)
# def configure_logging():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         handlers=[
#             logging.FileHandler("test_log.log"),  # Запись логов в файл
#             logging.StreamHandler()  # Вывод логов в консоль
#         ]
#     )


# def test_example_loging():
#     logger = logging.getLogger("test_example")
#     logger.info("Запуск теста")
#     step_result = 1 + 1
#     logger.info(f"Результат первого шага: {step_result}")
#     assert step_result == 2
#     logger.info("Тест завершён успешно")


class TestExample:


    def setup_method(self, method):
        print(f"Настройка для теста {method.__name__}")
        # код для подготовки перед тестом

    def test_one(self, request: pytest.FixtureRequest):
        print(f"Тест 1 {request.node.name}")
        print(request.cls.my)

    def test_two(self, request: pytest.FixtureRequest):
        print(f"Тест 2 {request.function.__name__}")