from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

with open("LICENSE", 'r') as f:
    license = f.read()

project_urls = {
  'GitHub': 'https://github.com/sidqdev/django-custom-fieldsets',
  'Telegram': 'https://t.me/sidqdev'
}


setup(
    name='django-custom-fieldsets',
    version='0.0.1',
    author='Sidq',
    author_email='abba.dmytro@gmail.com',
    description='Custom fieldset settings for django admin',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=license,
    project_urls=project_urls,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    requires=[
        "django"
    ],
    python_requires='>=3.6',
)

