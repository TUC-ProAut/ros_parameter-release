Name:           ros-indigo-parameter-pa
Version:        1.2.1
Release:        0%{?dist}
Summary:        ROS parameter_pa package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib

%description
ProAut parameter package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Tue Dec 19 2017 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.2.1-0
- Autogenerated by Bloom

* Thu Dec 14 2017 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.2.0-0
- Autogenerated by Bloom

* Tue Aug 01 2017 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.1.0-0
- Autogenerated by Bloom

* Mon Jul 31 2017 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.0.2-0
- Autogenerated by Bloom

* Fri Jul 14 2017 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.0.0-0
- Autogenerated by Bloom

