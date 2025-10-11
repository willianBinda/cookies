Utilizado um modelo de visão computacional com yolo. Para realizar a contagem e detecção das gotas de chocolare de um ou varios cookies.

# processos utilizados.

1. Scrapping das imagens de cookies pegas do google imagens.

- Diretório `/scrapping`

2. Adição de labels para 25 imagens extraidas utilizando a ferramento labelImage do projeto `https://github.com/HumanSignal/labelImg.git`

3. Divisão do dataset entre treino e validação tanto as imagens quanto as labels para o treinamento com yolo.

4. Criação do modelo yolov8n.pt e trinamento baseado no dataset.

- resultado e metricas do modelo estão no diretório `/yolo_novo_dataset` ou `/yolo_chocolate`. Foram treinados 2 modelos um com um dataset de 25 imagens e outro com 150 imagens.

# Utilização

1. Projeto criado com virtualenv

2. Colocar as imagens no diretório `/input`

3. Resultado crido no diretório `/runs/detect`

4. Rodar o arquivo main para realizar as previsões.
