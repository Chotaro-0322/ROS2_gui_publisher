from setuptools import setup

package_name = 'gui_changer'
submodules = "gui_changer/submodule"

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='itolab-chotaro',
    maintainer_email='bq17088@shibaura-it.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gui_changer = gui_changer.gui_changer_main:main"
        ],
    },
)
