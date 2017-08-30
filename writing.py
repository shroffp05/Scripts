import math
def clean_text(txt):
        """ takes a string of text 'txt' as a parameter and returns
            a list containing the words in txt after it has been
            'cleaned'.
        """
        lst=[]
        txt= txt.lower()                 #converts the text into lower case letters
        new_txt=txt.split(' ')
        
        for w in range(len(new_txt)):                 #loops over each character in the txt.
            
            if new_txt[w] in '.,!?/:;()-_':          #checks if the character is a punctuation.
                
                new_txt[w]=new_txt[w].replace(new_txt[w],'')    #converts the punctuation into an empty string.
                
            lst+=[new_txt[w]]                       #adds the stirng into a list.
            
        return lst
#function 
def sample_file_write(filename):
    """ A function that demonstrates how to write a
        Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()

#function 
def sample_file_read(filename):
    """ A function that demonstrates how to read a
        Python dictionary form a file.
    """
    f = open(filename, 'r')   # Open for reading.
    d_str = f.read()          # Read in a string that represents a dict.
    f.close()        

    d = dict(eval(d_str))     # Converts the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def stem(s):
        """ accpets a string as a parameter and returns the stem s."""
        if len(s)>=4:
                if s[-3:] == 'ing':            
                        if s[-4] == s[-5]:
                                s=s[:-4]
                        if s[-4] == 'y':
                                s=s[:-4]+'i'
                        else:
                                s=s[:-3]
                elif s[-2:] == 'er':
                        if s[-4] == s[-5]:
                                s=s[:-4]
                        else:
                                s=s[:-2]

                elif s[-1] == 'y':
                        s=s[:-1]+'i'
                        
                elif s[-3:] == 'ies':
                        s=s[:-3]+'i'

                elif s[-1] == 'e' or s[-1]=='s':
                        if s[-4:] == 'ness':
                                if  s[-7:] == 'fulness':
                                        s=s[:-7]
                                else:
                                        s=s[:-4]
                        elif s[-3:] == 'ers':
                                s=s[:-3]
                        else:
                                s=s[:-1]

                elif s[-3:] == 'ful':
                        s=s[:-3]

                
        else:
                s=s
                
        return s

def compare_dictionaries(d1,d2):
        """ takes two feature dictionaries as inputs,
            and it should compute and return their log
            similarilty score.
        """
        score=0
        total=0
        for w in d1:
               total += d1[w]     # Uses a for loop to calculate the total number of elements in the dicitonary d1
                                  # using running sum
        for word in d2:
               if word in d1:
                       score+=round(math.log((d1[word]/total))*(d2[word]),3) #Calculates the sum of the log of the probability of a word occuring in the d1 dictionary
                                                                             #Multiplied by the number of times it occurs in d2
               else:
                        score+=round(math.log((0.5/total))*(d2[word]),3) 

        return score
    
class TextModel:
    #This class will model a body of text.
    #function 1
    def __init__(self, model_name):
        """ constructs a new Text Model object by accepting
               a string 'model_name' as a parameter.
        """

        self.name=model_name #a string that is a label for the text model.

        self.words={}        # creates a new dictionary that stores unique words
        
        self.word_lengths={} # creates a new dictionary that stores lenght of words
        
        self.stems={}               # A Dictionary that records the number of times each word
                               # stem appears.
                               
        self.sentence_lengths={}    # A Dicitonary that records the number of times each sentence
                               # length appears.

        self.no_of_punctuation={}   # A Dictionary that recoreds the number of times a punctuation
                               # appears.

    #function 2
    def __str__(self):
        """ return a string that includes the name of the model
            as well as the sizes of the dictionaries for each
            featur of the text.
        """
        s = 'text model name:'+' '+self.name+'\n'
        s += 'number of words:'+' '+ str(len(self.words))+'\n'
        s += 'number of word lengths:'+' '+ str(len(self.word_lengths))+'\n'
        s += 'number of stems:' + ' '+ str(len(self.stems))+'\n'
        s += 'number of sentence lengths:' + ' '+ str(len(self.sentence_lengths))+'\n'
        s += 'number of punctuations:' + ' '+ str(len(self.no_of_punctuation))

        return s

    #function3
    def add_string(self, s):
        """ adds a string of text 's' to the model by augmenting the
            feature defined in the constructor.
        """
        sent_word=s.split(' ')  
        count=1
        for w in range(len(sent_word)):
                if sent_word[w][-1] in '.!?':     # Checks if the last charcater is a period, exclamation or question mark
                                                
                        if count not in self.sentence_lengths:  
                                self.sentence_lengths[count]=1  # Adds a unique sentence length into the dictionary
                                count=0
                        else:
                                self.sentence_lengths[count]+=1 # Adds 1 to a non-uniques sentence length into the dicitonary
                                count=0
                count+=1

        for w in range(len(sent_word)):
                if sent_word[w][-1] in ".':;,!?":   #Checks if the last character is a punctuation mark
                        
                        if sent_word[w] not in self.no_of_punctuation:
                                self.no_of_punctuation[sent_word[w][-1]]=1 # Adds a unique punctuation mark into the dicitionary
                        else:
                                self.no_of_punctuation[sent_word[w][-1]]+=1 # Adds 1 to a non-unique punctuation mark into the dicitonary
                                
        words = clean_text(s) # 'Cleans' the text.

        for w in words:
                if w not in self.words:
                        self.words[w] = 1  # Adds a unique word to the dicitonary
                else:
                        self.words[w] += 1 # Adds 1 to a non-unique word
        for w in words:
                if len(w) not in self.word_lengths:
                        self.word_lengths[len(w)]=1 # Adds a unique word length to the dicitonary
                else:
                        self.word_lengths[len(w)]+=1 #Adds 1 to a non-unique word_length 
        for w in words:
                if stem(w) not in self.stems:
                        self.stems[stem(w)]=1
                else:
                        self.stems[stem(w)]+=1

    #function4
    def add_file(self, filename):
        """ adds all of the text in the file identified by 'filename'
            to the model.
        """

        f = open(filename, 'r', encoding='utf8', errors='ignore') #opens the file and reads it

        count=1
        text=f.read()
        f.close()
        
        sent_word=text.split(' ')
        for w in range(len(sent_word)):
                if '\n' in sent_word[w]:
                        sent_word[w]=sent_word[w].replace('\n',' ')
        
        for w in range(len(sent_word)):
                if '.' in sent_word[w]:     # Checks if the last charcater is a period, exclamation or question mark
                                                
                        if count not in self.sentence_lengths:  
                                self.sentence_lengths[count]=1  # Adds a unique sentence length into the dictionary
                                count=1
                        else:
                                self.sentence_lengths[count]+=1 # Adds 1 to a non-uniques sentence length into the dicitonary
                                count=1
                count+=1

        for w in range(len(sent_word)):
                if ',' in sent_word[w] or ':' in sent_word[w] or '.' in sent_word[w] or '?' in sent_word[w] or \
                   "!" in sent_word[w] or ';' in sent_word[w]:   #Checks if the last character is a punctuation mark
                        
                        if sent_word[w] not in self.no_of_punctuation:
                                self.no_of_punctuation[sent_word[w][-1]]=1 # Adds a unique punctuation mark into the dicitionary
                        else:
                                self.no_of_punctuation[sent_word[w][-1]]+=1 # Adds 1 to a non-unique punctuation mark into the dicitonary
        for line1 in sent_word:
                words = clean_text(line1) # 'Cleans' the text.
                
        for w in words:
                if w not in self.words:
                        self.words[w] = 1  # Adds a unique word to the dicitonary
                else:
                        self.words[w] += 1 # Adds 1 to a non-unique word
        for w in words:
                if len(w) not in self.word_lengths:
                        self.word_lengths[len(w)]=1 # Adds a unique word length to the dicitonary
                else:
                        self.word_lengths[len(w)]+=1 #Adds 1 to a non-unique word_length 
        for w in words:
                if stem(w) not in self.stems:
                        self.stems[stem(w)]=1
                else:
                        self.stems[stem(w)]+=1

        
        
        

    #function 6
    def save_model(self):
        """ Saves the TextModel object for self by writing its various
            feature dictionaries to files.
        """
        filename1= self.name + '_' + 'words'+'.txt' # creates a filename
        filename2= self.name + '_' + 'word_lengths'+'.txt'
        filename3= self.name + '_' + 'stems'+'.txt'
        filename4= self.name + '_' + 'sentence_lengths'+'.txt'
        filename5= self.name + '_' + 'punctuations'+'.txt'
        
        f = open(filename1, 'w') #opens the file
        f.write(str(self.words)) # writes to the file the contents of that dicitionary
        f.close()
        
        f1 = open(filename2, 'w') 
        f1.write(str(self.word_lengths))
        f1.close()
        
        f = open(filename3, 'w') 
        f.write(str(self.stems))
        f.close()
        
        f = open(filename4, 'w') 
        f.write(str(self.sentence_lengths)) 
        f.close()
        
        f = open(filename5, 'w') 
        f.write(str(self.no_of_punctuation)) 
        f.close() 

    #function 7
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel
            object form their files and assigns them to the attributes
            of the called TextModel.
        """

        filename1=self.name+ '_' + 'words'+'.txt'
        filename2=self.name+ '_' + 'word_lengths'+'.txt'
        filename3= self.name + '_' + 'stems'+'.txt'
        filename4= self.name + '_' + 'sentence_lengths'+'.txt'
        filename5= self.name + '_' + 'punctuations'+'.txt'
        
        f = open(filename1, 'r')
        d_str = f.read() #reads the content of the file and stores it in d_str

        f.close()

        d=dict(eval(d_str)) # converts the string into a dictionary
        
        self.words=d

        f = open(filename2, 'r')
        d_str2 = f.read()
        f.close()

        d1=dict(eval(d_str2))

        self.word_lengths=d1

        f = open(filename3, 'r')
        d_str3 = f.read()
        f.close()

        d2=dict(eval(d_str3))

        self.stems=d2
        
        f = open(filename4, 'r')
        d_str4 = f.read()
        f.close()

        d3=dict(eval(d_str4))

        self.sentence_lengths=d3
        
        f = open(filename5, 'r')
        d_str5 = f.read()
        f.close()

        d4=dict(eval(d_str5))

        self.no_of_punctuation=d4


    def similarity_scores(self, other):
            lst=[]
            
            word=compare_dictionaries(other.words, self.words)
            
            word_len=compare_dictionaries(other.word_lengths, self.word_lengths)
            
            stem=compare_dictionaries(other.stems, self.stems)
            
            sentence_len=compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
            
            punct=compare_dictionaries(other.no_of_punctuation,self.no_of_punctuation)
            
            lst=[word]+[word_len]+[stem]+[sentence_len]+[punct]   # Concatenates all the scores in the list lst
            
            return lst

    def classify(self, source1, source2):
            scores1= self.similarity_scores(source1)
            scores2= self.similarity_scores(source2)
            
            print('scores for' + ' '+ source1.name +':'+ str(scores1))
            print('scores for' + ' '+ source2.name +':'+ str(scores2))

            weighted_sum1= (len(self.words)*scores1[0])+(len(self.word_lengths)*scores1[1])+ \
                           (len(self.stems)*scores1[2])+(len(self.sentence_lengths)*scores1[3])+\
                           (len(self.no_of_punctuation)*scores1[4])

            weighted_sum2= (len(self.words)*scores2[0])+(len(self.word_lengths)*scores2[1])+ \
                           (len(self.stems)*scores2[2])+(len(self.sentence_lengths)*scores2[3])+\
                           (len(self.no_of_punctuation)*scores2[4])

            if weighted_sum1>weighted_sum2:
                    print(self.name + ' is more likely to have come form ' + source1.name)
            else:
                    print(self.name + ' is more likely to have come form ' + source2.name)
                        

def test():
        """ Compares two text models"""
        source1= TextModel('source1')
        source1.add_string('It is interesting that she is interested.')

        source2=TextModel('source2')
        source2.add_string('I am very, very excited about this!')

        mystery = TextModel('mystery')
        mystery.add_string('Is he interested? No, but I am.')

        mystery.classify(source1,source2)

# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def run_tests():
        """ Compares articles from different newspapers"""
        source1 = TextModel('Times_Of_India')
        source1.add_file('Times_of_India.txt')
        source1.save_model()

        source2 = TextModel('New_York_Times')
        source2.add_file('New_York_Times.txt')
        source2.save_model()

        new1 = TextModel('Boston_Globe')
        new1.add_file('Boston_Globe.txt')
        new1.classify(source1, source2)
        new1.save_model()

        # Add code for three other new models below.

        new2 = TextModel('BostonUniv')
        new2.add_file('BU_News.txt')
        new2.classify(source1,source2)
        new2.save_model()

        new3 = TextModel('NY_Art')
        new3.add_file('NY_Article.txt')
        new3.classify(source1,source2)
        new3.save_model()

        new4 = TextModel('TOI_Art')
        new4.add_file('TOI_Article.txt')
        new4.classify(source1,source2)
        new4.save_model()
