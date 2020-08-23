class SignUp():
    def __init__(self, name, password ):
        self.name = name
        self.password = password
        self.store = dict()
        
    def successSignUp(self):
        self.store = dict()
        self.store[self.name] = self.password
        print(self.store)
    
    def login(self):
        username = input("Enter your username:\n" )
        password = input("Enter your password:\n" )
        if username == self.store(0) and password ==  in self.store:
            print("Login success") 


        
# new = SignUp("Harsh", "123")
# new.successSignUp
# # print("Your SignUp is successful", new.name, "and your password is", new.password)
# new.successSignUp()
# new.login()