import web
import twsslib
        
urls = (
    '/train/(.*)', 'train',
    '/query/(.*)', 'query',
    '/', 'index',
)


app = web.application(urls, globals())
twss = twsslib.TextClassifier()
twss.train()

class query:
    def GET(self, text):
        return 'Not implemented yet.'


class query:
    def GET(self, text):
        if text.strip() == '':
            print 'Welcome!'
        
        try:
            return twss.is_positive(text)
        except:
            return False

class index:
    def GET(self):
        return 'Welcome!'



if __name__ == '__main__':
    app.run()
