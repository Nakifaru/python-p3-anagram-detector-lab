class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, tester_list):
        self.tester_list = tester_list

        sorted_word_letters = sorted([letter for letter in self.word])
        matched_word = []
    
        for tester in tester_list:
            sorted_tester_letters = sorted([letter for letter in tester])
            if sorted_word_letters == sorted_tester_letters:
                matched_word.append(tester)
        return matched_word
    
Anagram("enlist").match(["listen", "poison", "hello"])

        


