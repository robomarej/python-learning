names=["james", "john", 'jack']
email_domains=['gmail', 'hotmail', 'yahoo']

zipped = zip(names, email_domains)

for i,j in zipped:
    print(i,j)
