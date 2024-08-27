# conftest.py

# # Bootstrapping
# def pytest_addhooks(pluginmanager):
#     print()
#     print("_________________________pytest_addhooks: Добавляем свои хуки")
#
# # Инициализация
# def pytest_configure(config):
#     print()
#     print("_________________________pytest_configure: Настройка завершена")
#
# # Сбор тестов
# def pytest_collection_modifyitems(session, config, items):
#     print()
#     print("_________________________pytest_collection_modifyitems: Сбор тестов завершен")
#     # Изменяем порядок тестов:
#     items.reverse()
#
# # Выполнение тестов
# def pytest_runtest_setup(item):
#     print()
#     print(f"_________________________pytest_runtest_setup: Подготовка к тесту {item.name}")
#
# # Репортинг
# def pytest_report_header(config):
#     print()
#     return "_________________________pytest_report_header: Заголовок отчета"
