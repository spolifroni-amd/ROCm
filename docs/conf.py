# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import shutil
import jinja2
import os

# Environment to process Jinja templates.
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))

# Jinja templates to render out.
templates = []

# Render templates and output files without the last extension.
# For example: 'install.md.jinja' becomes 'install.md'.
for template in templates:
    rendered = jinja_env.get_template(template).render()
    with open(os.path.splitext(template)[0], 'w') as file:
        file.write(rendered)

shutil.copy2('../RELEASE.md','./about/release-notes.md')
# Keep capitalization due to similar linking on GitHub's markdown preview.
shutil.copy2('../CHANGELOG.md','./about/CHANGELOG.md')

latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{tgtermes}
\usepackage{tgheros}
\renewcommand\ttdefault{txtt}
"""
}

# configurations for PDF output by Read the Docs
project = "ROCm Documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."
version = "6.1.0"
release = "6.1.0"
setting_all_article_info = True
all_article_info_os = ["linux", "windows"]
all_article_info_author = ""

# pages with specific settings
article_pages = [
    {
        "file":"about/release-notes",
        "os":["linux", "windows"],
        "date":"2024-04-16"
    },
    {
        "file":"about/CHANGELOG",
        "os":["linux", "windows"],
        "date":"2024-04-16"
    },

    {"file":"install/windows/install-quick", "os":["windows"]},
    {"file":"install/linux/install-quick", "os":["linux"]},

    {"file":"install/linux/install", "os":["linux"]},
    {"file":"install/linux/install-options", "os":["linux"]},
    {"file":"install/linux/prerequisites", "os":["linux"]},

    {"file":"install/docker", "os":["linux"]},
    {"file":"install/magma-install", "os":["linux"]},
    {"file":"install/pytorch-install", "os":["linux"]},
    {"file":"install/tensorflow-install", "os":["linux"]},

    {"file":"install/windows/install", "os":["windows"]},
    {"file":"install/windows/prerequisites", "os":["windows"]},
    {"file":"install/windows/cli/index", "os":["windows"]},
    {"file":"install/windows/gui/index", "os":["windows"]},

    {"file":"about/compatibility/docker-image-support-matrix", "os":["linux"]},
    {"file":"about/compatibility/user-kernel-space-compat-matrix", "os":["linux"]},

    {"file":"reference/library-index", "os":["linux"]},

    {"file":"how-to/deep-learning-rocm", "os":["linux"]},
    {"file":"how-to/gpu-enabled-mpi", "os":["linux"]},
    {"file":"how-to/system-debugging", "os":["linux"]},
    {"file":"how-to/tuning-guides", "os":["linux", "windows"]},

    {"file":"how-to/rocm-for-ai/index", "os":["linux"]},
    {"file":"how-to/rocm-for-ai/install", "os":["linux"]},
    {"file":"how-to/rocm-for-ai/train-a-model", "os":["linux"]},
    {"file":"how-to/rocm-for-ai/deploy-your-model", "os":["linux"]},
    {"file":"how-to/rocm-for-ai/hugging-face-models", "os":["linux"]},

    {"file":"how-to/rocm-for-hpc/index", "os":["linux"]},

    {"file":"how-to/llm-fine-tuning-optimization/index", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/overview", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/fine-tuning-and-inference", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/single-gpu-fine-tuning-and-inference", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/multi-gpu-fine-tuning-and-inference", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/llm-inference-frameworks", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/model-acceleration-libraries", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/model-quantization", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/optimizing-with-composable-kernel", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/optimizing-triton-kernel", "os":["linux"]},
    {"file":"how-to/llm-fine-tuning-optimization/profiling-and-debugging", "os":["linux"]},
]

exclude_patterns = ['temp']

external_toc_path = "./sphinx/_toc.yml"

extensions = ["rocm_docs", "sphinx_reredirects"]

external_projects_current_project = "rocm"

html_theme = "rocm_docs_theme"
html_theme_options = {"flavor": "rocm-docs-home"}

html_static_path = ["sphinx/static/css"]
html_css_files = ["rocm_custom.css"]

html_title = "ROCm Documentation"

html_theme_options = {
    "link_main_doc": False
}

redirects = {
     "reference/openmp/openmp": "../../about/compatibility/openmp.html"
}
