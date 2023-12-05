from manim import *
import time

class differentParametrications(Scene):
    def construct(self):
        text_1 = MathTex(r"y = x^2", font_size=96)
                         
        #x=t                 
        text_2_1 = MathTex(r"x &= t", font_size=96)
        text_2_2 = MathTex(r"y &= t^2", font_size=96)

        #x=2t                 
        text_3_1 = MathTex(r"x &= 2t", font_size=96)
        text_3_2 = MathTex(r"y &= 2t^2", font_size=96)
        #x=t^2                 
        text_4_1 = MathTex(r"x &= t^2", font_size=96)
        text_4_2 = MathTex(r"y &= t^4", font_size=96)
        #x=t + 3                 
        text_5_1 = MathTex(r"x &= t + 3", font_size=96)
        text_5_2 = MathTex(r"y &= t^2+6t+9", font_size=96)
        

        self.play(Write(text_1))
        self.wait(2)
        self.play(Transform(text_1 ,VGroup(text_2_1, text_2_2).arrange(DOWN, aligned_edge=LEFT)))
        self.wait(5)
        self.play(Transform(text_1 ,VGroup(text_3_1, text_3_2).arrange(DOWN, aligned_edge=LEFT)))
        self.wait(2)
        self.play(Transform(text_1 ,VGroup(text_4_1, text_4_2).arrange(DOWN, aligned_edge=LEFT)))
        self.wait(2)
        self.play(Transform(text_1 ,VGroup(text_5_1, text_5_2).arrange(DOWN, aligned_edge=LEFT)))

class ExampleFunctionGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            #axis_config={"font_size": 24},
        ).add_coordinates()

        t = 1;

        curve = ax.plot(lambda x: x**2)

        dot = Dot(ax.c2p(0, 0))

        self.add(ax, curve, dot)
        self.wait(3)

        
        self.play(dot.animate.move_to(ax.c2p(t,t**2)))

