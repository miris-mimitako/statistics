from sre_constants import SUCCESS
import jinja2
from jinja2 import Template, Environment, FileSystemLoader
import json
import os
import datetime
import re
from pathlib import Path

'''
Rev: 0.0.2
'''
# debug
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


class HtmlGenerator():
    def __init__(self) -> None:
        self.params = {"parameter": []}
        self.global_counter = 0  # This value is number of input plot datas.

    def make_directory_for_result(self, this_title):
        base_directory = Path(__file__).resolve().parent.parent.parent
        now_date = datetime.datetime.today()
        folder_name = str(now_date.date()) + "-" + \
            re.sub(r"[^a-zA-Z0-9]", "", this_title)

        flag_of_mkdir = True
        mkdir_counter = 0
        while flag_of_mkdir:
            try:
                os.makedirs(os.path.join(base_directory, "results/tmp",
                            str(folder_name), str(mkdir_counter)))
                flag_of_mkdir = False
                self.directory_location = os.path.join(base_directory, "results/tmp",
                                                       str(folder_name), str(mkdir_counter))
                self.relation_directory_location = os.path.join(
                    "../../results/tmp", str(folder_name), str(mkdir_counter))
                print("success mkdir")
            except FileExistsError:
                mkdir_counter += 1
            # E while

    def plot_image_generator(self, plot_data, title="", comment=""):
        if title == False:
            title = "plot :" + str(self.global_counter)

        plot_data.savefig(os.path.join(self.directory_location, "test.png"))
        self.params["parameter"].append({"title": str(title), "img_src": str(os.path.join(
            self.relation_directory_location, "test.png")), "comment": str(comment)})

        # self.params["parameter"].append[self.global_counter]["title"] = "test_title"
        # self.params["parameter"].append[self.global_counter]["img_src"] = os.path.join(
        #     self.relation_directory_location, "test.png")
        # self.params["parameter"].append[self.global_counter]["comment"] = "test_comment"
        self.global_counter += 1

    def html_writer(self, session_title):
        # Read template
        env = Environment(loader=FileSystemLoader(
            'template/statistics/', encoding='utf8'))
        tmpl = env.get_template('plotview.j2')  # set your templates

        sns.set_theme()
        np.random.seed(0)
        x = np.random.randn(100)
        ax = sns.distplot(x)
        sfig = ax.get_figure()

        MD = self.make_directory_for_result(str(session_title))  # debug only
        NP = self.plot_image_generator(sfig, "testtitle", "cco")
        NP = self.plot_image_generator(sfig, "testtitle2", "cco2")

        # rendering and output HTML
        set_data = self.params["parameter"]
        rendered_html = tmpl.render(set_data=set_data, html_title="this title")
        with open('results/html/'+ str(session_title)+ "-" +str(self.global_counter) + '.html', 'w', encoding="utf-8") as f:
            f.write(rendered_html)
        # E def html_writer

    def __del__(self):
        pass


if __name__ == "__main__":
    HG = HtmlGenerator()
    test = HG.html_writer("test_title2")
    del HG
