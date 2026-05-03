# 🎵 Album Collection Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-OOP%20%26%20Sorting-purple)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> *"Your documentation is a direct reflection of your software, so hold it to the same standards."*

---

## 🌟 Highlights

- Models a real-world music collection using a custom `Album` class
- Sorts albums by number of songs or alphabetically by album name
- Demonstrates list operations: sorting, swapping, extending, and appending
- Searches a collection and returns the index of a specific album
- Clean, readable output using a custom `__str__` method

---

## ℹ️ Overview

**Album Collection Manager** is a Python project built as part of a bootcamp exercise in Object-Oriented Programming (OOP). It demonstrates how to design a class with instance variables, create and manage lists of objects, and apply sorting and searching techniques to real-world data.

The project uses two album collections — `albums1` and `albums2` — and walks through common list operations including sorting by different criteria, swapping elements, merging collections, and finding a specific album by name.

### ✍️ Author

**Ni Ni** — [@ninitwin4](https://github.com/ninitwin4)

---

## 🚀 Usage

Run the script and it will automatically print each stage of the collection:

```
(MoonMusic, Coldplay, 10)
(Lemonade, Beyonce, 13)
(Shawn, Shawn Mendes, 12)
(GNX, Kendrick Lamar, 12)
(30, Adele, 12)

--- albums1 (after swapping index 0 and index 1) ---
(30, Adele, 12)
(MoonMusic, Coldplay, 10)
...

--- albums2 (sorted alphabetically by album name) ---
(30, Adele, 12)
(Dark Side of the Moon, Pink Floyd, 9)
...

--- Search Result ---
Dark Side of the Moon found at index 1
```

---

## 🧠 Concepts Demonstrated

| Concept | How it's used |
|---|---|
| OOP / Classes | Custom `Album` class with `__init__` and `__str__` |
| Instance variables | `album_name`, `album_artist`, `number_of_songs` |
| Lambda functions | Used as the `key` parameter in `.sort()` |
| List methods | `.sort()`, `.extend()`, `.append()` |
| Tuple unpacking | Swapping two elements simultaneously |
| `enumerate()` | Searching a list and returning an index |

---

## ⬇️ Installation

### Prerequisites

- Python 3.x installed on your machine. Check by running:

```bash
python --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the repository:**

```bash
git clone https://https://github.com/ninitwin4/python-album-sorter.git
```

2. **Navigate into the project folder:**

```bash
cd album-collection-manager
```

3. **Run the script:**

```bash
python album_management.py
```

> No external libraries needed — this project uses pure Python only. ✅

---

## 💭 Feedback and Contributing

Have a suggestion or spotted a bug? Feel free to [open an issue](https://github.com/sonnet-sam/album-collection-manager/issues) or start a discussion in the [Discussions tab](https://github.com/sonnet-sam/album-collection-manager/discussions).

🔮 Future Ideas
These are features not yet built, but possible next steps for this project:

Add a method to the Album class that returns the average songs per artist
Sort albums by artist name
Let the user search for any album interactively via input()