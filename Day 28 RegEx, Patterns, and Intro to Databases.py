import re

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    for N_itr in range(N):
        first_name, email_id = input().rstrip().split()

        # Regex to match a valid gmail address
        if re.search(r'[a-z]+@gmail\.com$', email_id):
            gmail_users.append(first_name)

    # Sort the list alphabetically and print each name on a new line
    for name in sorted(gmail_users):
        print(name)
