import urllib.request
import re

urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Eru33hgf3nbNUXfzhKbXX_TEoS7sYGzFx2fDST_a-tdV24g04_JE6nXAdNeYz3MVZ2jsIqXnvdfxwu6b7LyhskcCv3dusk-E-tD8Jn1FqA-PjKlJAo_7zU1ZZeOGwZZFpbWeyCVzQuAZh3-3qiUxHIAel9jWlui7lRY0_vakN3krg9SH3NbVqaG_FAPJmpjUxi1b",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgclL7cA8nNJ-gL8zKV1L1OxXLaTmM7qOrY_Y3zMESll2WctGd9Vdnj0IIKKX15hOjIbS6_ddbyiq4TKRbNaGBpRnB_kwA-1pgercM_e0aWbfMcXnjxVfwJ9UA-6YFP0aLjVHVDPTMql2Ju4UeloSDSx_z65X-ihjqWpZpLdhqntaRk8CCJrLjDEJjw5TzahGStci4Wx404ZU=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjR2TbujxR20PTTfw6ZF3XJ2odx-COApW15LVyNdXazI-11lhja_vYHr1_iozbbrhLO6xI8my0Os7wlylb2rA66ph3ywFE0X8cKqUvU7BzTohsT3p4mouzix8="
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        final_url = res.geturl()
        print("Final URL:", final_url)
        # Extract ID (last segment after hyphen or slash)
        # unpslash slugs are like /photos/title-XXXXX
        photo_id = final_url.split('/')[-1].split('-')[-1]
        print("Candidate ID:", photo_id)
    except Exception as e:
        print("Error following redirect:", e)
