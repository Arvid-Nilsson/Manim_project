from manim import *
import math
from scipy.integrate import quad

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

class parametricationsVisualized(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            #axis_config={"font_size": 24},
        ).add_coordinates()

        t = ValueTracker(0);

        curve = ax.plot(lambda x: x ** 2)

        dot = Dot(ax.c2p(0, 0))
        dot2 = Dot(ax.c2p(0, 0))

        def update_dot(dot):
            x_val = t.get_value()  
            new_point = ax.input_to_graph_point(x_val, curve)
            dot.move_to(new_point)
        
        def update_dot2(dot):
            x_val = t.get_value() * 2  
            new_point = ax.input_to_graph_point(x_val, curve)
            dot.move_to(new_point)

        dot.add_updater(update_dot)
        dot2.add_updater(update_dot2)

        t_label = Text("t = ").scale(0.8).to_corner(UL)
        t_value = DecimalNumber(0).scale(0.8).next_to(t_label, RIGHT)

        t_value.add_updater(lambda v: v.set_value(t.get_value()))

        self.add(ax, curve, dot, dot2, t_label, t_value)
        self.play(t.animate.set_value(2), rate_func = linear, run_time=10)


class UnitCircle(Scene):
    def func(self, t):
        return np.array((np.cos(t), np.sin(t), 0))

    def construct(self):
        ax = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
        ).add_coordinates()

        t = ValueTracker(0)

        curve = ax.plot_parametric_curve(self.func, t_range=[0, 2*np.pi], color=RED)

        dot = Dot(ax.c2p(1, 0))
        dot2 = Dot(ax.c2p(1, 0))

        def update_dot(dot):
            t_val = t.get_value()
            new_point = ax.input_to_graph_point(t_val, curve)
            dot.move_to(new_point)

        def update_dot2(dot):
            t_val = t.get_value()
            new_point = ax.input_to_graph_point(2*t_val, curve)
            dot.move_to(new_point)

        dot.add_updater(update_dot)
        dot2.add_updater(update_dot2)

        t_label = Text("t = ").scale(0.8).to_corner(UL)
        t_value = DecimalNumber(0).scale(0.8).next_to(t_label, RIGHT)

        equation1_lable = Text("Parametricering 1", font_size=22)
        equation1_x = MathTex(r"x &= \cos t")
        equation1_y = MathTex(r"x &= \sin t")
        equation1 = VGroup(equation1_lable, equation1_x, equation1_y).arrange(DOWN, aligned_edge=LEFT)

        equation2_lable = Text("Parametricering 2", font_size=22)
        equation2_x = MathTex(r"x &= \cos 2t")
        equation2_y = MathTex(r"x &= \sin 2t")
        equation2 = VGroup(equation2_lable, equation2_x, equation2_y).arrange(DOWN, aligned_edge=LEFT)

        t_value.add_updater(lambda v: v.set_value(t.get_value()))

        self.add(ax, curve, t_label, t_value, dot, dot2, VGroup(equation1, equation2).arrange(DOWN, aligned_edge=LEFT).to_corner(UR))
        self.play(t.animate.set_value(2 * PI), rate_func=linear, run_time=10)

class arclength(Scene):
    def func(self, t):
        return np.array((np.cos(t), np.sin(t), 0))
    
    def integrand(self, x):
        return math.sqrt((math.sin(x)**2) + ((-math.cos(x))**2))
    
    def construct(self):
        ax = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
        ).add_coordinates()

        t = ValueTracker(0)

        curve = ax.plot_parametric_curve(self.func, t_range=[0, 2*np.pi], color=ORANGE)

        dot = Dot(ax.c2p(1, 0))

        def update_dot(dot):
            t_value = t.get_value()
            new_point = ax.input_to_graph_point(t_value, curve)
            dot.move_to(new_point)

        dot.add_updater(update_dot)
        
        text = Text("")
        text1 = MathTex(r"\int")
        text2 = MathTex(r"\int_{a}^{b}")
        text3 = MathTex(r"\int_{a}^{b} \sqrt{\left(\frac{dy}{dt}\right)^2 \cdot \left(\frac{dx}{dt}\right)^2}")
        text4 = MathTex(r"\int_{a}^{b} \sqrt{\left(\frac{dy}{dt}\right)^2 \cdot \left(\frac{dx}{dt}\right)^2} =").to_corner(UR).scale(0.5)
        text6 = DecimalNumber(0).scale(0.5).next_to(text4, RIGHT)
        text6.add_updater(lambda v: v.set_value(quad(self.integrand, 0, t.get_value())[0]))       
        



        self.add(text)
        self.play(Transform(text, text1))
        self.play(Transform(text, text2))
        self.play(Transform(text, text3))
        self.wait(3)
        self.play(text.animate.to_corner(UR).scale(0.5))
        self.play
        self.play(FadeIn(ax))
        self.wait(3)
        self.add(curve)
        self.wait(3)
        self.play(Create(dot), Transform(text, text4), FadeIn(text6))
        self.wait(3)
        self.play(t.animate.set_value(2 * PI), rate_func=linear, run_time=10)
        self.wait(3)


       