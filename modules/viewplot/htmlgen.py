from sre_constants import SUCCESS
import jinja2
from jinja2 import Template, Environment, FileSystemLoader
import json
import os
import datetime
import re
from pathlib import Path

# debug
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

'''
Rev: 0.0.4
'''


class HtmlGenerator:
    def __init__(self, project_title):
        self.params = {"parameter": []}
        self.global_counter = 0  # This value is number of input plot datas.
        self.project_title = project_title
        self.make_directory_for_result()

    def make_directory_for_result(self):
        self.base_directory = Path(__file__).resolve().parent.parent.parent
        now_date = datetime.datetime.today()
        folder_name = str(now_date.date()) + "-" + \
            re.sub(r"[^a-zA-Z0-9]", "", self.project_title)

        flag_of_mkdir = True
        mkdir_counter = 0
        while flag_of_mkdir:
            try:
                os.makedirs(os.path.join(self.base_directory, "results/tmp",
                            str(folder_name), str(mkdir_counter)))
                flag_of_mkdir = False
                self.directory_location = os.path.join(self.base_directory, "results/tmp",
                                                       str(folder_name), str(mkdir_counter))
                print(self.directory_location)
                self.relation_directory_location = os.path.join(
                    "../../results/tmp", str(folder_name), str(mkdir_counter))
                print("success mkdir")
            except FileExistsError:
                mkdir_counter += 1
        self.dir_counter = 0
        self.dir_counter = mkdir_counter
        # E while

    def plot_image_generator(self, plot_data, title="", comment=""):
        if title == False:
            title = "plot :" + str(self.global_counter)

        plot_data.savefig(os.path.join(self.directory_location, title))
        self.params["parameter"].append({"title": str(title), "img_src": str(os.path.join(
            self.relation_directory_location, title + ".png")), "comment": str(comment), "flag": "img"})

        self.global_counter += 1

    def data_frame_generator(self, data_frame, title="", comment=""):
        if title == False:
            title = "dataframe :" + str(self.global_counter)

        self.params["parameter"].append({"title": str(
            title), "dataframe": data_frame, "comment": str(comment), "flag": "dataframe"})

        self.global_counter += 1

    def html_writer(self):
        # Read template
        env = Environment(loader=FileSystemLoader(os.path.join(
            self.base_directory, 'template/statistics/'), encoding='utf8'))
        tmpl = env.get_template('plotview.j2')  # set your templates

        try:
            os.makedirs(os.path.join(self.base_directory, "results/html"))
        except:
            pass
        # E try

        # rendering and output HTML
        set_data = self.params["parameter"]
        rendered_html = tmpl.render(
            set_data=set_data, html_title=self.project_title)
        with open(os.path.join(self.base_directory, "results/html")+"/" + str(self.project_title) + "-" + str(self.dir_counter) + '.html', 'w', encoding="utf-8") as f:
            f.write(rendered_html)
        # E def html_writer

    def __del__(self):
        pass


if __name__ == "__main__":
    pass
