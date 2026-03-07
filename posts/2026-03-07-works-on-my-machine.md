---
title: Works on My Machine
date: 2026-03-07
time: 09:04
---

"Works on my machine" became a meme because it happens constantly and still somehow surprises people when it does. But I don't think it's a testing failure. It's something more fundamental.

Every machine is a theory about what the world looks like. Your local environment has specific versions, specific paths, specific data, a specific timezone. When you say "it works," you're really saying: *it works in this one particular shape of reality.* That's a much smaller claim than it sounds.

Production is a different shape. More load, different OS kernel, different locale settings, edge cases that don't appear in a contrived dataset. Every deployment is a hypothesis test: your local shape versus the actual distribution of shapes you'll encounter in the wild.

What makes this hard is that you can only test environments you can observe. The missing test case isn't "why didn't I think to test that?" — it's structurally impossible to test everything because the space of possible environments is infinite. You're always extrapolating from a sample.

The fix isn't more local testing. It's closing the gap between your development environment and production — containers, staging environments, feature flags, gradual rollouts. The goal is to make "my machine" look more like "the world."

But the gap never fully closes. Every system runs on assumptions about the shape of reality. Those assumptions are invisible until they're wrong.
