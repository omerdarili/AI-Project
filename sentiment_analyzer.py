from transformers import pipeline

try:
    print("Türkçe duygu analizi modeli yükleniyor...")
    classfier = pipeline('sentiment-analysis', model='savasy/bert-base-turkish-sentiment-cased')
    print("---model başarıyla yükledi---")
except Exception as e:
    print("!!! MODEL YÜKLENİRKEN BİR HATA OLUSTU !!!")
    classfier = None

def analyze_sentiment(text):
    """
    -Verilen metnin duygu analizini yapar,
    Args:
        text(str): analiz edilecek metin,
    returns:
        dict: Modelin etiket ve skor iceren sonuc sözlüğü,
            model yüklenmemişse none döner.    
    """   
    if classfier is None:
        return {"label": "HATA,", "score": 0.0, "error": "Model yüklenemedi."}

    try:
        #gelen metni modele verip sonucu alıyoruz.
        return classfier(text)[0]
    except Exception as e:
        return {"label": "HATA", "score": 0.0, "eroor": str(e)}


    #bu blok dosya dogrudan calıstırıldıgında test amaclı yazılmıstır
    if __name__ == '__main__':
        test_text = "Bu filmi izlerken çok keyif aldım, harikaydı"
        result = analyze_sentiment(test_text)
        print(f"Test Metni: '{test_text}'")
        print(f"Analiz Sonucu: {result}")

        test_text_2 = "Ürün kalitesi beklediğimden kötü çıktı beklentimi karşılamadı"
        result_2 = analyze_sentiment(text_text_2)
        print(f"Test Metni: '{test_text_2}'")
        print(f"Analiz Sonucu: {result_2}")
        

        "" 
