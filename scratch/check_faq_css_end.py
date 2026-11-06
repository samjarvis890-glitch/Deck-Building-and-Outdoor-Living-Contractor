with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("Last 1500 chars of faq.css:")
print(text[-1500:])
