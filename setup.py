from setuptools import find_packages, setup
setup(
    name='datasciencehackathonanalytical',
    extras_require=dict(tests=['pytest', 'pandas', 'numpy']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_reqiures=['pytest', 'pandas', 'numpy']
)