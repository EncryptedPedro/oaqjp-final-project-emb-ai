from emotion_detection import emotion_analyzer
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy_emotion(self):
        result = emotion_analyzer("I am glad this happened")
        self.assertEqual(result['dominant_emotion:'][0], 'joy')

    def test_anger_emotion(self):
        result = emotion_analyzer("I am really mad about this")
        self.assertEqual(result['dominant_emotion:'][0], 'anger')

    def test_disgust_emotion(self):
        result = emotion_analyzer("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion:'][0], 'disgust')

    def test_sadness_emotion(self):
        result = emotion_analyzer("I am so sad about this")
        self.assertEqual(result['dominant_emotion:'][0], 'sadness')

    def test_fear_emotion(self):
        result = emotion_analyzer("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion:'][0], 'fear')


unittest.main()