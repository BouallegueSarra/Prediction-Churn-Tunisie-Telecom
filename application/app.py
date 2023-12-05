from flask import Flask, render_template, request, jsonify
import json



import pickle
model = pickle.load(open("model/randomForest.pkl", 'rb'))



app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('prediction.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route("/predict", methods=["POST"])
def predict():
    nb_jour_abonnee= int(request.form.get("nb_jour_abonnee"))
    duree_appel_jour = float(request.form.get("duree_appel_jour"))
    nb_appel_jour = int(request.form.get("nb_appel_jour"))
    cout_appel_jour = float(request.form.get("cout_appel_jour"))
    duree_appel_soirée = float(request.form.get("duree_appel_soirée"))
    nb_appel_soirée = int(request.form.get("nb_appel_soirée"))
    cout_appel_soirée = float(request.form.get("cout_appel_soirée"))
    duree_appel_nuit = float(request.form.get("duree_appel_nuit"))
    nb_appel_nuit = int(request.form.get("nb_appel_nuit"))
    cout_appel_nuit = float(request.form.get("cout_appel_nuit"))
    duree_appel_inter = float(request.form.get("duree_appel_inter"))
    nb_appel_inter = int(request.form.get("nb_appel_inter"))
    cout_appel_inter =float(request.form.get("cout_appel_inter"))
    active_msg_vocaux = request.form.get("active_msg_vocaux")
    nb_msg_vocaux = int(request.form.get("nb_msg_vocaux"))
    nb_reclamation = int(request.form.get("nb_reclamation"))
    if active_msg_vocaux == "Oui":
        active_msg_vocaux = "1"
    else:
        active_msg_vocaux = "0"   
    input_data = [[nb_jour_abonnee,duree_appel_jour, nb_appel_jour, cout_appel_jour,
                   duree_appel_soirée, nb_appel_soirée, cout_appel_soirée,
                   duree_appel_nuit, nb_appel_nuit, cout_appel_nuit,
                   duree_appel_inter, nb_appel_inter, cout_appel_inter,
                   int(active_msg_vocaux), nb_msg_vocaux, nb_reclamation]]
    prediction = int(model.predict(input_data))
    message_resiliation = "Résultat de prédiction : Le client résiliera son abonnement"
    message_non_resiliation = "Résultat de prédiction : Le client ne résiliera pas son abonnement"
    if prediction == 1:
        message = message_resiliation
    else:
        message = message_non_resiliation
    response = {
        "prediction": message    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()

