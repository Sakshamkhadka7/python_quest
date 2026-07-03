class ValidationSystem:
    def validate_name(self, name):
        if name.strip() == "":
            return False, "Name cannot be empty."
        elif len(name) < 3:
            return False, "Name must be at least 3 characters."
        return True, "Valid Name."

    def validate_age(self, age):
        if not age.isdigit():
            return False, "Age must be a number."

        age = int(age)

        if age < 18:
            return False, "Age must be at least 18."

        return True, "Valid Age."

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            return False, "Invalid email format."

        return True, "Valid Email."

    def validate_password(self, password):
        if len(password) < 8:
            return False, "Password must contain at least 8 characters."

        return True, "Valid Password."


class UserRegistration:
   
    def __init__(self):
        self.validator = ValidationSystem()

    def register(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        validations = [
            self.validator.validate_name(name),
            self.validator.validate_age(age),
            self.validator.validate_email(email),
            self.validator.validate_password(password)
        ]

        print("\nValidation Result")
        print("-----------------------")

        success = True

        for status, message in validations:
            print(message)
            if not status:
                success = False

        if success:
            print("\nRegistration Successful!")
        else:
            print("\nRegistration Failed!")



obj = UserRegistration()
obj.register()
