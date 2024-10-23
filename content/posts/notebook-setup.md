# Jupyter Notebook Setup for Research and Production

Over time, I've accumulated over 100 Jupyter notebooks containing various research, strategies, reports, and other trading-related things. Versioning Jupyter notebooks can be a bit of a pain, and there are packages that help with that. Of those, I've tried jupytext but never stuck with it. To prevent a disaster in case of a disk failure, I've set up twice-daily off-box backups of the notebooks folder on the server.

I wanted to improve on that setup and, while I’m at it, solve a few other issues:

* **Code reuse** - There's a common setup that repeats across notebooks, where some behavior is reused in many of them, e.g., data fetching, some DataFrame manipulation functions, and graph generation. It would be great to have that behavior extracted into a single place.
* **Editor** - I've been using Jupyter's browser editor for 4+ years now, and it's time to upgrade to something better—ideally, a proper text editor.
* **Notebook execution** - I have notebooks where I've iterated on something to produce a report, and now I’d like to have them run daily. So the ideal solution would involve a way to run a Jupyter notebook, collect some results, and store them somewhere.
* **Local and remote** - My entire setup is currently running on a Hetzner dedicated server (a future post on this is incoming), and some portions of the new setup will still have to run there because (a) that’s where the data is (and it's not trivial to replicate that amount of data) and (b) batch jobs. However, I would like to move some parts locally, e.g., development and testing of notebooks.

## Editor

![Python snippet in VS Code interactive mode](https://i.snap.as/H30I84Ct.png)
<div style="text-align:center;"><small><em>Python snippet in VS Code interactive mode</em></small></div>

I recently discovered [VS Code Interactive mode for Python](https://code.visualstudio.com/docs/python/jupyter-support-py), and it checked off some of the boxes I had for a notebook/development solution. I decided to try it and liked it a lot. The main reason I liked it is that the notebook is valid Python code, not code intermingled with output in a JSON blob like `.ipynb`. The cell-focused development workflow is still present, though. There are also some nice features like outputs in a separate panel and a solid [data explorer](https://code.visualstudio.com/docs/datascience/data-wrangler). So, even though I don't use VS Code as my main editor, I switched to it for notebook development.

Having notebooks as pure Python files also solved the versioning issue, as well as code reuse. I can now simply extract common code into another Python module and import it where needed.

## Batch Jobs

Next up was figuring out how to run a notebook as a batch job. I'm currently using [Dagster](https://github.com/dagster-io/dagster) as a workflow automation tool for my trading, which includes running anything that resembles a cron job. So, I needed a way to somehow run the `.py` notebook from a Dagster job. One solution was to wrap the code in the notebook in a function, then import that function and run it, however, I would then lose the notebook-centric development style of working and iterating on individual cells. Wrapping each cell into its own function just sounded too cumbersome - I didn't want to have to make changes to a notebook just because I wanted to run it as a batch job.

The solution ended up being simpler than I thought it would be: since all the code in the notebook is top-level, meaning it’s executed on import, all that was needed was to import the notebook from my batch job runner. `importlib` to the rescue! Additionally, when developing/testing a notebook, I don’t always want to store or persist the results. Sometimes just viewing a DataFrame or any other output is enough. However, for running batch jobs, I usually want to store the results, which means I needed a way to fetch some outputs from the notebook.

Here's the code snippet that does both of the above:

```python
import importlib


def run_notebook(notebook: str, results: list[str]) -> list:
    """Runs a notebook with a given name.

    Since notebooks contain top-level code which is executed on import,
    this will just import the notebook and return the variables from
    the module namespace.

    Returns a list of variables matching the input parameter `results`.
    Variables can be anything that's defined in the notebook—DataFrames,
    lists, simple types, etc.

    """
    module = importlib.import_module(notebook)
    res = []
    variables = module.__dict__
    for r in results:
        if r in variables:
            res.append(variables[r])
        else:
            res.append(None)

    return res

```

So, if I wanted to run a notebook called `performance_report` and fetch the `perf_df` DataFrame, I would do:

    perf_df = run_notebook("performance_report", results=["perf_df"])[0]

The results are then persisted from within the Dagster job. I have that snippet alongside the notebooks in the `research` git repo, so anything that wants to run any notebook just calls that function. In my case, my Dagster deployment has a dependency on the `research` git repo, so any notebook in the repo can be executed like this.

## Future Improvements

One thing I'd like to try is running VS Code on the server and using the remote development feature to develop on the server (thanks [Senko](https://senko.net/) for the suggestion). This would help with notebooks for which I can’t download a sample test dataset to my workstation for development and testing. It should also make it easier to develop on the go since the handoff between machines would be simpler in that case. However, I haven’t found my current setup (commit + push to git + pull on another machine) to cause much friction yet.
