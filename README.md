# err-settingthetable

Plugin for Errbot.
It detects table flipping `(╯°□°）╯︵ ┻━┻` and answers by `┬──┬ ノ( ゜-゜ノ)`.

Based on this tweet:
<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">So I configured slackbot to clean up flipped tables and I&#39;m convinced my team now hate me: <a href="https://t.co/85e9kyKnjO">pic.twitter.com/85e9kyKnjO</a></p>&mdash; Michael Pearson (@mipearson) <a href="https://twitter.com/mipearson/status/735306904642199552">25 mai 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

If you work with tricky people flipping multiples tables in one message, the plugin will try to set them all:

* `(╯°□°）╯︵ ┻━┻ (╯°□°）╯︵ ┻━┻` gives `┬──┬ ┬──┬ ノ( ゜-゜ノ)`
* `(╯°□°）╯︵ ┻━┻ ┻━┻` gives `┬──┬ ┬──┬ ノ( ゜-゜ノ)`

Updates:

* 2016/06/01: Setting multiple tables flipped in one message.
* 2016/05/25: First basic working version.

I may add more patterns in the future.
