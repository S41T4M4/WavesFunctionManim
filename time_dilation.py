from manim import *

class TimeDilation(Scene):
    def construct(self):
        # Títulos
        title = Text("Dilatação do Tempo", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # Explicação inicial
        explanation = Text(
            "Tempo passa mais lentamente para um objeto em movimento\n"
            "em relação a um observador estacionário.",
            font_size=24
        )
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        self.wait(2)

        # Ajustando os relógios para ficarem mais próximos ao centro
        stationary_clock = Circle(radius=1.5)
        moving_clock = Circle(radius=1.5)

        stationary_clock.shift(LEFT * 3)
        moving_clock.shift(RIGHT * 3)

        stationary_label = Text("Observador Estacionário", font_size=24).next_to(stationary_clock, DOWN)
        moving_label = Text("Objeto em Movimento", font_size=24).next_to(moving_clock, DOWN)

        self.play(FadeIn(stationary_clock), FadeIn(moving_clock))
        self.play(FadeIn(stationary_label), FadeIn(moving_label))

        # Animação dos ponteiros dos relógios
        stationary_hand = Line(ORIGIN, UP * 1.5, color=BLUE)
        moving_hand = Line(ORIGIN, UP * 1.5, color=RED)

        stationary_hand.move_to(stationary_clock.get_center())
        moving_hand.move_to(moving_clock.get_center())

        self.play(GrowFromCenter(stationary_hand), GrowFromCenter(moving_hand))

        # Rotações dos ponteiros
        stationary_rotation = Rotate(stationary_hand, angle=-2 * PI, about_point=stationary_clock.get_center())
        moving_rotation = Rotate(moving_hand, angle=-PI, about_point=moving_clock.get_center())

        self.play(stationary_rotation, run_time=4)
        self.play(moving_rotation, run_time=4)

        # Texto explicativo final
        conclusion = Text(
            "Para o objeto em movimento, o tempo parece passar mais devagar.",
            font_size=24
        )
        conclusion.next_to(explanation, DOWN)
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(stationary_clock),
                  FadeOut(moving_clock), FadeOut(stationary_label), FadeOut(moving_label),
                  FadeOut(stationary_hand), FadeOut(moving_hand))
        self.play(FadeIn(conclusion))
        self.wait(3)

        # Fim
        self.play(FadeOut(conclusion))
        
        final_text1 =Text("Vitor Ibraim" ,gradient=(GREEN, BLUE, RED), font_size=68)
        self.play(FadeIn(final_text1), run_time=2)
        final_text2 =Text("https://github.com/S41T4M4/" ,gradient=(RED, BLUE, GREEN), font_size =60).next_to(final_text1,DOWN)
        self.play(FadeIn(final_text2), run_time=2)
        self.play(FadeOut(final_text1), FadeOut(final_text2))
        self.wait(1)
