from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "bc119c81-ab86-4842-b01c-9a91bc1fbbc8"
NICKNAME = "ESTSimiQ"


@app.route('/')
def get_faceit_elo():
  try:
    response = requests.get(
        f'https://open.faceit.com/data/v4/players?nickname={NICKNAME}',
        headers={'Authorization': f'Bearer {API_KEY}'})
    data = response.json()
    elo = data['games']['cs2']['faceit_elo']
    lvl = data['games']['cs2']['skill_level']

    return f'{NICKNAME} ELO: {elo}, lvl: {lvl}'

  except Exception as e:
    return f"Error: {str(e)}", 500


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
