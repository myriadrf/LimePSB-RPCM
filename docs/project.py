# Copyright date and release version should be updated accordingly!

project = 'LimePSB RPCM'
copyright = '2024-2026 Lime Microsystems'
author = 'Lime Microsystems'
release = 'v1.4'

# These are used for the "Edit on GitHub" links.
# github_repo_path should be set to the branch + path to the docs.
# E.g. 'master/docs/', 'main/docs/' or 'docs/docs/' etc.

github_repo = 'LimePSB-RPCM'
github_repo_path = 'docs/docs/'

# The default language for syntax highlighting in code blocks.
# This can be overridden using the ".. code-block::" directive.
highlight_language = 'console'

# Intersphinx mapping
# To minimise build time only include projects that are referenced.
intersphinx_internal = [
#    'suiteng',
]

intersphinx_external = [
#    'sphinx',
]

# Set to True if the project is archived.
archived = False

# When True internal intersphinx targets point at stage.myriadrf.org.
staging = True
