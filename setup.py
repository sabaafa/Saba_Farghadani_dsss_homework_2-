from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any dependencies here, e.g., numpy, pandas, etc.
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz_game',  # Ensure this matches your main function path
        ],
    },
    author='Saba Farghadani',
    author_email='your.email@example.com',
    description='A simple math quiz game.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sabaafa/Saba_Farghadani_dsss_homework_2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
