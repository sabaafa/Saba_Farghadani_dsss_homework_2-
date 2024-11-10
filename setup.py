from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Add dependencies if needed
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz_game',  # Adjust to match your main function
        ],
    },
    author='Your Name',
    author_email='sabafarghadani99@gmail.com',
    description='A simple math quiz game.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sabaafa/Saba_Farghadani_dsss_homework_2-.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
