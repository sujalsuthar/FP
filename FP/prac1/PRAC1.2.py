import datetime

def submit_form():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    submission_time = datetime.datetime.now()

    
    print("\nForm Submitted Successfully!")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Form submitted at: {submission_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    submit_form()