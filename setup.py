import setuptools

setuptools.setup(
  name="autogui-engine",
  version="1.0.0",
  package=setuptools.find_packages(),
  classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
  ],
  python_requires=">=3.7",
  install_requires=[
      "numpy",
      "opencv-python",
      "pillow",
  ],
  extras_require={
      "dev": [
          "autoflake",
          "black",
          "isort",
          "yq",
      ]
  },
)