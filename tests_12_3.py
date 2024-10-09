import runner as rn
import runner_and_tournament as rat
import unittest as un


class RunnerTest(un.TestCase):
    is_frozen = False

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        run1 = rn.Runner('Пешеход')
        print('test_walk:', run1.name)
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run2 = rn.Runner('Бегун')
        print('test_run:', run2.name)
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        run1 = rn.Runner('Черепаха')
        run2 = rn.Runner('Заяц')
        print(f'test_challenge: {run2} (run) VS {run1} (walk)')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)


class TournamentTest(un.TestCase):
    is_frozen = True

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def setUp(self):
        self.runner1 = rat.Runner('Усейн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)
        self.runner4 = rat.Runner('Эдисон', 15)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def tearDown(self):
        self.runner_name = []
        self.place = 0
        self.check_results = {}
        full_speed = [runner.speed for runner in self.results.values()]
        for runners in self.results.values():
            self.runner_name.append(runners)
            for speed in full_speed:
                if runners.speed >= speed:
                    self.runner_name += runners.name
            self.place += 1
            self.check_results[self.place] = runners.name
        self.assertEqual(self.check_results, self.results, False)
        self.assertTrue(self.check_results == self.results, True)
        self.assertEqual(self.check_results, self.results)
        self.all_results.update(self.check_results)
        print('Результат забега:', self.all_results)

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run1(self):
        print('\033[31m1 забег:\033[0m')
        self.tournament = rat.Tournament(90, self.runner1, self.runner3)
        self.results = self.tournament.start()

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run2(self):
        print('\033[33m2 забег:\033[0m')
        tournament = rat.Tournament(90, self.runner3, self.runner2)
        self.results = tournament.start()

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run3(self):
        print('\033[32m3 забег:\033[0m')
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.results = tournament.start()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    un.main()
