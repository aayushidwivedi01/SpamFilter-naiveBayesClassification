############################################################
# CIS 521: Homework 5
############################################################

student_name = "Aayushi Dwivedi"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email
from collections import Counter, defaultdict
from math import log, exp
from os import listdir
############################################################
# Section 1: Spam Filter
############################################################


def load_tokens(email_path):
    fo = open(email_path, 'r');
    message = email.message_from_file(fo);
    tokens = [token for line in email.iterators.body_line_iterator(message)\
            for token in line.split()];
    return tokens;      
    

def log_probs(email_paths, smoothing):
    tokens = [token for email_path in email_paths for token in load_tokens(email_path)];
    total_count = len(tokens);
    prob_w = Counter(tokens);
    vocab_len = len(prob_w);
    log_probs = dict((word, log(count + smoothing) - log(total_count + smoothing *(vocab_len + 1)))\
                for word, count in prob_w.iteritems());
    log_probs['<UNK>'] = log(smoothing) - log(total_count + smoothing *(vocab_len + 1));
    
    return log_probs
class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        spam_paths = [spam_dir + '/' + sfile for sfile in listdir(spam_dir)]
        ham_paths = [ham_dir + '/' + hfile for hfile in listdir(ham_dir)]

        self.log_probs_spam = log_probs(spam_paths, smoothing);
        self.log_probs_ham = log_probs(ham_paths, smoothing);
        self.p_spam = log(len(spam_paths) / float(len(spam_paths) + len(ham_paths)));
        self.p_ham = log(1 - self.p_spam);
    
    def is_spam(self, email_path):
        words = load_tokens(email_path);
        prob_spam = self.p_spam;
        prob_ham = self.p_ham;    
        for word in words:
            if word in self.log_probs_spam:
                prob_spam +=  self.log_probs_spam[word];
            else:
                prob_spam += self.log_probs_spam["<UNK>"];

            if word in self.log_probs_ham:
                prob_ham +=  self.log_probs_ham[word];
            else:
                prob_ham +=  self.log_probs_ham["<UNK>"];

        if prob_spam > prob_ham:
            return True;
        else:
            return False;

    
    def most_indicative_spam(self, n):
        indicative_prob = dict((word,exp(log_prob)/(exp(log_prob) + exp(self.log_probs_ham[word]))) \
            for word, log_prob in self.log_probs_spam.iteritems() \
            if word in self.log_probs_ham)
        return [word for word, log_prob in sorted(indicative_prob.items(),\
                 key = lambda (k,v):v, reverse = True)][:n]
                
    def most_indicative_ham(self, n):
        indicative_prob = dict((word,exp(log_prob)/(exp(log_prob) + exp(self.log_probs_spam[word]))) \
            for word, log_prob in self.log_probs_ham.iteritems() \
            if word in self.log_probs_spam)
        return [word for word, log_prob in sorted(indicative_prob.items(),\
                 key = lambda (k,v):v, reverse = True)][:n]

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
5hrs
"""

feedback_question_2 = """
The homework was overall pretty straightforward.
No stumbling blocks.
"""

feedback_question_3 = """
Was a simple homework. Would have liked if
it was a bit more challenging.
"""
