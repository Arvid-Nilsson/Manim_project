from manim import *

class IndexLabelsMathTex(Scene):
    def construct(self):
        text_1 = MathTex(r"y = x^2", font_size=96)
        text_2 = MathTex(r"y = x^2", font_size=96)

        self.add(text)