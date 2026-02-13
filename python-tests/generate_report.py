import subprocess
import sys
import os
from datetime import datetime

# Change to the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run pytest with HTML report generation
result = subprocess.run([
    sys.executable, '-m', 'pytest',
    'test_search_pytest.py',
    '--html=test-report.html',
    '--self-contained-html',
    '-v'
], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)

# Read the generated report
with open('test-report.html', 'r') as f:
    content = f.read()

# Inject custom CSS
custom_css = """
<style>
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin: 0;
    padding: 20px;
}
.container {
    max-width: 1400px;
    margin: 0 auto;
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    padding: 40px;
}
h1 {
    color: #667eea;
    text-align: center;
    font-size: 2.8em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    font-weight: 700;
}
h2 {
    color: #764ba2;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
    margin-top: 40px;
    font-size: 1.8em;
}
.summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
    margin: 40px 0;
}
.summary-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
}
.summary-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
}
.summary-card .number {
    font-size: 3.5em;
    font-weight: bold;
    display: block;
    margin-bottom: 10px;
}
.summary-card .label {
    font-size: 1.2em;
    opacity: 0.95;
    text-transform: uppercase;
    letter-spacing: 1px;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 30px 0;
    box-shadow: 0 3px 20px rgba(0,0,0,0.1);
    border-radius: 12px;
    overflow: hidden;
}
thead {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
th {
    padding: 18px;
    text-align: left;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.95em;
    letter-spacing: 1.5px;
}
td {
    padding: 15px 18px;
    border-bottom: 1px solid #f0f0f0;
    font-size: 1em;
}
tbody tr:hover {
    background-color: #f8f9ff;
    transition: background-color 0.2s ease;
}
.passed {
    color: #10b981;
    font-weight: bold;
    font-size: 1.1em;
}
.failed {
    color: #ef4444;
    font-weight: bold;
    font-size: 1.1em;
}
.passed::before {
    content: "✓ ";
    font-size: 1.3em;
}
.failed::before {
    content: "✗ ";
    font-size: 1.3em;
}
.environment {
    background: linear-gradient(135deg, #f8f9ff 0%, #e8eaff 100%);
    padding: 25px;
    border-radius: 12px;
    margin: 30px 0;
    border-left: 6px solid #667eea;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.timestamp {
    text-align: center;
    color: #666;
    font-style: italic;
    margin-top: 40px;
    padding-top: 25px;
    border-top: 2px solid #e0e0e0;
    font-size: 1.1em;
}
.header-info {
    text-align: center;
    color: #764ba2;
    font-size: 1.2em;
    margin-bottom: 30px;
    font-weight: 500;
}
.progress-bar {
    width: 100%;
    height: 35px;
    background: #f0f0f0;
    border-radius: 20px;
    overflow: hidden;
    margin: 25px 0;
    box-shadow: inset 0 2px 8px rgba(0,0,0,0.1);
}
.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #10b981 0%, #059669 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    font-size: 1.1em;
    transition: width 1.5s ease;
}
</style>
"""

# Insert custom CSS before </head>
content = content.replace('</head>', custom_css + '</head>')

# Wrap content in container
content = content.replace('<body>', '<body><div class="container">')
content = content.replace('</body>', '</div></body>')

# Add header info
header_info = f'<div class="header-info">Generated on {datetime.now().strftime("%B %d, %Y at %H:%M:%S")}</div>'
content = content.replace('<h1>', header_info + '<h1>')

# Write enhanced report
with open('test-report.html', 'w') as f:
    f.write(content)

print("\n✅ Enhanced HTML report generated: test-report.html")
