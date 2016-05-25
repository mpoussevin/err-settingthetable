"""Errbot plugin to set the table when it's flipped."""
import re
from errbot import BotPlugin, re_botcmd


class SettingTheTable(BotPlugin):
    """Errbot plugin to set the table when it's flipped."""

    @re_botcmd(pattern=r"\(╯°□°\）╯︵ ┻━┻", prefixed=False, flags=re.IGNORECASE)
    def look_out_for_table_flips(self, msg, match):
        """Set the table when it's flipped."""
        return "┬──┬ ノ( ゜-゜ノ)"
