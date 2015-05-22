

import webapp2
import cgi

form = """
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%s</textarea>
      <br>
      <input type="submit">
    </form>
 """
class MainHandler(webapp2.RequestHandler):

    def scape_html(self,txt):
        return cgi.escape(txt,quote = True)

    def encrypt(self,txt):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        #text = txt.lower()
        result =""

        for i in txt:

            uppercase = False
            if i.isupper():
                alphabet = alphabet.upper()
                uppercase = True

            if i not in alphabet:
                result += i
            else:
                if i == "n" or i == "N":
                    result += alphabet[0]
                else:
                    ini_position = alphabet.find(i)
                    if (ini_position+13) >26:
                        res = 26 - ini_position
                        result += alphabet[13-res]
                    else:
                        result += alphabet[ini_position+13]
            if uppercase:
                alphabet = alphabet.lower()

        return result

    def get(self):
        self.response.write(form % '')

    def post(self):

        text = self.encrypt(self.request.get('text'))
        self.response.write(form % self.scape_html(text))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
