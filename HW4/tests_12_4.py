# Домашнее задание по теме "Логирование"
# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно
# скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если
# передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие
# параметры:
# 1. Уровень - INFO
# 2. Режим - чтение
# 3. Название файла - runner_tests.log
# 4. Кодировка - UTF-8
# 5. Формат вывода - на своё усмотрение, обязательная информация: уровень логирования,
# сообщение логирования.
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте отрицательное значение в speed.
# 3. В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте его на
# уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте что-то кроме строки в name.
# 3. В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте его на
# уровне WARNING с сообщением "Неверный тип данных для объекта Runner".

import rt_with_exceptions as runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run_1 = runner.Runner('Бегун_1', speed=-5)
            for _ in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner. {err.args}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run_2 = runner.Runner(['Бегун_2'])
            for _ in range(10):
                run_2.run()
            self.assertEqual(run_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner. {err.args}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            run_1 = runner.Runner('Бегун_1')
            for _ in range(10):
                run_1.walk()
            run_2 = runner.Runner('Бегун_2')
            for _ in range(10):
                run_2.run()
            self.assertNotEqual(run_1.distance, run_2.distance)
            logging.info('"test_challenge" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner.', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logging.info('Старт тестирования')

if __name__ == '__main__':
    unittest.main()
