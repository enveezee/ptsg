#!/usr/bin/env python3
#
#   PTSG - Python Turtle SimpleGUI
#
from inspect import signature
import turtle

import PySimpleGUI as sg


class SimpleTurtle():
    '''The SimpleTurtle class implements an easy to use graphical interface to
    the turtle module.

     This class aims to be highly flexible, allowing you to easily tweak the
    settings used to create a turtle GUI to suit your testing needs.
    '''
    def __init__(self, **kwargs):
        '''Initialize a SimpleTurtle instance.

         If you pass a layout parameter, that will be the layout for the GUI of
        the main window, and all the default UI elements will be ignored.

         If you merely want to configure various individual elements of the GUI
        try passing "elementArgs" which will be passed as additional arguments 
        to the individual UI elements. For example to configure the canvas in 
        the default UI layout, just pass a dict containing arguments as 
        canvasArgs.

         If however you want to remove or re-arrange rows of the default GUI
        layout while still using others, pass a rows argument as a list of the
        default layout rows you want to use in the order you want them shown.

         Furthermore if you want to customize the layout of individual rows,
        the following arguments are customizable portions of the default GUI:

            menubar     the pulldown menu bar at the top of the window.
            toolbar     the toolbar which is a customizable column.
            controls    the turtle controls which is a second such column.
            windowmenu  the right-click context menu shown on right click.

        You may also pass title and icon arguments to customize the titlebar.
        '''
        if not 'layout' in kwargs:
            # Control tabs:
            ctrlTabs = {
                'Movement': {
                    'element_justification': 'center',
                    'k': '_Movement_',
                    'layout': [
                        [
                            sg.Button('Left'),
                            sg.Button('Forward'),
                            sg.Button('Right'),
                            sg.Button('Back'),
                        ],
                        [
                            sg.Text('Distance:'),
                            sg.Spin(
                                list(range(1,1001)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=10,
                                k='_distance_',
                            ),
                            sg.Text('Rotation:'),
                            sg.Spin(
                                list(range(1,91)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=45,
                                k='_rotation_',
                            ),
                            sg.Text('Speed:'),
                            sg.Spin(
                                list(range(1,101)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=10,
                                k='_speed_',
                            ),
                        ],
                    ],
                },                
                'Pen': {
                    'element_justification': 'center',
                    'k': '_Pen_',
                    'layout': [
                        [
                            sg.Button('Pen Up'),
                            sg.Button('Pen Down'),
                            sg.Text('Color:'),
                            sg.Combo(
                                ['Black', 'Blue', 'Red', 'Green', 'Pink', 
                                'Yellow', 'Purple', 'Orange', 'Brown', 'Gray',
                                'Brown', 'White'],
                                auto_size_text=True,
                                default_value='Black',
                                enable_events=True,
                                k='_pencolor_',
                            ),
                            sg.Text('Fill:'),
                            sg.Combo(
                                ['Black', 'Blue', 'Red', 'Green', 'Pink', 
                                'Yellow', 'Purple', 'Orange', 'Brown', 'Gray',
                                'Brown', 'White'],
                                auto_size_text=True,
                                default_value='Gray',
                                enable_events=True,
                                k='_fillcolor_',
                            ),
                           sg.Text('Size:'),
                            sg.Spin(
                                list(range(1,11)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=1,
                                k='_pensize_',
                            ),
                        ],
                    ],
                },
                'Turtle': {
                    'element_justification': 'center',
                    'k': '_Turtle_',
                    'layout': [
                        [
                            sg.Button('Hide'),
                            sg.Button('Show'),
                            sg.Text('Shape:'),
                            sg.Combo(
                                ['arrow', 'circle', 'classic', 
                                'square', 'triangle', 'turtle'],
                                auto_size_text=True,
                                default_value='classic',
                                enable_events=True,
                                k='_shape_',
                            ),
                            sg.Text('Turtle:'),
                            sg.Combo(
                                ['default'],
                                auto_size_text=True,
                                default_value='default',
                                enable_events=True,
                                k='_turtle_',
                            ),
                        ],
                    ],
                },
            }

            # Deafult arguments.
            args = {
                'window': {
                    'element_justification': 'center',
                    'finalize': True,
                    'resizable': True,
                    'title': 'Python Turtle SimpleGUI',
                },
                'banner': {
                    'auto_size_text': True,
                    'border_width': 1,
                    'justification': 'center',
                    'k': '_banner_',
                    'size': (90,1),
                    'text': 'Python Turtle SimpleGUI Demonstration',
                },
                'toolbar': {
                    'element_justification': 'center',
                    'expand_x': True,
                    'k': '_toolbar_',
                    'layout': [
                        [
                            sg.Text('Canvas'),
                            sg.Spin(
                                list(range(640,1360)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=640,
                                k='_canvasWidth_',
                            ),
                            sg.Text('x'),
                            sg.Spin(
                                list(range(480,1024)),
                                auto_size_text=True,
                                enable_events = True,
                                initial_value=480,
                                k='_canvasHeight_',
                            ),
                            sg.Button('Clear'),
                            sg.Button('Home'),
                        ],
                   ],
                },
                'header': {
                    'auto_size_text': True,
                    'border_width': 2,
                    'justification': 'center',
                    'size': (90,1),
                    'k': '_header_',
                    'text': 'Turtle screen',
                },
                'canvas': {
                    'k': '_canvas_',
                    'size': (640, 480),    
                },
                'footer': {
                    'auto_size_text': True,
                    'border_width': 2,
                    'justification': 'center',
                    'k': '_footer_',
                    'size': (90,1),
                    'text': '',
                },
                'controls': {
                    'element_justification': 'center',
                    'expand_x': True,
                    'k': '_controls_',
                    'layout': [
                        [
                            sg.TabGroup(
                                [
                                    [
                                    sg.Tab(
                                        'Movement',
                                        layout=ctrlTabs['Movement']['layout'],
                                        element_justification='center',
                                    ),
                                    sg.Tab(
                                        'Pen',
                                        layout=ctrlTabs['Pen']['layout'],
                                        element_justification='center',
                                    ),
                                    sg.Tab(
                                        'Turtle',
                                        layout=ctrlTabs['Turtle']['layout'],
                                        element_justification='center',
                                    ),
                                    ]
                                ],
                                tab_location='top',
                            ),
                        ],
                    ],
                },
                'cmdline': {
                    'default_value': '',
                    'enable_events': True,
                    'k': '_cmdline_',
                    'size': (80,1),
                },
                'console': {
                    'autoscroll': True,
                    'disabled': True,
                    'echo_stdout_stderr': True,
                    'k': '_console_',
                    'reroute_stderr': True,
                    'reroute_stdout': True,
                    'size': (90, 6),
                },
                'status': {
                    'auto_size_text': True,
                    'border_width': 2,
                    'justification': 'center',
                    'k': '_status_',
                    'relief': sg.RELIEF_SUNKEN,
                    'size': (90, 1)
                },
            }

            # Check for "elementArgs" and override default arguments.
            for row in args:

                if f'{row}Args' in kwargs:

                    for arg in kwargs[f'{row}Args']:
                        args[row][arg] = kwargs[f'{row}Args'][arg]
    
            # Default row layouts.
            banner =    [sg.Text(**args['banner'])]

            if not 'toolbar' in kwargs:
                toolbar = [sg.Column(**args['toolbar'])]

            header = [sg.Text(**args['header'])]
            canvas = [sg.Canvas(**args['canvas'])]
            footer = [sg.Text(**args['footer'])]

            if not 'controls' in kwargs:
                controls = [sg.Column(**args['controls'])]

            cmdline = [
                #sg.Input(**args['cmdline']),
                sg.Combo(
                    [],
                    **args['cmdline'],
                ),
                sg.Button('Run', bind_return_key=True)
            ]

            console = [sg.Multiline(**args['console'])]
            status = [sg.Text(**args['status'])]

            if not 'rows' in kwargs:
                # Default layout.
                layout = [
                    banner,
                    toolbar,
                    header,
                    canvas,
                    footer,
                    controls,
                    cmdline,
                    console,
                    status,
                ]

            else: # Load custom layout from rows argument.
                layout = []
                # Get local vars (for the default rows).
                local = locals()

                for row in rows:

                    # Load builtin default rows by name from strings.
                    if type(row) == str:
                        layout.append(local[row])

                    # Load custom row from a list into the layout.
                    elif type(row) == list:
                        layout.append(row)

        # Create the main window.
        self.window = sg.Window(layout=layout, **args['window'])
        # Create pointer to the actual canvas.
        self.canvas = self.window['_canvas_'].TKCanvas

        # Turtles and settings.
        self.turtles = {}

        # Create the default turtle.
        self.newTurtle('default')
    
        # Set default distance, rotation.
        self.distance = self.window.Element('_distance_').Get()
        self.rotation = self.window.Element('_rotation_').Get()


    def checkInt(self, arg):
        '''Check if string is an integer and do conversion'''
        if arg[0] in ['+', '-'] and arg[1:].isdigit() or arg.isdigit():
            return int(arg)

        return arg


    def config(self, element, **kwargs):
        '''Change a GUI Element's configuration.'''
        self.window.Element(element).config(**kwargs)


    def cmdline(self, cmd):
        '''Basic command string interpreter.

         This could be replaced with something more robust, but for now it does
        basic shorthand of turtle commands.'''
        tokens = cmd.strip().split(' ')
        print(f'Running command list:\n{tokens}')

        while len(tokens):
            token = tokens.pop(0)
            print(f'Processing token: {token}')

            if token in turtle.__all__:
                turtleCmd = getattr(self.turtle, token)
                takesArgs = len(signature(turtleCmd).parameters)

                if not takesArgs:
                    print(f'Calling turtle.{token}()')

                    try:
                        ret = turtleCmd()
                    except Exception as e:
                        print(e)

                    if ret:
                        print(f'{token}: {ret}')

                else:
                    args = []
                    for arg in range(takesArgs):
                        try:
                            arg = tokens.pop(0)
                        except IndexError:
                            print(
                                f'turtle.{token} takes {takesArgs} '
                                f'arguments but {len(args)} were given.'
                            )
                            self.cmdlineHistory.append(' '.join(tokens))
                        if arg in turtle.__all__:
                            print(
                                f'turtle.{token} takes {takesArgs} '
                                f'arguments but {len(args)-1} were given.'
                            )
                            tokens.append(arg)
                            self.cmdlineHistory.append(' '.join(tokens))
                        if ',' in arg:
                            splitArgs = arg.split(',')
                            tupleArgs = []

                            for arg in splitArgs:
                                tupleArgs.append(self.checkInt(arg))

                            arg = tuple(arg.split(','))

                        else:
                            arg = self.checkInt(arg)
                        args.append(arg)

                    print(f'Calling turtle.{token}() and passing {args}')

                    try:
                        turtleCmd(*args)
                    except Exception as e:
                        print(e)

            else:
                print(f'{token} is not a valid turtle command, suspending.')
                break


    def eventLoop(self):
        '''Call to read window events with the default event handler.

        Use this call if you want a truely simple turtle GUI.
        '''
        print('PGST initialized.')

        self.cmdlineHistory = []
        self.window.Element('_cmdline_').Widget.bind('<Key-Return>', self.run)

        while True:
            self.turtleStatus(self.turtle)
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 'Run':
                self.run()

            elif event in [
                'Forward', 
                'Back', 
                'Left', 
                'Right',
            ]:
                self.move(event[0])

            elif event in [
                'Pen Up', 
                'Pen Down', 
                'Hide', 
                'Show',
            ]:
                if event.startswith('Pen'):
                    cmd = ''.join(event.split(' ')).casefold()

                else:
                    cmd = f'{event.casefold()}turtle'

                turtleCmd = getattr(self.turtle, cmd)
                turtleCmd()

            elif event[0] == '_' and event[-1] == '_':
                self.widgetEvent(event, values)

            elif event in ['Clear', 'Home',]:
                turtleCmd = getattr(self.turtle, event.casefold())
                turtleCmd()


        self.window.close()
        return


    def move(self, cmd):
        '''Move the selected turtle.'''
        cmd = cmd.casefold()

        if cmd == 'f':
            self.turtle.forward(self.distance)

        elif cmd == 'b':
            self.turtle.backward(self.distance)

        elif cmd in ['r', 'l']:
            turtleCmd = getattr(self.turtle, f'{cmd}t')
            turtleCmd(self.rotation)


    def newTurtle(self, name, **kwargs):
        '''Create a new turtle.'''
        defaults = {
            'anglemode': 'deg',
            #'fillcolor': 'Gray',
            #'mode': 'logo',
            'pendown': False,
            'pencolor': 'Black',
            'shape': 'classic',
            'pensize': 1,
            'speed': 10,
        }

        self.turtles[name] = turtle.RawTurtle(self.canvas)

        for setting in defaults:

            if setting in kwargs:
                defaults[setting] = kwargs[setting]
            
            if setting == 'anglemode':
            
                if 'degrees'.startswith(defaults['anglemode']):
                    self.turtles[name].degrees()
            
                elif 'radians'.startswith(defaults['anglemode']):
                    self.turtles[name].radians()
            
            elif setting == 'pendown':

                if defaults['pendown']:
                    self.turtles[name].pendown()

                else:
                    self.turtles[name].penup()

            else:
                setTurtle = getattr(self.turtles[name], setting)
                setTurtle(defaults[setting])

        self.selectTurtle(name)


    def readEvent(self):
        '''Call to read window events for a custom event handler loop.

        Use this call if you want to handle your own events and just use this
        class to handle your GUI and Turtle creation.
        '''
        return self.window.read()


    def run(self, *args):
        cmd = self.window.Element('_cmdline_').Get()
        self.cmdlineHistory.append(cmd)
        self.cmdline(cmd)
        self.window.Element('_cmdline_').update(
            value='', 
            values=self.cmdlineHistory,
        )


    def selectTurtle(self, name):
        '''Select active turtle by name'''
        self.turtle = self.turtles[name]


    def turtleStatus(self, t):
        pen = 'Up'

        if t.isdown():
            pen = 'Down'

        pos = t.pos()
        deg = t.heading()

        self.window.Element('_status_').Update(f'[Pen {pen}] @{pos}:{deg}')


    def widgetEvent(self, event, values):
        event = event[1:-1]

        # Turtle values that get set in the class.
        if event in ['distance', 'rotation']:
            value = values[f'_{event}_']
            setattr(self, event, value)

        # Trutle values that get set in the turtle.
        elif event in ['fillcolor', 'pencolor', 'pensize', 'speed', 'shape']:
            turtleCmd = getattr(self.turtle, event)
            turtleCmd(values[f'_{event}_'])

        elif event in ['canvasWidth', 'canvasHeight']:
            self.canvas.config(
                width=values['_canvasWidth_'], 
                height=values['_canvasHeight_']
            )

        elif event == 'Return':
            print(event)
        


if __name__ == '__main__':
    '''Demonstration Mode.

     If this module is ran directly rather than being imported, then give a
    visual demonstration of the SimpleTurtle defaults.

     Below is the minimal code required to use this module once you have
    imported the SimpleTurtle class into your module.
    '''
    demo = SimpleTurtle()
    demo.eventLoop()
