class PasswordManager:
    def __init__(self, initial_password):
        self.old_passwords = [initial_password]

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return "Password changed successfully"
        else:
            return "Please choose a different password"

    def is_correct(self, input_password):
        return input_password == self.get_password()
        
password_manager = PasswordManager("Initial123")
current_password = password_manager.get_password()
print("Current password:", current_password) 
print(password_manager.is_correct("Initial123")) 
print(password_manager.is_correct("NewPassword456"))
