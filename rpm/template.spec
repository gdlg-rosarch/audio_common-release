Name:           ros-indigo-audio-capture
Version:        0.2.9
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
Requires:       ros-indigo-audio-common-msgs
Requires:       ros-indigo-roscpp
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  ros-indigo-audio-common-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roscpp

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.9-0
- Autogenerated by Bloom

* Fri Oct 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.8-0
- Autogenerated by Bloom

