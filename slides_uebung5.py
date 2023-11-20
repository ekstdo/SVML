from ctypes import alignment
from manim import *
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


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

def shift_circ_plot(scene, lines, dots, amount, length, reversed = True, shift = True):
    insert_index, pop_index = (length, 0) if reversed  else (0, -1)
    l = VGroup(*lines, *dots)
    if shift:
        scene.play(l.animate.shift(amount))
    scene.play(lines[pop_index].animate.shift(-length * amount), dots[pop_index].animate.shift(-length * amount))
    last_line, last_dot = lines.pop(pop_index), dots.pop(pop_index)
    lines.insert(insert_index, last_line)
    dots.insert(insert_index, last_dot)

class Slide5Scratch(SlideScene):
    def construct(self):

        t1 = Table([["hi", "yo"], ["this", "is awesome"], ["wow", "cool"]], element_to_mobject = Tex)


        self.play(Write(t1.get_rows()[0]))
        self.play(Write(t1.get_rows()[2]))
        self.play(Write(t1.get_rows()[1]))

class Slide51(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [0, 5, 1], y_range=[0, 7, 1], y_length=3, x_length=5).shift(UP * 1.7 + LEFT * 3)
        axes2 = Axes(x_range = [0, 5, 1], y_range=[0, 7, 1], y_length=3, x_length=5).shift(UP * 1.7 + RIGHT * 3)
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$x_2[k]$", [0, 0, 1, 0, 0, 0], axes1)
        title2, lines2, dots2, group2 = plot_time_discrete(self, "$x_1[k]$", [1, 2, 3, 4, 5, 6], axes2)
        self.play(Write(group1))
        self.play(Write(group2))
        self.slide_break()
        self.play(group1.animate.flip())
        self.play(title1.animate.become(MathTex("x_2[-k]").move_to(title1)))
        self.slide_break()
        self.play(group1.animate.shift(1.2* RIGHT+ 3.5 * DOWN))

        self.slide_break()
        x_axis = axes1.get_axis(0)
        y_axis = axes1.get_axis(1)
        self.play(y_axis.animate.shift(RIGHT * 6))
        self.play(VGroup(*lines1).animate.shift(RIGHT * 6), VGroup(*dots1).animate.shift(RIGHT * 6))
        self.play(title1.animate.shift(RIGHT * 6 + 0.5 * DOWN), x_axis.animate.shift(RIGHT * 6))

        tz = MathTex("n = -2 + 6 = 4").scale(.8).move_to(dots1[1]).shift(UP)
        self.play(Write(tz))
        
        self.slide_break()
        self.play(FadeOut(tz))


        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6, shift = False)
        self.play(y_axis.animate.shift(LEFT), x_axis.animate.shift(LEFT))
        
        t1 = Table([["k", "0", "1", "2", "3", "4", "5", ""],
                    ["x_1[k]", "1", "2", "3", "4", "5", "6", "y[n]"],
                    ["x_2[0- k]", "0", "0", "0", "0", "1", "0", r"\to 5"],
                    ["x_2[1- k]", "0", "0", "0", "0", "0", "1", r"\to 6"],
                    ["x_2[2- k]", "1", "0", "0", "0", "0", "0", r"\to 1"],
                    ["x_2[3- k]", "0", "1", "0", "0", "0", "0", r"\to 2"],
                    ["x_2[4- k]", "0", "0", "1", "0", "0", "0", r"\to 3"],
                    ["x_2[5- k]", "0", "0", "0", "1", "0", "0", r"\to 4"],
                ], element_to_mobject = MathTex).scale(0.5).shift(3.5 * LEFT)

        self.play(Write(t1.get_rows()[0]), Write(t1.get_rows()[1][:-1]))

        self.slide_break()

        self.play(title1.animate.become(MathTex("x_2[0-k]").move_to(title1)))
        self.play(Write(t1.get_rows()[2][:-1]))
        self.slide_break()

        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6)
        title1.animate.become(MathTex("x_2[1-k]").move_to(title1))
        self.play(Write(t1.get_rows()[3][:-1]))
        self.slide_break()


        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6)
        title1.animate.become(MathTex("x_2[2-k]").move_to(title1))
        self.play(Write(t1.get_rows()[4][:-1]))
        self.slide_break()

        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6)
        title1.animate.become(MathTex("x_2[3-k]").move_to(title1))
        self.play(Write(t1.get_rows()[5][:-1]))
        self.slide_break()

        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6)
        title1.animate.become(MathTex("x_2[4-k]").move_to(title1))
        self.play(Write(t1.get_rows()[6][:-1]))
        self.slide_break()

        shift_circ_plot(self, lines1, dots1, 1 * RIGHT, 6)
        title1.animate.become(MathTex("x_2[5-k]").move_to(title1))
        self.play(Write(t1.get_rows()[7][:-1]))
        self.slide_break()


        self.play(group1.animate.shift(RIGHT), group2.animate.shift(RIGHT))

        self.slide_break()

        last_col = t1.get_columns()[-1]
        last_col.shift(0.5 * RIGHT)
        self.play(Write(last_col))

class Slide52b(SlideScene):
    def construct(self):
        axes1 = Axes(x_range = [-1, 7, 1], y_range=[0, 4, 1], y_length=3, x_length=5).shift(UP * 1.7 + LEFT * 3)
        axes2 = Axes(x_range = [-1, 7, 1], y_range=[0, 4, 1], y_length=3, x_length=5).shift(UP * 1.7 + RIGHT * 3)
        axes3 = Axes(x_range = [-1, 7, 1], y_range=[0, 4, 1], y_length=3, x_length=5).shift(DOWN* 1.7 + LEFT * 3)
        axes4 = Axes(x_range = [-1, 7, 1], y_range=[0, 4, 1], y_length=3, x_length=5).shift(DOWN* 1.7 + RIGHT * 3)
        title1, lines1, dots1, group1 = plot_time_discrete(self, "$x_1[n]$", [0, 1, 1, 1, 1, 0], axes1, offset = -1)
        title2, lines2, dots2, group2 = plot_time_discrete(self, "lin. Faltung: $x_1[n] * x_1[n]$", [1, 2, 3, 4, 3, 2, 1], axes2, offset = 0)
        title3, lines3, dots3, group3 = plot_time_discrete(self, r"4-Pkt. zirkulär: $x_1[n] \raisebox{.5pt}{\textcircled{\raisebox{-.9pt} {4}}} x_1[n]$", [4, 4, 4, 4], axes3, offset = 0)
        title4, lines4, dots4, group4 = plot_time_discrete(self, r"8-Pkt. zirkulär: $x_1[n] \raisebox{.5pt}{\textcircled{\raisebox{-.9pt} {8}}} x_1[n]$", [1, 2, 3, 4, 3, 2, 1], axes4, offset = 0)

        t2 = Tex("7 wäre auch ausreichend gewesen").shift(RIGHT * 4 + DOWN * 4)


        self.add(group1.scale(0.7))
        self.play(FadeIn(group2.scale(0.7)))
        self.play(FadeIn(group3.scale(0.7)))
        self.play(FadeIn(group4.scale(0.7)))
        
        self.slide_break()
