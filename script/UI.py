import Level
from script.GameController import *


class Button(GameObject):
    lock: bool

    def __init__(self, position, button_id, image=None):
        super(Button, self).__init__(position)
        self._layer = Layer.UI
        self.id = button_id
        self.lock = True
        self.font = pygame.font.Font("font/BRLNSB.ttf", 30)
        self.text = ""
        self.text_color = (0, 0, 0)
        self.text_offset = (0, 0)

        if image is not None:
            self._image = pygame.image.load("image/" + image)

    def set_font_size(self, size):
        self.font = pygame.font.Font("font/BRLNSB.ttf", size)

    def update(self):
        pass
    
    def render(self):
        super(Button, self).render()
        if self.text != "" and self._active:
            text = self.font.render(self.text, True, self.text_color)
            screen.blit(text,
                        (self._position[0] + self.text_offset[0] - text.get_width()/2, self._position[1] + self.text_offset[1]))

    def set_image(self, image):
        self._image = image

    def is_in_mouse_up(self):
        if self.is_below_mouse_position() and GameController.mouse_up:
            if pygame.mouse.get_cursor() != pygame.cursors.broken_x:
                GameController.mouse_up = False
                return True
        return False

    def is_in_mouse_down(self):
        if self.is_below_mouse_position() and GameController.mouse_down:
            GameController.mouse_down = False
            return True
        return False

    def is_below_mouse_position(self):
        rect = self._image.get_rect()
        rect.topleft = self._position
        return rect.collidepoint(pygame.mouse.get_pos())


class UserInterface:
    main_menu = None
    level_menu = None
    options = None
    credits = None
    play_menu = None

    def __init__(self, level: Level.LevelController):
        UserInterface.main_menu = MainMenu((0, 0))
        UserInterface.options = OptionsMenu((0, 0))
        UserInterface.credits = CreditsMenu((0, 0))
        UserInterface.level_menu = LevelMenu((100, 100), level)
        UserInterface.play_menu = GameplayMenu((75, 485), level)
        UserInterface.options.set_active(False)
        UserInterface.credits.set_active(False)
        UserInterface.level_menu.set_active(False)
        UserInterface.play_menu.set_active(False)


class MainMenu(GameObject):
    def __init__(self, position):
        super(MainMenu, self).__init__(position)
        self._layer = Layer.UI
        self.name = Button((225, SCREEN_HEIGHT / 2 - 250), 0, "name.png")
        self.btn_play = Button((SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 85), 0, "btn_play.png")
        self.btn_options = Button((SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2), 0, "btn_options.png")
        self.btn_credits = Button((SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 85), 0, "btn_credits.png")

    def update(self):
        if self.btn_play.is_in_mouse_up():
            UserInterface.level_menu.set_active(True)
            self.set_active(False)
        if self.btn_credits.is_in_mouse_up():
            UserInterface.credits.set_active(True)
            self.set_active(False)
        if self.btn_options.is_in_mouse_up():
            UserInterface.options.set_active(True)
            self.set_active(False)

    def set_active(self, boolean):
        super(MainMenu, self).set_active(boolean)
        self.name.set_active(boolean)
        self.btn_play.set_active(boolean)
        self.btn_credits.set_active(boolean)
        self.btn_options.set_active(boolean)


class OptionsMenu(GameObject):
    def __init__(self, position):
        super(OptionsMenu, self).__init__(position)
        self._layer = Layer.UI
        sound_x, sound_y = SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 30
        music_x, music_y = SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 + 60
        self.setting = Button((SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 200), 0, "setting.png")

        self.btn_save = Button((music_x + 35, music_y + 90), 0, "btn_save.png")

        self.btn_txt_music = Button((music_x, music_y), 0, "btn_txt_music.png")
        self.btn_txt_sound = Button((sound_x, sound_y), 0, "btn_txt_sound.png")

        self.btn_sound = Button((sound_x + 220, sound_y), 1)
        self.btn_music = Button((music_x + 220, music_y), 1)
        self.btn_sound.set_image(GameLoader.LOADER["spr_sound"])
        self.btn_music.set_image(GameLoader.LOADER["spr_music"])

    def update(self):
        if self.btn_sound.is_in_mouse_up():
            if self.btn_sound.id == 1:
                self.btn_sound.set_image(GameLoader.LOADER["spr_no_sound"])
                self.btn_sound.id = 0
            else:
                self.btn_sound.set_image(GameLoader.LOADER["spr_sound"])
                self.btn_sound.id = 1
        if self.btn_music.is_in_mouse_up():
            if self.btn_music.id == 1:
                self.btn_music.set_image(GameLoader.LOADER["spr_no_music"])
                self.btn_music.id = 0
            else:
                self.btn_music.set_image(GameLoader.LOADER["spr_music"])
                self.btn_music.id = 1
        if self.btn_save.is_in_mouse_up():
            UserInterface.main_menu.set_active(True)
            self.set_active(False)

    def set_active(self, boolean):
        super(OptionsMenu, self).set_active(boolean)
        self.btn_sound.set_active(boolean)
        self.btn_music.set_active(boolean)
        self.btn_save.set_active(boolean)
        self.btn_txt_music.set_active(boolean)
        self.btn_txt_sound.set_active(boolean)
        self.setting.set_active(boolean)


class CreditsMenu(GameObject):
    def __init__(self, position):
        super(CreditsMenu, self).__init__(position)
        self._layer = Layer.UI
        self.about = Button((SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 200), 0,  "about.png")
        self.btn_home = Button((SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT - 100), 0, "btn_home.png")

    def update(self):
        if self.btn_home.is_in_mouse_up():
            UserInterface.main_menu.set_active(True)
            self.set_active(False)

    def set_active(self, boolean):
        super(CreditsMenu, self).set_active(boolean)
        self.about.set_active(boolean)
        self.btn_home.set_active(boolean)


class LevelMenu(GameObject):
    level_buttons: list[Button] = []

    def __init__(self, position, level: Level.LevelController):
        super(LevelMenu, self).__init__(position)
        self._position = position
        self._layer = Layer.UI
        self.level = level
        d = 90
        self.btn_home = Button((SCREEN_WIDTH/2 - 30, SCREEN_HEIGHT - 100), 0, "btn_home.png")
        for i in range(0, 4):
            for j in range(0, 8):
                self.level_buttons.append(Button((self._position[0] + d*j, self._position[1] + d*i), 8*i+j+1))
        self.level_buttons[0].lock = False

    def update(self):
        if self.btn_home.is_in_mouse_up():
            UserInterface.main_menu.set_active(True)
            self.set_active(False)
        for i in range(0, 32):
            if self.level_buttons[i].lock:
                self.level_buttons[i].set_image(GameLoader.LOADER["spr_level_lock"])
            else:
                if self.level_buttons[i].text == "":
                    self.level_buttons[i].text = str(self.level_buttons[i].id).zfill(2)
                    self.level_buttons[i].text_offset = (35, 13)
                    self.level_buttons[i].set_image(GameLoader.LOADER["spr_level_unlock"])
                if self.level_buttons[i].is_in_mouse_up():
                    self.set_active(False)
                    UserInterface.play_menu.set_active(True)
                    self.level.load_level(self.level_buttons[i].id)

    def set_active(self, boolean):
        super(LevelMenu, self).set_active(boolean)
        self.btn_home.set_active(boolean)
        for i in range(0, 32):
            self.level_buttons[i].set_active(boolean)
            if self.level_buttons[i].id <= self.level.level:
                self.level_buttons[i].lock = False


class GameplayMenu(GameObject):
    def __init__(self, position, level):
        super(GameplayMenu, self).__init__(position)
        self._layer = Layer.UI
        self.level = level
        self.btn_home = Button(position, 0, "btn_home.png")
        self.btn_reload = Button((position[0] + 85, position[1]), 0, "btn_reload.png")

    def update(self):
        if self.btn_home.is_in_mouse_up():
            UserInterface.main_menu.set_active(True)
            UserInterface.level_menu.level.hide_board()
            GameController.clear_layer(Layer.block)
            self.set_active(False)
        if self.btn_reload.is_in_mouse_up():
            self.level.restart_level()

    def set_active(self, boolean):
        super(GameplayMenu, self).set_active(boolean)
        self.btn_home.set_active(boolean)
        self.btn_reload.set_active(boolean)