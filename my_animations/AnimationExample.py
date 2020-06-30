from manimlib.imports import *
import math


''' Name my animation as Example
GraphScene contains all the magic '''
class Example(GraphScene):
    CONFIG = {
        "graph_origin": 3*DOWN + 5*LEFT,
        "x_min": 0,
        "x_max": 2,
        "x_tick_frequency": 0.5,
        "x_labeled_nums": [0, 1, 2],
        "y_min": 0,
        "y_max": 4,
        "y_tick_frequency": 0.5,
        "y_labeled_nums": [0, 1, 2, 3, 4],
        "y_axis_height": 5,
        "exclude_zero_label": False,
    }

    def construct(self):
        # Make axes
        self.setup_axes(animate=True)

        # Make graph
        graphX = self.get_graph(self.functionX)
        labelX = self.get_graph_label(graphX, label="y = x")
        graphXCopy = self.get_graph(self.functionX)

        graphX2 = self.get_graph(self.functionX2)
        labelX2 = self.get_graph_label(graphX2, label="y = x^{2}")

        # Make and move text
        text = TextMobject("and job done.")
        text.shift(1*UP, 1*LEFT)

        # Make animation
        self.play(ShowCreation(graphX))
        self.play(Transform(graphX, graphX2))
        self.play(FadeOut(graphX))
        self.play(Write(graphXCopy), Write(graphX2),
                  Write(labelX), Write(labelX2))
        self.play(Write(text))
        self.wait(2)


    def functionX(self, x):
        return (x)

    def functionX2(self, x):
        return(x**2)
