from setuptools import setup, find_packages

setup(
    name='you_personal_assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prompt_toolkit',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'your_project = modules.console_interface:main',
        ],
    },
)