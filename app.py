from flask import Flask, request, render_template
from sentiment_analyzer import analyze_sentiment

app = Flask(__name__)

# ana sayfa ('/') isteği geldiğinde, index.html dosyasını render edip kullanıcıya gösteriyoruz
@app.route('/')
def home():
    return render_template('index.html')

# html formundan '/analyze' adresine bir POST isteği geldiğinde bu fonksiyon çalışacak
@app.route('/analyze', methods=['POST'])
def analyze():
    
    #formdaki 'text_to_analyze' isimli textarea'dan gelen metni alıyoruz
    text = request.form['text_to_analyze']

    #eğer metin boşsa, kullanıcıyı uyaran bir mesaj gönderiyoruz
    if not text:
        return render_template('result.html', text="Boş metin gönderdiniz.", label="HATA", score=0)
    
    #gelen metni duygu analizi fonksiyonumuza gönderiyoruz
    result = analyze_sentiment(text)

    #sonucu göstermek için 'result.html' sablonunu kullanıyoruz.
    #bu sablona analiz edilen metni ve sonucu parametre olarak gönderiyouz.
    return render_template('result.html', text=text, label=result['label'], score=result['score'])

if __name__ == '__main__':
    app.run(debug=True)


