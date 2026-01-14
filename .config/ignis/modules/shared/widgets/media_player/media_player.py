from ignis import  widgets
from ignis.services.mpris import MprisService, MprisPlayer

from .players import  PlayerBar

mpris = MprisService.get_default()

class MediaPlayer(widgets.Box):
    def __init__(self, widget: str) -> None:
        super().__init__(
            vertical=True,
            setup=lambda self: mpris.connect(
                "player_added",
                lambda x, player: self._add_player(widget, player)
            )
        )

    def _add_player(self, widget: str, mpris: MprisPlayer):
        player = PlayerBar(mpris)

        self.append(player)
        # player.set_reveal_child(True)
