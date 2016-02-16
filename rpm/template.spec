Name:           ros-jade-audio-capture
Version:        0.2.11
Release:        0%{?dist}
Summary:        ROS audio_capture package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/audio_capture
Source0:        %{name}-%{version}.tar.gz

Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Requires:       ros-jade-audio-common-msgs
Requires:       ros-jade-roscpp
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  ros-jade-audio-common-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-roscpp

%description
Transports audio from a source to a destination. Audio sources can come from a
microphone or file. The destination can play the audio or save it to an mp3
file.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Feb 16 2016 Austin Hendrix <namniart@gmail.com> - 0.2.11-0
- Autogenerated by Bloom

* Thu Jan 21 2016 Austin Hendrix <namniart@gmail.com> - 0.2.10-0
- Autogenerated by Bloom

* Wed Dec 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.9-0
- Autogenerated by Bloom

* Fri Oct 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.8-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Austin Hendrix <ahendrix@willowgarage.com> - 0.2.7-0
- Autogenerated by Bloom

