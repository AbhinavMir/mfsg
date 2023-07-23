import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

source = """
Hello, *world*! This is a ~~good~~marvelous day!
Here is an auto link: https://example.org/

Le me introduce you to [task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk

You can also have fenced code blocks:

```python
import this
```

$1=1$
"""

# Direct conversion:
html = markdown.markdown(
    source, extensions=[GithubFlavoredMarkdownExtension()])

# Factory-like:
md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
html = md.convert(source)

# By module name (not recommended if you need custom configs):
html = markdown.markdown(source, extensions=['mdx_gfm'])

with open('output.html', 'w') as f:
    f.write(html)