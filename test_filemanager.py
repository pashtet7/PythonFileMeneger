import pytest
import os
import shutil
from console_file_manager import list_folders, list_files, os_info, creator_info

# Фикстура для создания тестовой директории
@pytest.fixture(scope="function")
def setup_test_directory():
    test_dir = "test_directory"
    os.mkdir(test_dir)
    yield  # После выполнения теста удаляем папку
    shutil.rmtree(test_dir)

@pytest.fixture(scope="function")
def setup_test_files():
    filenames = ["test1.txt", "test2.txt"]
    for filename in filenames:
        with open(filename, "w") as f:
            f.write("Test data")
    yield  # После выполнения теста удаляем файлы
    for filename in filenames:
        os.remove(filename)

# Тест для list_folders
def test_list_folders(setup_test_directory, capsys):
    list_folders()  # Выводим список папок
    captured = capsys.readouterr()  # Перехватываем вывод
    assert "test_directory" in captured.out  # Проверяем, что папка есть в выводе

# Тест для list_files
def test_list_files(setup_test_files, capsys):
    list_files()  # Выводим список файлов
    captured = capsys.readouterr()  # Перехватываем вывод
    assert "test1.txt" in captured.out
    assert "test2.txt" in captured.out

# Тест для os_info (проверяем, что вывод не пустой)
def test_os_info(capsys):
    os_info()
    captured = capsys.readouterr()
    assert "Операционная система" in captured.out

# Тест для creator_info
def test_creator_info(capsys):
    creator_info()
    captured = capsys.readouterr()
    assert "Программа создана пользователем" in captured.out