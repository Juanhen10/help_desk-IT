from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Call(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    responsible = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Aberto")
    created_by = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sla_time = db.Column(db.Integer, nullable=False)
    archived_at = db.Column(db.DateTime, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/register_call', methods=['POST'])
def register_call():
    data = request.get_json()
    priority = data['priority']
    
    # Calcular tempo SLA com base na prioridade
    if priority == "Alta":
        sla_time = 24 * 60 * 60  # 24 horas em segundos
    elif priority == "Média":
        sla_time = 2 * 24 * 60 * 60  # 2 dias em segundos
    else:
        sla_time = 7 * 24 * 60 * 60  # 1 semana em segundos
    
    new_call = Call(
        title=data['title'],
        description=data['description'],
        type=data['type'],
        priority=data['priority'],
        responsible=data['responsible'],
        status=data['status'],
        created_by=data['created_by'],
        created_at=datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S'),
        sla_time=sla_time
    )
    db.session.add(new_call)
    db.session.commit()
    return jsonify({"message": "Chamado registrado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
