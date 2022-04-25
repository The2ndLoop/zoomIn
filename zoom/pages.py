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
        flag = self.player.page_back
        
        if self.player.sw_point is False:
            flag = False

        return flag

    def before_next_page(self):
        '''
        【パターン1】
        最初からW(1)を選択する変なやつの場合
        分析から外したいので、ZoomInのページは表示しない。
        sw_pointにFalseでもいれてfor文抜ける。
        flagが1になる可能性があるので、とっととfor文を抜ける
        '''
        if self.player.risk1 == 1:
                sw_point = False
        else:
            risks = [self.player.risk1, self.player.risk2, self.player.risk3, self.player.risk4, self.player.risk5,]
            
            # くじMの1問目の価格をとりあえず入れとく。後で理由は分かる。
            # 本当はConstantsとかに設定しておくべき
            sw_point = 400

            risks_len = len(risks)  

            # スイッチポイントの計算
            for idx, risk in enumerate(risks):
                '''
                【パターン2】
                全部Mのやつ
                これは0->1にスイッチしないので、flagが永遠に0でfor文を完遂する。
                今回の場合、最後の質問は「確実に0円」、100円刻みなので、-100円をスイッチポイントとして仮定する。
                '''

                # ２問目でスイッチしたとするとスイッチポイントは300円
                # ということは、ループする度にsw_pointから100ずつ引いていけばスイッチポイントになる。
                sw_point -= 100

                # 例外処理
                # 最終ループのときさっさと抜けないとflagの計算でidx+1番目の要素がないとエラーが起きる。
                if risks_len == idx + 1:
                    break

                # このコードは最終ループでエラーを起こす。
                # idx + 1が5になったらそんなのリストにありませんって言われる。
                flag = risks[idx +1] - risks[idx]

                '''
                【パターン2】
                合理的にいくと初めはM(0)を選択する。
                途中でW(1)に選択をスイッチする。
                M->Wすなわち0->1にスイッチしたときはflagが1のときで捕捉できる。
                【パターン3】
                MWMMWWみたいなM→W行ったのにMに戻る変な人。
                最初のM→Wの部分がスイッチポイントで処理。
                これもflagが1になった瞬間にfor文抜ければ良い。
                '''
                
                if flag == 1:
                    break

        self.player.sw_point = sw_point



class Zoom(Page):
    form_model = 'player'

    zooms = ["zoom" + str(i) for i in range(1,6)] 

    form_fields = [*zooms, "page_back"]
    
    def is_displayed(self):
        flag = self.player.page_back
        
        if self.player.sw_point is False:
            flag = False

        return flag

    def vars_for_template(self):
        # スイッチポイントをつかって
        # 画面に表示する選択肢の数字を調整
        # スイッチポイントが確実に400円の時だったらそれを基準にして
        # price1 = sw_point-100, price2 = sw_point-50, price3 = sw_point, price4 = sw_point+50, price5 = sw_point+100
        # というような感じで画面に表示したい

        return dict(
                price1 = self.player.sw_point + 50, 
                price2 = self.player.sw_point + 25, 
                price3 = self.player.sw_point, 
                price4 = self.player.sw_point - 25, 
                price5 = self.player.sw_point - 50
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
