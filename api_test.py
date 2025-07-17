import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

print("istek gönderilen url:",{})

try:
    #isteği gönderiyoruz
    response = requests.get(url)

    #sunucudan cevap gelip gelmediğini kontrol et
    response.raise_for_status()

    #istek başarılıysa gelen json verisini alıyoruz
    data = response.json()
    print("Veri Başariyla Cekildi!")

    #gelen veriyi ekrana basma
    print(json.dumps(data, indent=4))

    #belirli verileri çekme
    user_id = data['userId']
    title = data['title']
    completed = data['completed']
    
    print("Cekilen Verinin Detaylari")
    print(f"Kullanici ID: {user_id}")
    print(f"Baslik: {title}")
    print(f"Tamamlandı mı?: {completed}")

except requests.exceptions.RequestException as e:
    print(f"Bir hata olustu: {e}")
