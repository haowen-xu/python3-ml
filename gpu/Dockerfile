FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

MAINTAINER Haowen Xu <public@korepwx.com>

ARG UBUNTU_MIRROR=archive.ubuntu.com
ARG CRAN_MIRROR=https://cloud.r-project.org
ARG TZ=Asia/Shanghai

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV SHELL=/bin/bash
ENV PIP_DEFAULT_TIMEOUT=120
ENV LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"

RUN echo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    chsh -s /bin/bash && \
    sed -i "s/archive.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils lsb-release && \
    echo "deb ${CRAN_MIRROR}/bin/linux/ubuntu $(lsb_release -c -s)/" \
        >> /etc/apt/sources.list.d/added_repos.list && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        wget \
        git \
        mercurial \
        vim \
        locales \
        language-pack-en \
        tzdata \
        ssh \
        libcairo-dev \
        libedit-dev \
        python3 python3-dev python3-pip \
        r-base r-base-dev \
    && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python --version && \
    python -m pip --version && \
    python -m pip install --no-cache-dir --upgrade setuptools pip six && \
    python -m pip install --no-cache-dir --upgrade numpy scipy sympy pandas tables scikit-learn matplotlib ipython[all] tqdm \
        seaborn pillow PyYAML sqlalchemy pymongo jinja2 scikit-image scipy progressbar2 mock pep8 coverage \
        sacred sacredboard mako GitPython tinydb tinydb-serialization hashfs && \
    python -m pip install --no-cache-dir http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl torchvision && \
    python -m pip install --no-cache-dir tensorflow-gpu==1.8.0 && \
    python -m pip install --no-cache-dir rpy2 && \
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

# Force invalidate the cache layer
ARG CACHEBUST=1

# Install Jupyterlab and other Jupyter extensions
RUN pip install jupyterlab jupyter_nbextensions_configurator jupyter_contrib_nbextensions && \
    jupyter contrib nbextension install --sys-prefix && \
    jupyter nbextensions_configurator enable --sys-prefix && \
    jupyter serverextension enable --py jupyterlab --sys-prefix

# install other frequently updated libraries
RUN python -m pip install \
        git+https://github.com/thu-ml/zhusuan.git \
        git+https://github.com/korepwx/tfsnippet.git \
        git+https://github.com/korepwx/mltoolkit.git \
        git+https://github.com/facebookresearch/visdom.git

CMD ["/bin/bash"]
