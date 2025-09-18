
# :warning::warning::warning:

Use at your own discretion.
I do a force edit on the git history somewhere, so be really careful if you decide to try this out

# Intro / Motivation

I wanted to have the ability to edit the timestamps at which commits show up in my Git log / GitHub / etc.

> :spiral_note_pad: I want to preserve the time between commits, so maybe just starting with adding X hours to all uncommited commits.

# Context

Git commits have 2 timestamps:

| Type | ENV Variable name | Description |
|--|--|--
| **Author** | `GIT_AUTHOR_DATE` | When the work was *made* |
| **Committer** | `GIT_COMMITTER_DATE` | When the work was *committed*|

Usually the author date and the committer date are the same, so I work under that assumption.
