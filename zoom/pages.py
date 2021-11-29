from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class PreZoom(Page):
    form_model = 'player'

    # modelsのrisk1~risk5まで入れたい場合は、range(x, y)のxに1、yに5+1の6をいれる
    # modelsのrisk5~risk10まで入れたい場合は、range(x, y)のxに5、yに10+1の11をいれる
    # この書き方はforの内包表記という
    # str()はintegrをstringに変換する関数
    risks = ["risk" + str(i) for i in range(1,6)] 

    # *記号はリストの展開
    form_fields = [*risks,]

    def is_displayed(self):
        return self.player.page_back

    def before_next_page(self):
        # スイッチポイントの計算
        pass
        


class Zoom(Page):
    form_model = 'player'

    zooms = ["zoom" + str(i) for i in range(1,6)] 

    form_fields = [*zooms, "page_back"]
    
    def is_displayed(self):
        return self.player.page_back

    def vars_for_template(self):
        # スイッチポイントをつかって
        # 画面に表示する選択肢の数字を調整
        # スイッチポイントが確実に400円の時だったらそれを基準にして
        # price1 = sw_point-100, price2 = sw_point-50, price3 = sw_point, price4 = sw_point+50, price5 = sw_point+100
        # というような感じで画面に表示したい

        return dict(
                price1 = self.player.sw_point - 100, 
                price2 = self.player.sw_point - 50, 
                price3 = self.player.sw_point, 
                price4 = self.player.sw_point + 50, 
                price5 = self.player.sw_point + 100
            )

    def before_next_page(self):
        self.player.page_back_count += 1

# ページループ用
zooms = []
for i in range(30):
    zooms.append(PreZoom)
    zooms.append(Zoom)

# ページの順番
page_sequence = [
    *zooms,
    ]
