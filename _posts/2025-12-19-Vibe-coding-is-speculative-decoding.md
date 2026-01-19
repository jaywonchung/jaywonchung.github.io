---
title: "Vibe Coding is Speculative Decoding"
layout: single
excerpt: "AI assistance should be hidden behind the abstraction of the author."
categories:
  - thoughts
---

Imagine reviewing some text, be it code or a paper.
You find some weird parts about it and take the time to write down comments, only to be told "Oh, I used AI to generate that part."
I don't think this is a good answer.

I treat AI-assisted programming or writing as an instance of speculative decoding.
For those unfamiliar with the term, [*speculative decoding*](https://arxiv.org/abs/2211.17192) is a technique that speeds up LLM text generation by using a smaller, faster model (the *draft model*) to generate multiple tokens, and then having the original, larger model (the *verifier model*) accept or reject those tokens through rejection sampling.
The crucial property of speculative decoding is that once we go through rejection sampling, the resulting accepted tokens *exactly* follow the distribution of the original larger model; there is no quality loss.

When I use an AI coding assistant (e.g., Copilot, Cursor) to produce code, for instance, the AI model is the *draft model*, and I (the human programmer) am the *verifier model* that accepts or rejects AI-generated code based on whether they work correctly and fit my intent.
And I make sure that the code that ultimately gets committed follows the distribution of code that I would have written myself.

I put on this mindset not only when I write text, but also when I review others' text.
I assume that whatever text has been put forward for review follows the distribution of text the author would have written themselves, and I don't care whether they used AI assistance or not; it's an implementation detail that should be hidden behind the *abstraction* of the author.
That's why I get annoyed when the answer to my review comment is "Oh, I used AI to generate that part."
It shows that the author doesn't have a proper explicit intent for that part of the text, signaling that they didn't verify thoroughly and is shifting accountability to the AI model.
This makes authorship a *leaky abstraction* and breaks the assumption that the text follows the author's distribution.

This is why I think whatever has been put forward by a human author should be attributed only to the author, and whether AI assistance was used or not is irrelevant.
If the text is great, the author should get credit for it; if it's bad, the author should take accountability for it.
I believe this mindset will help us reap the productivity benefits of AI assistance (with increasing *draft acceptance rate* as AI models get better) while maintaining quality and accountability.
