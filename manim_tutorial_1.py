from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array(3,0,0),np.array(5,0,0))
        triangle=Polygon(np.array(0,0,0),np.array(1,1,0),np.array(1,-1,0))

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))

class MoreShapes(Scene):
    #A few more simple shapes
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class MovingShapes(Scene):
    #Show the difference between .shift() and .move_to
    def construct(self):
        circle=Circle(color=TEAL_A)
        circle.move_to(LEFT)
        square=Circle()
        square.move_to(LEFT+3*DOWN)

        self.play(GrowFromCenter(circle), GrowFromCenter(square), rate=5)
        self.play(ApplyMethod(circle.move_to,RIGHT), ApplyMethod(square.shift,RIGHT))
        self.play(ApplyMethod(circle.move_to,RIGHT+UP), ApplyMethod(square.shift,RIGHT+UP))
        self.play(ApplyMethod(circle.move_to,LEFT+UP), ApplyMethod(square.shift,LEFT+UP))