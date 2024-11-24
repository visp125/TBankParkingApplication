from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from PIL import Image as PILImage
import os


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Добавление белого фона
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        image_path = os.path.expanduser('~') + '/pythonProjectTBank/design/logo1.png'

        # Добавление картинки перед фразой "Добро пожаловать"
        image = Image(source=image_path, size_hint=(1, 0.9))  # Устанавливаем размер изображения (например, 40% от высоты)
        layout.add_widget(image)

        # Заголовок
        layout.add_widget(Label(text='[b][color=000000]Добро пожаловать[/color][/b]',markup=True, font_size='30sp', size_hint=(1, 0.2)))

        # Поля для ввода логина и пароля
        self.username_input = TextInput(hint_text='Логин', multiline=False, size_hint=(1, 0.1))
        self.password_input = TextInput(hint_text='Пароль', multiline=False, password=True, size_hint=(1, 0.1))

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)

        # Кнопка "Войти"
        login_button = Button(text='[b][color=000000]Войти[/color][/b]',markup=True, background_color=(255, 255, 0, 1), font_size='30sp', size_hint=(1, 0.2))
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        # Обновляем размер и позицию фона при изменении размера экрана
        self.rect.pos = self.pos
        self.rect.size = self.size

    def login(self, instance):
        # Авторизация
        if self.username_input.text == "1111" and self.password_input.text == "1111":
            app = App.get_running_app()
            app.root.current = 'game'  # Переход на экран игры
        else:
            self.username_input.text = ""
            self.password_input.text = ""
            self.username_input.hint_text = "Неверный логин или пароль"
            self.password_input.hint_text = "Попробуйте снова"


class ColoredRectangle(Widget):
    def __init__(self, **kwargs):
        super(ColoredRectangle, self).__init__(**kwargs)
        self.current_color = 'white'  # Изначально белый фон

        with self.canvas:
            # Белый цвет для прямоугольника
            self.fill_color = Color(1, 1, 1, 1)  # Белый цвет
            self.fill_rect = Rectangle(pos=self.pos, size=self.size)

            # Черный контур
            self.border_color = Color(0, 0, 0, 1)  # Черный цвет для контура
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)  # Конкретная толщина контура

        self.bind(pos=self.update_rectangles, size=self.update_rectangles)

    def update_rectangles(self, *args):
        self.fill_rect.pos = self.pos
        self.fill_rect.size = self.size

        # Обновление контура при изменении размера прямоугольника
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def toggle_color(self):
        # Переключение между белым и зеленым цветом
        if self.current_color == 'white':
            self.fill_color.rgba = (0, 1, 0, 1)  # Зеленый цвет
            self.current_color = 'green'
        else:
            self.fill_color.rgba = (1, 1, 1, 1)  # Белый цвет
            self.current_color = 'white'


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        # Добавление белого фона
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Метки рядов
        row_labels = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=50)
        row_labels.add_widget(Label(text='[b][color=000000]Ряд 1[/color][/b]',markup=True, font_size='20sp', size_hint=(0.5, None), halign='left', valign='middle'))
        row_labels.add_widget(Label(text='[b][color=000000]Ряд 2[/color][/b]',markup=True, font_size='20sp', size_hint=(0.5, None), halign='right', valign='middle'))

        layout.add_widget(row_labels)

        # Верхняя часть с прямоугольниками
        grid_layout = GridLayout(cols=2, spacing=[100, 70], size_hint=(1, 0.8))

        # Добавляем прямоугольники
        for row in range(4):  # 5 прямоугольников в каждом ряду
            for col in range(2):  # 2 ряда
                rect = ColoredRectangle(size_hint=(1, None), height=80)
                rect.bind(on_touch_down=self.on_rectangle_touch)
                grid_layout.add_widget(rect)

        layout.add_widget(grid_layout)

        # Кнопка "Забронировать"
        reserve_button = Button(text='[b][color=000000]Забронировать[/color][/b]',markup=True, size_hint=(1, 0.2), background_color=(255, 255, 0, 1), font_size='30sp')
        reserve_button.bind(on_press=self.reserve_seats)

        layout.add_widget(reserve_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        # Обновляем размер и позицию фона при изменении размера экрана
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_rectangle_touch(self, instance, touch):
        # Проверяем, был ли клик внутри прямоугольника
        if instance.collide_point(*touch.pos):
            instance.toggle_color()

    def reserve_seats(self, instance):
        # Переход на следующий экран
        app = App.get_running_app()
        app.root.current = 'reservation'


class ReservationScreen(Screen):
    def __init__(self, **kwargs):
        super(ReservationScreen, self).__init__(**kwargs)

        # Добавление белого фона
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Путь к GIF
        image_path = os.path.join(os.path.expanduser('~'), 'pythonProjectTBank', 'design', 'success_check.gif')

        # Используем Pillow для обработки GIF
        self.gif_image = PILImage.open(image_path)
        self.gif_texture = Texture.create(size=self.gif_image.size, colorfmt='rgba')

        # Создаем виджет для отображения изображения
        self.gif_widget = Image(size_hint=(1, 0.9))
        layout.add_widget(self.gif_widget)

        # Добавляем текст
        text = Label(text='[b][color=000000]Успешно![/color][/b]', markup=True, font_size='30sp', size_hint=(1, 0.2),
                     halign='center')
        layout.add_widget(text)

        text2 = Label(text='[b][color=000000]Ваше место :[/color][/b]', markup=True, font_size='30sp',
                      size_hint=(1, 0.2), halign='center')
        layout.add_widget(text2)

        self.add_widget(layout)

        # Инициализация для управления кадрами GIF
        self.frame_index = 0
        self.gif_frames = self.gif_image.n_frames
        self.frame_delay = self.gif_image.info.get('duration', 100) / 1000.0  # Задержка из GIF (в секундах)

    def on_enter(self):
        # Метод вызывается при переходе на экран
        self.frame_index = 0  # Сбросить на первый кадр
        Clock.schedule_interval(self.update_animation, self.frame_delay)

    def update_animation(self, dt):
        if self.frame_index < self.gif_frames:
            try:
                # Получаем текущий кадр
                self.gif_image.seek(self.frame_index)
                frame = self.gif_image.convert("RGBA")

                # Переворачиваем изображение
                frame = frame.transpose(PILImage.FLIP_TOP_BOTTOM)

                # Обновляем текстуру
                self.gif_texture.blit_buffer(frame.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
                self.gif_widget.texture = self.gif_texture

                # Переходим к следующему кадру
                self.frame_index += 1
            except EOFError:
                pass
        else:
            # Останавливаем анимацию на последнем кадре
            Clock.unschedule(self.update_animation)

    def update_rect(self, *args):
        # Обновляем размер и позицию фона при изменении размера экрана
        self.rect.pos = self.pos
        self.rect.size = self.size

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Экран авторизации
        sm.add_widget(LoginScreen(name='login'))

        # Экран с прямоугольниками
        sm.add_widget(GameScreen(name='game'))

        # Экран с гифкой
        sm.add_widget(ReservationScreen(name='reservation'))

        return sm


if __name__ == '__main__':
    MyApp().run()
