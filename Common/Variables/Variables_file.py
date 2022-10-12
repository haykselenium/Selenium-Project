class VariablesClass:
    __username = "testcaseselenium123321@gmail.com"
    __password = "Test123321"
    searchText = "iphone"
    amazonSignInUrl = "https://www.amazon.com/gp/sign-in.html"

    @classmethod
    def get_username(cls):
        return cls.__username

    @classmethod
    def get_password(cls):
        return cls.__password
