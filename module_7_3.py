
class WordsFinder:
    punctuation = (',','.','=','!','?',';',' - ','\n')
    file_names = []
    def __init__(self,*file_names_args):
        for filename in file_names_args:
            self.file_names.append(filename)
                
    def get_all_words(self):
        all_words = {}
        for f_name in self.file_names:
            with open(f_name,'r',encoding = 'utf-8') as cur_file:
                cur_line = cur_file.read().lower()
                for symbol in self.punctuation:
                    cur_line = cur_line.replace(symbol,' ')
                cur_list = cur_line.split()
                all_words[f_name] = cur_list   
        return all_words

    
    def find(self,word):
        all_words = self.get_all_words()
        sample = word.lower()
        sample_dict = {}
        for f_name in all_words.keys():
            i = 1
            for dict_word in all_words[f_name]:
                if sample == dict_word:
                    sample_dict[f_name] = i
                    break
                else:
                    i += 1
        return sample_dict

    def count(self,word):
        all_words = self.get_all_words()
        sample = word.lower()
        count_dict = {}
        for (f_name,f_words) in all_words.items():
            i = 0
            for dict_word in all_words[f_name]:
                 if sample == dict_word:
                     i += 1
            count_dict[f_name] = i
        return count_dict

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))    

         
             
        
