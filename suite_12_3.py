import unittest as un
import tests_12_3 as t3


test_suite = un.TestSuite()
test_suite.addTest(un.TestLoader().loadTestsFromTestCase(t3.RunnerTest))
test_suite.addTest(un.TestLoader().loadTestsFromTestCase(t3.TournamentTest))
test_runer = un.TextTestRunner(verbosity=2)
test_runer.run(test_suite)
