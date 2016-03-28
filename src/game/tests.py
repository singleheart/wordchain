from django.test import TestCase

from .myDictionary import myDictionary
from .gameRule import Game

# Create your tests here.

class BasicTests(TestCase):
    def testIsExist(self):
        self.assertTrue(myDictionary.isExist("사과"))
        self.assertFalse(myDictionary.isExist("빠빠빠"))


    def testIsNoMoreWord(self):
        """
        this should return True
        """
        gameRule = Game()
        self.assertEqual(False, gameRule.isNoMoreWord("빠빠빠"))
        