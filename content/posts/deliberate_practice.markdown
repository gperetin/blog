Title: Deliberate practice in software engineering
Date: 2017-07-29
Slug: deliberate-practice-software-engineering

Recently I read a book called [Peak][1], from Anders Ericsson, in which author
describes how people become good (world class good) at what they do. I don't
want to spoil it for you, but I'll say that author believes that talent has
nothing (or very little) to do with it. Continued, persistent, focused and
targeted training is the key. Author calls it *deliberate practice*.

There are many examples in the book on how exactly deliberate practice looks
like for people mastering chess, music instrument or a simpler task
such as trying to memorize a lot of numbers.

They all come down to these main principles:

* **Long term** - The efforts these people put in is often times spanning decades.
* **Hard** - The practice has to be outside of one's comfort zone. It is hard to
    learn something new and improve if we keep repeating what we already know.
    I also think that this is what differentiates people with "10 years of
    experience" and "1 year repeated 10 times".
* **Specific** - Practice has to be focused on a specific area, for example,
    playing a certain note, mastering a specific chess strategy or achieving a
    certain milestone. Progress has to be measurable.
* **Feedback** - Proper feedback is critical. Not only this helps us improve in
    the right way, but it is often times also crucial for motivation to keep
    working, which is required over such a long time.

Author provides much more evidence in the book as to what exactly happens
during deliberate practice, but here's the brief: **Deliberate practice helps
to develop new mental representations that are held in long term memory.
Expert performance is the ability to see patterns that seem random or
confusing to people with less developed mental representations, therefore the
main goal of deliberate practice is developing new mental representations.**

There are two prerequisites for deliberate practice to be most effective:

* **Reasonably well developed field** - Best performers have attained a
    level of performance that clearly sets them apart from people just
    entering the field, and we can easily identify those experts.
* **Teacher** - Teacher provides practice activities designed to help a student
    improve his or hers performance.

When it comes to software engineering, we're a bit unlucky, as our field
doesn't lend itself nicely to deliberate practice. It is a reasonably new
field and we're still trying to figure out what exactly sets experts apart.
Additionally, it is sometimes hard to measure progress in software engineering
performance. There are areas that are measurable such as algorithmic
programming which even has a competitive scene, but those hardly encompass
what we as software engineers do. Luckily, I think we're over the "how many
lines of code can one write" as a measure of performance.

Furthermore, author says: *Deliberate practice develops skills that other
people have already figured out how to do and for which effective training
techniques have been established*. I don't think we've figured out software
engineering yet and we definitely don't have effective training techniques. I
also don't think this is necessarily a bad idea, it just means that more
things are left on us to experiment with. Additionally, our field and
environment in which we work change so fast it will be hard to establish
techniques that will be valid in a couple of years or decades. Computers we
have today are vastly more powerful than those of 20 years ago, problems we're
facing today are very different and require different approaches and skills to
solve and business requirements have evolved as well. While we're on this
topic, I don't think our tools have evolved proportionally - we're still using
the same tools and methods to develop software we did 40 or 50 years ago and
seems like we're convinced a new JavaScript framework will save the day. This
is a topic for another post, but [Bret Victor][2] has some
great content on this.

## What can we do

However, we can get close. While we might not know what exactly does it mean
to be an expert or a master in software engineering, we can still employ the
ideas of deliberate practice to improve.

Here are some things that worked for me:

* **Try out different programming languages** - If you're using Java or Python at
    your day job, try Clojure, Scala or Haskell. Pick a different programming
    paradigm, that will make it easier to achieve your goal of creating mental
    representations. I haven't realized the benefit of this until a job change
    forced me to try another language, and now I'm happy I did. While
    you're experimenting, don't get bogged down by the syntax, tooling,
    ecosystem and libraries, these are all incidental to your mission here.
    Focus on *how* and *why* are things done differently? For example, if you're starting
    with Haskell, ask yourself these questions: how do we deal with state
    here? How is that different from what I know? What are the benefits and
    drawbacks of using pure functions and how does that impact the program
    structure? Do they have exceptions here and how to deal with those? What
    exactly does lazy mean?
* **Try doing the same thing different way** - If you usually write the code
    first, then tests, try doing it the other way around. If you develop core
    abstractions first and work your way out from there, try developing the
    API first and work down.
* **Take on a scary task** - One of those for which you would say "no way I know
    how to do this". This can be contributing to an open source library you
    use or documenting a certain part of a system you know nothing about.
* **Dive deep** - Understand how a library, tool or system works. Ask yourself why
    does it work that way, would you make it other way? Try to find out the
    context that engineers had when they were designing it. Don't just glance
    over the code, draw out diagrams, what are the inputs, outputs? Which
    data stores are being used? How does the API look like? For which use
    cases do you think this would work well, for which would it not?
* **Find your expert** - Find a friend or coworker that you know is better than
    you in a certain area. Discuss his or hers approach to working in that
    area, best practices and ask for suggestions on tasks you could do to
    improve. Request feedback and discuss solutions.

Lastly, remember, by definition deliberate practice is outside of your comfort zone,
which means it will and should be hard. If you're struggling, that's good, keep it up.

[1]: https://www.amazon.com/Peak-Secrets-New-Science-Expertise-ebook/dp/B011H56MKS/ref=sr_1_2?ie=UTF8&qid=1501346265&sr=8-2&keywords=peak
[2]: http://worrydream.com/
