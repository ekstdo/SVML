from ctypes import alignment
from manim import *
from manim_slide import SlideScene
import math
import numpy as np

def noise_from(x, freq, phase, amplitude): 
    return (np.sin((1./freq).clip(0, 4) * (x + phase)) * amplitude).sum()

def interp_access(a, i):
    iint = int(i)
    ifloat = i - iint
    ifloat3 = ifloat ** 3
    return (1 - ifloat) * a[iint] + ifloat * a[(iint + 1) % len(a)]
    # return a[iint]

def echo(*args):
    print(*args)
    return args[0]


class Slide34(SlideScene):
    def construct(self):

        text1 = MathTex(r"\nabla f &= \begin{pmatrix}\frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{pmatrix}& ", 
                        r"\\\frac{\partial f}{\partial x} &= \frac{\partial}{\partial x} \left[127.5 \sin\left(\frac 1 2 \pi \frac{(x - 320)^2 + (y - 240)^2}{640} \right) + 127.5\right]& ",
                        r"\\&=127.5 \frac{\partial}{\partial x} \sin(a) + \underbrace{\frac{\partial}{\partial x} 127.5}_{=0} & (\text{A1, A2})",
                        r"\\&=127.5 \cdot \frac{\partial}{\partial x} \sin(a) & (\text{A6})",
                        r"\\&=127.5 \cdot cos(a) \frac{\partial}{\partial x}\frac{\pi}{2 \cdot 640}\left((x - 320)^2 + (y-240)^2\right)& (\text{A3}, \text{A8})",
                        r"\\&=127.5 \cdot cos(a) \frac{\pi}{2 \cdot 640} \left(\frac{\partial}{\partial x}(x - 320)^2 + \underbrace{\frac{\partial}{\partial x}(y-240)^2}_{=0}\right)& (\text{A3}, \text{A8})",
                        r"\\&=127.5 \cdot cos(a) \frac{\pi}{2 \cdot 640} \frac{\partial}{\partial x}(x - 320)^2& (\text{A6})",
                        r"\\&=127.5 \cdot cos(a) \frac{\pi}{2 \cdot 640} 2(x - 320) \frac{\partial}{\partial x}(x - 320)& (\text{A3}, \text{A7})",
                        r"\\&=127.5 \cdot cos(a) \frac{\pi}{2 \cdot 640} 2(x - 320) (\underbrace{\frac{\partial}{\partial x} x}_1 - \underbrace{\frac{\partial}{\partial x} 320}_0)& (\text{A3}, \text{A7})",
                        r"\\&=127.5 \cdot \cos\left(\frac 1 2 \pi \frac{(x - 320)^2 + (y - 240)^2}{640} \right) \frac \pi {640} (x - 320)"
                        )


        text1.scale(0.8)
        text1.move_to(DOWN  * 3)
        self.play(Write(text1[0]))
        self.slide_break()
        self.play(Write(text1[1]))
        self.slide_break()
        text1[2].move_to(UP)
        text1[3].move_to(UP)
        text1[4].move_to(UP)
        text1[5].move_to(UP)
        text1[6].move_to(UP)
        text1[7].move_to(UP)
        text1[8].move_to(UP)
        text1[9].move_to(UP)
        self.play(text1[1].animate.become(text1[2]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[3]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[4]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[5]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[6]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[7]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[8]))
        self.slide_break()
        self.play(text1[1].animate.become(text1[9]))
        self.slide_break()


class Slide31(SlideScene):
    def construct(self):
        freq = np.random.rand(5, 10)
        phase = np.random.rand(5, 10)
        amplitude = np.random.rand(5, 10)
        k = ValueTracker(0)

        axes1 = Axes(x_range= [0, 6, 1], y_range=[-8, 8, 1])
        axes2 = Axes(x_range= [0, 6, 1], y_range=[-8, 8, 1])
        axes3 = Axes(x_range= [0, 6, 1], y_range=[-8, 8, 1])
        axes4 = Axes(x_range= [0, 6, 1], y_range=[-8, 8, 1])
        function1 = lambda t: noise_from(t, interp_access(freq, k.get_value()), interp_access(phase, k.get_value()), interp_access(amplitude, k.get_value()))
        function2 = lambda t: round(1. * noise_from(t, interp_access(freq, k.get_value()), interp_access(phase, k.get_value()), interp_access(amplitude, k.get_value()))) / 1.


        noisefunc = axes1.plot(function1, color = BLUE, x_range=[0, 6])

        # noisefunc.add_updater(lambda func: func.become(axes1.plot(function1, color = BLUE, x_range=[0, 6])))

        function1_group = VGroup(axes1, noisefunc)

        self.add(axes1)
        self.play(Write(noisefunc))

        text1 = MathTex("x_c(t)")
        text2 = MathTex("x[n] = x_c(nT)")
        text3 = MathTex(r"\text{das Signal wird zu festen Zeiten abgetastet}")
        text4 = MathTex("T")
        brace = BraceBetweenPoints(axes1.coords_to_point(0, -7.5), axes1.coords_to_point(0.5, -7.5))
        text4.next_to(brace, DOWN)
        text1.next_to(axes1, UP)
        text2.next_to(axes1, UP)
        text3.next_to(axes1, DOWN)
        self.play(Write(text1))
        # self.play(k.animate.set_value(4.99), run_time = 6)
        # noisefunc.clear_updaters()
        # self.play(noisefunc.animate.become(axes1.plot( function2, x_range=[0, 6], use_smoothing=False).make_jagged()))

        lines = []
        dots = list(zip(*[(i, function1(i)) for i in np.arange(0, 6, 0.5)]))
        dots2 = list(zip(*[(i, function2(i)) for i in np.arange(0, 6, 0.5)]))
        for i in range(12):
            l = axes1.plot_line_graph(x_values = [i * 0.5, i*0.5], y_values = [-8, 8], add_vertex_dots=False, line_color= "#aaaaaa")
            lines.append(l)
            self.play(Write(l), run_time = 0.01)

        dots_plot = axes1.plot_line_graph(x_values = dots[0], y_values = dots[1])
        self.play(Write(dots_plot["vertex_dots"]))
        self.play(text1.animate.become(text2))
        self.play(Write(brace))
        self.play(Write(text4))

        self.play(noisefunc.animate.set_color("#113366"))
        for i in lines:
            self.play(i.animate.set_line_color("#555555"))

        hlines = []
        for i in range(16):
            l = axes1.plot_line_graph(x_values = [0, 6], y_values = [i - 8, i - 8], add_vertex_dots=False, line_color= "#aaaaaa")
            hlines.append(l)
            self.play(Write(l), run_time = 0.01)

        self.play(dots_plot["vertex_dots"].animate.become(axes1.plot_line_graph(x_values = dots2[0], y_values = dots2[1])["vertex_dots"]))
