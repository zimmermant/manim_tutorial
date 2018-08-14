from big_ol_pile_of_manim_imports import *

HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3


class StickMan(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "propagate_style_to_family" : True,
        "height" : 3,
        "corner_scale_factor" : 0.75,
        "flip_at_start" : False,
        "is_looking_direction_purposeful" : False,
        "start_corner" : None,
        #Range of proportions along body where arms are
        "right_arm_range" : [0.55, 0.7],
        "left_arm_range" : [.34, .462],
    }
    def __init__(self, mode = "plain", **kwargs):
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR, 
                "stick_man_%s.svg"%mode
            )
            SVGMobject.__init__(self, file_name = svg_file, **kwargs)
        except:
            warnings.warn("No StickMan design with mode %s"%mode)
            svg_file = os.path.join(
                SVG_IMAGE_DIR, 
                "stick_man.svg"
            )
            SVGMobject.__init__(self, file_name = svg_file, **kwargs)

        if self.flip_at_start:
            self.flip()
        if self.start_corner is not None:
            self.to_corner(self.start_corner)

    def name_parts(self):
        #self.mouth = self.submobjects[MOUTH_INDEX]
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.head.set_fill(RED, opacity = 0)
        self.body.set_fill(self.color, opacity = 1)
        self.arms.set_fill(YELLOW, opacity = 0)
        self.legs.set_fill(GREEN, opacity = 0)
        return self




class SVGTest2(Scene):
	def construct(self):
		start_man = StickMan()
		#comp = Laptop().move_to(2*RIGHT)
		plain_man = StickMan()
		waving_man = StickMan("wave1")

		self.add(start_man)
		self.wait()
		self.play(Transform(start_man,waving_man))
		self.play(Transform(start_man,plain_man))
		#self.add(comp)

		self.wait()


class CirclesAndSquares(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "propagate_style_to_family" : True,
        "height" : 3,
        "corner_scale_factor" : 0.75,
        "flip_at_start" : False,
        "is_looking_direction_purposeful" : False,
        "start_corner" : None,
        "circle_index" : 0,
        "line1_index" :1,
        "line2_index" : 2,
        "square1_index" : 3,
        "square2_index" : 4,
    }
    def __init__(self, mode = "plain", **kwargs):
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR, 
                "circles_and_squares_%s.svg"%mode
            )
            SVGMobject.__init__(self, file_name = svg_file, **kwargs)
        except:
            warnings.warn("No other mode design with mode %s"%mode)
            svg_file = os.path.join(
                SVG_IMAGE_DIR, 
                "circles_and_squares.svg"
            )
            SVGMobject.__init__(self, file_name = svg_file, **kwargs)


    def name_parts(self):
        self.circle = self.submobjects[self.circle_index]
        self.line1 = self.submobjects[self.line1_index]
        self.line2 = self.submobjects[self.line2_index]
        self.square1 = self.submobjects[self.square1_index]
        self.square2 = self.submobjects[self.square2_index]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        self.name_parts()
        self.circle.set_fill(RED, opacity = 1)
        self.line1.set_fill(self.color, opacity = 0)
        self.line2.set_fill(self.color, opacity = 0)
        self.square1.set_fill(GREEN, opacity = 1)
        self.square2.set_fill(BLUE, opacity = 1)
        return self


class SVGTest3(Scene):
	def construct(self):
		thingy = CirclesAndSquares()

		self.add(thingy)
		self.wait()
       
