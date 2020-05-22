"""
Setup for carla_manual_control
"""
import os
ROS_VERSION = int(os.environ['ROS_VERSION'])

if ROS_VERSION == 1:
    from distutils.core import setup
    from catkin_pkg.python_setup import generate_distutils_setup

    d = generate_distutils_setup(
        packages=['carla_manual_control'],
        package_dir={'': 'src'}
    )

    setup(**d)

elif ROS_VERSION == 2:
    from setuptools import setup

    package_name = 'carla_manual_control'
    setup(
        name=package_name,
        version='0.0.0',
        packages=['src/' + package_name],
        data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            ('share/' + package_name + '/config',
             ['config/settings.yaml', 'config/sensors.json'])
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='CARLA Simulator Team',
        maintainer_email='carla.simulator@gmail.com',
        description='CARLA ego vehicle for ROS2 bridge',
        license='MIT',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'manual_control = carla_manual_control.carla_manual_control:main'
            ],
        },
    )
