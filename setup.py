from setuptools import find_packages, setup


VERSION = "0.0.1.dev"

setup(
    name="gym-text",
    version=VERSION,
    author="Mayank Mishra",
    author_email="mayank31398@gmail.com",
    url="https://github.com/mayank31398/gym-text",
    packages=find_packages("./"),
    include_package_data=True,
    package_data={"": ["**/*.cu", "**/*.cpp", "**/*.cuh", "**/*.h", "**/*.pyx"]},
)
