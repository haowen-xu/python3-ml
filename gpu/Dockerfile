FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

MAINTAINER Haowen Xu <haowen.xu@outlook.com>

ARG UBUNTU_MIRROR=archive.ubuntu.com
ARG CRAN_MIRROR=https://cloud.r-project.org
ARG PYTHON_VERSION=3.6.6
ARG PIP_OPTS=""
ARG TZ=Asia/Shanghai

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV SHELL=/bin/bash
ENV PIP_DEFAULT_TIMEOUT=120


ENV LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
  # lock the versions of cuda and libcudnn, such that TensorFlow + cudnn can work properly
RUN apt-get -y update && apt-mark hold cuda* libcudnn*


# do configuration and update packages
RUN echo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    chsh -s /bin/bash && \
    mkdir -p /var/run/sshd && \
    sed -i "s/archive.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apt-utils apt-transport-https lsb-release openssl gnupg dirmngr software-properties-common \
        build-essential ca-certificates wget git mercurial \
        locales language-pack-en tzdata vim ssh \
        libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
        libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev \
        libnlopt-dev libpq-dev libffi-dev libcairo-dev libedit-dev \
    && \
    add-apt-repository "deb ${CRAN_MIRROR}/bin/linux/ubuntu $(lsb_release -c -s)/" && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        r-base r-base-dev \
    && \
    wget -O /tmp/Python-${PYTHON_VERSION}.tgz https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz  && \
        cd /tmp && tar -xzvf Python-${PYTHON_VERSION}.tgz && \
        cd Python-${PYTHON_VERSION} && \
        ./configure --enable-optimizations && \
        make -j8 && \
        make altinstall && \
        rm /tmp/Python-${PYTHON_VERSION}.tgz && \
        rm -rf /tmp/Python-${PYTHON_VERSION} && \
    ln -sf /usr/local/bin/python3.6 /usr/bin/python && \
    ln -sf /usr/local/bin/pip3.6 /usr/bin/pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python --version && \
    python -m pip --version && \
    python -m pip install ${PIP_OPTS} --no-cache-dir --upgrade setuptools pip six && \
    python -m pip install ${PIP_OPTS} --no-cache-dir --upgrade \
        numpy==1.14.5 scipy sympy pandas tables scikit-learn matplotlib==2.0.2 ipython[all] tqdm \
        seaborn pillow imageio PyYAML sqlalchemy pymongo jinja2 scikit-image scipy progressbar2 mock pep8 coverage \
        mako GitPython tinydb tinydb-serialization hashfs && \
    python -m pip install ${PIP_OPTS} --no-cache-dir torchvision && \
    python -m pip install ${PIP_OPTS} --no-cache-dir tensorflow-gpu==1.9.0 && \
    python -m pip install ${PIP_OPTS} --no-cache-dir rpy2 && \
    rm -rf /root/.cache

RUN R --version && \
    echo "broom\n\
        DBI\n\
        dbplyr\n\
        dplyr\n\
        hexbin\n\
        ggplot2\n\
        lme4\n\
        RSQLite\n\
        tidyr" > /tmp/rpacks.txt && \
    R -e 'install.packages(sub("(.+)\\\\n","\\1", scan("/tmp/rpacks.txt", "character")), repos="'"${CRAN_MIRROR}"'")' && \
    rm /tmp/rpacks.txt

# Install Jupyterlab and other Jupyter extensions
ARG JUPYTER_BUILD_VERSION=1
RUN pip install ${PIP_OPTS} jupyterlab jupyter_nbextensions_configurator jupyter_contrib_nbextensions && \
    jupyter contrib nbextension install --sys-prefix && \
    jupyter nbextensions_configurator enable --sys-prefix && \
    jupyter serverextension enable --py jupyterlab --sys-prefix

# Force invalidate the cache layer
ARG CACHEBUST=1

# install other frequently updated libraries
RUN python -m pip install ${PIP_OPTS} \
        git+https://github.com/thu-ml/zhusuan.git \
        git+https://github.com/haowen-xu/tfsnippet.git \
        git+https://github.com/haowen-xu/mltoolkit.git \
        git+https://github.com/haowen-xu/mlstorage.git \
        git+https://github.com/facebookresearch/visdom.git

CMD ["/bin/bash"]
