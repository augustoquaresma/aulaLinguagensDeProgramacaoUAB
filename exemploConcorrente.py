import threading
import time
import random

# Função que simula o download de um arquivo
def baixar_arquivo(nome, tempo_download):
    print(f"Iniciando download: {nome}")
    time.sleep(tempo_download)  # simula tempo de rede
    print(f"Download concluído: {nome} (levou {tempo_download} segundos)")

if __name__ == "__main__":
    # Lista de arquivos a serem baixados
    arquivos = [
        ("Livro_POO.pdf", random.randint(2, 5)),
        ("Geoprocessamento_QGIS.zip", random.randint(2, 5)),
        ("Banco_de_Dados_PostgreSQL.mp4", random.randint(2, 5)),
        ("Paradigmas_de_Programacao.docx", random.randint(2, 5)),
    ]

    threads = []

    print("\n--- Iniciando downloads concorrentes ---")

    # Criando uma thread para cada download
    for nome, tempo in arquivos:
        thread = threading.Thread(target=baixar_arquivo, args=(nome, tempo))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    print("\nTodos os downloads foram concluídos!")
