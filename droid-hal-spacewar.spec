%define device spacewar
%define vendor nothing

%define rpm_device spacewar

%define vendor_pretty Nothing
%define device_pretty Phone (1)

%define droid_target_aarch64 1

#define installable_zip 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

%define enable_dtbo_update 1
%define enable_vendor_boot_update 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8+ the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /odm /product /system /system_ext /vendor

Requires: droid-system

%define straggler_files \
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

