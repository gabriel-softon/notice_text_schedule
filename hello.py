import mysql.connector
import os
from dotenv import load_dotenv
import schedule
import time
from services.PageContentFetcher import PageContentFetcher

load_dotenv()

def find_empty_notice_text():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
    )

    cursor = conn.cursor()

    cursor.execute("SELECT id, URL FROM TB_NOTICIA_RASPADA WHERE TEXTO_NOTICIA IS NULL LIMIT 100")
    results = cursor.fetchall()

    fetcher = PageContentFetcher()

    for linha in results:
        id_noticia, url = linha
        print(f"Processando URL: {url}")

        try:
            texto_noticia = fetcher.fetch(url)
            
            if texto_noticia:
                update_query = "UPDATE TB_NOTICIA_RASPADA SET TEXTO_NOTICIA = %s WHERE id = %s"
                print('Texto:', texto_noticia)
                
                cursor.execute(update_query, (texto_noticia, id_noticia))
                conn.commit()
                print(f"Texto da notícia inserido na notícia de id: {id_noticia}")
            else:
                print(f"Não foi possível extrair o texto para o id {id_noticia}")
        except Exception as e:
            print(f"Erro ao processar o id {id_noticia}: {e}")
            continue

    cursor.close()
    conn.close()

def main():
    print("Hello from text-schedule!")
    find_empty_notice_text()

schedule.every(5).hours.do(main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
