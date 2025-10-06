"""
Musobaqa g'olibi
Algoritmik musobaqada jamoalar round-robin usulida o‘ynashadi — har jamoa boshqalari bilan bir martadan bellashadi.

Har bir o‘yinda faqat bitta g‘olib bo‘ladi: uy jamoasi g‘alaba qozonsa 1, mehmon jamoasi yutsa 0 bilan belgilanadi.

Sizga competitions va results nomli ikkita array beriladi. competitions o‘yinda ishtirok etgan jamoalarni, results esa har bir o‘yin natijasini bildiradi. G‘olib 3 ball oladi, mag‘lub esa 0 ball. Natijada eng ko‘p ball to‘plagan jamoa musobaqa g‘olibi bo‘ladi.

💡 Eslatma: musobaqada kamida ikkita jamoa qatnashadi.

Misol uchun
competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
results = [0, 0, 1]
Kutilgan natija
"Python"
Tushuntirish:  C# — HTML ni yengdi, Python — C# ni yengdi, Python — HTML ni ham yengdi.
 HTML — 0 ball
 C# — 3 ball
 Python — 6 ball

"""
from idlelib.window import add_windows_to_menu


def tournamentWinner(competitions, results):
    scores = {}
    best_team = ""
    max_score = 0

    for i in range(len(competitions)):
        home, away = competitions[i]
        result = results[i]

        winner = home if result == 1 else away
        scores[winner] = scores.get(winner, 0) + 3

        if scores[winner] > max_score:
            best_team = winner
            max_score = scores[winner]

    return best_team
