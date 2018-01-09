FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

MAINTAINER Haowen Xu <public@korepwx.com>

ARG UBUNTU_MIRROR=archive.ubuntu.com
ARG TZ=Asia/Shanghai

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV PATH="/miniconda/bin:${PATH}"
ENV SHELL=/bin/bash
ENV LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"

RUN echo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    chsh -s /bin/bash && \
    sed -i "s/archive.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        wget \
        git \
        vim \
        locales \
        language-pack-en \
        tzdata \
        ssh \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O /tmp/miniconda.sh \
            && \
    /bin/bash /tmp/miniconda.sh -b -p /miniconda && \
    rm /tmp/miniconda.sh && \
    conda config --set always_yes yes --set changeps1 no && \
    conda update --yes -q conda && \
    conda info -a && \
    conda install --yes -q python=3.6 && \
    python -m pip install numpy scipy pandas tables scikit-learn matplotlib ipython[all] \
        tensorflow-gpu==1.5.0rc0

# Force invalidate the cache layer
ARG CACHEBUST=1
RUN python -m pip install \
        git+https://github.com/thu-ml/zhusuan.git \
        git+https://github.com/korepwx/tfsnippet.git \
        git+https://github.com/korepwx/mltoolkit.git

CMD ["/bin/bash"]
