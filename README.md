<div align="center">

# 🔍 TG-User_Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-blue?logo=telegram)](https://t.me/l27_0)

<img src="https://i.imgur.com/YrCMUEd.png" alt="TG-User_Finder Logo" width="180"/>

**A powerful and elegant tool for finding available Telegram usernames with customizable patterns**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing) • [License](#-license)

</div>

## 📋 Description

TG-User_Finder is an advanced Python utility that helps you discover available Telegram usernames using various pattern configurations. The tool leverages the Telegram API to check username availability and sends notifications directly to your Telegram account when a match is found.

With a colorful terminal interface and easy-to-use commands, finding that perfect username has never been easier!

## ✨ Features

- **Multiple Username Patterns**: Choose from various username patterns (3-5 characters with different separator configurations)
- **Real-time Notifications**: Receive instant Telegram notifications when available usernames are found
- **Colorful Interface**: Enjoy a visually appealing terminal experience with color-coded outputs
- **Continuous Scanning**: Automatically continues searching without manual intervention
- **Customizable**: Easy to modify and extend for your specific needs

## 🛠️ Requirements

- Python 3.6 or higher
- Telegram Bot Token (create one via [@BotFather](https://t.me/BotFather))
- Telegram User ID (get yours via [@userinfobot](https://t.me/userinfobot))
- Internet connection

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mrVXBoT/TG-User_Finder.git
cd TG-User_Finder
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

## 📦 Dependencies

This project requires the following Python packages:

- `requests`: For making HTTP requests to check username availability
- `telebot`: For sending Telegram notifications
- `TGcrypto`: For Telegram API encryption
- `pyrogram`: For advanced Telegram API interactions
- `pyromod`: For extending Pyrogram functionality
- `colorama`: For colorful terminal output

## 🚀 Usage

### Basic Usage

```bash
python TG-Finder.py
```

Follow the on-screen instructions:

1. Enter your Telegram Bot Token
2. Enter your Telegram User ID
3. Select a username pattern:
   - Option 1: 3-character IDs with format `a_b_c`
   - Option 2: 3-character IDs with format `a__b_c`
   - Option 3: 4-character IDs with format `a_b_c_d`
   - Option 4: 5-character IDs with format `abcde`

### Pattern Examples

| Option | Pattern Format | Example |
|--------|---------------|----------|
| 1 | `a_b_c` | `user_x_y` |
| 2 | `a__b_c` | `cool__v_z` |
| 3 | `a_b_c_d` | `pro_q_r_s` |
| 4 | `abcde` | `coolz` |

## 🌟 Examples

### Example 1: Finding a 3-character username with format a_b_c

```
[?] TOKEN: 1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ
[?] ID: 123456789

[1] 3-ID | #_#_#  
[2] 3_ID | #__#_#
[3] 4-ID | #_#_#_#
[4] 5ID | #####

[?] CHOSE: 1
[•] GooD: cool_x_y
[✗] BaD: test_a_b
[•] GooD: pro_z_q
```

When a good username is found, you'll receive a notification in your Telegram:

```
< TELEGRAM USERNAME > GooD
[•] < @cool_x_y > 🔸
_______
BY : [ @KoXVX ]
CHANNEL: [ @l27_0 ]
```

## 💡 Tips & Tricks

- For best results, let the script run for extended periods to find rare usernames
- The most desirable usernames are typically short ones (Option 4)
- Consider running the script on a VPS for 24/7 operation
- Use a dedicated Telegram bot for notifications to avoid mixing with other messages

## ⚠️ Disclaimer

This tool is for educational purposes only. Please use responsibly and in accordance with Telegram's Terms of Service. Excessive use may result in rate limiting or account restrictions.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

- **mrVXBoT** - [GitHub](https://github.com/mrVXBoT) | [Telegram](https://t.me/KoXVX)

## 🙏 Acknowledgements

- [Telegram API](https://core.telegram.org/api)
- [Fragment.com](https://fragment.com/) for username availability checking
- All contributors and supporters

---

<div align="center">

### ⭐ Star this repository if you find it useful! ⭐

</div>
