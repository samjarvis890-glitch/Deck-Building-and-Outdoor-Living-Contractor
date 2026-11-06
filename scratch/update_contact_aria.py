with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<a href="contact.html" class="nav-link-item active">Contact</a>',
    '<a href="contact.html" class="nav-link-item active" aria-current="page">Contact</a>'
).replace(
    '<a href="contact.html" class="drawer-link active">Contact</a>',
    '<a href="contact.html" class="drawer-link active" aria-current="page">Contact</a>'
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated contact.html aria-current successfully!")
