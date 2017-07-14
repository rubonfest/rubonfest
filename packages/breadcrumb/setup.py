from setuptools import setup

setup(
    name='lektor-breadcrumb',
    version='0.1',
    author=u'Dzianis Jackievic',
    author_email='den.overtone@gmail.com',
    license='MIT',
    py_modules=['lektor_breadcrumb'],
    entry_points={
        'lektor.plugins': [
            'breadcrumb = lektor_breadcrumb:BreadcrumbPlugin',
        ]
    }
)
