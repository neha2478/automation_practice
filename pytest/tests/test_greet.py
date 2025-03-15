def greet(person):
    return "Hi {name}". format(**person)

def test_greet():
    bob = {"name": "bob"} #Arrange
    greeting = greet(bob) #Act
    assert greeting == "Hi bob" #Assert

#here we can take user input ..
#here we work in Arrange , Act , Assert 