from nltk import tokenize


def create_txt():
    file = open("file.txt", "w")
    
def write_txt(message):
    create_txt()
    with open("file.txt","w") as file:
        file.write(message)
def read_txt():
    with open("file.txt", "r") as file:
        print (file.read())
def key_words():
    with open("file.txt","r") as file:
        read_file = file.read()
        total_words = 0
        if "time" in read_file:
            total_words += 1
        return total_words

message = "This is the first time I am creating a txt file in python"
write_txt(message)
read_txt()
message = "This is the first time I am editing a txt file in python"
write_txt(message)
read_txt()
print(key_words())
