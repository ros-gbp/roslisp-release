Name:           ros-indigo-roslisp
Version:        1.9.19
Release:        0%{?dist}
Summary:        ROS roslisp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslisp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-roslang
Requires:       ros-indigo-rospack
Requires:       ros-indigo-std-srvs
Requires:       sbcl
BuildRequires:  ros-indigo-catkin

%description
Lisp client library for ROS, the Robot Operating System.

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
* Fri Aug 14 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 1.9.19-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 1.9.18-0
- Autogenerated by Bloom

