with open('faq.html', 'rb') as f:
    b = f.read(1000)
    print("CRLF present:", b'\r\n' in b)
