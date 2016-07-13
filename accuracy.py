import homework5 as hw5
import unittest
import timeit
from os import listdir

class TestSudoku(unittest.TestCase):
    
    def test_most_indicative_spam(self):
        sf = hw5.SpamFilter("./train/spam",
        "./train/ham", 1e-5);
        spam_dir = './dev/spam'
        ham_dir = './dev/ham'
        spam_paths = ['./dev/spam' + '/' + sfile for sfile in listdir(spam_dir)]
        ham_paths = ['./dev/ham' + '/' + hfile for hfile in listdir(ham_dir)]

        spam_count = 0;
        ham_count = 0;

        s_result = [1 if sf.is_spam(s_file) else 0 for s_file in spam_paths]
        h_result = [1 if not sf.is_spam(h_file) else 0 for h_file in ham_paths]

        print "Accuracy spam:{}".format(sum(s_result)*0.5);
        print "Accuracy ham:{}".format(sum(h_result)*0.5);
        print "Accuracy overall:{}".format((sum(s_result)+sum(h_result))*.25);

if __name__ == '__main__':
    unittest.main()

