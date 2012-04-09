import web
import json
import twsslib
from web import form

render = web.template.render('templates/')

myform = form.Form(
    form.Textbox('query'),
)
        
urls = (
    '/train/(.*)', 'train',
    '/query/(.*)', 'query',
    '/', 'index',
)

app = web.application(urls, globals())
twss = twsslib.TextClassifier()
try:
    twss.load()
except:
    twss.train()
    twss.save()

class query:
    def GET(self, text):
        return 'Not implemented yet.'


class query:
    def GET(self, text):
        try:
            return json.dumps(twss.is_positive(text))
        except:
            return json.dumps(False)

class index:
    def GET(self):
        form = myform()
        return render.inputform(form=form, istwss=None)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.inputform(form)
        else:
            try:
                istwss = twss.is_positive(form.query.value)
            except:
                istwss = False
            
            return render.inputform(form=form, istwss=istwss)


if __name__ == '__main__':
    app.run()
