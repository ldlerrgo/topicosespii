from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bienvenido a Azure Container Registry</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            margin: 0;
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .container {
            background: rgba(0, 0, 0, 0.3);
            padding: 40px 60px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            max-width: 480px;
        }
        h1 {
            font-weight: 700;
            margin-bottom: 16px;
            font-size: 2.8rem;
            letter-spacing: 1.2px;
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 24px;
            line-height: 1.5;
        }
        .btn {
            background-color: #f6d365;
            color: #764ba2;
            padding: 12px 28px;
            border: none;
            border-radius: 25px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        .btn:hover {
            background-color: #fda085;
            color: white;
        }
        footer {
            margin-top: 40px;
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola desde Azure Container Registry!</h1>
        <p>Esta es una aplicación Flask desplegada con Docker y CI/CD en Azure.</p>
        <a href="https://azure.microsoft.com" target="_blank" class="btn">Visita Azure</a>
        <footer>Flask App con Docker & CI/CD</footer>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
