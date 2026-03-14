import re, os, http.server, socketserver

base = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base, 'elektra-ifs-site.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(
    r'src="data:image/png;base64,/9j/[^"]{1000,}"',
    'src="LOGO ELEKTRA (1).png"',
    content
)

count = content.count('data:image/png;base64,/9j/') - new_content.count('data:image/png;base64,/9j/')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Done — {count} logo(s) replaced.")

os.chdir(base)
PORT = 8082
Handler = http.server.SimpleHTTPRequestHandler
Handler.log_message = lambda *a: None
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
