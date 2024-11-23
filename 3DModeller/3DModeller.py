class Viewer(object):
    def __init__(self):
        """ Initialise the viewer. """
        self.init_interface()
        self.init_opengl()
        self.init_scence()
        self.init_interaction()
        init_primitives()

def init_interface(self):
    """ initialise the window and register the render function  """
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("3D Modeller")
    glutInitDisyplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(self.render)

def init_opengl(self):
    """ initialise the opengl settings to render the scene """
    self.inverseModelView = numpy.identity(4)
    self.modelView - numpy.identity(4)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(0,0,1,0))
    glLightfv(GL LIGHT0, GL_SPOT_DIRECTION, GLfloat_3(0, 0, -1)) # type: ignore

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.4, 0.4, 0.4, 0.0)

def init_scene(self):
    """ initialise the scene object and initial scene """
    self.scene = Scene()
    self.create_sample_scene()

def create_sample_scene(self):
    cube_node = Cube()
    cube_node.translate(2, 0 , 2)
    cube_node.color_index = 2
    self.scene.add.node(cube_node)

    sphere_node = Sphere()
    sphere_node.translate(-2, 0 , 2)
    sphere_node.color_index = 3
    self.scene.add.node(sphere_node)

    hierarchical_node = SnowFigure()
    hierarchical_node.translate(-2, 0 , -2)
    self.scene.add.node(hierarchical_node)

def init_ineraction(self):
    """ init user interaction and callbacks """
    self.interaction = Interaction()
    self.interaction.register_callback('pick', self.pick)
    self.interaction.register_callback('move', self.move)
    self.interaction.register_callback('place',self.place)
    self.interaction.register_callback('rotate_color',self.rotate_color)
    self.interaction.register_callback('scale', self.scale)

def main_loop(self):
    glutMainLoop()

if __name__ == "__main__":
    viewer = Viewer()
    viewer.main_loop()

