# Копия tests_12_2 с замороженными тестами для модуля suite_12_3


import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        # cls.is_frozen = False

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runer_1 = rt.Runner('Усэйн', 10)
        self.runer_2 = rt.Runner('Андрей', 9)
        self.runer_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = rt.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn4(self):
        """
        Дополнительный тест, выявляющий ошибку алгоритма start класса Tournament
        Ошибка заключается в том, что удаление объекта из списка participants может
        происходить до того, как будет обработан весь цикл и для каждого объекта будет
        запущен метод participant.run()
        :return: None
        """
        turn_4 = rt.Tournament(6, self.runer_1, self.runer_2, self.runer_3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn4'] = result


    if __name__ == '__main__':
        unittest.main()
