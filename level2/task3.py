import re
def password_strength(password):
  if len(password) < 8:
    return "Weak"
  if not any(char.isupper() for char in password):
    return "Weak"
  if not any(char.islower() for char in password):
    return "Weak"
  if not any(char.isdigit() for char in password):
    return "Weak"

  regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
  if(regex.search(password) == None):
    return "Weak"
  return "Strong"

pw = input("enter the password : ")
chek=password_strength(pw)
print(chek)