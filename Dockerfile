# Use the latest Ubuntu image
FROM ubuntu:latest

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop

ENV SPARK_VERSION=3.5.1
ENV SPARK_HOME=/opt/spark

ENV SCALA_VERSION=2.13

ENV HBASE_VERSION=2.5.8
ENV HBASE_HOME=/opt/hbase

ENV ZOOKEEPER_VERSION=3.8.4
ENV ZOOKEEPER_HOME=/opt/zookeeper

# Update the package repository and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    openjdk-8-jdk \
    wget \
    curl \
    ssh \
    rsync \
    vim \
    net-tools \
    iputils-ping \
    sudo \
    && apt-get clean

# Download and install Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz -C /opt && \
    mv /opt/hadoop-$HADOOP_VERSION /opt/hadoop && \
    rm hadoop-$HADOOP_VERSION.tar.gz

# Download and install Spark
RUN wget https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3-scala$SCALA_VERSION.tgz && \
    tar -xzvf spark-$SPARK_VERSION-bin-hadoop3-scala$SCALA_VERSION.tgz -C /opt && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop3-scala$SCALA_VERSION /opt/spark && \
    rm spark-$SPARK_VERSION-bin-hadoop3-scala$SCALA_VERSION.tgz

# Download and install HBase
RUN wget https://downloads.apache.org/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-bin.tar.gz && \
    tar -xzvf hbase-$HBASE_VERSION-bin.tar.gz -C /opt && \
    mv /opt/hbase-$HBASE_VERSION /opt/hbase && \
    rm hbase-$HBASE_VERSION-bin.tar.gz

# Download and install ZooKeeper
RUN wget https://downloads.apache.org/zookeeper/zookeeper-$ZOOKEEPER_VERSION/apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz && \
    tar -xzvf apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz -C /opt && \
    mv /opt/apache-zookeeper-$ZOOKEEPER_VERSION-bin /opt/zookeeper && \
    rm apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz

# Create a non-root user
RUN useradd -ms /bin/bash alfa

# Set password for 'alfa' user (for the sake of example, it's 'password')
RUN echo 'alfa:alfa' | chpasswd

# Add 'alfa' to sudoers (optional, if sudo access is needed)
RUN usermod -aG sudo alfa

RUN mkdir -p /home/hadoop/hdfs/{namenode,datanode}
RUN mkdir -p /home/zookeeper

RUN chown -R alfa:alfa /opt
RUN chown -R alfa:alfa /opt/hadoop
RUN chown -R alfa:alfa /opt/zookeeper
RUN chown -R alfa:alfa /opt/spark
RUN chown -R alfa:alfa /opt/hbase
RUN chown -R alfa:alfa /home/hadoop
RUN chown -R alfa:alfa /home/hadoop/hdfs
RUN chown -R alfa:alfa /home/zookeeper

COPY .bashrc /home/alfa/

# Switch to the alfa user
USER alfa

# Expose necessary ports for Hadoop, Spark, HBase, and ZooKeeper
EXPOSE 22 50070 8088 9870 9864 7077 8080 16000 16010 16020 16030 2181 2888 3888

# Start a shell by default
CMD ["/bin/bash"]
#CMD service ssh start && bash
#CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D & bash"]

# docker build -t my-hadoop-base_image .
# docker run -it --name my-hadoop -p 22:22 -p 50070:50070 -p 8088:8088 -p 9870:9870 -p 9864:9864 -p 7077:7077 -p 8080:8080 -p 16000:1600 -p 16010:16010 -p 16020:16020 -p 16030:16030 -p 2181:2181 -p 2888:2888 -p 3888:388 my_hadoop_image
# docker run -it --name my-hadoop -v C:\GitHub\docker_mount:/home/docker_mount -p 22:22 -p 50070:50070 -p 8088:8088 -p 9870:9870 -p 9864:9864 -p 7077:7077 -p 8080:8080 -p 16000:1600 -p 16010:16010 -p 16020:16020 -p 16030:16030 -p 2181:2181 -p 2888:2888 -p 3888:388 my_hadoop_image
# docker attach my-hadoop
