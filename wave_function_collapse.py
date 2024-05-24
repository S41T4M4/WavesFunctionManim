from manim import *

class WaveFunctionCollapse(Scene):
    def construct(self):
        # Títulos
        title = Text("Wave's Function", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # Explicação inicial
        explanation = Text(
            "Superposition of quantum states",
            font_size=24
        )
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(explanation))
        self.wait(1)

        # Criação da onda em superposição
        superposition_wave = FunctionGraph(
            lambda x: np.sin(3 * x),
            x_range=[-6, 6],
            color=BLUE
        )

        # Desenho da onda em superposição
        self.play(Create(superposition_wave))
        self.wait(2)

        # Explicação do colapso
        collapse_text = Text("Collapse of the wave function", font_size=36)
        collapse_text.next_to(explanation, DOWN)
        self.play(FadeIn(collapse_text))
        self.wait(2)

        # Criação do estado colapsado
        collapsed_state = Dot(point=ORIGIN, color=RED, radius=0.2)
        collapsed_text = Text("State Collapsed", font_size=24).next_to(collapsed_state, RIGHT)

        # Animação do colapso
        self.play(Transform(superposition_wave, collapsed_state))
        self.play(FadeIn(collapsed_text))
        self.wait(2)
        
        
        

        # Fim
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(collapse_text),
                  FadeOut(collapsed_state), FadeOut(collapsed_text), FadeOut(superposition_wave))
        final_text1 =Text("Vitor Ibraim" ,gradient=(GREEN, BLUE, RED), font_size=68).next_to(collapse_text, ORIGIN)
        self.play(FadeIn(final_text1), run_time=2)
        final_text2 =Text("https://github.com/S41T4M4/" ,gradient=(RED, BLUE, GREEN), font_size =60).next_to(final_text1,DOWN)
        self.play(FadeIn(final_text2), run_time=2)
        self.play(FadeOut(final_text1), FadeOut(final_text2))
        self.wait(1)