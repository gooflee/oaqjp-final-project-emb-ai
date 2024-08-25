""" Test case for Emotion Detection """

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """ Base class for the tests """
    def test_emotion_detection(self):
        """ tests """

        # test for joy
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"],"joy")

        # test for anger
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'],"anger")

        # test for disgust
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'],"disgust")

        # test for sadness
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'],"sadness")

        # test for fear
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'],"fear")


unittest.main()

