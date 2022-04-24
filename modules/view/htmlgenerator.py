import jinja2
from jinja2 import Template, Environment, FileSystemLoader
import json


class HtmlGenerator():
    def __init__(self) -> None:
        self.params = {"parameter": [
            {"title": "", "img_src": "", "comment": ""}]}

    def add_params(self):
        # debug only
        self.params["parameter"][0]["title"] = "test_title"
        self.params["parameter"][0]["img_src"] = r"../../results/tmp/20220422_test/mimitako.png"
        self.params["parameter"][0]["comment"] = "test_comment"
        ##E debug

    def html_writer(self):
        # Read template
        env = Environment(loader=FileSystemLoader(
            'template/statistics/', encoding='utf8'))
        tmpl = env.get_template('test.j2')  # set your templates

        NN = self.add_params() # debug only

        # rendering and output HTML
        set_data = self.params["parameter"]
        rendered_html = tmpl.render(set_data = set_data, html_title = "this title")
        with open('results/html/result.html', 'w', encoding="utf-8") as f:
            f.write(rendered_html)
        ##E def html_writer

    def __del__(self):
        pass


if __name__ == "__main__":
    HG = HtmlGenerator()
    test = HG.html_writer()
    del HG
