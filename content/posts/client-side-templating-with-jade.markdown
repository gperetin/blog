Title: Client side templating with Jade and Node.js
Date: 2012-03-14
Slug: client-side-templating-with-jade-and-nodejs

At my current job, we heavily use client side templating, specifically [Jade][1] template engine. We've been using Jade for couple of months now and are very happy with it. In this post, I will describe how client side templating works and how to set up development environment that allows you to work on templates and then view them in browser quickly.

We use Jade in client side mode, which means that templates are compiled to JavaScript on server (using Node.js) and populated with values on client. If this sounds weird at first, read on, it should get clearer by the end of the post :)

Whole workflow looks like this:

1. Edit `.jade` template file
2. Compile template files to JavaScript
3. Refresh page in browser to see changes

Key here is detecting that there was change to one of `.jade` files and recompiling templates; you definitely don't want to do that by hand.

### Compiling templates

Compiling templates in Jade is very simple:

<div class="gist">https://gist.github.com/3065949.js?file=sample_jade_compile.js</div>

Now you have `func` which is JavaScript function that you call with values you want to render your template with and `func` returns you HTML that you just need to put somewhere on page. Since `func` is executed in client's web browser we need to save `func` to a JavaScript file (let's call that file `templates.js`) and serve it as any other static file. So, `templates.js` will contain all of our Jade templates compiled to JavaScript.

Since templates are usually in `.jade` files, we need to parse all files and compile them. For that purpose, I wrote this short Node.js script:

<div class="gist">https://gist.github.com/3065819.js?file=jade_compile.js</div>

In order to run this script, you need to have Node.js and Jade installed. After you [install Node.js][3], Jade is simple:

    npm install jade

Now run the script:

    node jade_compile.js templates/ output/


If you go to `output` folder, you will see a file called `templates.js` which contains all your templates. You do not have to know how compiled templates look, but if you are interested in how exactly Jade *compiles* templates to JavaScript you can examine `templates.js` file. Inside, you'll find a bunch of JavaScript functions assigned to variables, one variable for each `.jade` file found in `templates` folder. Eg. if you had a file called `login.jade`, then `templates.js` would contain a function named `login` which, when called, returns HTML for your login form.

This is probably not the best way to do this because you have to link `templates.js` in your client side code, and since we know that JavaScript sucks at namespaces, if there is something else called `login` there would be name clashes. I deal with this by putting `_tpl` suffix on each of our `.jade` files, so we can access templates in browser by issuing simple `login_tpl()`. If your application is really large, probably the best solution would be to introduce namespaces to `templates.js` file.


### Detecting changes

Now that we have a way to compile all our templates, we need some way of detecting changes to `.jade` files and run compilation automatically. I use [Watchdog][2] library that comes with simple `watchmedo` command:

<div class="gist">https://gist.github.com/3066361.js?file=run_watchmedo.sh</div>

Basically, this command tells Watchdog to start monitoring `*.jade` files in `templates` folder, and if anything changes, run `node jade_compile.js templates/ output/` command.


### Performance

If you are worried about compiling *all* your templates every time you change something in any template, don't be. Node.js is *very fast* with this compilation, you probably can't Alt+Tab to browser faster than Node compiles your templates. If you have a lot of templates, try this way first and if it turns out too slow for you, then introduce some logic to template change detection process. First thing that comes to my mind is separating templates into smaller chunks (multiple folders) and treat each of them as described above.


### Conclusion
This whole process can seem a bit complicated when you read it first, but in reality it's really integrating couple of tools the way you need them to work. It took me couple of hours to set it up and I haven't touched it for couple of months now, it just works.

[1]: http://jade-lang.com
[2]: http://packages.python.org/watchdog/
[3]: http://nodejs.org/#download
