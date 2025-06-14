# 🎵 Tkinter Music Player

A clean and modern **Python-based Music Player** built using `Tkinter` for the GUI and `Pygame` for audio playback. Easily navigate through your `.mp3` files with Play, Pause, Stop, Next, and Previous controls, all inside a polished desktop interface.

---

## ✨ Features

- 🎧 Play `.mp3` files from a local folder
- ⏯️ Control playback: Play / Pause / Resume / Stop
- ⏮️ Previous and ⏭️ Next track functionality
- 📂 Auto-load songs from the `music/` directory
- 🎨 Custom dark-themed GUI using `Tkinter`

---





## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tk-music-player.git
cd tk-music-player
````

### 2. Install Dependencies

Ensure Python 3 is installed. Then install `pygame`:

```bash
pip install pygame
```

### 3. Setup Folders

Make sure the following folders and files exist:

* 📁 `music/` – Add your `.mp3` files here
* 📁 `btns/` – Add your control button images:

  * `play_img.png`
  * `pause_img.png`
  * `stop_img.png`
  * `prev_img.png`
  * `next_img.png`

> You can download free icon assets from:
>
> * [icons8.com](https://icons8.com)
> * [flaticon.com](https://www.flaticon.com)

### 4. Run the App

```bash
python main.py
```

---

## 🗂️ Project Structure

```
tk-music-player/
├── music_player.py        # Main Python script
├── music/                 # Folder for your MP3 files
├── btns/                  # Folder for control icons
└── README.md              # Project documentation
```

---

## 🧰 Tech Stack

* **[Python 3.x](https://www.python.org/)**
* **[Tkinter](https://docs.python.org/3/library/tkinter.html)** – GUI library
* **[pygame.mixer](https://www.pygame.org/docs/ref/mixer.html)** – Audio engine
* **Built-in Modules**: `os`, `fnmatch`

---

## 💡 Future Enhancements

* 🎚️ Volume control slider
* 🌀 Shuffle and Repeat mode
* ⏱️ Song duration + progress bar
* 📝 Lyrics viewer and ID3 metadata support
* 🖱️ Drag-and-drop file support

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo, create a new branch, and submit a pull request.


## 👤 Author

**Keyur Bhatiya**
🔗 [GitHub Profile](https://github.com/keyurbhatiya)





