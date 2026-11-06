with open('assets/css/responsive.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("Last 1000 chars of responsive.css:")
print(text[-1000:])
