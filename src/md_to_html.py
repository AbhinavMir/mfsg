import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

def markdown_to_html(source):
    md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
    return md.convert(source)
