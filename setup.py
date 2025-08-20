from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ida-pro-mcp-enhanced",
    version="1.0.0",
    author="CodeBuddy",
    author_email="",
    description="Enhanced IDA Pro MCP Server with comprehensive editing capabilities and 32/64-bit compatibility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/ida-pro-mcp-enhanced",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        # IDA Pro 自带所需的依赖
    ],
    entry_points={
        "console_scripts": [
            "ida-mcp-install=ida_pro_mcp.install:main",
        ],
    },
    package_data={
        "ida_pro_mcp": ["*.py"],
    },
    include_package_data=True,
    keywords="ida pro, reverse engineering, mcp, model context protocol, binary analysis",
    project_urls={
        "Bug Reports": "https://github.com/your-username/ida-pro-mcp-enhanced/issues",
        "Source": "https://github.com/your-username/ida-pro-mcp-enhanced",
        "Documentation": "https://github.com/your-username/ida-pro-mcp-enhanced/wiki",
    },
)