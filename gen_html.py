import html
import os
import json
   
with open('descriptions.json', 'r', encoding='utf-8') as json_file:
    descriptions = json.load(json_file)
    
# List of Python source files
code_blocks = []

# Read and prepare code from each configured file
for file_config in descriptions["files"]:
    filename = file_config["filename"]
    description = file_config["description"]
    with open(filename, 'r', encoding='utf-8') as file:
        code = file.read()
    # Escape HTML characters
    escaped_code = html.escape(code)
    code_blocks.append((os.path.basename(filename), escaped_code, description))
    
# HTML template for the whole page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Code Display with TOC</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/themes/prism-okaidia.min.css" rel="stylesheet"/>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet"/>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #fafafa;
            color: #333;
        }}
        .container {{
            display: flex;
            justify-content: space-between;
        }}
        .toc {{
            width: 20%;
            border-right: 2px solid #ccc;
            padding-right: 20px;
        }}
        .content {{
            width: 75%;
        }}
        h1, h2 {{
            color: #333;
        }}
        pre {{
            background-color: transparent;
            border-left: 5px solid #f36d33;
            overflow: auto;
            padding: 1em;
            position: relative;
        }}
        code {{
            font-size: 1.1em;
        }}
        a {{
            text-decoration: none;
            color: #06f;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        /* Custom styling for line numbers */
        .line-numbers .line-numbers-rows {{
            border-right: 1px solid #ddd;
        }}
        .line-numbers-rows > span:before {{
            color: #888;
        }}
    </style>
</head>
<body>
    <h1>Introduction to Image Processing with OpenCV</h1>
    <p>This introduction sits are creating for the experimental class at Dept. of Applied Computer Engineering, TOKAI Univ.</p>
    <div class="container">
        <div class="toc">
            <h2>Table of Contents</h2>
        <ol>
            {toc_items}
        </ol>
    </div>
    <div class="content">
        <h1>Python Code Examples</h1>
        {code_sections}
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/components/prism-python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
</body>
</html>
"""

# Generate HTML for TOC and code sections
toc_html = []
code_html_parts = []
code_html_parts = []
for idx, (filename, code, description) in enumerate(code_blocks, start=1):
    anchor_id = f"source{idx}"
    toc_html.append(f'<li><a href="#{anchor_id}">{filename}</a></li>')
    code_html = f'<h2 id="{anchor_id}">{filename}</h2><p>{description}</p><pre class ="line-numbers"><code class="language-python">{code}</code></pre>'
    code_html_parts.append(code_html)

 
# Join all HTML parts
toc_html_string = "\n".join(toc_html)
full_code_html = "\n".join(code_html_parts)

# Final HTML
final_html = html_template.format(toc_items=toc_html_string, code_sections=full_code_html)

# Write to output HTML file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(final_html)

print("HTML file has been generated with a table of contents!")
