from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="multi_lingual_rouge_score",
    description="Multi lingual Rouge Score using BPE-tokenizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "six",
        "rouge-score",
        "transformers",
    ],
    extras_require ={
        "dev":[
            "pytest >=3.7",
        ]
    },
    python_requires='>=3.6',
)
