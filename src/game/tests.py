from django.test import TestCase

from .myDictionary import myDictionary
from .gameRule import Game

# Create your tests here.

# 1. Home
#  * Animation(script loading 확인)
#  * Game Link
#   - Login이 안되면 Login page로 이동
#   - Login이 되면 Menu page로 이동
# 2. Login
#  * 실 계정으로만 로그인 되는 것 동작
#  * Signin Signup 제공
#  * 로그인이 안되면 error 보여줌
#  * 되면 Menu Page로 이동
# 3. Menu
#  * 로그인이 안되어 있으면 Login page로 이동
#  * 각 페이지로 이동(play, ranking)
# 4. Play
#  * 로그인이 안되어 있으면 Login page로 이동
#  * History 갱신 check
#  * Form 또는 버튼의 이벤트 확인
#  * Menu page로 이동 하는 link 확인
#  * 관찰자 모드 기능 확인
#  * Game Rule 확인
# 5. Ranking
#  * 로그인이 안되어 있으면 Login page로 이동
#  * Ranking 기능 동작 여부 확인
#  * view가 잘 보여지는지 확인
#  * Menu page로 이동 링크 확인
# 6. Game Rule 확인


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
        