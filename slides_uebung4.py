from ctypes import alignment
from manim import *
from manim_slide import SlideScene
import math
import numpy as np

def elements_time_discrete(numbers, ax, x_dist = 1, offset = 0):
    lines = []
    dots = []
    for (index, i) in enumerate(numbers):
        point = ax.coords_to_point(index * x_dist + offset, i)
        dots.append(Dot(point))
        lines.append(ax.get_vertical_line(point, line_config = {"dashed_ratio": 0.5}))
    return lines, dots

def plot_time_discrete(scene, title, numbers, ax, x_dist=1, offset = 0):
    lines, dots = elements_time_discrete(numbers, ax, x_dist, offset)
    title = Tex(title)
    title.next_to(ax, UP)
    group = VGroup(ax, title, *lines, *dots)
    return title, lines, dots, group





class Slide41(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [0, 6, 1], y_range=[-3, 3, 1], y_length=3, x_length=7).shift(UP * 1.7)
        axes2 = Axes(x_range = [0, 6, 1], y_range=[-3, 3, 1], y_length=3, x_length=7).shift(DOWN * 1.7)
        values = (np.random.rand(6) - 0.5) * 6
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$x[n]$", values, axes1)
        title2, lines2, dots2, group2 = plot_time_discrete(self, r"$T\{x[n]\} = \sum_{k = - \infty}^n x[k]$", np.cumsum(values), axes2)

        self.play(Write(group1))
        self.play(Write(group2)) 

        self.play(group1.animate.shift(LEFT * 3))
        self.play(group2.animate.shift(LEFT * 3))


        texts = [
            "1. linear",
            r"T(\{a x_1[m] + x_2[m]\}, n)\\ = a y_1[n] + y_2[n]",
            "2. zeitinvariant",
            r"&\forall n_0 \in \mathbb N:\\& x_1[n - n_0] = x_2[n] \Rightarrow y_1[n - n_0] = y_2[n]",
            "3. kausal",
            r"y[n]\text{ hängt nur von den } x[m] \text{ Werten } m \leq n \text{ ab }",
            "4. gedächtnislos",
            r"T(\{x[m]\}, n) = T(x[n])",
            "5. stabil",
            r"&\exists B_x: |x[n]| < B < \infty \Rightarrow \\&\exists B_y: |y[n]| < B_y < \infty"
        ]
        text_objects = VGroup()

        for index, i in enumerate(texts):
            if index % 2 == 0:
                text_objects.add(Tex(i))
            else: 
                text_objects.add(MathTex(i))
            if index == 0:
                text_objects[0].shift(RIGHT * 1 + UP * 4)
            else:
                text_objects[index].next_to(text_objects[index - 1], DOWN, aligned_edge = LEFT)

        text_objects.scale(0.8)


        for i in range(5):
            self.play(Write(text_objects[i * 2]))
            self.play(Write(text_objects[i * 2 + 1]))
            self.slide_break()


        self.play(Wait(1))

class Slide42(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [-2, 2, 1], y_range=[-1, 2, 1], y_length=3, x_length=5).shift(UP * 1.7 + LEFT * 3)
        axes2 = Axes(x_range = [-2, 2, 1], y_range=[-1, 2, 1], y_length=3, x_length=5).shift(UP * 1.7 + RIGHT * 3)
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$x[k]$", [0, 0, 1, 0, 0], axes1, offset = -2)
        title2, lines2, dots2, group2 = plot_time_discrete(self, "$h[k]$", [0, 0, 2, 1, 0], axes2, offset = -2)
        self.play(Write(group1))
        self.play(Write(group2))
        self.slide_break()
        self.play(group1.animate.flip())
        self.play(title1.animate.become(MathTex("x[-k]").move_to(title1)))
        self.slide_break()
        self.play(group1.animate.shift(6 * RIGHT + 3.5 * DOWN))
        self.play(Write(MathTex("k").shift(LEFT * 6 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("-2").shift(LEFT * 5 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 4 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 3 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 2 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 1 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("h[k]").shift(LEFT * 6 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 5 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 4 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 3 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 2 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 1 + UP * 2)), run_time = 0.1)
        self.slide_break()

        self.play(title1.animate.become(MathTex("x[0-k]").move_to(title1)))
        self.play(Write(MathTex("x[0 - k]").shift(LEFT * 6 + UP * 1)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 3 + UP * 1)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(1.25 * RIGHT),
             title1.animate.become(MathTex("x[1-k]").move_to(title1).shift(1.25 * RIGHT)))
        self.play(Write(MathTex("x[1 - k]").shift(LEFT * 6 + UP * 0)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 2 + UP * 0)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(RIGHT), group2.animate.shift(RIGHT))
        self.play(Write(MathTex("y[n]").shift(RIGHT * 0.5 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex(r"\to 2").shift(UP * 1)), run_time = 0.1)
        self.play(Write(MathTex(r"\to 1").shift(UP * 0)), run_time = 0.1)
        self.slide_break()
        self.play(Wait(1))
class Slide42b(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [-1, 3, 1], y_range=[-1, 2, 1], y_length=3, x_length=5).shift(UP * 1.7 + LEFT * 3)
        axes2 = Axes(x_range = [-2, 2, 1], y_range=[-1, 2, 1], y_length=3, x_length=5).shift(UP * 1.7 + RIGHT * 3)
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$x[k]$", [0, 0, 2, -1, 0], axes1, offset = -1)
        title2, lines2, dots2, group2 = plot_time_discrete(self, "$h[k]$", [0, -1, 2, 1, 0], axes2, offset = -2)
        self.play(Write(group1))
        self.play(Write(group2))
        self.slide_break()
        self.play(group1.animate.flip())
        self.play(title1.animate.become(MathTex("x[-k]").move_to(title1)))
        self.slide_break()
        self.play(group1.animate.shift(4.75 * RIGHT + 3.5 * DOWN))
        self.play(Write(MathTex("k").shift(LEFT * 6 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("-2").shift(LEFT * 5 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 4 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 3 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 2 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 1 + UP * 3)), run_time = 0.1)
        self.play(Write(MathTex("h[k]").shift(LEFT * 6 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 5 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 4 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 3 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("1").shift(LEFT * 2 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex("0").shift(LEFT * 1 + UP * 2)), run_time = 0.1)
        self.slide_break()

        self.play(title1.animate.become(MathTex("x[0-k]").move_to(title1)))
        self.play(Write(MathTex("x[0 - k]").shift(LEFT * 6 + UP * 1)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 5 + UP * 1)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 4 + UP * 1)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(1.25 * RIGHT),
             title1.animate.become(MathTex("x[1-k]").move_to(title1).shift(1.25 * RIGHT)))
        self.play(Write(MathTex("x[1 - k]").shift(LEFT * 6 + UP * 0)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 4 + UP * 0)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 3 + UP * 0)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(1.25 * RIGHT),
             title1.animate.become(MathTex("x[2-k]").move_to(title1).shift(1.25 * RIGHT)))
        self.play(Write(MathTex("x[2 - k]").shift(LEFT * 6 + DOWN)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 3 + DOWN * 1)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 2 + DOWN * 1)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(1.25 * RIGHT),
             title1.animate.become(MathTex("x[3-k]").move_to(title1).shift(1.25 * RIGHT)))
        self.play(Write(MathTex("x[3 - k]").shift(LEFT * 6 + 2* DOWN)), run_time = 0.1)
        self.play(Write(MathTex("-1").shift(LEFT * 2 + DOWN * 2)), run_time = 0.1)
        self.play(Write(MathTex("2").shift(LEFT * 1 + DOWN * 2)), run_time = 0.1)
        self.slide_break()

        self.play(group1.animate.shift(RIGHT), group2.animate.shift(RIGHT))
        self.play(Write(MathTex("y[n]").shift(RIGHT * 0.5 + UP * 2)), run_time = 0.1)
        self.play(Write(MathTex(r"\to -2").shift(UP * 1)), run_time = 0.1)
        self.play(Write(MathTex(r"\to 5").shift(UP * 0)), run_time = 0.1)
        self.play(Write(MathTex(r"\to 0").shift(DOWN)), run_time = 0.1)
        self.play(Write(MathTex(r"\to -1").shift(DOWN * 2)), run_time = 0.1)
        self.slide_break()
        self.play(Wait(1))



class Slide43(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [0, 14, 1], y_range=[-3, 3, 1], y_length=3, x_length=7).shift(UP * 1.7 + LEFT * 2)
        axes2 = Axes(x_range = [0, 5, 1], y_range=[-3, 3, 1], y_length=3, x_length=2.5).shift(UP * 1.7 + RIGHT * 5)
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$h[k]$", [2, -1, 1, 2, 3, -2, 1, 2, -1, 1, -2, -2, 1, -1], axes1, offset = 0)
        title2, lines2, dots2, group2 = plot_time_discrete(self, "$x[k]$", [-1, -2, 2, 1, 3], axes2, offset = 0)
        self.play(Write(group1))
        self.play(Write(group2))
        self.slide_break()
        N0 = axes1.get_vertical_line(axes1.coords_to_point(0, -4, 0), line_config = {"dashed_ratio": 0.5})
        N0T = MathTex("N_0").move_to(axes1.coords_to_point(0, -4.5, 0))
        N1 = axes1.get_vertical_line(axes1.coords_to_point(14, -4, 0), line_config = {"dashed_ratio": 0.5})
        N1T = MathTex("N_1").move_to(axes1.coords_to_point(14, -4.5, 0))

        N2 = axes2.get_vertical_line(axes2.coords_to_point(0, -4, 0), line_config = {"dashed_ratio": 0.5})
        N2T = MathTex("N_2").move_to(axes2.coords_to_point(0, -4.5, 0))
        N3 = axes2.get_vertical_line(axes2.coords_to_point(5, -4, 0), line_config = {"dashed_ratio": 0.5})
        N3T = MathTex("N_3").move_to(axes2.coords_to_point(5, -4.5, 0))
        self.play(Write(N0), run_time = 0.5)
        self.play(Write(N0T))
        self.play(Write(N1), run_time = 0.5)
        self.play(Write(N1T))
        self.play(Write(N2), run_time = 0.5)
        self.play(Write(N2T))
        self.play(Write(N3), run_time = 0.5)
        self.play(Write(N3T))
        group1.add(N0, N0T, N1, N1T)
        group2.add(N2, N2T, N3, N3T)
        self.slide_break()
        self.play(title1.animate.shift(4 * LEFT + 2.25 * DOWN))
        self.play(title2.animate.shift(2 * LEFT + 2.25 * DOWN))
        self.play(group1.animate.flip())

        self.play(title1.animate.become(MathTex("h[-k]").move_to(title1)))
        self.play(N1T.animate.become(MathTex("-N_1").move_to(N1T)))
        self.play(N0T.animate.become(MathTex("-N_0").move_to(N0T)))
        self.slide_break()
        self.play(group1.animate.scale(0.8))
        self.play(group2.animate.scale(0.8))
        self.play(group2.animate.shift(3.75 * LEFT + 3.5 * DOWN))
        self.play(N1T.animate.become(MathTex("n - N_1").move_to(N1T).scale(0.8)))
        self.play(N0T.animate.become(MathTex("n - N_0").move_to(N0T).scale(0.8)))
        self.play(title1.animate.become(MathTex("h[n-k]").move_to(title1).shift(0.5 * RIGHT).scale(0.8)))

        self.slide_break()
        exp1 = MathTex("n - N_0 = N_2").shift(UP * 1.7 + RIGHT * 5)
        self.play(Write(exp1))
        self.slide_break()
        self.play(exp1.animate.become(MathTex("n = N_0 + N_2").move_to(exp1)))

        self.slide_break()
        self.play(group1.animate.shift(3.8 * RIGHT))
        self.play(exp1.animate.become(MathTex("n - N_1 = N_3").move_to(exp1).shift(9 * LEFT)))
        self.play(group2.animate.shift(3.8 * LEFT))
        self.slide_break()
        self.play(exp1.animate.become(MathTex("n = N_1 + N_3").move_to(exp1)))

