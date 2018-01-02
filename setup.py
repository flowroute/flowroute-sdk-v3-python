from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='flowroutenumbersandmessaging',
    version='3.0.0',
    description='The Flowroute APIs are organized around REST. Our APIs have resource-oriented URLs, support HTTP Verbs, and respond with HTTP Status Codes. All API requests and responses, including errors, will be represented as JSON objects. You can use the Flowroute APIs to manage your Flowroute phone numbers including setting primary and failover routes for inbound calls, and sending text messages (SMS and MMS) using long-code or toll-free numbers in your account.',
    long_description=long_description,
    author='APIMatic SDK Generator',
    author_email='support@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)