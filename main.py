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

        t_value.add_updater(lambda v: v.set_value(t.get_value()))

        self.add(ax, curve, t_label, t_value, dot, dot2)
        self.play(t.animate.set_value(2 * PI), rate_func=linear, run_time=10)
