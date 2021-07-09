import pytest


def create_txt():
    file = open("file.txt", "w")
    
def write_txt():
    with open("file.txt","w") as file:
        file.write("This is the first time I am creating a file txt in python")

def test_create_txt():
    expected = create_txt()
    assert expected == True
