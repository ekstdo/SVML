from ctypes import alignment
from manim.animation.transform_matching_parts import TransformMatchingTex
from manim_slide import *
import math

temp = TexTemplate()
temp.add_to_preamble(r"""
    \usepackage{stmaryrd,mathtools,marvosym,fontawesome}
    \newcommand{\comm}[2]     {\left\llbracket#1,#2\right\rrbracket}
    \newcommand{\bra}[1]      {\left\langle #1\right|}
    \newcommand{\ket}[1]      {\left|#1\right\rangle}
    \newcommand{\braket}[2]   {\left\langle #1\middle|#2\right\rangle}
    \newcommand{\ketbra}[2]   {\left|#1\middle\rangle\!\middle\langle#2\right|}
    \newcommand{\braopket}[3] {\left\langle #1\middle|#2\middle|#3\right\rangle}
    \newcommand{\proj}[1]     {\left| #1\middle\rangle\!\middle\langle#1\right|}
    \newcommand{\abs}[1]      {\left| #1 \right|}
    \newcommand{\norm}[1]     {\left\| #1 \right\|}
    \newcommand{\Tr}          {\mathrm{Tr}}
""")
temp.add_to_document(r"""
    \fontfamily{lmss}\selectfont
""")


def MyTex(*x,tex_environment="center",color=WHITE):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color
    )

def MyMathTex(*x,tex_environment="align*",color=WHITE):
    return MyTex(*x,
        tex_environment=tex_environment,
        color=color
    )

class Slide21(SlideScene):

    def construct(self):
        # definitions
        vg = VGroup()
        text = MyMathTex(r"|z_1 z_2| \stackrel ! = |z_1| |z_2|, z_1 := x_1 + i y_1, z_2 := x_2 + i y_2")
        text2 = MyMathTex(r"|z_1 z_2|")
        text3 = MyMathTex(r"\stackrel {\text{def}.} = |(x_1 + i y_1) (x_2 + i y_2)|")
        text4 = MyMathTex(r"= |x_1 y_1 + i x_1 y_2 + i x_2 y_1 - x_2 y_2|")
        text5 = MyMathTex(r"= |(x_1 y_1 - x_2 y_2) + i (x_1 y_2 + x_2 y_1)|")
        text6 = MyMathTex(r"= |\underbrace{(x_1 y_1 - x_2 y_2)}_{\text{Realteil}} + i \underbrace{(x_1 y_2 + x_2 y_1)}_{\text{Imaginärteil}}|")
        text8 = MyMathTex(r"= \sqrt{(x_1 x_2 - y_1 y_2)^2 + (x_1 y_2 + x_2 y_1)^2}")
        text9 = MyMathTex(r"= {\small\sqrt{(x_1 x_2)^2 - 2 (x_1 x_2)(y_1 y_2) + (y_1 y_2)^2 + (x_1 y_2)^2 + 2 (x_1 y_2)(x_2 y_1) + (x_2 y_1)^2}}")
        text10 = MyMathTex(r"= \sqrt{(x_1^2 + y_1^2)(x_2^2 + y_2^2)}")
        text11 = MyMathTex(r"= \sqrt{x_1^2 + y_1^2} \sqrt{x_2^2 + y_2^2}")
        text12 = MyMathTex(r"= |z_1| |z_2|")


        # arrangement

        text.to_edge(UL)
        text2.next_to(text, DOWN, aligned_edge = LEFT)
        text3.next_to(text2, RIGHT)
        text4.next_to(text3, DOWN, aligned_edge=LEFT)
        text5.next_to(text4, DOWN, aligned_edge=LEFT)
        text6.next_to(text4, DOWN, aligned_edge=LEFT)


        # playback
        self.play(Write(text))
        self.slide_break()
        self.play(Write(text2))
        self.play(Write(text3))
        self.slide_break()
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(TransformMatchingTex(text5, text6))
        self.slide_break()
        self.play(FadeOut(text3))
        self.play(FadeOut(text4))
        self.play(text6.animate.next_to(text2, RIGHT, aligned_edge=UP))
        text8.next_to(text6, DOWN, aligned_edge=LEFT)
        text9.next_to(text8, DOWN, aligned_edge=LEFT)

        self.slide_break()
        self.play(Write(text8))
        self.play(Write(text9))
        self.slide_break()
        text10.next_to(text9, DOWN, aligned_edge=LEFT)
        text11.next_to(text10, DOWN, aligned_edge=LEFT)
        text12.next_to(text11, DOWN, aligned_edge=LEFT)
        self.play(Write(text10))
        self.slide_break()
        self.play(Write(text11))
        self.slide_break()
        self.play(Write(text12))
        self.slide_break()

class Slide212(SlideScene):
    def construct(self):
        eq1 = MyMathTex(r"\left|\frac{z_1}{z_2}\right| \stackrel ! = \frac{|z_1|}{|z_2|}, z_1:= r_1e^{i\varphi_1}, z_2 := r_2e^{i\varphi_2}").to_edge(UL)
        eq2 = MyMathTex(r"\left|\frac{z_1}{z_2}\right|")
        eq3 = MyMathTex(r"= \left|\frac{r_1 e^{i \varphi_1}}{r_2 e^{i \varphi_2}}\right|")
        eq4 = MyMathTex(r"= \left|\frac{r_1}{r_2} e^{i \varphi_1 - i \varphi_2}\right|")
        eq5 = MyMathTex(r"\stackrel {\text{def.} r}= \frac{r_1}{r_2}")
        eq6 = MyMathTex(r"\stackrel {\text{def.} r}= \frac{|z_1|}{|z_2|}")

        eq2.next_to(eq1, DOWN)
        eq3.next_to(eq2, RIGHT)
        eq4.next_to(eq3, DOWN, aligned_edge=LEFT)
        eq5.next_to(eq4, DOWN, aligned_edge=LEFT)
        eq6.next_to(eq5, DOWN, aligned_edge=LEFT)

        self.play(Write(eq1))
        self.slide_break()
        self.play(Write(eq2))
        self.slide_break()
        self.play(Write(eq3))
        self.slide_break()
        self.play(Write(eq4))
        self.slide_break()
        self.play(Write(eq5))
        self.slide_break()
        self.play(Write(eq6))
        self.slide_break()

class Slide221(SlideScene):
    def construct(self):
        eq0 = MyMathTex(r"re^{i \varphi} \stackrel ! = r(\text{cos}(\varphi) + i \text{sin}(\varphi))").to_edge(UL)
        eq1 = MyMathTex(r"\Leftrightarrow e^{i \varphi} \stackrel ! = \text{cos}(\varphi) + i \text{sin}(\varphi)")
        eq2 = MyMathTex(r"\text{cos}(\varphi) + i \text{sin}(\varphi)")
        eq3 = MyMathTex(r"= \frac{e^{i\varphi} + e^{-i\varphi}}2 + i \frac{e^{i\varphi} - e^{-i\varphi}}{2i}")
        eq4 = MyMathTex(r"= \frac{e^{i\varphi} + e^{-i\varphi}}2 + i \frac{e^{i\varphi} - e^{-i\varphi}}{2i}")
        eq5 = MyMathTex(r"= \frac{e^{i\varphi} + e^{-i\varphi} + e^{i\varphi} - e^{-i\varphi}}2")
        eq6 = MyMathTex(r"= e^{i\varphi}")
        eq1.next_to(eq0, DOWN, aligned_edge=LEFT)
        eq2.next_to(eq1, DOWN, aligned_edge=LEFT)
        eq3.next_to(eq2, RIGHT)
        eq4.next_to(eq3, DOWN, aligned_edge=LEFT)
        eq5.next_to(eq4, DOWN, aligned_edge=LEFT)
        eq6.next_to(eq5, DOWN, aligned_edge=LEFT)
        self.play(Write(eq0))
        self.slide_break()
        self.play(Write(eq1))
        self.slide_break()
        self.play(Write(eq2))
        self.slide_break()
        self.play(Write(eq3))
        self.slide_break()
        self.play(Write(eq4))
        self.slide_break()
        self.play(Write(eq5))
        self.slide_break()
        self.play(Write(eq6))
        self.slide_break()

class Slide222(SlideScene):
    def construct(self):
        eq0 = MyMathTex(r"z_1 z_2 \stackrel ! = (r_1 r_2)e^{i(\varphi_1 + \varphi_2)}, z_1 := r_1 e^{i\varphi_1}, z_2 := r_2 e^{i\varphi_2}")
        eq1 = MyMathTex(r"z_1 z_2 \stackrel {\text{def.}}= r_1 e^{i\varphi_1} r_2 e^{i \varphi_2} = (r_1 r_2) e^{i\varphi_1 + i\varphi_2} = (r_1 r_2) e^{i(\varphi_1 + \varphi_2)}")
        eq1.next_to(eq0, DOWN)
        self.play(Write(eq0))
        self.slide_break()
        self.play(Write(eq1))
        self.slide_break()

class Slide231(SlideScene):
    def construct(self):
        self.play(Create(NumberPlane()))
        dot = Dot(UP)
        staticdot1 = Dot(UP)
        staticdot2 = Dot(LEFT)
        staticdot3 = Dot(DOWN)
        staticdot4 = Dot(RIGHT)
        l = Line(ORIGIN, UP)
        bracelabel = MyMathTex(r"1")
        label1 = MyMathTex(r"i")
        label2 = MyMathTex(r"-1")
        label3 = MyMathTex(r"-i")
        label4 = MyMathTex(r"1")
        label1.next_to(staticdot1, UL)
        label2.next_to(staticdot2, UL)
        label3.next_to(staticdot3, UL)
        label4.next_to(staticdot4, UL)
        brace = BraceBetweenPoints(ORIGIN, UP)
        bracelabel.next_to(brace, RIGHT)
        def dot_callback(mobject):
            mobject.put_start_and_end_on(ORIGIN, dot.get_center())

        l.add_updater(dot_callback)
        self.add(dot, staticdot1, l, brace, bracelabel, label1)
        self.slide_break()
        self.play(FadeOut(brace))
        self.play(FadeOut(bracelabel))
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 2, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot2, label2)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 2, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot3, label3)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 2, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot4, label4)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 2, run_time=1, rate_func=linear))
        self.slide_break()

from math import cos, sin, pi, sqrt

class Slide233(SlideScene):
    def construct(self):
        self.play(Create(NumberPlane()))
        pos1 = [cos(pi / 3), sin(pi/3), 0.]
        pos2 = [cos(2 * pi / 3), sin(2* pi/3), 0.]
        pos3 = [cos(3 * pi / 3), sin(3* pi/3), 0.]
        pos4 = [cos(4 * pi / 3), sin(4* pi/3), 0.]
        pos5 = [cos(5 * pi / 3), sin(5* pi/3), 0.]
        pos6 = [cos(6 * pi / 3), sin(6* pi/3), 0.]
        dot = Dot(pos1)
        staticdot1 = Dot(pos1)
        staticdot2 = Dot(pos2)
        staticdot3 = Dot(pos3)
        staticdot4 = Dot(pos4)
        staticdot5 = Dot(pos5)
        staticdot6 = Dot(pos6)
        l = Line(ORIGIN, UP)
        def dot_callback(mobject):
            mobject.put_start_and_end_on(ORIGIN, dot.get_center())

        l.add_updater(dot_callback)
        self.add(dot, staticdot1, l)
        self.slide_break()
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot2)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot3)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot4)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot5)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()
        self.add(staticdot6)
        self.play(Rotate(dot, about_point = ORIGIN, angle=PI / 3, run_time=1, rate_func=linear))
        self.slide_break()

class Slide234(SlideScene):
    def construct(self):
        eq0 = MyMathTex(r"z").to_edge(UL)
        eq1 = MyMathTex(r"=", r"{{{x}} + {{y}} i", r"\over ", r"{{y}} - {{x}} i}")
        eq2 = MyMathTex(r"=", r"{{{3}} + {{4}} i", r"\over ", r"{{4}} - {{3}} i}")
        eq3 = MyMathTex(r"=", r"{({{3}} + {{4}}i)({{4}} + {{3}}i)", r"\over ", r"({{4}} - {{3}}i)({{4}} + {{3}}i)}")
        eq32 = MyMathTex(r"=", r"{({{x}} + {{y}}i)({{y}} + {{x}}i)", r"\over ", r"({{y}} - {{x}}i)({{y}} + {{x}}i)}")
        eq4 = MyMathTex(r"=",r"{{{12}} + {{9}}i + {{16}}i - {{12}}", r"\over ", r"{{16}} - i^2{{9}}}")
        eq42 = MyMathTex(r"=", r"{{{xy}} + {{x^2}}i + {{y^2}}i - {{xy}}", r"\over ", r"{{y^2}} - i^2{{x^2}}}")
        eq5 = MyMathTex(r"=", r"{{{12}} + {{9}}i + {{16}}i - {{12}}", r"\over ", r"{{16}} + {{9}}}")
        eq52 = MyMathTex(r"=", r"{{{xy}} + {{x^2}}i + {{y^2}}i - {{xy}}", r"\over ", r"{{y^2}} + {{x^2}}}")
        eq6 = MyMathTex(r"=", r"{{{25}}i", r"\over ", r"25}")
        eq62 = MyMathTex(r"=", r"{{{(y^2 + x^2)}}i", r"\over ", r"y^2+ x^2}")
        eq7 = MyMathTex(r"= i = e^{i \frac \pi 2}")

        self.add(eq0)
        eq1.next_to(eq0, RIGHT)
        eq2.next_to(eq1, DOWN, aligned_edge = LEFT)
        eq3.next_to(eq2, DOWN, aligned_edge = LEFT)
        eq4.next_to(eq3, DOWN, aligned_edge = LEFT)
        eq5.next_to(eq4, DOWN, aligned_edge = LEFT)
        eq6.next_to(eq5, DOWN, aligned_edge = LEFT)
        eq7.next_to(eq6, RIGHT)
        self.play(Write(eq1))
        self.slide_break()
        self.play(Write(eq2))
        self.slide_break()
        self.play(Write(eq3))
        self.slide_break()
        self.play(Write(eq4))
        self.slide_break()
        self.play(Write(eq5))
        self.slide_break()
        self.play(Write(eq6))
        self.slide_break()
        self.play(Write(eq7))
        self.slide_break()
        self.play(FadeOut(eq2))
        eq32.next_to(eq2, DOWN, aligned_edge = LEFT)
        self.play(TransformMatchingTex(eq3, eq32))
        eq42.next_to(eq32, DOWN, aligned_edge = LEFT)
        self.play(TransformMatchingTex(eq4, eq42))
        eq52.next_to(eq42, DOWN, aligned_edge = LEFT)
        self.play(TransformMatchingTex(eq5, eq52))
        eq62.next_to(eq52, DOWN, aligned_edge = LEFT)
        self.play(TransformMatchingTex(eq6, eq62))
        eq7.next_to(eq62, RIGHT)
        self.slide_break()
        eq32.next_to(eq1, DOWN, aligned_edge = LEFT)
        eq42.next_to(eq32, DOWN, aligned_edge = LEFT)
        eq52.next_to(eq42, DOWN, aligned_edge = LEFT)
        eq62.next_to(eq52, DOWN, aligned_edge = LEFT)
        eq7.next_to(eq62, RIGHT)

        self.slide_break()
