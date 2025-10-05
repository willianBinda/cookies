import cv2
import glob
import matplotlib.pyplot as plt
from skimage.feature import blob_log
from skimage.color import rgb2gray
from skimage import io
import numpy as np
import os
from skimage import exposure
import shutil

diretorio = "resultados"
diretorio2 = "resultados2"
diretorio3 = "resultados3"

# recria diretórios
for d in (diretorio, diretorio2, diretorio3):
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)


for filename in glob.glob("imagens/*.*"):
    imagem = cv2.imread(filename)
    if imagem is None:
        continue

    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    # === Detectar círculo principal (cookie) ===
    circles = cv2.HoughCircles(
        gray_blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=30,
        minRadius=20,
        maxRadius=300
    )
    if circles is None:
        print(f"Nenhum círculo detectado em {filename}")
        continue

    circles = np.uint16(np.around(circles))
    x, y, r = circles[0][0]

    # Criar máscara circular
    mask = np.zeros_like(gray)
    cv2.circle(mask, (x, y), r, 255, -1)

    # Recortar cookie
    cookie_crop = imagem[y-r:y+r, x-r:x+r]
    mask_crop = mask[y-r:y+r, x-r:x+r]

    # Fundo branco
    fundo_branco = np.ones_like(cookie_crop, dtype=np.uint8) * 255
    cookie_final = np.where(mask_crop[..., None] == 255, cookie_crop, fundo_branco)

    name = os.path.basename(filename)
    cv2.imwrite(f"{diretorio}/{name}", cookie_final)

    # === Resultado 2: normalizar em cinza ===
    gray_cookie = cv2.cvtColor(cookie_final, cv2.COLOR_BGR2GRAY)
    norm = cv2.normalize(gray_cookie, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(f"{diretorio2}/{name}", norm)


    # === Analisar pixels claros/escuros ===


    bin_dark = np.uint8(norm <= 100) * 255  # 0=claro, 255=escuro


    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    cleaned = cv2.morphologyEx(bin_dark, cv2.MORPH_OPEN, kernel)  # remove pequenos ruídos


    norm_custom = np.where(cleaned==255, norm, 0)  # aqui usamos norm original


    norm_custom[norm_custom == 255] = 0
    norm_custom[norm_custom >= 100] = 0


    cv2.imwrite(f"{diretorio3}/{name}", norm_custom)
    np.savetxt(f"{diretorio3}/{name}_pixels.txt", norm_custom, fmt="%3d")

    