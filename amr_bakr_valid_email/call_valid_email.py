from module.vali_email2 import check_email

while True:
    email = input("enter your email address: ").strip()
    result = check_email(email)
    print(result)

    if "Valid" in result:
        break  
    else:
        print("pls try again.\n")
