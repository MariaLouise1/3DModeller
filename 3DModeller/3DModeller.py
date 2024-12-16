class Viewer(object):
    def __init__(self):
        """ Initialise the viewer. """
        self.init_interface()
        self.init_opengl()
        self.init_scene()
        self.init_interaction()
        init_primitives()

def init_interface(self):
    """ initialise the window and register the render function  """
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("3D Modeller")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
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
BEC
def init_interaction(self):
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

# class Viewer
def render(self):
    """ The render pass for the scene """
    self.init.view()

    glEnable(GL_LIGHTING)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Load the modelview matrix from the current state of the trackball
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    loc = self.interaction.translation
    glTranslated(loc[0], loc[1], loc[2])
    glMultMaxtrixf(self.interaction.trackball.matrix)

    # store the inverse of the current modelview.
    currentModelView = numpy.array(glGetFloatv(GL_MODELVIEW_MATRIX))
    self.modelView = numpy.transpose(currentModelView)
    self.inverseModelView = inv(numpy.transpose(currentModelView))

    # render the scene. This will call the render function for each object
    # in the scene
    self.scene.render()

    # draw the grid
    glDisable(GL_LIGHTING)
    glCallList(G_OBJ_PLANE)
    glPopMatrix()

    # flush the buffer so that the scene can be drawn
    glFlush()

def init_view(self):
    """ initialize the projection matrix """
    xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    aspect_ratio = float(xSize) / float(ySize)

    # load the project matrix. Always the same
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glViewport(0, 0, xSize, ySize)
    gluPerspective(70, aspect_ratio, 0.1, 1000.0)
    glTranslated(0, 0, -15)

# Class Scene

class Scene(object):

    # the default depth from the camera to place an object at PLACE_DEPTH = 15.0

    def __init__(self):
        # The scene keeps a list of nodes that are displayed
        self.node_list = list()
        # Keep track of the currently selected node.
        # Actions may depend on whether or not something is selected
        self.selected_node = None

    def add_node(self, node):
        """ Add a new node to the scene """
        self.node_list.append(node)

    def render(self):
        """ Render the scene """
        for node in self.node_list:
            node.render()

            