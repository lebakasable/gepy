from statistics import mean as _mean
import math as _math
import random as _random
import asyncio as _asyncio
import pymunk as _pymunk
import pygame.gfxdraw
import os as _os
import logging as _logging
import warnings as _warnings

import pygame
pygame.init()


class Oops(Exception):
    def __init__(self, message):
        message = '\n\n\tOops!\n\n\t'+message.replace('\n', '\n\t')+'\n'
        super(Oops, self).__init__(message)


class Hmm(UserWarning):
    pass


color_names = {
    'aliceblue':            (240, 248, 255),
    'antiquewhite':         (250, 235, 215),
    'aqua':                 (0, 255, 255),
    'aquamarine':           (127, 255, 212),
    'azure':                (240, 255, 255),
    'beige':                (245, 245, 220),
    'bisque':               (255, 228, 196),
    'black':                (0,   0,   0),
    'blanchedalmond':       (255, 235, 205),
    'blue':                 (0,   0, 255),
    'blueviolet':           (138,  43, 226),
    'brown':                (165,  42,  42),
    'burlywood':            (222, 184, 135),
    'cadetblue':            (95, 158, 160),
    'chartreuse':           (127, 255,   0),
    'chocolate':            (210, 105,  30),
    'coral':                (255, 127,  80),
    'cornflowerblue':       (100, 149, 237),
    'cornsilk':             (255, 248, 220),
    'crimson':              (220,  20,  60),
    'cyan':                 (0, 255, 255),
    'darkblue':             (0,   0, 139),
    'darkcyan':             (0, 139, 139),
    'darkgoldenrod':        (184, 134,  11),
    'darkgray':             (169, 169, 169),
    'darkgreen':            (0, 100,   0),
    'darkgrey':             (169, 169, 169),
    'darkkhaki':            (189, 183, 107),
    'darkmagenta':          (139,   0, 139),
    'darkolivegreen':       (85, 107,  47),
    'darkorange':           (255, 140,   0),
    'darkorchid':           (153,  50, 204),
    'darkred':              (139,   0,   0),
    'darksalmon':           (233, 150, 122),
    'darkseagreen':         (143, 188, 143),
    'darkslateblue':        (72,  61, 139),
    'darkslategray':        (47,  79,  79),
    'darkslategrey':        (47,  79,  79),
    'darkturquoise':        (0, 206, 209),
    'darkviolet':           (148,   0, 211),
    'deeppink':             (255,  20, 147),
    'deepskyblue':          (0, 191, 255),
    'dimgray':              (105, 105, 105),
    'dimgrey':              (105, 105, 105),
    'dodgerblue':           (30, 144, 255),
    'firebrick':            (178,  34,  34),
    'floralwhite':          (255, 250, 240),
    'forestgreen':          (34, 139,  34),
    'fuchsia':              (255,   0, 255),
    'gainsboro':            (220, 220, 220),
    'ghostwhite':           (248, 248, 255),
    'gold':                 (255, 215,   0),
    'goldenrod':            (218, 165,  32),
    'gray':                 (128, 128, 128),
    'grey':                 (128, 128, 128),
    'green':                (0, 128,   0),
    'greenyellow':          (173, 255,  47),
    'honeydew':             (240, 255, 240),
    'hotpink':              (255, 105, 180),
    'indianred':            (205,  92,  92),
    'indigo':               (75,   0, 130),
    'ivory':                (255, 255, 240),
    'khaki':                (240, 230, 140),
    'lavender':             (230, 230, 250),
    'lavenderblush':        (255, 240, 245),
    'lawngreen':            (124, 252,   0),
    'lemonchiffon':         (255, 250, 205),
    'lightblue':            (173, 216, 230),
    'lightcoral':           (240, 128, 128),
    'lightcyan':            (224, 255, 255),
    'lightgoldenrodyellow': (250, 250, 210),
    'lightgray':            (211, 211, 211),
    'lightgreen':           (144, 238, 144),
    'lightgrey':            (211, 211, 211),
    'lightpink':            (255, 182, 193),
    'lightsalmon':          (255, 160, 122),
    'lightseagreen':        (32, 178, 170),
    'lightskyblue':         (135, 206, 250),
    'lightslategray':       (119, 136, 153),
    'lightslategrey':       (119, 136, 153),
    'lightsteelblue':       (176, 196, 222),
    'lightyellow':          (255, 255, 224),
    'lime':                 (0, 255,   0),
    'limegreen':            (50, 205,  50),
    'linen':                (250, 240, 230),
    'magenta':              (255,   0, 255),
    'maroon':               (128,   0,   0),
    'mediumaquamarine':     (102, 205, 170),
    'mediumblue':           (0,   0, 205),
    'mediumorchid':         (186,  85, 211),
    'mediumpurple':         (147, 112, 219),
    'mediumseagreen':       (60, 179, 113),
    'mediumslateblue':      (123, 104, 238),
    'mediumspringgreen':    (0, 250, 154),
    'mediumturquoise':      (72, 209, 204),
    'mediumvioletred':      (199,  21, 133),
    'midnightblue':         (25,  25, 112),
    'mintcream':            (245, 255, 250),
    'mistyrose':            (255, 228, 225),
    'moccasin':             (255, 228, 181),
    'navajowhite':          (255, 222, 173),
    'navy':                 (0,   0, 128),
    'oldlace':              (253, 245, 230),
    'olive':                (128, 128,   0),
    'olivedrab':            (107, 142,  35),
    'orange':               (255, 165,   0),
    'orangered':            (255,  69,   0),
    'orchid':               (218, 112, 214),
    'palegoldenrod':        (238, 232, 170),
    'palegreen':            (152, 251, 152),
    'paleturquoise':        (175, 238, 238),
    'palevioletred':        (219, 112, 147),
    'papayawhip':           (255, 239, 213),
    'peachpuff':            (255, 218, 185),
    'peru':                 (205, 133,  63),
    'pink':                 (255, 192, 203),
    'plum':                 (221, 160, 221),
    'powderblue':           (176, 224, 230),
    'purple':               (128,   0, 128),
    'red':                  (255,   0,   0),
    'rosybrown':            (188, 143, 143),
    'royalblue':            (65, 105, 225),
    'saddlebrown':          (139,  69,  19),
    'salmon':               (250, 128, 114),
    'sandybrown':           (244, 164,  96),
    'seagreen':             (46, 139,  87),
    'seashell':             (46, 139,  87),
    'sienna':               (160,  82,  45),
    'silver':               (192, 192, 192),
    'skyblue':              (135, 206, 235),
    'slateblue':            (106,  90, 205),
    'slategray':            (112, 128, 144),
    'slategrey':            (112, 128, 144),
    'snow':                 (255, 250, 250),
    'springgreen':          (0, 255, 127),
    'steelblue':            (70, 130, 180),
    'tan':                  (210, 180, 140),
    'teal':                 (0, 128, 128),
    'thistle':              (216, 191, 216),
    'tomato':               (255,  99,  71),
    'turquoise':            (64, 224, 208),
    'violet':               (238, 130, 238),
    'wheat':                (245, 222, 179),
    'white':                (255, 255, 255),
    'whitesmoke':           (245, 245, 245),
    'yellow':               (255, 255,   0),
    'yellowgreen':          (154, 205,  50),
    'transparent':          (0,   0,   0, 0),
}


def _color_name_to_rgb(name):
    if type(name) == tuple:
        return name

    try:
        return color_names[name.lower().strip().replace('-', '').replace(' ', '')]
    except KeyError as exception:
        raise Oops(f"""You gave a color name we didn't understand: '{name}'
If this our mistake, please let us know. Otherwise, try using the RGB number form of the color e.g. '(0, 255, 255)'.
You can find the RGB form of a color on websites like this: https://www.rapidtables.com/web/color/RGB_Color.html\n""") from exception


keypress_map = {
    pygame.K_BACKSPACE: 'backspace',
    pygame.K_TAB: 'tab',
    pygame.K_CLEAR: 'clear',
    pygame.K_RETURN: 'enter',
    pygame.K_PAUSE: 'pause',
    pygame.K_ESCAPE: 'escape',
    pygame.K_SPACE: 'space',
    pygame.K_EXCLAIM: '!',
    pygame.K_QUOTEDBL: '"',
    pygame.K_HASH: '#',
    pygame.K_DOLLAR: '$',
    pygame.K_AMPERSAND: '&',
    pygame.K_QUOTE: "'",
    pygame.K_LEFTPAREN: '(',
    pygame.K_RIGHTPAREN: ')',
    pygame.K_ASTERISK: '*',
    pygame.K_PLUS: '+',
    pygame.K_COMMA: ',',
    pygame.K_MINUS: '-',
    pygame.K_PERIOD: '.',
    pygame.K_SLASH: '/',
    pygame.K_0: '0',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9',
    pygame.K_COLON: ':',
    pygame.K_SEMICOLON: ';',
    pygame.K_LESS: '<',
    pygame.K_EQUALS: '=',
    pygame.K_GREATER: '>',
    pygame.K_QUESTION: '?',
    pygame.K_AT: '@',
    pygame.K_LEFTBRACKET: '[',
    pygame.K_BACKSLASH: '\\',
    pygame.K_RIGHTBRACKET: ']',
    pygame.K_CARET: '^',
    pygame.K_UNDERSCORE: '_',
    pygame.K_BACKQUOTE: '`',
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z',
    pygame.K_DELETE: 'delete',
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
    pygame.K_RIGHT: 'right',
    pygame.K_LEFT: 'left',
    pygame.K_INSERT: 'insert',
    pygame.K_HOME: 'home',
    pygame.K_END: 'end',
    pygame.K_PAGEUP: 'pageup',
    pygame.K_PAGEDOWN: 'pagedown',
    pygame.K_F1: 'F1',
    pygame.K_F2: 'F2',
    pygame.K_F3: 'F3',
    pygame.K_F4: 'F4',
    pygame.K_F5: 'F5',
    pygame.K_F6: 'F6',
    pygame.K_F7: 'F7',
    pygame.K_F8: 'F8',
    pygame.K_F9: 'F9',
    pygame.K_F10: 'F10',
    pygame.K_F11: 'F11',
    pygame.K_F12: 'F12',
    pygame.K_F13: 'F13',
    pygame.K_F14: 'F14',
    pygame.K_F15: 'F15',
    pygame.K_NUMLOCK: 'numlock',
    pygame.K_CAPSLOCK: 'capslock',
    pygame.K_SCROLLOCK: 'scrollock',
    pygame.K_RSHIFT: 'shift',
    pygame.K_LSHIFT: 'shift',
    pygame.K_RCTRL: 'control',
    pygame.K_LCTRL: 'control',
    pygame.K_RALT: 'alt',
    pygame.K_LALT: 'alt',
    pygame.K_RMETA: 'meta',
    pygame.K_LMETA: 'meta',
    pygame.K_LSUPER: 'super',
    pygame.K_RSUPER: 'super',
    pygame.K_EURO: '€',
}


def _pygame_key_to_name(pygame_key_event):
    english_name = keypress_map[pygame_key_event.key]
    if not pygame_key_event.mod and len(english_name) > 1:
        return english_name
    return pygame_key_event.unicode


def _clamp(num, min_, max_):
    if num < min_:
        return min_
    elif num > max_:
        return max_
    return num


def _point_touching_sprite(point, sprite):
    return sprite.left <= point.x <= sprite.right and sprite.bottom <= point.y <= sprite.top


def _sprite_touching_sprite(a, b):
    if a.left >= b.right or a.right <= b.left or a.top <= b.bottom or a.bottom >= b.top:
        return False
    return True


class _screen(object):
    def __init__(self, width=800, height=600):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, _width):
        self._width = _width

        _remove_walls()
        _create_walls()

        pygame.display.set_mode((self._width, self._height))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, _height):
        self._height = _height

        _remove_walls()
        _create_walls()

        pygame.display.set_mode((self._width, self._height))

    @property
    def top(self):
        return self.height / 2

    @property
    def bottom(self):
        return self.height / -2

    @property
    def left(self):
        return self.width / -2

    @property
    def right(self):
        return self.width / 2


screen = _screen()


_pygame_display = pygame.display.set_mode(
    (screen.width, screen.height), pygame.DOUBLEBUF)
pygame.display.set_caption("Gepy")


class _mouse(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self._is_clicked = False
        self._when_clicked_callbacks = []
        self._when_click_released_callbacks = []

    @property
    def is_clicked(self):
        return self._is_clicked

    def is_touching(self, other):
        return _point_touching_sprite(self, other)

    def when_clicked(self, func):
        async_callback = _make_async(func)

        async def wrapper():
            await async_callback()
        self._when_clicked_callbacks.append(wrapper)
        return wrapper

    def when_click_released(self, func):
        async_callback = _make_async(func)

        async def wrapper():
            await async_callback()
        self._when_click_released_callbacks.append(wrapper)
        return wrapper

    def distance_to(self, x=None, y=None):
        assert (not x is None)

        try:

            x = x.x
            y = x.y
        except AttributeError:
            x = x
            y = y

        dx = self.x - x
        dy = self.y - y

        return _math.sqrt(dx**2 + dy**2)


def when_mouse_clicked(func):
    return mouse.when_clicked(func)


def when_click_released(func):
    return mouse.when_click_released(func)


mouse = _mouse()


all_sprites = []

_debug = True


def debug(on_or_off):
    global _debug
    if on_or_off == 'on':
        _debug = True
    elif on_or_off == 'off':
        _debug = False


backdrop = (255, 255, 255)


def set_backdrop(color_or_image_name):
    global backdrop

    _color_name_to_rgb(color_or_image_name)

    backdrop = color_or_image_name


def random_number(lowest=0, highest=100):
    if type(lowest) == int and type(highest) == int:
        return _random.randint(lowest, highest)
    else:

        return round(_random.uniform(lowest, highest), 2)


def random_color():
    return (random_number(0, 255), random_number(0, 255), random_number(0, 255))


class _Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, indices):
        if indices == 0:
            return self.x
        elif indices == 1:
            return self.y
        raise IndexError()

    def __iter__(self):
        yield self.x
        yield self.y

    def __len__(self):
        return 2

    def __setitem__(self, i, value):
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        else:
            raise IndexError()


def random_position():
    return _Position(
        random_number(screen.left, screen.right),
        random_number(screen.bottom, screen.top)
    )


def _raise_on_await_warning(func):
    async def f(*args, **kwargs):
        with _warnings.catch_warnings(record=True) as w:
            await func(*args, **kwargs)
            for warning in w:

                str_message = warning.message.args[0]
                if 'was never awaited' in str_message:
                    unawaited_function_name = str_message.split("'")[1]
                    raise Oops(f"""Looks like you forgot to put "await" before ge.{unawaited_function_name} on line {warning.lineno} of file {warning.filename}.
To fix this, just add the word 'await' before ge.{unawaited_function_name} on line {warning.lineno} of file {warning.filename} in the function {func.__name__}.""")
                else:
                    print(warning.message)
    return f


def _make_async(func):
    if _asyncio.iscoroutinefunction(func):

        return _raise_on_await_warning(func)

    @_raise_on_await_warning
    async def async_func(*args, **kwargs):
        return func(*args, **kwargs)
    return async_func


class _MetaGroup(type):
    def __iter__(cls):
        for item in cls.__dict__.values():
            if isinstance(item, Sprite):
                yield item

    def __getattr__(cls, attr):
        def f(*args, **kwargs):
            results = []
            for sprite in cls:
                result = getattr(sprite, attr)
                if callable(result):
                    result(*args, **kwargs)
                else:
                    results.append(attr)
            if results:
                return results
        return f

    @property
    def x(cls):
        return _mean(sprite.x for sprite in cls)

    @x.setter
    def x(cls, new_x):
        x_offset = new_x - cls.x
        for sprite in cls:
            sprite.x += x_offset

    @property
    def y(cls):
        return _mean(sprite.y for sprite in cls)

    @y.setter
    def y(cls, new_y):
        y_offset = new_y - cls.y
        for sprite in cls:
            sprite.y += y_offset


class Group(metaclass=_MetaGroup):
    def __init__(self, *sprites):
        self.sprites_ = sprites

    @classmethod
    def sprites(cls):
        for item in cls.__dict__.values():

            if isinstance(item, Sprite):
                yield item

    def sprites(self):
        for sprite in self.sprites_:
            yield sprite
        print(self.__class__.sprites)
        for sprite in type(self).sprites():
            yield sprite

    def __iter__(self):
        for sprite in self.sprites:
            yield sprite

    def go_to(self, x_or_sprite, y):
        try:
            x = x_or_sprite.x
            y = x_or_sprite.y
        except AttributeError:
            x = x_or_sprite
            y = y

        max_x = max(sprite.x for sprite in self)
        min_x = min(sprite.x for sprite in self)
        max_y = max(sprite.y for sprite in self)
        min_y = min(sprite.y for sprite in self)

        center_x = (max_x - min_x) / 2
        center_y = (min_y - max_y) / 2
        offset_x = x - center_x
        offset_y = y - center_y

        for sprite in self:
            sprite.x += offset_x
            sprite.y += offset_y

    @property
    def right(self):
        return max(sprite.right for sprite in self)

    @property
    def left(self):
        return min(sprite.left for sprite in self)

    @property
    def width(self):
        return self.right - self.left


def new_group(*sprites):
    return Group(*sprites)


def new_image(image=None, x=0, y=0, size=100, angle=0, transparency=100):
    return Sprite(image=image, x=x, y=y, size=size, angle=angle, transparency=transparency)


class Sprite(object):
    def __init__(self, image=None, x=0, y=0, size=100, angle=0, transparency=100):
        self._image = image
        self._x = x
        self._y = y
        self._angle = angle
        self._size = size
        self._transparency = transparency

        self.physics = None
        self._is_clicked = False
        self._is_hidden = False

        self._compute_primary_surface()

        self._when_clicked_callbacks = []

        all_sprites.append(self)

    def _compute_primary_surface(self):
        try:
            self._primary_pygame_surface = pygame.image.load(
                _os.path.join(self._image))
        except pygame.error as exc:
            raise Oops(f"""We couldn't find the image file you provided named "{self._image}".
If the file is in a folder, make sure you add the folder name, too.""") from exc
        self._primary_pygame_surface.set_colorkey(
            (255, 255, 255, 255))

        self._should_recompute_primary_surface = False

        self._compute_secondary_surface(force=True)

    def _compute_secondary_surface(self, force=False):
        self._secondary_pygame_surface = self._primary_pygame_surface.copy()

        if self._transparency != 100 or force:
            try:

                array = pygame.surfarray.pixels_alpha(
                    self._secondary_pygame_surface)

                array[:, :] = (
                    array[:, :] * (self._transparency/100.)).astype(array.dtype)
                del array
            except Exception as e:

                self._secondary_pygame_surface.set_alpha(
                    round((self._transparency/100.) * 255))

        if (self.size != 100) or force:
            ratio = self.size/100.
            self._secondary_pygame_surface = pygame.transform.scale(
                self._secondary_pygame_surface,
                (round(self._secondary_pygame_surface.get_width() * ratio),
                 round(self._secondary_pygame_surface.get_height() * ratio)))

        if (self.angle != 0) or force:
            self._secondary_pygame_surface = pygame.transform.rotate(
                self._secondary_pygame_surface, self._angle)

        self._should_recompute_secondary_surface = False

    @property
    def is_clicked(self):
        return self._is_clicked

    def move(self, steps=3):
        angle = _math.radians(self.angle)
        self.x += steps * _math.cos(angle)
        self.y += steps * _math.sin(angle)

    def turn(self, degrees=10):
        self.angle += degrees

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, _x):
        prev_x = self._x
        self._x = _x
        if self.physics:
            self.physics._pymunk_body.position = self._x, self._y
            if prev_x != _x:

                self.physics._pymunk_body.velocity = _x - \
                    prev_x, self.physics._pymunk_body.velocity.y
            if self.physics._pymunk_body.body_type == _pymunk.Body.STATIC:
                _physics_space.reindex_static()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, _y):
        prev_y = self._y
        self._y = _y
        if self.physics:
            self.physics._pymunk_body.position = self._x, self._y
            if prev_y != _y:

                self.physics._pymunk_body.velocity = self.physics._pymunk_body.velocity.x, _y - prev_y
            if self.physics._pymunk_body.body_type == _pymunk.Body.STATIC:
                _physics_space.reindex_static()

    @property
    def transparency(self):
        return self._transparency

    @transparency.setter
    def transparency(self, alpha):
        if not isinstance(alpha, float) and not isinstance(alpha, int):
            raise Oops(f"""Looks like you're trying to set {self}'s transparency to '{alpha}', which isn't a number.
Try looking in your code for where you're setting transparency for {self} and change it a number.
""")
        if alpha > 100 or alpha < 0:
            _warnings.warn(f"""The transparency setting for {self} is being set to {alpha} and it should be between 0 and 100.
You might want to look in your code where you're setting transparency and make sure it's between 0 and 100.  """, Hmm)

        self._transparency = _clamp(alpha, 0, 100)
        self._should_recompute_secondary_surface = True

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image_filename):
        self._image = image_filename
        self._should_recompute_primary_surface = True

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, _angle):
        self._angle = _angle
        self._should_recompute_secondary_surface = True

        if self.physics:
            self.physics._pymunk_body.angle = _math.radians(_angle)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, percent):
        self._size = percent
        self._should_recompute_secondary_surface = True
        if self.physics:
            self.physics._remove()
            self.physics._make_pymunk()

    def hide(self):
        self._is_hidden = True
        if self.physics:
            self.physics.pause()

    def show(self):
        self._is_hidden = False
        if self.physics:
            self.physics.unpause()

    @property
    def is_hidden(self):
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, hide):
        self._is_hidden = hide

    @property
    def is_shown(self):
        return not self._is_hidden

    @is_shown.setter
    def is_shown(self, show):
        self._is_hidden = not show

    def is_touching(self, sprite_or_point):
        rect = self._secondary_pygame_surface.get_rect()
        if isinstance(sprite_or_point, Sprite):
            return _sprite_touching_sprite(sprite_or_point, self)
        else:
            return _point_touching_sprite(sprite_or_point, self)

    def point_towards(self, x, y=None):
        try:
            x, y = x.x, x.y
        except AttributeError:
            x, y = x, y
        self.angle = _math.degrees(_math.atan2(y-self.y, x-self.x))

    def go_to(self, x=None, y=None):
        assert (not x is None)

        try:

            self.x = x.x
            self.y = x.y
        except AttributeError:
            self.x = x
            self.y = y

    def distance_to(self, x, y=None):
        assert (not x is None)

        try:

            x1 = x.x
            y1 = x.y
        except AttributeError:
            x1 = x
            y1 = y

        dx = self.x - x1
        dy = self.y - y1

        return _math.sqrt(dx**2 + dy**2)

    def remove(self):
        if self.physics:
            self.physics._remove()
        all_sprites.remove(self)

    @property
    def width(self):
        return self._secondary_pygame_surface.get_width()

    @property
    def height(self):
        return self._secondary_pygame_surface.get_height()

    @property
    def right(self):
        return self.x + self.width/2

    @right.setter
    def right(self, x):
        self.x = x - self.width/2

    @property
    def left(self):
        return self.x - self.width/2

    @left.setter
    def left(self, x):
        self.x = x + self.width/2

    @property
    def top(self):
        return self.y + self.height/2

    @top.setter
    def top(self, y):
        self.y = y - self.height/2

    @property
    def bottom(self):
        return self.y - self.height/2

    @bottom.setter
    def bottom(self, y):
        self.y = y + self.height/2

    def _pygame_x(self):
        return self.x + (screen.width/2.) - (self._secondary_pygame_surface.get_width()/2.)

    def _pygame_y(self):
        return (screen.height/2.) - self.y - (self._secondary_pygame_surface.get_height()/2.)

    def when_clicked(self, callback, call_with_sprite=False):
        async_callback = _make_async(callback)

        async def wrapper():
            wrapper.is_running = True
            if call_with_sprite:
                await async_callback(self)
            else:
                await async_callback()
            wrapper.is_running = False
        wrapper.is_running = False
        self._when_clicked_callbacks.append(wrapper)
        return wrapper

    def _common_properties(self):
        return {'x': self.x, 'y': self.y, 'size': self.size, 'transparency': self.transparency, 'angle': self.angle}

    def clone(self):
        return self.__class__(image=self.image, **self._common_properties())

    def start_physics(self, can_move=True, stable=False, x_speed=0, y_speed=0, obeys_gravity=True, bounciness=1.0, mass=10, friction=0.1):
        if not self.physics:
            self.physics = _Physics(
                self,
                can_move,
                stable,
                x_speed,
                y_speed,
                obeys_gravity,
                bounciness,
                mass,
                friction,
            )

    def stop_physics(self):
        self.physics._remove()
        self.physics = None


_SPEED_MULTIPLIER = 10


class _Physics(object):

    def __init__(self, sprite, can_move, stable, x_speed, y_speed, obeys_gravity, bounciness, mass, friction):
        self.sprite = sprite
        self._can_move = can_move
        self._stable = stable
        self._x_speed = x_speed * _SPEED_MULTIPLIER
        self._y_speed = y_speed * _SPEED_MULTIPLIER
        self._obeys_gravity = obeys_gravity
        self._bounciness = bounciness
        self._mass = mass
        self._friction = friction

        self._make_pymunk()

    def _make_pymunk(self):
        mass = self.mass if self.can_move else 0

        if not self.can_move and isinstance(self.sprite, line):
            self._pymunk_body = _physics_space.static_body.copy()
            self._pymunk_shape = _pymunk.Segment(
                self._pymunk_body, (self.sprite.x, self.sprite.y), (self.sprite.x1, self.sprite.y1), self.sprite.thickness)
        else:
            if self.stable:
                moment = _pymunk.inf
            elif isinstance(self.sprite, Circle):
                moment = _pymunk.moment_for_circle(
                    mass, 0, self.sprite.radius, (0, 0))
            elif isinstance(self.sprite, line):
                moment = _pymunk.moment_for_box(
                    mass, (self.sprite.length, self.sprite.thickness))
            else:
                moment = _pymunk.moment_for_box(
                    mass, (self.sprite.width, self.sprite.height))

            if self.can_move and not self.stable:
                body_type = _pymunk.Body.DYNAMIC
            elif self.can_move and self.stable:
                if self.obeys_gravity or _physics_space.gravity == 0:
                    body_type = _pymunk.Body.DYNAMIC
                else:
                    body_type = _pymunk.Body.KINEMATIC
            else:
                body_type = _pymunk.Body.STATIC
            self._pymunk_body = _pymunk.Body(mass, moment, body_type=body_type)

            if isinstance(self.sprite, line):
                self._pymunk_body.position = self.sprite.x + \
                    (self.sprite.x1 - self.sprite.x)/2, self.sprite.y + \
                    (self.sprite.y1 - self.sprite.y)/2
            else:
                self._pymunk_body.position = self.sprite.x, self.sprite.y

            self._pymunk_body.angle = _math.radians(self.sprite.angle)

            if self.can_move:
                self._pymunk_body.velocity = (self._x_speed, self._y_speed)

            if not self.obeys_gravity:
                self._pymunk_body.velocity_func = lambda body, gravity, damping, dt: None

            if isinstance(self.sprite, Circle):
                self._pymunk_shape = _pymunk.Circle(
                    self._pymunk_body, self.sprite.radius, (0, 0))
            elif isinstance(self.sprite, line):
                self._pymunk_shape = _pymunk.Segment(
                    self._pymunk_body, (self.sprite.x, self.sprite.y), (self.sprite.x1, self.sprite.y1), self.sprite.thickness)
            else:
                self._pymunk_shape = _pymunk.Poly.create_box(
                    self._pymunk_body, (self.sprite.width, self.sprite.height))

        self._pymunk_shape.elasticity = _clamp(self.bounciness, 0, .99)
        self._pymunk_shape.friction = self._friction
        _physics_space.add(self._pymunk_body, self._pymunk_shape)

    def clone(self, sprite):
        return self.__class__(sprite=sprite, can_move=self.can_move, x_speed=self.x_speed,
                              y_speed=self.y_speed, obeys_gravity=self.obeys_gravity)

    def pause(self):
        self._remove()

    def unpause(self):
        if not self._pymunk_body and not self._pymunk_shape:
            _physics_space.add(self._pymunk_body, self._pymunk_shape)

    def _remove(self):
        if self._pymunk_body:
            _physics_space.remove(self._pymunk_body)
        if self._pymunk_shape:
            _physics_space.remove(self._pymunk_shape)

    @property
    def can_move(self):
        return self._can_move

    @can_move.setter
    def can_move(self, _can_move):
        prev_can_move = self._can_move
        self._can_move = _can_move
        if prev_can_move != _can_move:
            self._remove()
            self._make_pymunk()

    @property
    def x_speed(self):
        return self._x_speed / _SPEED_MULTIPLIER

    @x_speed.setter
    def x_speed(self, _x_speed):
        self._x_speed = _x_speed * _SPEED_MULTIPLIER
        self._pymunk_body.velocity = self._x_speed, self._pymunk_body.velocity[1]

    @property
    def y_speed(self):
        return self._y_speed / _SPEED_MULTIPLIER

    @y_speed.setter
    def y_speed(self, _y_speed):
        self._y_speed = _y_speed * _SPEED_MULTIPLIER
        self._pymunk_body.velocity = self._pymunk_body.velocity[0], self._y_speed

    @property
    def bounciness(self):
        return self._bounciness

    @bounciness.setter
    def bounciness(self, _bounciness):
        self._bounciness = _bounciness
        self._pymunk_shape.elasticity = _clamp(self._bounciness, 0, .99)

    @property
    def stable(self):
        return self._stable

    @stable.setter
    def stable(self, _stable):
        prev_stable = self._stable
        self._stable = _stable
        if self._stable != prev_stable:
            self._remove()
            self._make_pymunk()

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, _mass):
        self._mass = _mass
        self._pymunk_body.mass = _mass

    @property
    def obeys_gravity(self):
        return self._obeys_gravity

    @obeys_gravity.setter
    def obeys_gravity(self, _obeys_gravity):
        self._obeys_gravity = _obeys_gravity
        if _obeys_gravity:
            self._pymunk_body.velocity_func = _pymunk.Body.update_velocity
        else:
            self._pymunk_body.velocity_func = lambda body, gravity, damping, dt: None


class _Gravity(object):

    vertical = -100 * _SPEED_MULTIPLIER
    horizontal = 0


gravity = _Gravity()
_physics_space = _pymunk.Space()
_physics_space.sleep_time_threshold = 0.5

_physics_space.idle_speed_threshold = 0
_physics_space.gravity = gravity.horizontal, gravity.vertical


def set_gravity(vertical=-100, horizontal=None):
    global gravity
    gravity.vertical = vertical*_SPEED_MULTIPLIER
    if horizontal != None:
        gravity.horizontal = horizontal*_SPEED_MULTIPLIER

    _physics_space.gravity = gravity.horizontal, gravity.vertical


def _create_wall(a, b):
    segment = _pymunk.Segment(_physics_space.static_body, a, b, 0.0)
    segment.elasticity = 1.0
    segment.friction = .1
    _physics_space.add(segment)
    return segment


_walls = []


def _create_walls():
    _walls.append(_create_wall([screen.left, screen.top], [
                  screen.right, screen.top]))
    _walls.append(_create_wall([screen.left, screen.bottom], [
                  screen.right, screen.bottom]))
    _walls.append(_create_wall([screen.left, screen.bottom], [
                  screen.left, screen.top]))
    _walls.append(_create_wall([screen.right, screen.bottom], [
                  screen.right, screen.top]))


_create_walls()


def _remove_walls():
    _physics_space.remove(_walls)
    _walls.clear()


def new_box(color='black', x=0, y=0, width=100, height=200, border_color='light blue', border_width=0, angle=0, transparency=100, size=100):
    return Box(color=color, x=x, y=y, width=width, height=height, border_color=border_color, border_width=border_width, angle=angle, transparency=transparency, size=size)


class Box(Sprite):
    def __init__(self, color='black', x=0, y=0, width=100, height=200, border_color='light blue', border_width=0, transparency=100, size=100, angle=0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._border_color = border_color
        self._border_width = border_width

        self._transparency = transparency
        self._size = size
        self._angle = angle
        self._is_clicked = False
        self._is_hidden = False
        self.physics = None

        self._when_clicked_callbacks = []

        self._compute_primary_surface()

        all_sprites.append(self)

    def _compute_primary_surface(self):
        self._primary_pygame_surface = pygame.Surface(
            (self._width, self._height), pygame.SRCALPHA)

        if self._border_width and self._border_color:

            self._primary_pygame_surface.fill(
                _color_name_to_rgb(self._border_color))

            pygame.draw.rect(self._primary_pygame_surface, _color_name_to_rgb(self._color), (self._border_width,
                             self._border_width, self._width-2*self._border_width, self._height-2*self.border_width))

        else:
            self._primary_pygame_surface.fill(_color_name_to_rgb(self._color))

        self._should_recompute_primary_surface = False
        self._compute_secondary_surface(force=True)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, _width):
        self._width = _width
        self._should_recompute_primary_surface = True

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, _height):
        self._height = _height
        self._should_recompute_primary_surface = True

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, _color):
        self._color = _color
        self._should_recompute_primary_surface = True

    @property
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, _border_color):
        self._border_color = _border_color
        self._should_recompute_primary_surface = True

    @property
    def border_width(self):
        return self._border_width

    @border_width.setter
    def border_width(self, _border_width):
        self._border_width = _border_width
        self._should_recompute_primary_surface = True

    def clone(self):
        return self.__class__(color=self.color, width=self.width, height=self.height, border_color=self.border_color, border_width=self.border_width, **self._common_properties())


def new_circle(color='black', x=0, y=0, radius=100, border_color='light blue', border_width=0, transparency=100, size=100, angle=0):
    return Circle(color=color, x=x, y=y, radius=radius, border_color=border_color, border_width=border_width,
                  transparency=transparency, size=size, angle=angle)


class Circle(Sprite):
    def __init__(self, color='black', x=0, y=0, radius=100, border_color='light blue', border_width=0, transparency=100, size=100, angle=0):
        self._x = x
        self._y = y
        self._color = color
        self._radius = radius
        self._border_color = border_color
        self._border_width = border_width

        self._transparency = transparency
        self._size = size
        self._angle = angle
        self._is_clicked = False
        self._is_hidden = False
        self.physics = None

        self._when_clicked_callbacks = []

        self._compute_primary_surface()

        all_sprites.append(self)

    def clone(self):
        return self.__class__(color=self.color, radius=self.radius, border_color=self.border_color, border_width=self.border_width, **self._common_properties())

    def _compute_primary_surface(self):
        total_diameter = (self._radius + self._border_width) * 2
        self._primary_pygame_surface = pygame.Surface(
            (total_diameter, total_diameter), pygame.SRCALPHA)

        center = self._radius + self._border_width

        if self._border_width and self._border_color:

            pygame.draw.circle(self._primary_pygame_surface, _color_name_to_rgb(
                self._border_color), (center, center), self._radius)

            pygame.draw.circle(self._primary_pygame_surface, _color_name_to_rgb(
                self._color), (center, center), self._radius-self._border_width)
        else:
            pygame.draw.circle(self._primary_pygame_surface, _color_name_to_rgb(
                self._color), (center, center), self._radius)

        self._should_recompute_primary_surface = False
        self._compute_secondary_surface(force=True)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, _color):
        self._color = _color
        self._should_recompute_primary_surface = True

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, _radius):
        self._radius = _radius
        self._should_recompute_primary_surface = True
        if self.physics:
            self.physics._pymunk_shape.unsafe_set_radius(self._radius)

    @property
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, _border_color):
        self._border_color = _border_color
        self._should_recompute_primary_surface = True

    @property
    def border_width(self):
        return self._border_width

    @border_width.setter
    def border_width(self, _border_width):
        self._border_width = _border_width
        self._should_recompute_primary_surface = True


def new_line(color='black', x=0, y=0, length=None, angle=None, thickness=1, x1=None, y1=None, transparency=100, size=100):
    return line(color=color, x=x, y=y, length=length, angle=angle, thickness=thickness, x1=x1, y1=y1, transparency=transparency, size=size)


class line(Sprite):
    def __init__(self, color='black', x=0, y=0, length=None, angle=None, thickness=1, x1=None, y1=None, transparency=100, size=100):
        self._x = x
        self._y = y
        self._color = color
        self._thickness = thickness

        if length != None and angle != None:
            self._length = length
            self._angle = angle
            self._x1, self._y1 = self._calc_endpoint()
        elif x1 != None and y1 != None:
            self._x1 = x1
            self._y1 = y1
            self._length, self._angle = self._calc_length_angle()
        else:

            self._length = length or 100
            self._angle = angle or 0
            self._x1, self._y1 = self._calc_endpoint()

        self._transparency = transparency
        self._size = size
        self._is_hidden = False
        self._is_clicked = False
        self.physics = None

        self._when_clicked_callbacks = []

        self._compute_primary_surface()

        all_sprites.append(self)

    def clone(self):
        return self.__class__(color=self.color, length=self.length, thickness=self.thickness, **self._common_properties())

    def _compute_primary_surface(self):
        width = self.length
        height = self.thickness+1

        self._primary_pygame_surface = pygame.Surface(
            (width, height), pygame.SRCALPHA)

        self._should_recompute_primary_surface = False
        self._compute_secondary_surface(force=True)

    def _compute_secondary_surface(self, force=False):
        self._secondary_pygame_surface = self._primary_pygame_surface.copy()

        if force or self._transparency != 100:
            self._secondary_pygame_surface.set_alpha(
                round((self._transparency/100.) * 255))

        self._should_recompute_secondary_surface = False

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, _color):
        self._color = _color
        self._should_recompute_primary_surface = True

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, _thickness):
        self._thickness = _thickness
        self._should_recompute_primary_surface = True

    def _calc_endpoint(self):
        radians = _math.radians(self._angle)
        return self._length * _math.cos(radians) + self.x, self._length * _math.sin(radians) + self.y

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, _length):
        self._length = _length
        self._x1, self._y1 = self._calc_endpoint()
        self._should_recompute_primary_surface = True

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, _angle):
        self._angle = _angle
        self._x1, self._y1 = self._calc_endpoint()
        if self.physics:
            self.physics._pymunk_body.angle = _math.radians(_angle)

    def _calc_length_angle(self):
        dx = self.x1 - self.x
        dy = self.y1 - self.y

        return _math.sqrt(dx**2 + dy**2), _math.degrees(_math.atan2(dy, dx))

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, _x1):
        self._x1 = _x1
        self._length, self._angle = self._calc_length_angle()
        self._should_recompute_primary_surface = True

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, _y1):
        self._angle = _y1
        self._length, self._angle = self._calc_length_angle()
        self._should_recompute_primary_surface = True


def new_text(words='hi :)', x=0, y=0, font=None, font_size=50, color='black', angle=0, transparency=100, size=100):
    return text(words=words, x=x, y=y, font=font, font_size=font_size, color=color, angle=angle, transparency=transparency, size=size)


class text(Sprite):
    def __init__(self, words='hi :)', x=0, y=0, font=None, font_size=50, color='black', angle=0, transparency=100, size=100):
        self._words = words
        self._x = x
        self._y = y
        self._font = font
        self._font_size = font_size
        self._color = color
        self._size = size
        self._angle = angle
        self.transparency = transparency

        self._is_clicked = False
        self._is_hidden = False
        self.physics = None

        self._compute_primary_surface()

        self._when_clicked_callbacks = []

        all_sprites.append(self)

    def clone(self):
        return self.__class__(words=self.words, font=self.font, font_size=self.font_size, color=self.color, **self._common_properties())

    def _compute_primary_surface(self):
        try:
            self._pygame_font = pygame.font.Font(self._font, self._font_size)
        except:
            _warnings.warn(f"""We couldn't find the font file '{self._font}'. We'll use the default font instead for now.
To fix this, either set the font to None, or make sure you have a font file (usually called something like Arial.ttf) in your project folder.\n""", Hmm)
            self._pygame_font = pygame.font.Font(None, self._font_size)

        self._primary_pygame_surface = self._pygame_font.render(
            self._words, True, _color_name_to_rgb(self._color))
        self._should_recompute_primary_surface = False

        self._compute_secondary_surface(force=True)

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, string):
        self._words = str(string)
        self._should_recompute_primary_surface = True

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font_name):
        self._font = str(font_name)
        self._should_recompute_primary_surface = True

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, size):
        self._font_size = size
        self._should_recompute_primary_surface = True

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color_):
        self._color = color_
        self._should_recompute_primary_surface = True


def when_sprite_clicked(*sprites):
    def wrapper(func):
        for sprite in sprites:
            sprite.when_clicked(func, call_with_sprite=True)
        return func
    return wrapper


pygame.key.set_repeat(200, 16)
_pressed_keys = {}
_keypress_callbacks = []
_keyrelease_callbacks = []


def when_any_key_pressed(func):
    if not callable(func):
        raise Oops("""@ge.when_any_key_pressed doesn't use a list of keys. Try just this instead:

@ge.when_any_key_pressed
async def do(key):
    print("This key was pressed!", key)
""")
    async_callback = _make_async(func)

    async def wrapper(*args, **kwargs):
        wrapper.is_running = True
        await async_callback(*args, **kwargs)
        wrapper.is_running = False
    wrapper.keys = None
    wrapper.is_running = False
    _keypress_callbacks.append(wrapper)
    return wrapper


def when_key_pressed(*keys):
    def decorator(func):
        async_callback = _make_async(func)

        async def wrapper(*args, **kwargs):
            wrapper.is_running = True
            await async_callback(*args, **kwargs)
            wrapper.is_running = False
        wrapper.keys = keys
        wrapper.is_running = False
        _keypress_callbacks.append(wrapper)
        return wrapper
    return decorator


def when_any_key_released(func):
    if not callable(func):
        raise Oops("""@ge.when_any_key_released doesn't use a list of keys. Try just this instead:

@ge.when_any_key_released
async def do(key):
    print("This key was released!", key)
""")
    async_callback = _make_async(func)

    async def wrapper(*args, **kwargs):
        wrapper.is_running = True
        await async_callback(*args, **kwargs)
        wrapper.is_running = False
    wrapper.keys = None
    wrapper.is_running = False
    _keyrelease_callbacks.append(wrapper)
    return wrapper


def when_key_released(*keys):
    def decorator(func):
        async_callback = _make_async(func)

        async def wrapper(*args, **kwargs):
            wrapper.is_running = True
            await async_callback(*args, **kwargs)
            wrapper.is_running = False
        wrapper.keys = keys
        wrapper.is_running = False
        _keyrelease_callbacks.append(wrapper)
        return wrapper
    return decorator


def key_is_pressed(*keys):
    for key in keys:
        if key in _pressed_keys.values():
            return True
    return False


_NUM_SIMULATION_STEPS = 3


def _simulate_physics():
    for _ in range(_NUM_SIMULATION_STEPS):

        _physics_space.step(1/(60.0*_NUM_SIMULATION_STEPS))


_loop = _asyncio.get_event_loop()
_loop.set_debug(False)

_keys_pressed_this_frame = []
_keys_released_this_frame = []
_keys_to_skip = (pygame.K_MODE,)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP,
                         pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION])
_clock = pygame.time.Clock()


def _game_loop():
    _keys_pressed_this_frame.clear()
    _keys_released_this_frame.clear()
    click_happened_this_frame = False
    click_release_happened_this_frame = False

    _clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q and (
                    pygame.key.get_mods() & pygame.KMOD_META or pygame.key.get_mods() & pygame.KMOD_CTRL
                )):

            _loop.stop()
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_happened_this_frame = True
            mouse._is_clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            click_release_happened_this_frame = True
            mouse._is_clicked = False
        if event.type == pygame.MOUSEMOTION:
            mouse.x, mouse.y = (
                event.pos[0] - screen.width/2.), (screen.height/2. - event.pos[1])
        if event.type == pygame.KEYDOWN:
            if not (event.key in _keys_to_skip):
                name = _pygame_key_to_name(event)
                _pressed_keys[event.key] = name
                _keys_pressed_this_frame.append(name)
        if event.type == pygame.KEYUP:
            if not (event.key in _keys_to_skip) and event.key in _pressed_keys:
                _keys_released_this_frame.append(_pressed_keys[event.key])
                del _pressed_keys[event.key]

    for key in _keys_pressed_this_frame:
        for callback in _keypress_callbacks:
            if not callback.is_running and (callback.keys is None or key in callback.keys):
                _loop.create_task(callback(key))

    for key in _keys_released_this_frame:
        for callback in _keyrelease_callbacks:
            if not callback.is_running and (callback.keys is None or key in callback.keys):
                _loop.create_task(callback(key))

    if click_happened_this_frame and mouse._when_clicked_callbacks:
        for callback in mouse._when_clicked_callbacks:
            _loop.create_task(callback())

    if click_release_happened_this_frame and mouse._when_click_released_callbacks:
        for callback in mouse._when_click_released_callbacks:
            _loop.create_task(callback())

    for callback in _repeat_forever_callbacks:
        if not callback.is_running:
            _loop.create_task(callback())

    _loop.call_soon(_simulate_physics)

    _pygame_display.fill(_color_name_to_rgb(backdrop))

    for sprite in all_sprites:

        sprite._is_clicked = False

        if sprite.is_hidden:
            continue

        if sprite.physics and sprite.physics.can_move:

            body = sprite.physics._pymunk_body
            angle = _math.degrees(body.angle)
            if isinstance(sprite, line):
                sprite._x = body.position.x - \
                    (sprite.length/2) * _math.cos(angle)
                sprite._y = body.position.y - \
                    (sprite.length/2) * _math.sin(angle)
                sprite._x1 = body.position.x + \
                    (sprite.length/2) * _math.cos(angle)
                sprite._y1 = body.position.y + \
                    (sprite.length/2) * _math.sin(angle)

            else:

                if str(body.position.x) != 'nan':
                    sprite._x = body.position.x
                if str(body.position.y) != 'nan':
                    sprite._y = body.position.y

            sprite.angle = angle
            sprite.physics._x_speed, sprite.physics._y_speed = body.velocity

        if mouse.is_clicked and not type(sprite) == line:
            if _point_touching_sprite(mouse, sprite):

                if click_happened_this_frame:
                    sprite._is_clicked = True
                    for callback in sprite._when_clicked_callbacks:
                        if not callback.is_running:
                            _loop.create_task(callback())

        if sprite._should_recompute_primary_surface:

            _loop.call_soon(sprite._compute_primary_surface)
        elif sprite._should_recompute_secondary_surface:
            _loop.call_soon(sprite._compute_secondary_surface)

        if type(sprite) == line:

            x = screen.width/2 + sprite.x
            y = screen.height/2 - sprite.y
            x1 = screen.width/2 + sprite.x1
            y1 = screen.height/2 - sprite.y1
            if sprite.thickness == 1:
                pygame.draw.aaline(_pygame_display, _color_name_to_rgb(
                    sprite.color), (x, y), (x1, y1), True)
            else:
                pygame.draw.line(_pygame_display, _color_name_to_rgb(
                    sprite.color), (x, y), (x1, y1), sprite.thickness)
        else:
            _pygame_display.blit(
                sprite._secondary_pygame_surface, (sprite._pygame_x(), sprite._pygame_y()))

    pygame.display.flip()
    _loop.call_soon(_game_loop)
    return True


async def timer(seconds=1.0):
    await _asyncio.sleep(seconds)
    return True


async def animate():
    await _asyncio.sleep(0)


_repeat_forever_callbacks = []


def repeat_forever(func):
    async_callback = _make_async(func)

    async def repeat_wrapper():
        repeat_wrapper.is_running = True
        await async_callback()
        repeat_wrapper.is_running = False

    repeat_wrapper.is_running = False
    _repeat_forever_callbacks.append(repeat_wrapper)
    return func


_when_program_starts_callbacks = []


def when_program_starts(func):
    async_callback = _make_async(func)

    async def wrapper(*args, **kwargs):
        return await async_callback(*args, **kwargs)
    _when_program_starts_callbacks.append(wrapper)
    return func


def repeat(number_of_times):
    return range(1, number_of_times+1)


def start_program():
    for func in _when_program_starts_callbacks:
        _loop.create_task(func())

    _loop.call_soon(_game_loop)
    try:
        _loop.run_forever()
    finally:
        _logging.getLogger("asyncio").setLevel(_logging.CRITICAL)
        pygame.quit()
