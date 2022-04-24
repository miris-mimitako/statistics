import jinja2
from jinja2 import Template, Environment, FileSystemLoader
import json

class HtmlGenerator():
    def __init__(self) -> None:
        pass

    def html_writer(self):
        # Read template
        env = Environment(loader=FileSystemLoader('template/statistics/', encoding='utf8'))
        tmpl = env.get_template('test.j2') # set your templates


        params = {
            "shop_name": "雑貨屋",
            "item": "お皿",
            "price": "200"
        }

        # rendering and output HTML
        rendered_html = tmpl.render(params)
        with open('results/html/result.html', 'w',encoding="utf-8") as f:
            f.write(rendered_html)


    def __del__(self):
        pass


if __name__=="__main__":
    HG = HtmlGenerator()
    test = HG.html_writer()
    del HG

