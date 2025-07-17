from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def ana_sayfa():

    return "Merhaba, Flask Dünyası!"

@app.route('/islem')
def islem_yap():

    gelen_metin = request.args.get('metin', 'Herhangi bir metin girilmedi')

    sonuc = gelen_metin.upper()

    return f"""
       <h1>İslem Sayfasi</h1>
       <p> URL'den gelen orijinal metin: <strong>{gelen_metin}</strong></p>
       <p>İslem sonucu (Büyük Harf): <strong>{sonuc}</strong></p>
       <hr>
       <p><em>URL'nin sonuna "?metin=istediğin_bir_sey" ekleyerek deneme yapilabilir.</em></p>
    """   

if __name__ == '__main__':
    app.run(debug=True)
