import tkinter as tk
from tkinter import ttk, messagebox
import random
import math


# ─── Paleta de colores ───────────────────────────────────────────────────────
BG        = "#0f0f1a"
PANEL     = "#1a1a2e"
ACCENT    = "#e94560"
ACCENT2   = "#0f3460"
TEXT      = "#eaeaea"
TEXT_DIM  = "#888899"
SUCCESS   = "#00d4aa"
WARNING   = "#f5a623"
FONT_MAIN = ("Courier", 11)
FONT_HEAD = ("Courier", 14, "bold")
FONT_BIG  = ("Courier", 28, "bold")


# ─── App principal ────────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TK Demo — Panel de Control")
        self.geometry("860x620")
        self.resizable(False, False)
        self.configure(bg=BG)

        # Cabecera
        self._build_header()

        # Contenedor de pestañas personalizadas
        self._build_tabs()

    # ── Cabecera ─────────────────────────────────────────────────────────────
    def _build_header(self):
        bar = tk.Frame(self, bg=ACCENT2, height=52)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        tk.Label(bar, text="◈  TK DEMO", font=("Courier", 16, "bold"),
                 bg=ACCENT2, fg=ACCENT).pack(side="left", padx=20)
        tk.Label(bar, text="Panel de Control · tkinter",
                 font=FONT_MAIN, bg=ACCENT2, fg=TEXT_DIM).pack(side="left")

        # Botón cerrar estilizado
        tk.Button(bar, text="✕ Cerrar", font=FONT_MAIN,
                  bg=ACCENT, fg="white", bd=0, padx=12,
                  activebackground="#c73652", activeforeground="white",
                  cursor="hand2", command=self.destroy).pack(side="right", padx=16, pady=8)

    # ── Pestañas manuales ─────────────────────────────────────────────────────
    def _build_tabs(self):
        # Barra de pestañas
        tab_bar = tk.Frame(self, bg=PANEL, height=38)
        tab_bar.pack(fill="x")
        tab_bar.pack_propagate(False)

        self.tab_btns = {}
        self.tab_frames = {}
        self.active_tab = tk.StringVar(value="")

        # Área de contenido
        content = tk.Frame(self, bg=BG)
        content.pack(fill="both", expand=True, padx=0, pady=0)

        tabs = [
            ("Widgets",    self._tab_widgets),
            ("Calculadora",self._tab_calc),
            ("Canvas",     self._tab_canvas),
            ("Acerca de",  self._tab_about),
        ]

        for name, builder in tabs:
            frame = tk.Frame(content, bg=BG)
            self.tab_frames[name] = frame
            builder(frame)

            btn = tk.Button(tab_bar, text=name, font=FONT_MAIN,
                            bg=PANEL, fg=TEXT_DIM, bd=0,
                            padx=18, cursor="hand2",
                            activebackground=BG, activeforeground=TEXT,
                            command=lambda n=name: self._show_tab(n))
            btn.pack(side="left", fill="y")
            self.tab_btns[name] = btn

        self._show_tab("Widgets")

    def _show_tab(self, name):
        for n, f in self.tab_frames.items():
            f.pack_forget()
        for n, b in self.tab_btns.items():
            b.configure(bg=PANEL, fg=TEXT_DIM)
        self.tab_frames[name].pack(fill="both", expand=True)
        self.tab_btns[name].configure(bg=BG, fg=ACCENT)
        self.active_tab.set(name)

    # ══════════════════════════════════════════════════════════════════════════
    # Pestaña 1 — Widgets
    # ══════════════════════════════════════════════════════════════════════════
    def _tab_widgets(self, parent):
        tk.Label(parent, text="▸ GALERÍA DE WIDGETS", font=FONT_HEAD,
                 bg=BG, fg=ACCENT).pack(anchor="w", padx=24, pady=(18, 4))
        tk.Frame(parent, bg=ACCENT, height=2).pack(fill="x", padx=24)

        body = tk.Frame(parent, bg=BG)
        body.pack(fill="both", expand=True, padx=24, pady=16)

        # Columna izquierda
        left = tk.Frame(body, bg=PANEL, padx=16, pady=16)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        tk.Label(left, text="Entry + Button", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")
        self.entry_var = tk.StringVar()
        ent = tk.Entry(left, textvariable=self.entry_var, font=FONT_MAIN,
                       bg="#252540", fg=TEXT, insertbackground=ACCENT,
                       bd=0, relief="flat", width=26)
        ent.pack(fill="x", pady=(4, 8))
        tk.Button(left, text="Mostrar mensaje", font=FONT_MAIN,
                  bg=ACCENT, fg="white", bd=0, padx=10, pady=5,
                  cursor="hand2", activebackground="#c73652",
                  command=self._show_msg).pack(anchor="w")

        tk.Frame(left, bg="#2a2a42", height=1).pack(fill="x", pady=14)

        tk.Label(left, text="Checkboxes", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")
        self.checks = {}
        for opt in ("Opción Alpha", "Opción Beta", "Opción Gamma"):
            v = tk.BooleanVar()
            self.checks[opt] = v
            cb = tk.Checkbutton(left, text=opt, variable=v, font=FONT_MAIN,
                                bg=PANEL, fg=TEXT, selectcolor=ACCENT2,
                                activebackground=PANEL, activeforeground=ACCENT,
                                cursor="hand2")
            cb.pack(anchor="w")

        tk.Frame(left, bg="#2a2a42", height=1).pack(fill="x", pady=14)

        tk.Label(left, text="Radiobuttons", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")
        self.radio_var = tk.StringVar(value="A")
        for val, label in [("A", "Rojo"), ("B", "Verde"), ("C", "Azul")]:
            rb = tk.Radiobutton(left, text=label, variable=self.radio_var,
                                value=val, font=FONT_MAIN,
                                bg=PANEL, fg=TEXT, selectcolor=ACCENT2,
                                activebackground=PANEL, activeforeground=ACCENT,
                                cursor="hand2")
            rb.pack(anchor="w")

        # Columna derecha
        right = tk.Frame(body, bg=PANEL, padx=16, pady=16)
        right.grid(row=0, column=1, sticky="nsew")

        tk.Label(right, text="Combobox", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Dark.TCombobox",
                        fieldbackground="#252540", background=PANEL,
                        foreground=TEXT, arrowcolor=ACCENT)
        self.combo_var = tk.StringVar()
        combo = ttk.Combobox(right, textvariable=self.combo_var,
                             values=["Python", "JavaScript", "Rust", "Go", "C++"],
                             style="Dark.TCombobox", font=FONT_MAIN, width=22)
        combo.set("Python")
        combo.pack(fill="x", pady=(4, 14))

        tk.Label(right, text="Scale (slider)", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")
        self.scale_var = tk.IntVar(value=50)
        sc = tk.Scale(right, variable=self.scale_var, from_=0, to=100,
                      orient="horizontal", font=FONT_MAIN,
                      bg=PANEL, fg=TEXT, troughcolor=ACCENT2,
                      highlightthickness=0, sliderrelief="flat",
                      activebackground=ACCENT)
        sc.pack(fill="x", pady=(4, 14))

        tk.Label(right, text="Listbox", font=FONT_MAIN,
                 bg=PANEL, fg=TEXT_DIM).pack(anchor="w")
        lb = tk.Listbox(right, font=FONT_MAIN, bg="#252540", fg=TEXT,
                        selectbackground=ACCENT, selectforeground="white",
                        bd=0, height=5, width=26)
        for item in ["Elemento 1", "Elemento 2", "Elemento 3",
                     "Elemento 4", "Elemento 5"]:
            lb.insert("end", item)
        lb.pack(fill="x", pady=(4, 0))

        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)

    def _show_msg(self):
        txt = self.entry_var.get().strip() or "(vacío)"
        messagebox.showinfo("Mensaje", f"Escribiste:\n{txt}")

    # ══════════════════════════════════════════════════════════════════════════
    # Pestaña 2 — Calculadora
    # ══════════════════════════════════════════════════════════════════════════
    def _tab_calc(self, parent):
        tk.Label(parent, text="▸ CALCULADORA", font=FONT_HEAD,
                 bg=BG, fg=ACCENT).pack(anchor="w", padx=24, pady=(18, 4))
        tk.Frame(parent, bg=ACCENT, height=2).pack(fill="x", padx=24)

        calc_frame = tk.Frame(parent, bg=PANEL, padx=20, pady=20)
        calc_frame.pack(pady=20, padx=24, anchor="n")

        self.calc_expr = tk.StringVar(value="")
        self.calc_result = tk.StringVar(value="0")

        # Pantalla
        screen = tk.Frame(calc_frame, bg="#0a0a14", padx=10, pady=8)
        screen.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 10))
        tk.Label(screen, textvariable=self.calc_expr, font=FONT_MAIN,
                 bg="#0a0a14", fg=TEXT_DIM, anchor="e").pack(fill="x")
        tk.Label(screen, textvariable=self.calc_result, font=FONT_BIG,
                 bg="#0a0a14", fg=TEXT, anchor="e").pack(fill="x")

        layout = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        for r, row in enumerate(layout):
            for c, lbl in enumerate(row):
                is_op  = lbl in ("÷", "×", "−", "+", "=")
                is_clr = lbl in ("C", "±", "%")
                bg_c   = ACCENT if lbl == "=" else (WARNING if is_op else
                          (ACCENT2 if is_clr else "#252540"))
                fg_c   = "white"
                btn = tk.Button(calc_frame, text=lbl, font=("Courier", 13, "bold"),
                                bg=bg_c, fg=fg_c, bd=0, width=4, height=2,
                                cursor="hand2", activeforeground="white",
                                activebackground=ACCENT,
                                command=lambda x=lbl: self._calc_press(x))
                btn.grid(row=r + 1, column=c, padx=3, pady=3)

        self._calc_state = {"expr": "", "last_op": None, "result": "0", "new": True}

    def _calc_press(self, key):
        s = self._calc_state
        ops_map = {"÷": "/", "×": "*", "−": "-", "+": "+"}

        if key == "C":
            s["expr"] = ""; s["result"] = "0"; s["new"] = True
        elif key == "⌫":
            s["expr"] = s["expr"][:-1] or ""
            try:
                s["result"] = str(eval(s["expr"])) if s["expr"] else "0"
            except Exception:
                pass
        elif key == "=":
            try:
                res = eval(s["expr"].replace("÷","/").replace("×","*")
                           .replace("−","-"))
                s["result"] = str(int(res) if res == int(res) else round(res, 8))
                s["expr"] = s["result"]
            except Exception:
                s["result"] = "Error"
        elif key == "±":
            try:
                val = float(s["result"]) * -1
                s["result"] = str(int(val) if val == int(val) else val)
                s["expr"] = s["result"]
            except Exception:
                pass
        elif key == "%":
            try:
                val = float(s["result"]) / 100
                s["result"] = str(round(val, 8))
                s["expr"] = s["result"]
            except Exception:
                pass
        else:
            s["expr"] += key
            try:
                expr = s["expr"].replace("÷","/").replace("×","*").replace("−","-")
                s["result"] = str(eval(expr))
            except Exception:
                pass

        self.calc_expr.set(s["expr"])
        self.calc_result.set(s["result"])

    # ══════════════════════════════════════════════════════════════════════════
    # Pestaña 3 — Canvas
    # ══════════════════════════════════════════════════════════════════════════
    def _tab_canvas(self, parent):
        tk.Label(parent, text="▸ CANVAS INTERACTIVO", font=FONT_HEAD,
                 bg=BG, fg=ACCENT).pack(anchor="w", padx=24, pady=(18, 4))
        tk.Frame(parent, bg=ACCENT, height=2).pack(fill="x", padx=24)

        toolbar = tk.Frame(parent, bg=PANEL, padx=12, pady=8)
        toolbar.pack(fill="x", padx=24, pady=(10, 0))

        for lbl, cmd in [("Estrellas ✦", self._draw_stars),
                         ("Círculos ○",  self._draw_circles),
                         ("Espiral ◎",   self._draw_spiral),
                         ("Limpiar ✕",   self._clear_canvas)]:
            tk.Button(toolbar, text=lbl, font=FONT_MAIN,
                      bg=ACCENT2, fg=TEXT, bd=0, padx=10, pady=4,
                      cursor="hand2", activebackground=ACCENT,
                      activeforeground="white",
                      command=cmd).pack(side="left", padx=4)

        self.canvas = tk.Canvas(parent, bg="#08081a", bd=0,
                                highlightthickness=1,
                                highlightbackground=ACCENT2)
        self.canvas.pack(fill="both", expand=True, padx=24, pady=10)

        tk.Label(parent, text="Click en el canvas para dibujar un punto",
                 font=FONT_MAIN, bg=BG, fg=TEXT_DIM).pack(pady=(0, 8))

        self.canvas.bind("<Button-1>", self._canvas_click)

    def _canvas_click(self, event):
        x, y = event.x, event.y
        c = random.choice([ACCENT, SUCCESS, WARNING, "#a78bfa", "#38bdf8"])
        r = random.randint(4, 12)
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=c, outline="")

    def _draw_stars(self):
        w = self.canvas.winfo_width() or 700
        h = self.canvas.winfo_height() or 360
        for _ in range(80):
            x, y = random.randint(0, w), random.randint(0, h)
            r = random.uniform(1, 4)
            c = random.choice([TEXT, ACCENT, SUCCESS, "#a78bfa"])
            self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=c, outline="")

    def _draw_circles(self):
        w = self.canvas.winfo_width() or 700
        h = self.canvas.winfo_height() or 360
        cx, cy = w//2, h//2
        for i in range(1, 16):
            r = i * 18
            colors = [ACCENT, ACCENT2, SUCCESS, WARNING, "#a78bfa"]
            c = colors[i % len(colors)]
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r,
                                    outline=c, width=2)

    def _draw_spiral(self):
        w = self.canvas.winfo_width() or 700
        h = self.canvas.winfo_height() or 360
        cx, cy = w//2, h//2
        pts = []
        for i in range(400):
            angle = 0.15 * i
            radius = 2 * i / 4
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            pts.append((x, y))
        for i in range(len(pts) - 1):
            t = i / len(pts)
            r = int(233 * t + 15 * (1-t))
            g = int(69  * t + 52 * (1-t))
            b = int(96  * t + 96 * (1-t))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(*pts[i], *pts[i+1], fill=color, width=2)

    def _clear_canvas(self):
        self.canvas.delete("all")

    # ══════════════════════════════════════════════════════════════════════════
    # Pestaña 4 — Acerca de
    # ══════════════════════════════════════════════════════════════════════════
    def _tab_about(self, parent):
        frame = tk.Frame(parent, bg=BG)
        frame.pack(expand=True)

        tk.Label(frame, text="◈", font=("Courier", 48), bg=BG, fg=ACCENT
                 ).pack(pady=(40, 4))
        tk.Label(frame, text="TK DEMO", font=("Courier", 22, "bold"),
                 bg=BG, fg=TEXT).pack()
        tk.Label(frame, text="Una aplicación de ejemplo con tkinter",
                 font=FONT_MAIN, bg=BG, fg=TEXT_DIM).pack(pady=4)

        tk.Frame(frame, bg=ACCENT2, height=1, width=360).pack(pady=20)

        info = [
            ("Lenguaje",   "Python 3"),
            ("GUI",        "tkinter (stdlib)"),
            ("Pestañas",   "Widgets · Calculadora · Canvas · Acerca de"),
            ("Autor",      "Claude — Anthropic"),
        ]
        for label, val in info:
            row = tk.Frame(frame, bg=BG)
            row.pack(anchor="w", padx=80, pady=2)
            tk.Label(row, text=f"{label}:", font=("Courier", 11, "bold"),
                     bg=BG, fg=ACCENT, width=14, anchor="w").pack(side="left")
            tk.Label(row, text=val, font=FONT_MAIN,
                     bg=BG, fg=TEXT).pack(side="left")


# ─── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()