from icrawler.builtin import GoogleImageCrawler
import os
import shutil
import time

base_dir = "novo_dataset/cookies"

if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir)

palavras_chave = [
    "cookie com gotas de chocolate",
    "biscoito com gotas de chocolate",
    "cookie americano",
    "homemade chocolate chip cookie",
    "chocolate chip cookie close-up",
    "crispy chocolate chip cookie",
    "gooey chocolate chip cookie",
    "fresh baked chocolate chip cookies",
    "macro shot chocolate chip cookie"
]

for palavra in palavras_chave:
    pasta = os.path.join(base_dir, palavra.replace(" ", "_"))
    os.makedirs(pasta, exist_ok=True)

    crawler = GoogleImageCrawler(storage={'root_dir': pasta})
    crawler.crawl(
        keyword=palavra,
        max_num=150,
        filters={'size': 'large'},
        file_idx_offset=0
    )

    time.sleep(3)  # evita bloqueio pelo Google

print("[INFO] Download concluído!")