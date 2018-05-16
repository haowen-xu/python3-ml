Python3 Machine Learning Environment
====================================

This is a Ubuntu 16.04 Docker image for Python 3 machine learning environment.

Major Packages
--------------

* Python 3.5
* TensorFlow 1.8.0
* CUDA 9.0 + CUDNN 7
* `ZhuSuan <https://github.com/thu-ml/zhusuan>`_, `TFSnippet <https://github.com/korepwx/tfsnippet>`_
  and `MLToolkit <https://github.com/korepwx/mltoolkit>`_

Development
-----------

We have two variants of Dockerfiles, the CPU variant (without CUDA) and the GPU variant (with CUDA).
To populate the Dockerfiles of both variants, execute the following command::

    pip install jinja2
    python Dockerfile.py

Installation
------------

::

    # build the cpu image
    docker build \
        --build-arg UBUNTU_MIRROR=archive.ubuntu.com \
        --build-arg CACHEBUST="$(date +%s)" \
        -t ipwx/python3-ml:cpu \
        cpu

    # build the gpu image
    docker build \
        --build-arg UBUNTU_MIRROR=archive.ubuntu.com \
        --build-arg CACHEBUST="$(date +%s)" \
        -t ipwx/python3-ml:gpu \
        gpu

`CACHEBUST` disables cache for `ZhuSuan`, `TFSnippet` and `MLToolkit`.
