from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='strimzi-kafka-cli',
    version='0.1.0-alpha2',
    description="Command Line Interface for Strimzi Kafka Operator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['strimzi_kafka_cli'],
    package_dir={'strimzi_kafka_cli': ''},
    install_requires=[
        'Click',
        'PyYAML',
        'wget',
    ],
    entry_points='''
        [console_scripts]
        kfk=strimzi_kafka_cli.main:kfk
    ''',

    url="https://github.com/systemcraftsman/strimzi-kafka-cli",
    python_requires='>=3.5',
)
