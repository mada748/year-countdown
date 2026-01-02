from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


def get_time_remaining():
    target = datetime(2027, 1, 1)
    adesso = datetime.now()
    diff = target - adesso

    if diff.total_seconds() <= 0:
        return None

    sec_totali = int(diff.total_seconds())
    return {
        "ore_totali": sec_totali // 3600,
        "minuti_totali": sec_totali // 60,
        "giorni": diff.days,
        "ore": (sec_totali % 86400) // 3600,
        "minuti": (sec_totali % 3600) // 60,
        "secondi": sec_totali % 60,
    }


@app.route("/")
def home():
    dati = get_time_remaining()
    return render_template("index.html", dati=dati)


if __name__ == "__main__":
    app.run(debug=True)
