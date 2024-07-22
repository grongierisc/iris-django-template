ARG IMAGE=containers.intersystems.com/intersystems/iris-community:latest-preview
FROM $IMAGE 

WORKDIR /irisdev/app

## Python stuff
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"

ENV PYTHON_PATH=/usr/irissys/bin/
ENV LD_LIBRARY_PATH=${ISC_PACKAGE_INSTALLDIR}/bin:${LD_LIBRARY_PATH}

ENV PATH "/home/irisowner/.local/bin:/usr/irissys/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/irisowner/bin"

COPY . .

USER root

# Remove EXTERNAL-MANAGER from the system
RUN rm -f /usr/lib/python3.12/EXTERNALLY-MANAGED

# Update package and install sudo
RUN apt-get update && apt-get install -y \
	git \
	nano \
	sudo && \
	/bin/echo -e ${ISC_PACKAGE_MGRUSER}\\tALL=\(ALL\)\\tNOPASSWD: ALL >> /etc/sudoers && \
	sudo -u ${ISC_PACKAGE_MGRUSER} sudo echo enabled passwordless sudo-ing for ${ISC_PACKAGE_MGRUSER}

USER ${ISC_PACKAGE_MGRUSER}

RUN pip3 install -r requirements.txt

# change the entrypoint to run iris and the python script
ENTRYPOINT [ "/irisdev/app/entrypoint.sh" ]