with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update desktop active link
text = text.replace(
    '<a href="faq.html" class="nav-link-item active">FAQ</a>',
    '<a href="faq.html" class="nav-link-item active" aria-current="page">FAQ</a>'
)

# Update drawer active link
text = text.replace(
    '<a href="faq.html" class="drawer-link active">FAQ</a>',
    '<a href="faq.html" class="drawer-link active" aria-current="page">FAQ</a>'
)

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated faq.html aria-current attributes successfully!")
