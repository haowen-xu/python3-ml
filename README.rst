Python3 Machine Learning Environment
====================================

This is a Ubuntu 16.04 Docker image for Python 3 machine learning environment.

Development
-----------

We have two variants of Dockerfiles, the CPU variant (without CUDA) and the GPU variant (with CUDA).
To populate the Dockerfiles of both variants, execute the following command:

.. code-block:: python

    pip install jinja2
    python dockerfiles.py


Installation
------------

.. code-block:: bash

    # build the cpu image
    docker build -t ipwx/python3-ml:cpu cpu
    # build the gpu image
    docker build -t ipwx/python3-ml:gpu gpu
