''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package:
from flask import Flask, render_template, request
# Import the emotion_analyzer function from the package created:
from emotion_detection import emotion_analyzer

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion analysis over it using emotion_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_analyzer(text_to_analyse)

    if result['dominant_emotion:'][0] is None:
        resposta = "Invalid input! Try again."
    elif result['dominant_emotion:'][0] == "":
        resposta = "Empty input! Write something."
    else:
        dominant = result['dominant_emotion:'][0]
        anger = result['anger:']
        disgust = result['disgust:']
        fear = result['fear:']
        joy = result['joy:']
        sadness = result['sadness:']
        resposta = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is <b>{dominant}</b>."
    return resposta

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
