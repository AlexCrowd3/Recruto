from flask import Flask, request, render_template

app = Flask(__name__)

def validate_input(name, message):
    errors = []

    # Проверяем, были ли вообще переданы параметры
    if 'name' not in request.args:
        errors.append("Параметр 'name' должен быть указан в URL")
    if 'message' not in request.args:
        errors.append("Параметр 'message' должен быть указан в URL")

    # Остальные проверки остаются
    if len(name) > 100:
        errors.append("Имя слишком длинное (макс. 100 символов)")
    if len(message) > 200:
        errors.append("Сообщение слишком длинное (макс. 200 символов)")
    if not name.strip():
        errors.append("Имя не может быть пустым")
    if not message.strip():
        errors.append("Сообщение не может быть пустым")

    return errors

@app.route('/')
def greeting():
    name = request.args.get('name', '').strip()
    message = request.args.get('message', '').strip()
    errors = validate_input(name, message)

    if errors:
        return render_template('error.html', errors=errors)

    return render_template('greeting.html', name=name, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)