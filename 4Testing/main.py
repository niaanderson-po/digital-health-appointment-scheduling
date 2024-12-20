import re 

# Question 1: -----------------------------------
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
      
def check_email(email):  
    if (re.search(regex,email)):
        return True
    else:
        return False
      
def check_psw_upper(psw):
    result = False
    for char in psw:
        if char.isupper():
            result = True
            break
    return result

    #condensed: result = any(char.isupper() for char in psw)
def check_psw_digit(psw):
    result = False
    for char in psw:
        if char.isdigit():
            result = True
            break
    return result

    #condensed: result = any(char.isdigit() for char in psw)
def check_psw_lower(psw):
    result = False
    for char in psw:
        if char.islower():
            result = True
            break
    return result

    #condensed: result = any(char.islower() for char in psw)
def check_psw(psw):
    if(check_psw_digit(psw)
            and check_psw_upper(psw)
            and check_psw_lower(psw)
            and len(psw) >= 8):
        print("Valid password")
        return True
    else:
        print("Invalid password")    
        return False     

# New functions: ------------------------------------
def check_psw_equal(psw1, psw2):
    return psw1 == psw2

def check_credentials(email, psw1, psw2):
    return check_email(email) and check_psw(psw1) and check_psw_equal(psw1,psw2)