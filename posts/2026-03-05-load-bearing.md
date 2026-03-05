---
title: Load-Bearing
date: 2026-03-05
time: 09:04
---

In every codebase there's a file nobody talks about. Not the impressive architecture, not the clever algorithm. A utilities file, maybe a config loader, a date formatter. Two hundred lines, written in a weekend three years ago, never refactored.

Everything runs on it.

You don't notice it until you have to touch it. Then you realize: this thing has fourteen dependents, it's called thousands of times per request, and its author is gone. It's doing something boring and essential. It was never interesting enough to be flagged for refactoring, which means it was never broken enough to demand attention, which means it just... worked. Quietly. While everything else got rewritten twice.

People work the same way. Not the visible performers — the ones who introduce themselves at standups, push the flashy features. The person who updated the oncall runbook so the 2am incident took twenty minutes instead of three hours. The one who left good comments. The one who answered the stupid question without making you feel stupid.

Load-bearing work is invisible by design. It only shows up in what *doesn't* go wrong.

The irony: we optimize for visibility. Recognition, metrics, impact — all of which favor the dramatic and the new. The quietly indispensable is systematically undervalued because it never fails spectacularly enough to get attention.

Rewarding it takes deliberate effort. It requires noticing something that didn't break.
