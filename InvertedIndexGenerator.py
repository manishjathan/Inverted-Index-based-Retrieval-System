import TextProcessor


#doc0 = "Hello there, How are you doing today? The weather is great and Python is awesome. The Sky is pinkish-blue. You should not eat CardBoard."
#doc1 = "Hello Everyone, I am Learning Python. I am working on an inverted index table to understand retrieval systems."

#doc_list = []
#doc_list.append(doc0)
#doc_list.append(doc1)


token_list = [] # Tokens obtained after tokenizing
filtered_sentence_list = []
normalized_token_list = []



#To print the List conatining Token tuple and each tuple contains (token,document index)
def print_token_tuple_list(token_tuple_list):
    for token in token_tuple_list:
        print(token)

#To sort tokens by alphabetical order
def sort_by_tokens(token_tuple):
    return token_tuple[0]

# Below function creates a mapping of the tokens with the docID
#It makes use of the functions written in TextProcessor to perform textProcessing
#Uses the final Stemmed tokens to create map

def create_token_tuples(doc_list):
    token_tuple_list = []
    count = 0  # Count refers to the index of the document
    for documents in doc_list:

         token_list = TextProcessor.generate_tokens(documents)
         filtered_sentence_list = TextProcessor.remove_stop_words(token_list)
         normalized_token_list = TextProcessor.stem(filtered_sentence_list)

         for each in normalized_token_list:
             if([each.lower(),count] not in token_tuple_list):
                token_tuple_list.append([each.lower(),count])

         count += 1
    return token_tuple_list


#print_token_tuple_list(token_tuple_list)


def create_posting_lists(token_tuple_list):
    dict = {}
    for token in token_tuple_list:
        if(token[0] not in dict.keys()):
            dict[token[0]] = [token[1]]
        else:
            dict[token[0]].append(token[1])

    #for keys in dict:
    #    print(keys,dict[keys])
    return dict





