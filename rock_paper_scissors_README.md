<div align="center">

# ✊✋✌️ Rock Paper Scissors

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #2 — You vs Computer. Game doesn't stop until YOU win. 🖤**

</div>

---

## 💡 What It Does

```
You pick rock, paper, or scissors.
Computer randomly picks too.
Tie? Keep going.
Lose? Keep going.
Win? Game over. You earned it. 🏆
```

---

## 🎮 Demo

```bash
WELCOME TO ROCK PAPER SCISSORS GAME! ❤❤❤😊
> Enter your choice: rock
  Computer chose: paper
  You lose! 😢 Try again!

> Enter your choice: scissors
  Computer chose: scissors
  It's a tie! try again 🤝

> Enter your choice: rock
  Computer chose: scissors
  Congratulations! You win 🎉
```

---

## ▶️ Run It

```bash
python guess_rock_paper_scissors.py
```

---

## 🏆 Win Conditions

| Your Pick | Computer Pick | Result |
|-----------|--------------|--------|
| ✊ Rock | ✌️ Scissors | WIN 🎉 |
| ✋ Paper | ✊ Rock | WIN 🎉 |
| ✌️ Scissors | ✋ Paper | WIN 🎉 |
| Same | Same | TIE 🤝 |
| Anything | Stronger pick | LOSE 😢 |

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `random.choice()` | Computer picks random sign |
| `while True` | Keep playing until win |
| `input()` | Get player's choice |
| `if / elif / else` | Check win, lose, or tie |
| `and` operator | Two conditions at once |
| `break` | Exit when player wins |

---

## 💻 Source Code

```python
import random

print("WELCOME TO ROCK PAPER SCISSORS GAME! ❤❤❤😊")

while True:
    guess = input("Enter your choice rock, paper or scissors 💪🔥: ")
    secret_sign = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", secret_sign)

    if guess == secret_sign:
        print("It's a tie! try again 🤝")
    elif guess == "rock" and secret_sign == "scissors":
        print("Congratulations! You win 🎉")
        break
    elif guess == "paper" and secret_sign == "rock":
        print("Congratulations! You win 🎉")
        break
    elif guess == "scissors" and secret_sign == "paper":
        print("Congratulations! You win 🎉")
        break
    else:
        print("You lose! 😢 Try again!")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
