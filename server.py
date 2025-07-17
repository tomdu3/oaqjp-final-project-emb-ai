from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection_route():
    """Emotion detection handler."""

    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)
    
    if res['dominant_emotion'] is None:
        return {"message": "Invalid text! Please try again!"}, 400


    emotions = [f"'{key}': {value}" for key, value in res.items()]
    emotions.pop()


    output = f'''For the given statement, the system response is {','.join(emotions)}. The dominant emotion is <b>{res['dominant_emotion']}</b>.'''
    return output

@app.route("/")
def render_index_page():
    """Index page handler"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)