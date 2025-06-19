from flask import Flask, request, render_template

app = Flask(__name__)

def validate_input(name, message):
    errors = []
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
    name = request.args.get('name', 'Recruto').strip()
    message = request.args.get('message', 'Давай дружить').strip()
    errors = validate_input(name, message)
    
    return render_template('greeting.html', 
                         name=name, 
                         message=message, 
                         errors=errors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)