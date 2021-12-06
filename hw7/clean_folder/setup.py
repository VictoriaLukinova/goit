from setuptools import setup, find_namespace_packages

setup(
    name= 'clean_folder',
    version= '1',
    description= 'Folder parser',
    url= 'https://github.com/VictoriaLukinova/goit/blob/main/hw7/clean_folder/clean_folder/clean.py',
    author= 'Victoria Lukinova',
    author_email= 'ViktoriagLuka@gmail.com',
    license= '',
    packages= find_namespace_packages(),
    entry_points ={'console_scripts': ['clean-folder=clean_folder.clean:main']},
)
