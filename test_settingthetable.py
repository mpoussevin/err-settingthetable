"""Tests for the SettingTheTable module."""
import os
from errbot.backends.test import testbot


class TestSettingTheTable(object):
    extra_plugin_dir = "."

    def test_look_out_for_table_flips(self, testbot):
        """Test the module's function setting tables."""
        testbot.push_message("(╯°□°）╯︵ ┻━┻")
        assert "┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
        testbot.push_message("(╯°□°)╯︵ ┻━┻")
        assert "┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
        testbot.push_message("(╯°□°）╯︵ ┻━┻ ┻━┻")
        assert "┬──┬ ┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
        testbot.push_message("(╯°□°）╯︵ ┻━┻┻━┻")
        assert "┬──┬ ┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
        testbot.push_message("(╯°□°）╯︵ ┻━┻ ┻━┻ ┻━┻")
        assert "┬──┬ ┬──┬ ┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
        testbot.push_message("(╯°□°）╯︵ ┻━┻ ┻━┻ ┻━┻ ┻━┻")
        assert "┬──┬ ┬──┬ ┬──┬ ┬──┬ ノ( ゜-゜ノ)" in testbot.pop_message()
