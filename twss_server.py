import web
import twsslib
        
urls = (
    '/blah', 'blah',
    '/(.*)', 'hello'
)


app = web.application(urls, globals())

class hello:
    twss = twsslib.TextClassifier()
    twss.train()


    def GET(self, text):
        return self.twss.is_positive(text)

class blah:
    def GET(self):
        return 'hello'



if __name__ == "__main__":
    app.run()
