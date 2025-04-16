from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        emotion1 = emotion_detector("I'm glad this happened")
        emotion2 = emotion_detector("I'm really mad about this")
        emotion3 = emotion_detector("I feel disgusted just hearing about this")
        emotion4 = emotion_detector("I'm so sad about this")
        emotion5 = emotion_detector("I'm rally afraid that this will happen")

        self.assertEqual(emotion1['dominant_emotion'], 'joy')
        self.assertEqual(emotion2['dominant_emotion'], 'anger')
        self.assertEqual(emotion3['dominant_emotion'], 'disgust')
        self.assertEqual(emotion4['dominant_emotion'], 'sadness')
        self.assertEqual(emotion5['dominant_emotion'], 'fear')

unittest.main()