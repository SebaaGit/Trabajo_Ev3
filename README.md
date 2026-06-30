# 🎤 Cachipún x Karaoke 🎮

¡Bienvenido al proyecto **Cachipún x Karaoke**! Un programa en Python que combina el clásico juego chileno de **Cachipún** (piedra, papel o tijera) con una sesión de **karaoke**. El ganador de la partida es quien elige la canción para cantar 🎶
---

## 📖 ¿De qué trata?

**Cachipún** es la forma tradicional chilena de llamar al juego de "piedra, papel o tijera". En este proyecto, dos jugadores se enfrentan en una partida de Cachipún y, dependiendo del resultado, se desata la diversión:

- 🏆 Si hay un **ganador**, esa persona elige la canción que se va a cantar.
- 🤝 Si hay **empate**, ¡ambos jugadores cantan juntos!

---

## ⚙️ ¿Cómo funciona el código?

### 1️⃣ Importaciones
Se utiliza la librería `webbrowser`, que permite abrir automáticamente un link (como un video de YouTube) directamente en el navegador.

### 2️⃣ Archivo de canciones (`canciones.txt`)
El programa lee un archivo de texto llamado `canciones.txt`, donde cada línea contiene el nombre de una canción y su link, separados por el símbolo `|`. Ejemplo:

```
Mi muñeca me habló|https://www.youtube.com/watch?v=XOdfPs6Fbm4
Mi equilibrio espiritual|https://www.youtube.com/watch?v=f7OkO-2mdTM
Me cortaron mal el pelo|https://www.youtube.com/watch?v=jdQp_MxsgR0
```

Estas son las tres canciones que vienen incluidas en el archivo `canciones.txt` del proyecto, listas para que el ganador del Cachipún elija con cuál cantar 🎵

### 3️⃣ Función `karaoke()` 🎶
Esta función se encarga de:
1. Leer el archivo de canciones.
2. Mostrar un menú numerado con todas las canciones disponibles.
3. Pedirle al usuario que elija una opción.
4. Abrir automáticamente el link de la canción elegida en el navegador.

### 4️⃣ Función `cachipun()` ✊✋✌️
Esta función contiene la lógica del juego:
1. Muestra el menú de jugadas: `1 = Piedra`, `2 = Papel`, `3 = Tijera`.
2. Pide la jugada del **Jugador 1** y del **Jugador 2**.
3. Evalúa el resultado con condicionales:
   - Si ambos eligen lo mismo → **Empate**, y se llama a `karaoke()` para que ambos canten.
   - Si la combinación favorece al Jugador 1 → **Gana Jugador 1**, y se llama a `karaoke()`.
   - En cualquier otro caso → **Gana Jugador 2**, y se llama a `karaoke()`.

### 5️⃣ Ejecución del programa ▶️
Al final del archivo, se llama a `cachipun()`, lo que pone en marcha todo el juego.

---

## 🧩 Conceptos de programación usados

| Concepto | ¿Dónde se usa? |
|---|---|
| 📦 Importaciones | Traer la herramienta `webbrowser` |
| 📂 Archivos | Lectura de `canciones.txt` |
| 📋 Listas | Almacenar las canciones leídas |
| 🔁 Ciclo `for` | Mostrar el menú de canciones |
| ❓ Condicionales | Determinar quién ganó el Cachipún |
| 🧮 Funciones | Organizar el programa en partes (`karaoke()` y `cachipun()`) |
| 🚀 Ejecución final | Iniciar todo el juego con `cachipun()` |

---

## ▶️ ¿Cómo ejecutarlo?

1. Asegúrate de tener Python instalado.
2. Crea un archivo `canciones.txt` en la misma carpeta, con el formato `nombre|link`.
3. Ejecuta el archivo principal:

```bash
python prueba1.py
```

4. ¡Elige tu jugada y que gane la mejor voz! 🎤

---

## 👨‍💻 Créditos

Proyecto desarrollado como parte de una presentación universitaria sobre Git y GitHub 🎓
Henry [apellido pendiente, no me responde el wasa] - Lider del Proyecto, Programacion
Sebastian Pacheco - Programacion
Guillermo De la Cruz - Github README, Programacion
