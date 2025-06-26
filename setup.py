from setuptools import setup, find_packages

setup(
    name = 'csf',
    version = '0.1',
    packages = find_packages(where='src'),# 指定查找目录
    package_dir={'': 'src'},  # 关键：映射包位置
    entry_points = {
        'console_scripts': [
            # 'csf = check_localizable_strings_file:main',
            # 修正为: 包名.模块名:函数名
            'csf = csf.cli:main',
        ],
    },
    install_requires=[
        # 如果有依赖库，请列在这里，例如：
        # 'requests>=2.25.1',
    ],
)