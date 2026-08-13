# We can define our OWN exceptions in program
# used for Projects for Business related failures/error conditions


# this is how we define the custom exception on top of python's Exception
class AgeInvalidForVoting(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def voting(user_dict):
    # if user_dict['age'] < 18:
    #     print(f"User: {user_dict['name']} can not vote!")
    #     return 

    if user_dict['age'] < 18:
        # raise Exception(f"User: {user_dict['name']} can not vote!")
        # raise ValueError(f"User: {user_dict['name']} can not vote!")
        raise AgeInvalidForVoting(f"User: {user_dict['name']} can not vote!")
    
    print(f"User: {user_dict['name']} voting goes to: {user_dict['party']}" )

user1 = {
    "name": "Preshaan",
    "party": "Congress",
    "age": 17,
}

user2 = {
    "name": "Abhijit",
    "party": "AAP",
    "age": 27,
}

try:
    voting(user1)
except AgeInvalidForVoting as err:
    print(f"Error for user1 is: {err}")

try:
    voting(user2)
except:
    pass
