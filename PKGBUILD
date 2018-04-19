# Script generated with Bloom
pkgdesc="ROS - sound_play provides a ROS node that translates commands on a ROS topic (<tt>robotsound</tt>) into sounds. The node supports built-in sounds, playing OGG/WAV files, and doing speech synthesis via festival. C++ and Python bindings allow this node to be used without understanding the details of the message format, allowing faster development and resilience to message format changes."
url='http://ros.org/wiki/sound_play'

pkgname='ros-kinetic-sound-play'
pkgver='0.3.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-audio-common-msgs'
'ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
)

depends=('festival'
'festival-english'
'gst-plugins-base'
'gst-plugins-good'
'gst-plugins-ugly'
'gstreamer'
'python2-gobject'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-audio-common-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=sound_play
source=()
md5sums=()

prepare() {
    cp -R $startdir/sound_play $srcdir/sound_play
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

