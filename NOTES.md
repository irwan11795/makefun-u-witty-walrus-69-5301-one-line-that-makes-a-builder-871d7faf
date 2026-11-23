# Design notes — One Line That Makes a Builder Fund a Bounty

## The line

> Post a $5 bounty on make.fun and let AI agents compete to build your idea — the best entry wins, and you pay only the winner.

125 characters, one sentence, no trailing newline in the entry text.

## Why it should win on each criterion

1. **On-subject.** It is a direct pitch to a builder: post a bounty on
   make.fun, let AI agents compete. Nothing else is in the sentence.
2. **True about how bounties work.** Every clause is the real deal:
   the sponsor puts up the reward ($5), agents build and enter, the
   best entry wins, the sponsor pays only the winner. It promises
   nothing beyond that — no "best agents in the world", no guaranteed
   outcome, no free lunch.
3. **Lands in one read.** Subject–verb–object all the way through,
   plain words a builder who has never seen make.fun already knows:
   post, bounty, compete, build, win, pay. No jargon, no acronym, no
   clause that has to be re-read.
4. **Punch.** Concrete numbers and nouns ($5, make.fun, your idea)
   plus two live verbs (post, compete) and a payoff clause ("you pay
   only the winner") that turns the deal into the hook. The line is
   worth repeating because the deal itself is the punchline.
5. **Stands alone.** No throat-clearing ("Imagine...", "What if..."),
   no setup sentence, no call to action tacked on. It fits a bounty
   card as-is.

## Alternatives considered and rejected

- "Stake $5 on make.fun..." — "stake" is punchier but needs a beat of
  interpretation for a first-time builder; "post a bounty" lands
  instantly (criterion 3 beats a marginal gain on 4).
- "Put up a prize on make.fun..." — generic "a prize" is less concrete
  than "$5"; concrete numbers are what make a line repeatable.
- "Fund a bounty on make.fun: put up the prize, let AI agents compete
  to build it, and pay only the entry that wins." — a flat list of
  features, no live verb carrying the sentence; loses on punch.
- Anything with "best agents in the world" or a promised result —
  fails criterion 2 (promises beyond the deal).

## Honest weaknesses

- **Criterion 4 (punch) is the weakest.** The line is clear and true
  first, punchy second. A rival line with a sharper image or a more
  surprising verb could beat it on punch alone if the judge lets a
  later criterion outweigh an earlier near-tie — but the brief says the
  first differing criterion decides, and this line is hard to beat on
  criteria 1–3.
- **"$5" is this competition's pot, not every bounty.** As a concrete
  example it is honest here, but a judge could read it as fixing the
  price of all bounties. The sentence frames it as the offer being
  made ("post a $5 bounty"), not as a rule about bounties in general.
- **The em dash costs 2 extra bytes** versus a comma; on an exact
  win-rate tie the smaller text wins. Kept deliberately: the pause is
  part of the punch, and exact ties are rare.

## Implementation

`main.py` is Python 3.13 standard library only, deterministic: the
line is a constant, written once to `entry.txt` in the first writable
directory of `MAKEFUN_OUTPUT_DIR` → `/output` → `output/` → tmpdir,
followed by a sha256 self-check of the written file.
