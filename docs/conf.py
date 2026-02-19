project = 'pcmatic'
author = 'pcmatic'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
   <meta name="msvalidate.01" content="D36FE74240543E4E36AC2FBA4385E977" />
<meta name="google-site-verification" content="gl0BH9HEprohjlkLR-RbI_80ec_sPHkWIt6sAbCQoOk" />
    """
}

# Base URL for sitemap
html_baseurl = 'https://userhelpguide.readthedocs.io/en/latest/'
