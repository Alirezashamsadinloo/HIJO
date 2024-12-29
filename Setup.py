from setuptools import setup, find_packages

setup(
    name="hijo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",  # افزودن وابستگی‌های ضروری
    ],
    entry_points={
        "console_scripts": [
            "hijo = hijo.hijo:main"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Hijo is a simple yet powerful Python UI framework",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hijo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
