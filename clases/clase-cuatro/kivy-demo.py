from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class CalculadoraApp(App):
    def build(self):
        self.title = "Calculadora Kivy"

        # Layout principal vertical
        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Campos de entrada
        self.input_a = TextInput(
            hint_text="Número A",
            multiline=False,
            input_filter="float",
            font_size=24,
            size_hint_y=None,
            height=50,
        )
        self.input_b = TextInput(
            hint_text="Número B",
            multiline=False,
            input_filter="float",
            font_size=24,
            size_hint_y=None,
            height=50,
        )

        # Etiqueta de resultado
        self.resultado = Label(
            text="Resultado: —",
            font_size=26,
            bold=True,
            color=(0.2, 0.8, 0.4, 1),
        )

        # Botones de operaciones en grilla 2x2
        grilla = GridLayout(cols=2, spacing=8, size_hint_y=None, height=120)
        operaciones = [
            ("➕ Sumar", self.sumar),
            ("➖ Restar", self.restar),
            ("✖️ Multiplicar", self.multiplicar),
            ("➗ Dividir", self.dividir),
        ]
        for texto, accion in operaciones:
            btn = Button(text=texto, font_size=18, background_color=(0.15, 0.55, 0.85, 1))
            btn.bind(on_press=accion)
            grilla.add_widget(btn)

        root.add_widget(Label(text="Calculadora Multi-Plataforma", font_size=22, bold=True))
        root.add_widget(self.input_a)
        root.add_widget(self.input_b)
        root.add_widget(grilla)
        root.add_widget(self.resultado)

        return root

    def _obtener_valores(self):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            return a, b
        except ValueError:
            self.resultado.text = "⚠️ Ingresá números válidos"
            return None, None

    def sumar(self, instance):
        a, b = self._obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a + b}"

    def restar(self, instance):
        a, b = self._obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a - b}"

    def multiplicar(self, instance):
        a, b = self._obtener_valores()
        if a is not None:
            self.resultado.text = f"Resultado: {a * b}"

    def dividir(self, instance):
        a, b = self._obtener_valores()
        if a is not None:
            if b == 0:
                self.resultado.text = "⚠️ No se puede dividir por cero"
            else:
                self.resultado.text = f"Resultado: {a / b:.4f}"


if __name__ == "__main__":
    CalculadoraApp().run()