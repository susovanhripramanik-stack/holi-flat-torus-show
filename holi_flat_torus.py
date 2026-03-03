from manim import *
import numpy as np

class HoliFlatTorus(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#111111"

        # ==================================================
        # 1️⃣ Flat Torus as R^2 / Z^2
        # ==================================================
        square = Square(side_length=4)
        square.set_stroke(WHITE, width=3)

        left_edge = Line(square.get_corner(UL), square.get_corner(DL), color=RED)
        right_edge = Line(square.get_corner(UR), square.get_corner(DR), color=RED)

        top_edge = Line(square.get_corner(UL), square.get_corner(UR), color=BLUE)
        bottom_edge = Line(square.get_corner(DL), square.get_corner(DR), color=BLUE)

        label = Tex(r"$T^2 = \mathbb{R}^2 / \mathbb{Z}^2$")
        label.to_edge(UP)

        self.play(Create(square))
        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(top_edge), Create(bottom_edge))
        self.play(Write(label))
        self.wait(2)

        arrow1 = Arrow(left_edge.get_center(), right_edge.get_center(), color=RED)
        arrow2 = Arrow(bottom_edge.get_center(), top_edge.get_center(), color=BLUE)

        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(3)

        flat_text = Tex(r"\textbf{Flat Metric (Zero Gaussian Curvature)}")
        flat_text.to_edge(DOWN)

        self.play(Write(flat_text))
        self.wait(2)

        self.play(
            FadeOut(square),
            FadeOut(left_edge),
            FadeOut(right_edge),
            FadeOut(top_edge),
            FadeOut(bottom_edge),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(label),
            FadeOut(flat_text)
        )

        # ==================================================
        # 2️⃣ Embedded Torus in R^3
        # ==================================================
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)

        torus = Torus(major_radius=2, minor_radius=0.7)
        torus.set_fill_by_checkerboard(RED, ORANGE, opacity=0.9)

        self.play(Create(torus), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        embed_text = Tex(
            r"\textbf{Embedding in $\mathbb{R}^3$ (Not Flat)}"
        )
        embed_text.to_edge(DOWN)
        embed_text.set_color(YELLOW)

        self.add_fixed_in_frame_mobjects(embed_text)
        self.play(Write(embed_text))
        self.wait(4)

        self.play(FadeOut(torus), FadeOut(embed_text))
        self.stop_ambient_camera_rotation()

        # ==================================================
        # 3️⃣ Final Happy Holi Message
        # ==================================================
        self.move_camera(phi=0, theta=0)

        holi_text = Tex(r"\textbf{Happy Holi}")
        holi_text.scale(1.8)
        holi_text.set_color_by_gradient(
            RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE
        )

        self.add_fixed_in_frame_mobjects(holi_text)

        self.play(FadeIn(holi_text, scale=1.5), run_time=3)
        self.wait(4)
