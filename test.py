import homework5 as hw5
import unittest
import timeit

class TestSudoku(unittest.TestCase):
    def test_load_tokens(self):
        ham_dir = "./train/ham/";
        spam_dir = "./train/spam/";
        self.assertEquals(['of', 'my', 'outstanding', 'mail'],hw5.load_tokens(ham_dir + 'ham1')[200:204]);
        self.assertEquals(['for', 'Preferences', '-', "didn't"],hw5.load_tokens(ham_dir + 'ham2')[110:114]);
        self.assertEquals(['You', 'are', 'receiving', 'this'],hw5.load_tokens(spam_dir + 'spam1')[1:5]);
        self.assertEquals(['<html>', '<body>', '<center>', '<h3>'],hw5.load_tokens(spam_dir + 'spam2')[:4]);
        

    def test_log_probs(self):
        paths = ["./train/ham/ham%d" % i
                for i in range(1, 11)]        
        probs =  hw5.log_probs(paths, 1e-5)
        self.assertAlmostEqual(-3.6080194731874062, probs["the"],places = 15);
        self.assertAlmostEqual(-4.272995709320345, probs["line"], places = 14);

        paths = ["./train/spam/spam%d" % i
                for i in range(1, 11)]
        p = hw5.log_probs(paths, 1e-5)
        self.assertAlmostEqual(-5.837004641921745, p["Credit"],delta = .0000000001);
        self.assertAlmostEqual(-20.34566288044584, p["<UNK>"]);

    def test_init(self):
        nb = hw5.SpamFilter( './train/spam', './train/ham', 1e-5);
    
    #def test_is_spam(self):
    #    sf = hw5.SpamFilter( './train/spam', './train/ham', 1e-5);
    #    self.assertTrue(sf.is_spam("./train/spam/spam1"));
    #    self.assertTrue(sf.is_spam("./train/spam/spam2"));
    #    self.assertFalse(sf.is_spam("./train/ham/ham1"));
    #    self.assertFalse(sf.is_spam("./train/ham/ham2"));
    
    def test_most_indicative_spam(self):
        sf = hw5.SpamFilter("./train/spam",
        "./train/ham", 1e-5);
        self.assertEquals(['<a', '<input', '<html>', '<meta','</head>']\
        ,sf.most_indicative_spam(5))
        
        self.assertEquals(['Aug', 'ilug@linux.ie', 'install', 'spam.', 'Group:'],\
        sf.most_indicative_ham(5))
if __name__ == '__main__':
    unittest.main()

