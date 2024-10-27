from setuptools import setup, find_packages

setup(name='pddlgymnasium',
      version='0.0.0',
      install_requires=[
            'matplotlib',
            'pillow',
            'gymnasium<1.0.0',
            'imageio',
            'networkx',
            'scikit-image',
      ],
      python_requires='>=3.8',
      packages=find_packages(),
      package_data={'pddlgymnasium': ['rendering/assets/*', '**/*.pddl']},
      include_package_data=True,
)
