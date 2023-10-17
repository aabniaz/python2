import re

def validate_emails(num, emails):
    pattern = r'[\w\.-]+@hackerrank\.com'
    all_emails = re.findall(pattern, emails)
    sorted_emails = sorted(all_emails, key=lambda x: (x.split('@')[0], x))
    result_emails = sorted_emails[:num]
    return result_emails

if __name__ == "__main__":
    num = int(input().strip())
    emails = ""
    for _ in range(num):
        email = input().strip()
        emails += email + " "
    result = validate_emails(num, emails)
    print(result)
