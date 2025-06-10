from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Tus buenos vecinos</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #003DA5; /* Azul Banco General */
            color: white;
            margin: 0;
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        h1 {
            font-size: 3rem;
            font-weight: 700;
            color: white;
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <h1>Tus buenos vecinos!!! Prueba</h1>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
