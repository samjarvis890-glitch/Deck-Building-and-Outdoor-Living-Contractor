from PIL import Image, ImageStat

with Image.open("assets/images/services/services-final-cta.webp") as img:
    stat = ImageStat.Stat(img)
    print("Mean RGB of services-final-cta.webp:", stat.mean[:3])

with Image.open("assets/images/about/about-hero.webp") as img:
    stat = ImageStat.Stat(img)
    print("Mean RGB of about-hero.webp:", stat.mean[:3])

with Image.open("assets/images/about/about-lifestyle.webp") as img:
    stat = ImageStat.Stat(img)
    print("Mean RGB of about-lifestyle.webp:", stat.mean[:3])

with Image.open("assets/images/services/services-hero.webp") as img:
    stat = ImageStat.Stat(img)
    print("Mean RGB of services-hero.webp:", stat.mean[:3])
