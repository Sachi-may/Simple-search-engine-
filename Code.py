'''You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool'''

def matchingWords(sen1,sen2):
    matchings=0
    words1=sen1.split(" ")
    words2=sen2.split(" ")
    for w1 in words1:
        for w2 in words2:
            if w1.lower()==w2.lower():
                matchings+=1
    return matchings
if __name__ == '__main__':
    Sentences=["Python is a very good language","My name is sachi shome","Sachi is learning python","He is trying his best","Gg"]
    user_search=input("Please enter your search\n")
    matches=[matchingWords(user_search,sentence) for sentence in Sentences]
    sortedMatchesSentences=[i for i in sorted(zip(matches,Sentences),reverse=True)]

    print(f"{len(sortedMatchesSentences)} Results found\n")
    for match,item in sortedMatchesSentences:
        print(f"\"{item}\" : with {match} number of matches")
