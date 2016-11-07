"""Errbot plugin to set the table when it's flipped."""
import re
from errbot import BotPlugin, re_botcmd


class SettingTheTable(BotPlugin):
    """Errbot plugin to set the table when it's flipped."""

    @re_botcmd(pattern=r"\(╯°□°(）|\) ?)╯︵ ┻━┻", prefixed=False, flags=re.IGNORECASE)
    def look_out_for_table_flips(self, msg, match):
        """Set the table when it's flipped."""
        self.log.info("Table flip pattern matched for <%s>.", msg._body)
        # Count number of tables
        n_tables = len(re.findall("┻━┻", msg._body))
        if n_tables == 0:
            self.log.warning("No table in message: %s", msg._body)
        elif n_tables > 1:
            self.log.info("Setting the %d tables.", n_tables)
            text = " ".join(["┬──┬" for _ in range(n_tables)])
            text += " ノ( ゜-゜ノ)"
            self.log.info("Answering: %s", text)
            return text
        else:
            self.log.info("Setting the table.")
            text = "┬──┬ ノ( ゜-゜ノ)"
            self.log.info("Answering: %s", text)
            return text
