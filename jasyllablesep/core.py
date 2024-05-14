import re

class SyllableSeparator:
    def __init__(self):
        #「((ウ段＋「ァ/ィ/ェ/ォ」)|(イ段（「イ」を除く）＋「ャ/ュ/ェ/ョ」)|( 「テ/デ」＋「ィ/ュ」)|(大文字カナ))(「ー/ッ/ン」の連続文字列（０文字含む）)」の正規表現
        c1 = '[ウクスツヌフムユルグズヅブプヴ][ヮァィェォ]' #ウ段＋「ァ/ィ/ェ/ォ」
        c2 = '[イキシシニヒミリギジヂビピ][ャュェョ]' #イ段（「イ」を除く）＋「ャ/ュ/ェ/ョ」
        c3 = '[テデ][ィュ]' #「テ/デ」＋「ィ/ュ」
        c4 = '[アイウエオカ-ヂツ-モヤユヨ-ヲヴ]' #大文字カナ
        c5 = '[ーッン]*' #「ー/ッ/ン」の連続文字列（０文字含む）

        cond = '(?:'+c1+'|'+c2+'|'+c3+'|'+c4+')'+c5 #(?:)はサブパターンの参照を避けるカッコ
        cond = '('+cond+')'
        self.re_syllable = re.compile(cond)

    def parse(self, kana_text):
        return self.re_syllable.findall(kana_text)