### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    # Class variable to store emails
    inbox = []

    def __init__(self, email_address, subject_line, email_content):
        # Instance variables for emails
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        # Method to mark an email as read
        self.has_been_read = True

# --- Functions --- #

def populate_inbox():
    """Function to populate inbox with sample emails."""
    # Adding sample emails to the inbox
    Email.inbox.append(Email("john@example.com", "Welcome to HyperionDev!", "Dear student, welcome to our platform."))
    Email.inbox.append(Email("peter@example.com", "Great work on the bootcamp!", "Congratulations on your progress."))
    Email.inbox.append(Email("boris@example.com", "Your excellent marks!", "You scored exceptionally well in the last exam."))

def list_emails():
    """Function to list emails in the inbox."""
    print("Inbox:")
    for index, email in enumerate(Email.inbox):
        # Determine if the email has been read or not
        status = "Unread" if not email.has_been_read else "Read"
        print(f"{index}: {email.subject_line} - {status}")

def read_email(index):
    """Function to read an email and mark it as read."""
    if 0 <= index < len(Email.inbox):
        email = Email.inbox[index]
        print("\nEmail Details:")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print("Content:")
        print(email.email_content)
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
    else:
        print("Invalid index. Please enter a valid index.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Main menu loop
while True:
    user_choice = input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: ''')

    if user_choice == '1':
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
    elif user_choice == '2':
        print("Unread Emails:")
        for email in Email.inbox:
            if not email.has_been_read:
                print(email.subject_line)
    elif user_choice == '3':
        print("Exiting application.")
        break
    else:
        print("Oops - incorrect input.")
