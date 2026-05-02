from setuptools import find_packages, setup
from typing import List

e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this func returns list of requirements
    '''
    get_requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Aditya',
    author_email='adityachikkerur@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']
    install_requires=get_requirements('requirements.txt')
)