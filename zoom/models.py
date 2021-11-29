from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'zoom'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # PreZoom関係
    risk1 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    risk2 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    risk3 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    risk4 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    risk5 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )

    # ZoomIn関係
    zoom1 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    zoom2 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    zoom3 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    zoom4 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )
    zoom5 = models.IntegerField(
        label='',
        choices=[[1, 'くじW'], [0, 'くじM']],
        widget=widgets.RadioSelectHorizontal
    )    

    sw_point = models.IntegerField(initial=500)
    
    page_back = models.BooleanField(initial=True)

    page_back_count = models.IntegerField(initial=-1)

    