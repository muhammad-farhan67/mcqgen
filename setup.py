from setuptools import setup,find_packages
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Muhammad Farhan',
    author_email='farhanrafique6767@gmail.com',
    install_requires=["groq","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)