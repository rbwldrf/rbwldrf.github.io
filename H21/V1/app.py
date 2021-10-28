import flask as f
import random as r

textalisti = [
    "In three words I can sum up everything I've learned about life: it goes on.",
    "Two wrongs don't make a right, but they make a good excuse.",
    "I love deadlines. I love the whooshing noise they make as they go by.",
    "Dashed hopes and good intentions. Good, better, best, bested.",
    "It's said your life flashes before your eyes before you die. It's true, it's called Life.",
]

app = f.Flask(__name__)

#aðalsíða
@app.route('/')
def main_index():

    # aðalsíða, static texti og mynd

    a = f.render_template('hello.html', ttl = "hæ :)")

    return a

#fylgisíða 1
@app.route('/b1/')
def quote_and_pic():    

    # sækja random streng úr textalista
    # sækja random mynd frá picsum.photos

    quote = r.choice(textalisti)

    a = f.render_template('quote.html', ttl = "Tilvísun dagsins", quote = quote, img = "https://picsum.photos/1280/720")
    
    return a


#fylgisíða 2
@app.route('/b2/')
# catch-all sem færir allt sem fylgir b2 yfir á þessa síðu
@app.route('/b2/<path:a>')
def name_thingy(a=None):

    #sækja hluta hlekks sem fylgir eftir /b2/
    #prenta það sem sótt er í hlekk á síðunni
    
    wtf = f.request.path[4:]

    a = f.render_template('name.html', ttl = "Kveðja", name = wtf, img = "https://picsum.photos/1280/720")

    return a

if __name__ == "__main__":
    app.run(debug=True)