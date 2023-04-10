def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    emails = dict()

    for line in handle:
        line = line.rstrip()
        if line.startswith("From"):
            if len(line.split()) > 2:
                words = line.split()
                email=words[1]
                if email not in emails:
                    emails[email] = 1
                else:
                    emails[email] += 1
    
    bigcount = None
    em = None
    for aaa, bbb in emails.items():
        if bigcount is None or bbb > bigcount:
            em = aaa
            bigcount = bbb

    print(em, bigcount)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
