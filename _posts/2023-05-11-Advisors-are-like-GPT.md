---
title: "Advisors are like GPT"
layout: single
excerpt: "There are some similarities in talking with my PhD advisor and prompting ChatGPT."
categories:
  - research
  - thoughts
---

I mean, my advisor is not a GPT model of course.
However, talking with my advisor is not like just talking to my friend or colleague.
Efficiently getting advice from him within bounded time requires a certain mental model of how he thinks and acts, and I realized that it's sort of similar to prompting GPT models.

## GPT is Stateless

GPT will remember the details of the conversation in the same thread, but that's only because they cram in the entire conversation in their context window.
Outside that window, they are basically stateless; when you start a new conversation with GPT, it'll have an empty context and won't remember anything about your previous conversations.

Advisors are often also stateless.
Not that they're stateless intentionally or by design, but due to the sheer amount of things going on around them, it's more convenient for students to assume them to be stateless and forget everything.
It's just like how you don't ask ChatGPT, "Hey I think I asked you something about NP-Hardness in another thread last month, do you remember that?"

## Context is Important

That's why initializing GPT's context right is important.
You would have experienced some conversations with ChatGPT where you screwed up the initial description of your problem, and it takes more words to correct ChatGPT's understanding than what would have taken if you had described it right in the first place.
In such cases you can just mutter "Crap." and click 'New Chat' (because ChatGPT is stateless).
However, unfortunately, that's not so easy if you were talking to your advisor.
Therefore, I try to make sure my advisor's context is initialized with a concise and accurate picture of where my research is.

I think this is especially observable when I sometimes hear contradicting advice from my advisor.
Not contradicting with my opinion, but with his own advice in the past.
That's probably because the contexts I gave to my advisor that led to those contradictory advices were inconsistent in some way.
Therefore, usually my next action is to prompt my advisor further to find out if there are any misunderstandings, either in the previous meeting or this one.

## Fine-Tuning GPT

I've been saying all along that advisors are stateless, but we all know that they're not completely stateless all the time.
So, I like to think that they take one fine-tuning step at the end of every meeting, and their learning rate depends on how interesting the meeting was (and also on other things that I can't control).
If I excite my advisor with some interesting observation or good result, they're more likely to remember.
Otherwise, they probably won't remember what happened during the last meeting.

In that sense, I think it's an effective strategy to present my advisor with a concise summary at the end of the meeting.
That way they don't have to summarize the entire meeting on their own for fine-tuning, but rather just directly use the takeaway messages I present.
For that, I also try to set forth a couple TODO bullets that are rooted on the core takeaways of this meeting and roughly represent what my advisor can expect for the next meeting.
