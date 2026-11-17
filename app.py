from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    senha = ""
    forca = ""
    erro = ""
    tamanho = 12

    if request.method == "POST":

        try:
            tamanho = int(request.form["tamanho"])

            if tamanho < 8:
                erro = "A senha deve ter pelo menos 8 caracteres!"

            elif tamanho > 128:
                erro = "O tamanho máximo permitido é 128 caracteres!"

            else:
                caracteres = (
                    string.ascii_letters
                    + string.digits
                    + string.punctuation
                )

                senha_lista = [
                    secrets.choice(string.ascii_uppercase),
                    secrets.choice(string.ascii_lowercase),
                    secrets.choice(string.digits),
                    secrets.choice(string.punctuation)
                ]

                for i in range(tamanho - 4):
                    senha_lista.append(
                        secrets.choice(caracteres)
                    )

                secrets.SystemRandom().shuffle(senha_lista)

                senha = "".join(senha_lista)

                if tamanho < 12:
                    forca = "Senha razoável"
                elif tamanho < 16:
                    forca = "Senha forte"
                else:
                    forca = "Senha muito forte"

        except ValueError:
            erro = "Digite um número válido!"

    return render_template(
        "index.html",
        senha=senha,
        forca=forca,
        erro=erro,
        tamanho=tamanho
    )


if __name__ == "__main__":
    app.run(debug=True)