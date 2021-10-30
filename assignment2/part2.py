#Computing Summary Statistics

#Top 10 words in the text file


from mediawiki import MediaWiki
import re
import string

def choc():
    """Pulls the chocolate cake webpage data from wikipedia and turns it into a txt file."""
    wikipedia = MediaWiki()
    choc_cake = wikipedia.page("Chocolate_cake") # cake must be lowercase
    print(choc_cake.title)
    output = choc_cake.content
    with open('choc_cake.txt', 'w') as f: #this extracts data from the wikipedia page and writes it as a txt file
        f.write(output)

def most_frequent():
    "Opens choc_cake.txt file and then finds and counts the most frequent words of all the words given in the document with a range from 3-15 characters, all of them lowercase. Then stores words as a dictionary so keys can be printed with the frequency from most to least frequent. "
    f = open('choc_cake.txt', 'r')
    text_string = f.read().lower() #turns all capital letters into lowercase to count easier
    frequency = {} 
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string) #this uses the re module to scan all the words in the txt file using boundary.All words will have a character length in between 3 and 15.
    
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1 
    
    frequency_list = frequency.keys() 

    for words in frequency_list:
        print(words, frequency[words])

    # for freq, words in frequency[0:20]:
    #     print(words, '\t', freq)

def  main():
    # choc()
    most_frequent() 


if __name__ == "__main__":
    main()
    



    