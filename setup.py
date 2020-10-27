from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='${version}',
    description='Blog System base on Django',
    author='the5fire',
    author_email='thefivefire@gmail.com',
    url='https://www.the5fire.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': [    # 打包数据文件，方法一
        'themes/*/*/*/*',  # 需要按目录层级匹配
        'themes/*/*/*',
    ]},
    # include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'asgiref==3.2.3',
'autopep8==1.5',
'backcall==0.1.0',
'bcrypt==3.1.7',
'certifi==2019.11.28',
'cffi==1.14.0',
'coreapi==2.3.3',
'coreschema==0.0.4',
'cryptography==3.2',
'decorator==4.4.1',
'defusedxml==0.6.0',
'diff-match-patch==20181111',
'Django==2.2.10',
'django-autocomplete-light==3.2.10',
'django-ckeditor==5.9.0',
'django-cors-headers==3.2.1',
'django-crispy-forms==1.8.1',
'django-debug-toolbar==2.2',
'django-debug-toolbar-line-profiler==0.6.1',
'django-formtools==2.2',
'django-import-export==2.0.1',
'django-js-asset==1.2.2',
'django-redis==4.11.0',
'django-rest-framework==0.1.0',
'django-reversion==3.0.5',
'django-silk==4.0.0',
'djangorestframework==3.11.0',
'djdt-flamegraph==0.2.12',
'et-xmlfile==1.0.1',
'Fabric3==1.14.post1',
'future==0.18.2',
'gprof2dot==2019.11.30',
'gunicorn==20.0.4',
'hiredis==1.0.1',
'httplib2==0.9.2',
'idna==2.8',
'ipython==7.12.0',
'ipython-genutils==0.2.0',
'itypes==1.1.0',
'jdcal==1.4.1',
'jedi==0.16.0',
'Jinja2==2.11.1',
'line-profiler==3.0.2',
'MarkupPy==1.14',
'MarkupSafe==1.1.1',
'mistune==0.8.4',
'mysqlclient==1.4.6',
'odfpy==1.4.1',
'openpyxl==3.0.3',
'paramiko==2.7.1',
'parso==0.6.1',
'passlib==1.7.2',
'pexpect==4.8.0',
'pickleshare==0.7.5',
'Pillow==7.0.0',
'pip2pi==0.8.1',
'prompt-toolkit==3.0.3',
'ptyprocess==0.6.0',
'pycodestyle==2.5.0',
'pycparser==2.19',
'Pygments==2.5.2',
'Pympler==0.8',
'PyMySQL==0.9.3',
'PyNaCl==1.3.0',
'pypiserver==1.3.2',
'python-dateutil==2.8.1',
'pytz==2019.3',
'PyYAML==5.3',
'redis==3.4.1',
'requests==2.22.0',
'six==1.14.0',
'sqlparse==0.3.0',
'supervisor==4.1.0',
'tablib==0.14.0',
'traitlets==4.3.3',
'uritemplate==3.0.1',
'urllib3==1.25.8',
'wcwidth==0.1.8',
'xadmin==2.0.1',
'xlrd==1.2.0',
'xlwt==1.3.0',

    ],
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

)